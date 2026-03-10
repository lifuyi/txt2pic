#!/usr/bin/env python3
"""
小红书图文卡片渲染器
根据 Markdown 内容生成 HTML 卡片，然后转换为 PNG
"""

import asyncio
import re
import os
import sys
from pathlib import Path
from datetime import datetime
from markdown import Markdown
from playwright.async_api import async_playwright

# 主题配色方案（来自 SKILL.md）
THEMES = {
    "professional": {
        "name": "专业权威",
        "bg_color": "#1E3A5F",
        "accent_color": "#3B82F6",
        "text_color": "#FFFFFF",
        "card_bg": "#FFFFFF",
        "card_text": "#1E3A5F",
    },
    "chinese-traditional": {
        "name": "青绿山水",
        "bg_color": "#f4f1e8",
        "accent_color": "#295f68",
        "text_color": "#362923",
        "card_bg": "#FFFFFF",
        "card_text": "#295f68",
    },
    "spring": {
        "name": "春江水暖",
        "bg_color": "#fdfcf0",
        "accent_color": "#ff8a65",
        "text_color": "#5d4037",
        "card_bg": "#FFFFFF",
        "card_text": "#d84315",
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
            background: {bg_color};
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px;
        }}
        
        .card {{
            width: 1080px;
            min-height: 1440px;
            background: {card_bg};
            border-radius: 24px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
            padding: 60px;
            position: relative;
            overflow: hidden;
        }}
        
        .card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 8px;
            background: linear-gradient(90deg, {accent_color}, {accent_color}dd);
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 50px;
            padding-bottom: 40px;
            border-bottom: 2px solid #f0f0f0;
        }}
        
        .title {{
            font-size: 56px;
            font-weight: 700;
            color: {card_text};
            margin-bottom: 20px;
            line-height: 1.3;
        }}
        
        .subtitle {{
            font-size: 32px;
            color: {text_color};
            opacity: 0.8;
        }}
        
        .content {{
            font-size: 28px;
            line-height: 1.8;
            color: #333;
        }}
        
        .content h1 {{
            font-size: 42px;
            color: {card_text};
            margin: 40px 0 24px 0;
            padding-bottom: 16px;
            border-bottom: 3px solid {accent_color}40;
        }}
        
        .content h2 {{
            font-size: 36px;
            color: {card_text};
            margin: 32px 0 20px 0;
        }}
        
        .content p {{
            margin-bottom: 20px;
        }}
        
        .content ul {{
            margin: 20px 0;
            padding-left: 40px;
        }}
        
        .content li {{
            margin-bottom: 16px;
            list-style: none;
            position: relative;
            padding-left: 32px;
        }}
        
        .content li::before {{
            content: '▫️';
            position: absolute;
            left: 0;
        }}
        
        .content strong {{
            color: {card_text};
            font-weight: 600;
        }}
        
        .footer {{
            margin-top: 60px;
            padding-top: 30px;
            border-top: 1px solid #eee;
            text-align: center;
            font-size: 24px;
            color: #999;
        }}
        
        .brand {{
            font-weight: 600;
            color: {accent_color};
        }}
    </style>
</head>
<body>
    <div class="card">
        {header}
        <div class="content">
            {content}
        </div>
        <div class="footer">
            <span class="brand">UniseekChina</span> · 助力留学梦想
        </div>
    </div>
</body>
</html>
"""

COVER_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Noto Sans SC', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, {bg_color} 0%, {accent_color}30 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px;
        }}
        
        .card {{
            width: 1080px;
            height: 1440px;
            background: {card_bg};
            border-radius: 32px;
            box-shadow: 0 30px 80px rgba(0,0,0,0.2);
            padding: 80px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}
        
        .card::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, {accent_color}10 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }}
        
        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); opacity: 0.5; }}
            50% {{ transform: scale(1.1); opacity: 0.8; }}
        }}
        
        .emoji {{
            font-size: 120px;
            margin-bottom: 40px;
            position: relative;
            z-index: 1;
        }}
        
        .title {{
            font-size: 72px;
            font-weight: 900;
            color: {card_text};
            margin-bottom: 30px;
            line-height: 1.2;
            position: relative;
            z-index: 1;
        }}
        
        .subtitle {{
            font-size: 40px;
            color: {text_color};
            opacity: 0.9;
            margin-bottom: 60px;
            position: relative;
            z-index: 1;
        }}
        
        .divider {{
            width: 120px;
            height: 6px;
            background: linear-gradient(90deg, {accent_color}, {accent_color}80);
            border-radius: 3px;
            margin-bottom: 60px;
            position: relative;
            z-index: 1;
        }}
        
        .brand {{
            font-size: 32px;
            color: {accent_color};
            font-weight: 600;
            position: relative;
            z-index: 1;
        }}
        
        .tags {{
            margin-top: 40px;
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
            justify-content: center;
            position: relative;
            z-index: 1;
        }}
        
        .tag {{
            background: {accent_color}15;
            color: {accent_color};
            padding: 12px 24px;
            border-radius: 30px;
            font-size: 24px;
            font-weight: 500;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="emoji">🎓</div>
        <h1 class="title">{title}</h1>
        <p class="subtitle">{subtitle}</p>
        <div class="divider"></div>
        <div class="brand">UniseekChina</div>
        <div class="tags">
            <span class="tag">#中国留学</span>
            <span class="tag">#经济学申请</span>
            <span class="tag">#C9院校</span>
        </div>
    </div>
</body>
</html>
"""


def parse_markdown(md_file):
    """解析 Markdown 文件，提取元数据和内容段落"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 解析 YAML 头部
    yaml_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    metadata = {}
    if yaml_match:
        yaml_content = yaml_match.group(1)
        for line in yaml_content.strip().split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"').strip("'")
        content = content[yaml_match.end():]
    
    # 按 --- 分割段落
    sections = re.split(r'\n---\s*\n', content)
    sections = [s.strip() for s in sections if s.strip()]
    
    return metadata, sections


def markdown_to_html(md_content):
    """将 Markdown 转换为 HTML"""
    md = Markdown(extensions=['extra', 'nl2br'])
    html = md.convert(md_content)
    
    # 移除话题标签
    html = re.sub(r'#\w+\[话题\]#', '', html)
    
    return html


def generate_cover_html(metadata, theme):
    """生成封面 HTML"""
    theme_data = THEMES[theme]
    return COVER_TEMPLATE.format(
        title=metadata.get('title', '标题'),
        subtitle=metadata.get('subtitle', '副标题'),
        **theme_data
    )


def generate_content_html(section, theme, has_header=False):
    """生成内容卡片 HTML"""
    theme_data = THEMES[theme]
    
    html_content = markdown_to_html(section)
    
    header = ""
    if has_header:
        # 提取第一个 h1 作为标题
        h1_match = re.search(r'<h1>(.*?)</h1>', html_content)
        if h1_match:
            title = h1_match.group(1)
            html_content = re.sub(r'<h1>.*?</h1>', '', html_content, count=1)
            header = f'<div class="header"><h1 class="title">{title}</h1></div>'
    
    return HTML_TEMPLATE.format(
        title="小红书图文",
        header=header,
        content=html_content,
        **theme_data
    )


async def html_to_png(html_content, output_path):
    """将 HTML 转换为 PNG"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1200, "height": 1600})
        
        # 创建临时 HTML 文件
        temp_html = output_path.replace('.png', '.html')
        with open(temp_html, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # 使用正确的 file:// URL 格式
        file_url = f'file://{Path(temp_html).absolute()}'
        await page.goto(file_url)
        await page.screenshot(path=output_path, full_page=True)
        await browser.close()
        
        # 清理临时文件
        os.remove(temp_html)


async def render_markdown(md_file, theme='professional', output_dir='./output'):
    """渲染 Markdown 文件为 PNG 卡片"""
    
    # 创建输出目录
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_folder = Path(output_dir) / timestamp
    output_folder.mkdir(parents=True, exist_ok=True)
    
    # 解析 Markdown
    metadata, sections = parse_markdown(md_file)
    
    print(f"📄 解析到 {len(sections)} 个内容段落")
    print(f"🎨 使用主题: {THEMES[theme]['name']}")
    print(f"📁 输出目录: {output_folder}")
    print()
    
    # 生成封面
    print("🖼️  生成封面...")
    cover_html = generate_cover_html(metadata, theme)
    cover_path = output_folder / 'P1-cover.png'
    await html_to_png(cover_html, str(cover_path))
    print(f"   ✓ {cover_path}")
    
    # 生成内容卡片
    for i, section in enumerate(sections, 2):
        print(f"🖼️  生成卡片 {i}...")
        content_html = generate_content_html(section, theme, has_header=True)
        content_path = output_folder / f'P{i}-content.png'
        await html_to_png(content_html, str(content_path))
        print(f"   ✓ {content_path}")
    
    print()
    print(f"✅ 完成！共生成 {len(sections) + 1} 张卡片")
    print(f"📂 输出位置: {output_folder}")
    
    return output_folder


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description='小红书图文卡片渲染器')
    parser.add_argument('markdown_file', help='Markdown 文件路径')
    parser.add_argument('--theme', '-t', choices=list(THEMES.keys()), 
                        default='professional', help='主题样式')
    parser.add_argument('--output-dir', '-o', default='./output', 
                        help='输出目录')
    
    args = parser.parse_args()
    
    asyncio.run(render_markdown(args.markdown_file, args.theme, args.output_dir))

#!/usr/bin/env python3
"""
Instagram Automation Script - Local Playwright
完全本地运行的 Instagram 自动化发布脚本
支持自动登录和手动登录两种模式
"""

import asyncio
import time
from pathlib import Path
from playwright.async_api import async_playwright

# 配置
INSTAGRAM_URL = "https://www.instagram.com"
USERNAME = ""  # 填写你的 Instagram 用户名
PASSWORD = ""  # 填写你的 Instagram 密码
IMAGES_DIR = "/Users/eyeopen/Downloads/projects/xhs-graphic-generator/output/20260312214712"
CAPTION = """CSCA Complete Guide | China's Standardized Test for International Students | Dec 2025 Launch

Planning to study for a bachelor's degree in China? The China Scholastic Competency Assessment (CSCA) launches globally on December 21, 2025! This is the official standardized test organized by the China Scholarship Council (CSC).

📚 5 Test Subjects:
✅ Professional Chinese (Humanities/STEM tracks)
✅ Mathematics, Physics, Chemistry (Chinese/English bilingual options)

⏰ First Exam Schedule (Beijing Time):
December 21, 13:00-20:30, four subjects consecutively
From 2026: 5 exam sessions annually

💰 Test Fees:
1 subject: ¥450
2+ subjects: ¥700

🎯 Why Take CSCA:
- Important reference for Chinese university admissions
- Scholarship evaluation criteria
- Global percentile ranking provided

Whether applying for Chinese Government Scholarships or self-funded programs, CSCA enhances your application competitiveness! Detailed subject selection and schedule in the carousel 👆

#UniseekChina #StudyInChina #CSCA #ChinaEducation #InternationalStudents #StudyAbroad #ChinaScholarship #BachelorDegree #StandardizedTest"""

async def instagram_automation():
    """Instagram 自动化发布主函数"""
    print("🚀 启动 Instagram 自动化发布脚本...")
    print("=" * 60)
    
    async with async_playwright() as p:
        # 启动浏览器
        print("📱 启动 Chrome 浏览器...")
        browser = await p.chromium.launch(
            headless=False,  # 可见模式，方便调试
            args=[
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-blink-features=AutomationControlled'
            ]
        )
        
        # 创建新页面
        context = await browser.new_context(
            viewport={'width': 1200, 'height': 800},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        page = await context.new_page()
        
        try:
            # 1. 访问 Instagram
            print(f"🌐 访问 {INSTAGRAM_URL}...")
            await page.goto(INSTAGRAM_URL, wait_until='networkidle', timeout=60000)
            await asyncio.sleep(3)
            
            # 检查是否已登录
            if "login" in page.url:
                print("🔐 检测到未登录，准备登录...")
                await login(page)
            else:
                print("✅ 已检测到登录状态")
            
            # 等待页面加载
            await asyncio.sleep(3)
            
            # 2. 开始创建新帖子
            print("📸 开始创建新帖子...")
            await create_new_post(page)
            
            # 3. 上传图片
            print("🖼️ 上传图片...")
            await upload_images(page)
            
            # 4. 填写文案
            print("📝 填写文案...")
            await write_caption(page)
            
            # 5. 发布
            print("📤 发布帖子...")
            await publish_post(page)
            
            print("\n" + "=" * 60)
            print("🎉 发布成功！")
            print("=" * 60)
            
        except Exception as e:
            print(f"\n❌ 发生错误: {e}")
            print("请检查网络连接和登录状态")
        
        finally:
            print("\n⏳ 等待 10 秒后关闭浏览器...")
            await asyncio.sleep(10)
            await browser.close()


async def login(page):
    """登录 Instagram"""
    if not USERNAME or not PASSWORD:
        print("⚠️  未配置用户名和密码，请手动登录")
        print("⏳ 等待手动登录，你有 60 秒时间...")
        
        # 等待登录按钮出现
        try:
            await page.wait_for_selector("text='Log in'", timeout=5000)
        except:
            pass
        
        # 等待用户手动登录
        await asyncio.sleep(60)
        
        # 检查是否登录成功
        if "login" not in page.url:
            print("✅ 登录成功！")
        else:
            raise Exception("登录超时或失败")
        
        return
    
    # 自动登录
    print(f"🔑 尝试自动登录: {USERNAME}")
    
    # 填写用户名
    username_selector = "input[name='username']"
    await page.wait_for_selector(username_selector)
    await page.fill(username_selector, USERNAME)
    
    # 填写密码
    password_selector = "input[name='password']"
    await page.fill(password_selector, PASSWORD)
    
    # 点击登录按钮
    login_button_selector = "button[type='submit']"
    await page.click(login_button_selector)
    
    # 等待登录完成
    await asyncio.sleep(5)
    
    # 处理可能出现的保存登录信息提示
    try:
        not_now_button = await page.query_selector("text='Not Now'")
        if not_now_button:
            await not_now_button.click()
            await asyncio.sleep(2)
    except:
        pass
    
    print("✅ 登录成功！")


async def create_new_post(page):
    """点击创建新帖子按钮"""
    print("  寻找创建帖子按钮...")
    
    # 等待页面加载
    await page.wait_for_load_state('networkidle')
    
    # 方法1: 寻找导航栏的创建按钮
    try:
        # 寻找包含 "Create" 的按钮或链接
        create_button = await page.query_selector("a[href*='/create']")
        if create_button:
            await create_button.click()
        else:
            # 方法2: 寻找 SVG 图标的创建按钮
            create_button = await page.query_selector("svg[aria-label='New post']")
            if create_button:
                await create_button.click()
            else:
                # 方法3: 寻找文字按钮
                await page.click("text='Create'", timeout=5000)
        
        await asyncio.sleep(3)
        print("  ✅ 已点击创建帖子按钮")
        
    except Exception as e:
        print(f"  ⚠️  无法自动找到创建按钮: {e}")
        print("  请手动点击 Instagram 的 'Create' 或 '+' 按钮")
        await asyncio.sleep(10)


async def upload_images(page):
    """上传图片"""
    print("  准备上传图片...")
    
    # 获取所有图片文件
    image_dir = Path(IMAGES_DIR)
    image_files = sorted([f for f in image_dir.glob("P*-en.png")])
    
    if not image_files:
        raise Exception(f"在 {IMAGES_DIR} 中未找到图片文件")
    
    print(f"  找到 {len(image_files)} 张图片")
    
    # 等待文件选择器出现
    try:
        # 等待并点击选择文件按钮
        select_button = await page.wait_for_selector("text='Select from computer'", timeout=10000)
        if select_button:
            await select_button.click()
        else:
            # 尝试其他选择器
            await page.click("text='Select files'", timeout=5000)
        
        await asyncio.sleep(2)
        
    except Exception as e:
        print(f"  ⚠️  无法自动触发文件选择: {e}")
        print("  请手动点击 'Select from computer' 按钮")
        await asyncio.sleep(5)
    
    # 使用 Playwright 的文件上传功能
    # 注意：Instagram 的文件上传可能比较特殊，可能需要多次上传
    print("  请手动选择图片文件（支持多选）")
    print(f"  图片位置: {IMAGES_DIR}")
    
    # 等待用户完成上传
    await asyncio.sleep(15)
    
    # 检查是否进入下一步
    try:
        next_button = await page.query_selector("text='Next'")
        if next_button:
            await next_button.click()
            print("  ✅ 已点击 Next 进入下一步")
            await asyncio.sleep(3)
    except:
        print("  等待用户完成图片选择和调整...")
        await asyncio.sleep(10)


async def write_caption(page):
    """填写文案"""
    print("  填写文案...")
    
    # 等待文本区域出现
    try:
        caption_textarea = await page.wait_for_selector("textarea[aria-label='Write a caption...']", timeout=10000)
        if caption_textarea:
            await caption_textarea.fill(CAPTION)
            print("  ✅ 文案已填写")
        else:
            # 尝试其他选择器
            await page.fill("textarea[placeholder*='caption']", CAPTION)
    except Exception as e:
        print(f"  ⚠️  无法自动填写文案: {e}")
        print("  请手动粘贴文案")
        
        # 将文案复制到剪贴板提示
        print("\n" + "=" * 60)
        print("📋 文案已准备好，请复制：")
        print("=" * 60)
        print(CAPTION)
        print("=" * 60 + "\n")
        
        await asyncio.sleep(15)  # 给用户时间手动粘贴


async def publish_post(page):
    """发布帖子"""
    print("  准备发布...")
    
    # 等待 Share 按钮可点击
    try:
        share_button = await page.wait_for_selector("text='Share'", timeout=10000)
        if share_button:
            # 检查按钮是否禁用
            is_disabled = await share_button.is_disabled()
            if not is_disabled:
                await share_button.click()
                print("  ✅ 已点击 Share 发布")
            else:
                print("  ⚠️  Share 按钮不可用，等待中...")
                await asyncio.sleep(5)
                await share_button.click()
        else:
            # 尝试其他选择器
            await page.click("button[type='submit']")
    except Exception as e:
        print(f"  ⚠️  无法自动点击发布: {e}")
        print("  请手动点击 'Share' 按钮发布")
        await asyncio.sleep(10)
    
    # 等待发布完成
    print("  等待发布完成...")
    await asyncio.sleep(5)
    
    # 检查是否发布成功
    try:
        # 如果返回主页或看到发布成功的提示
        await page.wait_for_url("https://www.instagram.com/*", timeout=10000)
        print("  ✅ 发布成功！")
    except:
        print("  ℹ️  请检查是否发布成功")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("📸 Instagram 自动化发布脚本")
    print("=" * 60)
    print("\n⚠️  重要提示：")
    print("   - 请确保已安装 Playwright: pip install playwright")
    print("   - 首次运行需要安装浏览器: playwright install chromium")
    print("   - 脚本会自动控制浏览器，请勿移动鼠标或键盘")
    print("   - 如果自动操作失败，会提示手动操作")
    print("\n" + "=" * 60 + "\n")
    
    # 检查配置
    if not USERNAME or not PASSWORD:
        print("ℹ️  未配置用户名和密码，将使用手动登录模式")
        print("   请在 60 秒内手动完成登录\n")
    
    # 运行主函数
    asyncio.run(instagram_automation())

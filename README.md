# 小红书图文生成器 (XHS Graphic Generator)

将 Markdown 内容转换为小红书风格的 HTML 图文卡片。基于**主题配色系统**实现视觉设计，支持自动转换为 PNG 图片。

## 核心特性

- 🎨 **16种主题配色**：基于中国风水墨画的配色系统（太极锦鲤、青绿山水、傲骨寒梅等）
- 📐 **标准尺寸**：1080×1440px（3:4 竖版），适配小红书/Instagram
- 🔄 **自动化流程**：Markdown → HTML → PNG 一键转换
- 🎓 **大学内容支持**：内置39所中国大学资料库
- ✨ **CSS驱动设计**：纯CSS实现视觉效果，无需背景图片

## 快速开始

### 1. 环境准备

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# 安装依赖
pip install markdown playwright
playwright install chromium
```

### 2. 生成图文卡片

```bash
# 使用 render_cards.py 从 Markdown 生成 HTML
source venv/bin/activate
python render_cards.py your_content.md --theme professional

# 或使用 html_to_png.py 将现有 HTML 转为 PNG
python html_to_png.py output/20260309123456
```

## 工作流程

```
Markdown 内容
    ↓
分析内容主题
    ↓
选择视觉主题（16选1）
    ↓
生成 HTML 卡片
    ↓
转换为 PNG
```

### 详细步骤

1. **分析 Markdown 内容**：识别主题、大学、关键信息点
2. **选择主题配色**：从16个主题中选择最匹配的视觉风格
3. **生成 HTML 文件**：每张卡片独立HTML，CSS内联，可直接预览
4. **转换为 PNG**：使用 Playwright 批量转换

## 主题配色系统

所有视觉设计必须基于以下16个主题：

| 主题名称 | 风格特点 | 适用场景 |
|----------|----------|----------|
| **太极锦鲤** | 红黑白、动态平衡 | 招生类、祝福类内容 |
| **日出青岚** | 红日、青绿山水 | 开篇封面、愿景展示 |
| **红梅报春** | 红梅、暖棕枝干 | 新年祝福、春季招生 |
| **青绿山水** | 传统青绿、山水意境 | 文化类、艺术类内容 |
| **傲骨寒梅** | 梅花红、古雅棕 | 励志类、学术类内容 |
| **古韵边框** | 古铜金、对称边框 | 证书类、荣誉展示 |
| **春江水暖** | 暖黄、桃花橙粉 | 春季活动、招生季 |
| **春山叠翠** | 嫩绿、山峦叠嶂 | 自然类、旅游类内容 |
| **春晖大地** | 暖黄、翠绿山峦 | 希望类、成长类内容 |
| **绿柳垂丝** | 清新绿、生机勃勃 | 校园风光、环境介绍 |
| **春晖垂柳** | 淡绿、垂柳依依 | 毕业季、离别主题 |
| **柳丝依依** | 翠绿、柳丝飘逸 | 校园生活、青春主题 |
| **春山如黛** | 黛青、层山叠嶂 | 传统文化、诗词类 |
| **江南烟雨** | 灰蓝、烟雨朦胧 | 文艺类、散文类内容 |
| **梨花带雨** | 素雅白、雨丝灰 | 文艺类、情感类内容 |
| **幽谷兰草** | 墨绿、岩石灰 | 高雅类、品质类内容 |

### 主题选择指南

| 内容类型 | 推荐主题 |
|----------|----------|
| 大学招生/宣传 | 太极锦鲤、日出青岚、红梅报春 |
| 校园环境介绍 | 绿柳垂丝、春晖垂柳、柳丝依依 |
| 传统文化/诗词 | 青绿山水、春山如黛、江南烟雨 |
| 励志/学术类 | 傲骨寒梅、幽谷兰草、古韵边框 |
| 春季活动/招生季 | 春江水暖、春山叠翠、春晖大地 |

## 文件结构

```
xhs-graphic-generator/
├── SKILL.md                    # Skill 定义文件（工作流程、主题配色）
├── README.md                   # 本文件
├── render_cards.py             # Markdown 转 HTML 渲染器
├── html_to_png.py              # HTML 转 PNG 转换器
├── economics_tiers.md          # 示例：经济学项目分层内容
├── references/
│   ├── prompt-guide.md         # HTML 模板规范
│   ├── styles.md               # 视觉风格详解
│   ├── content-planning.md     # 内容规划方法
│   └── universities/           # 大学资料库（39所985大学）
│       ├── FUDAN_复旦大学/
│       ├── PKU_北京大学/
│       └── ...
├── output/                     # 输出目录
│   └── 20260309123456/         # 时间戳命名的子文件夹
│       ├── P1-cover.html
│       ├── P1-cover.png
│       ├── P2-content.html
│       └── ...
└── venv/                       # Python 虚拟环境
```

## 输出示例

```
output/
└── 20260309224000/
    ├── P1-cover.html          # 封面：主题标题
    ├── P1-cover.png
    ├── P2-c9-tier.html        # C9顶尖联盟
    ├── P2-c9-tier.png
    ├── P3-985-tier.html       # 985大学
    ├── P3-985-tier.png
    ├── P4-211-tier.html       # 211财经名校
    ├── P4-211-tier.png
    ├── P5-tips.html           # 申请建议
    ├── P5-tips.png
    ├── P6-locations.html      # 地理位置优势
    └── P6-locations.png
```

## Markdown 格式

```markdown
---
title: "The Tiers: C9 vs 985 vs Specialized Finance"
subtitle: "Economics Programs & Official Portals"
---

# 🎓 C9 Elite Tier

The pinnacle of Chinese economics education

▫️ **Fudan University** - C9/985
▫️ **Peking University** - C9/985
...

---

# ⭐ 985 Universities

Economics powerhouses...
```

## 技术栈

- **Python 3.14+**：核心逻辑
- **Playwright**：HTML 转 PNG 截图
- **Markdown**：内容输入格式
- **CSS3**：视觉效果（渐变、阴影、动画）

## 品牌配置

**品牌名称**: UniseekChina

品牌标签 `#UniseekChina` 会自动添加到相关内容卡片底部。

## License

MIT License

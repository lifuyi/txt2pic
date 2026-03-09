# 小红书图文生成器 (XHS Graphic Generator)

一个 AI Agent Skill，根据用户提供的 Markdown 内容，自动匹配大学图片，生成小红书风格的 HTML 图文卡片（3:4 竖版，2K 分辨率）。

## 功能特点

- 🎓 **大学图片库**：内置 39 所985大学资料和校园图片
- 🎨 **五种视觉风格**：青春活力、专业权威、简约现代、学院复古、清新自然
- 📐 **小红书标准**：3:4 竖版比例，2K 分辨率 (1536×2048px)
- 🖼️ **背景图片库**：50+ 精美背景模板可供选择
- 🔄 **内容驱动**：根据内容自动匹配图片和风格

## 目录结构

```
xhs-graphic-generator/
├── SKILL.md                    # Agent Skill 主文件 - 定义工作流程
├── references/
│   ├── prompt-guide.md         # Prompt 编写规范与 HTML 模板
│   ├── styles.md               # 视觉风格配色方案与布局
│   ├── content-planning.md     # 内容规划方法论
│   ├── bg/                     # 背景图片库 (50+ 张)
│   └── universities/           # 大学图片库 (39 所985大学)
│       ├── 浙江大学/
│       ├── 清华大学/
│       └── ...
├── output/                     # 生成输出目录
├── .env.example               # 环境变量模板
└── README.md
```

## 快速开始

### 1. 配置 API Key

```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 NVIDIA API Key
```

### 2. 使用方式

作为 iFlow CLI 的 Agent Skill 使用，当需要生成小红书图文时自动触发。

## 图片资源

### 大学图片库

已内置 39 所985大学的资料：
- 清华大学、北京大学、浙江大学、上海交通大学、复旦大学
- 南京大学、中国人民大学、武汉大学、中山大学、西安交通大学
- 华中科技大学、哈尔滨工业大学、北京航空航天大学、天津大学
- ... 等 39 所

### 背景图片库

`references/bg/` 包含 50+ 张背景图片，按风格分类：
- bg_1~bg_10：青春活力风格（明亮暖色系）
- bg_11~bg_20：专业权威风格（深蓝、金色系）
- bg_21~bg_30：简约现代风格（白色、浅灰、几何）
- bg_31~bg_36：学院复古风格（复古纹理、边框）
- bg_37~bg_50：清新自然风格（自然、艺术边框）

## 视觉风格

| 风格 | 主色 | 强调色 | 适用场景 |
|------|------|--------|----------|
| 青春活力 | #FFF7ED | #F97316, #FB923C | 校园生活、社团活动 |
| 专业权威 | #1E3A5F | #3B82F6, #F59E0B | 排名数据、官方介绍 |
| 简约现代 | #FFFFFF | #6366F1, #10B981 | 教程、科普、技术 |
| 学院复古 | #F5F0E6 | #8B4513, #2F4F4F | 历史名校、文化底蕴 |
| 清新自然 | #FAF9F7 | #B8E0D2, #5ABAB7 | 校园风景、环境介绍 |

## 输出格式

生成的 HTML 文件存放在以时间命名的子文件夹中：

```
output/
└── 20240309153045/          # 生成时间：年月日时分秒
    ├── P1-cover.html         # 封面
    ├── P2-content.html       # 内容图1
    ├── P3-content.html       # 内容图2
    └── ...
```

用户可自行将 HTML 转换为 PNG（使用浏览器截图、Puppeteer 等工具）。

## API 配置

使用 NVIDIA API 调用大模型。

```bash
# .env 文件配置
NVIDIA_API_KEY="your-nvidia-api-key"
NVIDIA_BASE_URL="https://integrate.api.nvidia.com/v1"

# 优先模型
KIMI_MODEL="moonshotai/kimi-k2-0711-preview"
```

## License

MIT License
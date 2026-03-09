# 视觉风格参考

## 1. 青春活力风

**适用**：综合类、理工类院校，吸引高中生群体

**配色方案**：
- 主背景：暖白 #FFF7ED、浅橙 #FFEDD5
- 强调色：活力橙 #F97316、阳光黄 #FB923C
- 文字色：深棕 #78350F、中灰 #57534E
- 点缀：天蓝 #38BDF8、草绿 #22C55E

**视觉特征**：
- 明亮温暖的色调
- 圆角卡片和图标
- 动感装饰元素（箭头、标签）
- 适合展示校园活动、社团生活

---

## 2. 专业权威风

**适用**：重点名校、医学类、法学类院校

**配色方案**：
- 主背景：深海蓝 #1E3A5F、纯白 #FFFFFF
- 强调色：科技蓝 #3B82F6、金色 #F59E0B
- 文字色：深蓝 #1E293B、纯白 #FFFFFF
- 点缀：银灰 #94A3B8

**视觉特征**：
- 深色背景强调厚重感
- 金色点缀提升品质
- 清晰的数据可视化
- 排名、数字突出展示

---

## 3. 简约现代风

**适用**：新兴院校、艺术类、设计类院校

**配色方案**：
- 主背景：纯白 #FFFFFF、浅灰 #F8FAFC
- 强调色：科技紫 #6366F1、薄荷绿 #10B981
- 文字色：深灰 #1F2937、中灰 #6B7280
- 点缀：渐变紫 #8B5CF6

**视觉特征**：
- 大面积留白
- 几何装饰元素
- 渐变色点缀
- 现代无衬线字体

---

## 4. 学院复古风

**适用**：历史名校、文法类、师范类院校

**配色方案**：
- 主背景：象牙白 #F5F0E6、米黄 #FAF8F5
- 强调色：深棕 #8B4513、墨绿 #2F4F4F
- 文字色：深棕 #5D4037、中棕 #8D6E63
- 点缀：金色 #C9A227、暗红 #8B0000

**视觉特征**：
- 书卷气氛围
- 徽章、印章元素
- 衬线字体标题
- 纸张纹理背景（5%透明度）

---

## 5. 清新自然风

**适用**：生态校园、师范类、农林类院校

**配色方案**：
- 主背景：奶白 #FAF9F7、浅绿 #F0FDF4
- 强调色：薄荷绿 #B8E0D2、森林绿 #5ABAB7
- 文字色：深灰棕 #3D3832、中灰 #666666
- 点缀：阳光金 #FBBF24

**视觉特征**：
- 自然光感，柔和阴影
- 大面积留白
- 植物装饰元素
- 适合展示校园风景

---

## 背景布局样式

### 卡片镂空式

**描述**：中央内容卡片区域镂空，背后的大学图片透过镂空区域露出

**视觉效果**：
```
┌─────────────────────┐
│   [大学图片背景]      │
│  ┌───────────────┐  │
│  │               │  │
│  │   内容卡片     │  │ ← 镂空区域
│  │   (透明/半透明) │  │
│  │               │  │
│  └───────────────┘  │
│                     │
└─────────────────────┘
```

**Prompt 关键词**：
- `cutout card design`
- `transparent center panel`
- `university photo showing through`
- `framed content area`

---

### 渐变遮罩式

**描述**：大学图片作为全背景，上面叠加渐变遮罩层，文字内容在遮罩上清晰显示

**视觉效果**：
```
┌─────────────────────┐
│ [大学图片] + 渐变遮罩 │
│ ███████████████████ │ ← 深色渐变
│    标题内容         │
│    █████████████    │ ← 浅色渐变
│    详细信息         │
│ ███████████████████ │
└─────────────────────┘
```

**Prompt 关键词**：
- `photo background with gradient overlay`
- `semi-transparent content layer`
- `university campus backdrop`
- `text readable over image`

---

### 边框留白式

**描述**：内容卡片居中，周围留白区域露出大学图片边缘

**视觉效果**：
```
┌─────────────────────┐
│ [图片] ┌─────┐ [图片] │
│       │ 内容 │       │
│ [图片] │ 卡片 │ [图片] │
│       │     │       │
│ [图片] └─────┘ [图片] │
└─────────────────────┘
```

**Prompt 关键词**：
- `centered card with photo border`
- `white space revealing background image`
- `content framed by campus photo`
- `elegant border design`

---

### 分割布局式

**描述**：上半部分展示大学图片，下半部分为内容卡片区域

**视觉效果**：
```
┌─────────────────────┐
│                     │
│    [大学图片区域]    │ ← 约40%高度
│                     │
├─────────────────────┤
│    标题/核心信息     │
│                     │ ← 约60%高度
│    详细内容列表      │
│                     │
└─────────────────────┘
```

**Prompt 关键词**：
- `split layout design`
- `top half campus photo`
- `bottom half content card`
- `horizontal divider`

---

## 风格与布局搭配建议

| 风格 | 推荐布局 | 理由 |
|------|----------|------|
| 青春活力 | 分割布局、卡片镂空 | 动感强，突出校园活力 |
| 专业权威 | 渐变遮罩、边框留白 | 突出信息，强调专业感 |
| 简约现代 | 边框留白、分割布局 | 留白多，干净利落 |
| 学院复古 | 卡片镂空、边框留白 | 经典设计，书卷气 |
| 清新自然 | 分割布局、渐变遮罩 | 自然过渡，柔和舒适 |

---

## 通用负面词库

**色彩**：dark background (except 专业权威), neon colors, fluorescent, high saturation, cyberpunk, cold blue tones, garish colors

**风格**：tech/digital style (except 简约现代), corporate look, stock photo, over-designed, cluttered, heavy filters, 3D render, cartoon, anime

**排版**：tiny text, text overflow, multiple fonts, walls of text, no white space, cramped, misaligned

**质量**：blurry, low quality, pixelated, watermarks, artifacts, noise
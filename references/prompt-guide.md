# Prompt 编写规范

## 核心原则

每个 Prompt 必须 300-500 英文词，包含完整的视觉描述和中文文案。

---

## 工作流程

### 1. 从 Markdown 分析到 HTML 排版

**步骤**：
1. 解析 Markdown 内容结构
2. 确定风格和布局
3. 生成 HTML 设计稿
4. 基于 HTML 编写 Prompt 或直接截图

### 2. HTML 设计规范

**基础尺寸**：
- 画布：1536 × 2048 px（3:4 @ 2K）
- 安全边距：48-64px
- 标题字号：48-72px
- 正文字号：28-36px
- 行高：1.5-1.8

**小红书审美特征**：
- 圆角：8-24px
- 阴影：柔和、轻量
- 留白：充足
- 配色：参考风格配色表
- 字体：思源黑体/苹方/系统默认

---

## HTML 模板库

### 封面图 - 分割布局

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1536px;
      height: 2048px;
      font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    .card {
      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
    }
    /* 图片区域 - 上半部分 */
    .image-section {
      height: 45%;
      background-size: cover;
      background-position: center;
      position: relative;
    }
    .image-section::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      height: 80px;
      background: linear-gradient(transparent, rgba(255,247,237,0.9));
    }
    /* 内容区域 - 下半部分 */
    .content-section {
      height: 55%;
      padding: 48px 64px;
      background: #FFF7ED;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }
    .logo {
      width: 120px;
      height: 120px;
      margin-bottom: 32px;
    }
    .logo img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .title {
      font-size: 72px;
      font-weight: 700;
      color: #78350F;
      line-height: 1.2;
      margin-bottom: 24px;
    }
    .subtitle {
      font-size: 36px;
      color: #F97316;
      margin-bottom: 40px;
    }
    .tags {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
    }
    .tag {
      padding: 12px 24px;
      background: #F97316;
      color: white;
      border-radius: 100px;
      font-size: 24px;
      font-weight: 500;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="image-section" style="background-image: url('campus-1.jpg')"></div>
    <div class="content-section">
      <div class="logo"><img src="logo.png" alt="logo"></div>
      <h1 class="title">浙江大学</h1>
      <p class="subtitle">东方剑桥 · 创新之城</p>
      <div class="tags">
        <span class="tag">综合排名 TOP5</span>
        <span class="tag">就业率 97.6%</span>
        <span class="tag">最美校园</span>
      </div>
    </div>
  </div>
</body>
</html>
```

### 内容图 - 卡片镂空

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1536px;
      height: 2048px;
      font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    .card {
      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
    }
    /* 背景图片 */
    .background {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      filter: brightness(0.7);
    }
    /* 半透明遮罩 */
    .overlay {
      position: absolute;
      inset: 0;
      background: rgba(30, 58, 95, 0.3);
    }
    /* 内容卡片 - 居中镂空 */
    .content-card {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 80%;
      background: rgba(255, 255, 255, 0.95);
      border-radius: 24px;
      padding: 64px 48px;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
    }
    .section-title {
      font-size: 48px;
      font-weight: 700;
      color: #1E293B;
      text-align: center;
      margin-bottom: 48px;
    }
    .info-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
    }
    .info-item {
      background: #F8FAFC;
      padding: 24px;
      border-radius: 16px;
      text-align: center;
    }
    .label {
      display: block;
      font-size: 24px;
      color: #64748B;
      margin-bottom: 8px;
    }
    .value {
      display: block;
      font-size: 36px;
      font-weight: 700;
      color: #1E3A5F;
    }
    .highlight {
      color: #F59E0B;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="background" style="background-image: url('campus-2.jpg')"></div>
    <div class="overlay"></div>
    <div class="content-card">
      <h2 class="section-title">📊 2024录取分数线</h2>
      <div class="info-grid">
        <div class="info-item">
          <span class="label">河南理科</span>
          <span class="value">582分</span>
        </div>
        <div class="info-item">
          <span class="label">山东综合</span>
          <span class="value">578分</span>
        </div>
        <div class="info-item">
          <span class="label">广东物理</span>
          <span class="value">591分</span>
        </div>
        <div class="info-item">
          <span class="label">浙江综合</span>
          <span class="value">586分</span>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```

### 内容图 - 渐变遮罩

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1536px;
      height: 2048px;
      font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    .card {
      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
    }
    /* 背景图片 */
    .background {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
    }
    /* 渐变遮罩 - 从左上到右下 */
    .gradient-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(
        135deg,
        rgba(30, 41, 59, 0.85) 0%,
        rgba(30, 41, 59, 0.6) 40%,
        rgba(30, 41, 59, 0.3) 100%
      );
    }
    /* 内容区域 */
    .content {
      position: relative;
      z-index: 1;
      height: 100%;
      padding: 80px 64px;
      display: flex;
      flex-direction: column;
    }
    .header {
      margin-bottom: auto;
    }
    .title {
      font-size: 56px;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 16px;
    }
    .subtitle {
      font-size: 28px;
      color: #94A3B8;
    }
    .main-content {
      margin-top: auto;
    }
    .feature-list {
      list-style: none;
    }
    .feature-item {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 32px;
    }
    .feature-icon {
      width: 48px;
      height: 48px;
      background: #3B82F6;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      color: white;
      flex-shrink: 0;
    }
    .feature-text {
      flex: 1;
    }
    .feature-title {
      font-size: 32px;
      font-weight: 600;
      color: #FFFFFF;
      margin-bottom: 8px;
    }
    .feature-desc {
      font-size: 24px;
      color: #CBD5E1;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="background" style="background-image: url('campus-3.jpg')"></div>
    <div class="gradient-overlay"></div>
    <div class="content">
      <div class="header">
        <h1 class="title">宿舍条件</h1>
        <p class="subtitle">舒适生活 · 温馨如家</p>
      </div>
      <div class="main-content">
        <ul class="feature-list">
          <li class="feature-item">
            <div class="feature-icon">🏠</div>
            <div class="feature-text">
              <div class="feature-title">4人间 · 上床下桌</div>
              <div class="feature-desc">宽敞舒适，独立空间</div>
            </div>
          </li>
          <li class="feature-item">
            <div class="feature-icon">❄️</div>
            <div class="feature-text">
              <div class="feature-title">空调 + 独立卫浴</div>
              <div class="feature-desc">四季舒适，生活便利</div>
            </div>
          </li>
          <li class="feature-item">
            <div class="feature-icon">🍳</div>
            <div class="feature-text">
              <div class="feature-title">公共厨房 · 洗衣房</div>
              <div class="feature-desc">每层配备，生活无忧</div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>
```

### 收尾图 - 边框留白

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      width: 1536px;
      height: 2048px;
      font-family: -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif;
    }
    .card {
      width: 100%;
      height: 100%;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    /* 背景图片 - 边框展示 */
    .background {
      position: absolute;
      inset: 0;
      background-size: cover;
      background-position: center;
      filter: blur(4px) brightness(0.8);
    }
    /* 内容卡片 - 居中留白 */
    .content-card {
      position: relative;
      z-index: 1;
      width: 75%;
      background: #FFFFFF;
      border-radius: 32px;
      padding: 80px 64px;
      text-align: center;
      box-shadow: 0 30px 80px rgba(0, 0, 0, 0.15);
    }
    .title {
      font-size: 56px;
      font-weight: 700;
      color: #78350F;
      margin-bottom: 48px;
      line-height: 1.3;
    }
    .summary-list {
      text-align: left;
      margin-bottom: 48px;
    }
    .summary-item {
      display: flex;
      align-items: center;
      gap: 16px;
      margin-bottom: 24px;
      font-size: 28px;
      color: #57534E;
    }
    .summary-icon {
      font-size: 32px;
    }
    .cta {
      padding: 24px 48px;
      background: linear-gradient(135deg, #F97316, #FB923C);
      color: white;
      border-radius: 100px;
      font-size: 28px;
      font-weight: 600;
      display: inline-block;
    }
    .cta-subtitle {
      margin-top: 24px;
      font-size: 24px;
      color: #9CA3AF;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="background" style="background-image: url('campus-sunset.jpg')"></div>
    <div class="content-card">
      <h2 class="title">浙江大学<br>等你来打卡 ✨</h2>
      <div class="summary-list">
        <div class="summary-item">
          <span class="summary-icon">🌟</span>
          <span>综合排名 TOP 5</span>
        </div>
        <div class="summary-item">
          <span class="summary-icon">🎯</span>
          <span>王牌专业 15 个</span>
        </div>
        <div class="summary-item">
          <span class="summary-icon">💪</span>
          <span>就业率 97%+</span>
        </div>
      </div>
      <div class="cta">评论区告诉我你的目标专业 👇</div>
      <p class="cta-subtitle">收藏这篇，填志愿用得上 ❤️</p>
    </div>
  </div>
</body>
</html>
```

---

## 从 HTML 到 Prompt

生成 HTML 后，可以：

### 方式一：直接截图

使用 Puppeteer/Playwright 将 HTML 渲染为 PNG 图片。

### 方式二：提取关键信息编写 Prompt

从 HTML 中提取：

```
**Style**: 根据 CSS 配色确定风格
**Background Layout**: 根据结构确定布局
**Background**: 提取 background 相关样式
**Main Subject/Layout**: 提取内容区域结构
**Typography**: 提取字体、字号、颜色
**Text Content**: 提取中文文案
```

---

## 通用负面词库

**色彩**：dark background (except 专业权威风格), neon colors, fluorescent, high saturation, cyberpunk, cold blue tones (except 专业权威风格), garish colors

**风格**：tech/digital style (except 简约现代), corporate look, stock photo appearance, over-designed, cluttered, heavy filters, 3D render, cartoon, anime, clip art

**排版**：tiny text, text overflow, multiple fonts (>3), walls of text, no white space, cramped, misaligned, busy layout

**质量**：blurry, low quality, pixelated, watermarks, artifacts, noise, distorted text

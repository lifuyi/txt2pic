# Instagram 自动化发布脚本

## 功能特点

- ✅ **完全本地运行**：不依赖任何第三方服务或 API
- ✅ **支持所有账号类型**：个人账号、Business 账号、Creator 账号
- ✅ **模拟真人操作**：不会被检测为机器人
- ✅ **自动/手动登录**：可配置自动登录或手动登录
- ✅ **批量上传**：支持多图片轮播图发布
- ✅ **智能等待**：自动等待页面加载和用户操作

## 安装步骤

### 1. 安装依赖

```bash
# 激活虚拟环境（如果已有）
cd /Users/eyeopen/Downloads/projects/xhs-graphic-generator
source venv/bin/activate

# 安装 Playwright
pip install playwright

# 安装浏览器
playwright install chromium
```

### 2. 配置脚本

编辑 `instagram_automation.py` 文件，填写你的 Instagram 账号信息：

```python
# 在第 20-22 行
USERNAME = "你的Instagram用户名"  # 可选，留空则手动登录
PASSWORD = "你的Instagram密码"  # 可选，留空则手动登录
```

**安全提示**：
- 如果不填写用户名密码，脚本会进入手动登录模式（更安全）
- 如果填写，脚本会自动登录（更方便）
- 建议首次运行使用手动登录模式

### 3. 确认图片路径

默认图片路径：
```python
IMAGES_DIR = "/Users/eyeopen/Downloads/projects/xhs-graphic-generator/output/20260312214712"
```

这是英文版图片的目录。如果要发布中文版，修改为：
```python
IMAGES_DIR = "/Users/eyeopen/Downloads/projects/xhs-graphic-generator/output/20260312211841"
```

### 4. 确认文案

脚本已包含完整的英文版文案。如需修改，编辑 `CAPTION` 变量。

## 使用方法

### 运行脚本

```bash
# 激活虚拟环境
source venv/bin/activate

# 运行自动化脚本
python instagram_automation.py
```

### 操作流程

1. **启动浏览器**
   - 脚本会自动打开 Chrome 浏览器
   - 访问 Instagram 网站

2. **登录 Instagram**
   - 如果配置了用户名密码：自动登录
   - 如果没有配置：手动登录（60秒时间）

3. **创建新帖子**
   - 脚本自动点击 "Create" 或 "+" 按钮
   - 进入图片上传界面

4. **上传图片**
   - 脚本会提示你手动选择图片文件
   - 打开文件选择对话框
   - **按住 Command/Ctrl 键**，选择所有 7 张图片
   - 点击 "打开" 上传

5. **调整图片（如果需要）**
   - Instagram 会显示图片预览
   - 可以调整顺序或裁剪（可选）
   - 点击 "Next"

6. **填写文案**
   - 脚本自动填写文案
   - 如果失败，会显示文案让你手动复制粘贴

7. **发布**
   - 脚本自动点击 "Share" 按钮
   - 等待发布完成

8. **完成**
   - 脚本会显示发布成功
   - 10秒后自动关闭浏览器

## 注意事项

⚠️ **重要提示**：

1. **首次运行**：建议使用手动登录模式，确保账号安全
2. **网络连接**：需要稳定的网络连接
3. **Instagram 限制**：
   - 24小时内最多发布 25 条帖子
   - 频繁发布可能触发验证码
4. **图片格式**：支持 JPG、PNG，已准备好的图片符合要求
5. **文案长度**：Instagram 文案最多 2200 字符，当前文案符合要求
6. **浏览器自动化**：
   - 运行时请勿移动鼠标或键盘
   - 如果自动操作失败，脚本会提示手动操作
   - 按照屏幕提示操作即可

## 故障排除

### 问题：浏览器无法启动
**解决**：确保已安装 Chromium：`playwright install chromium`

### 问题：找不到元素
**解决**：Instagram 可能更新了页面结构，需要更新脚本中的选择器

### 问题：登录失败
**解决**：
- 检查用户名密码是否正确
- 尝试手动登录模式
- 检查是否触发了 Instagram 的安全验证

### 问题：上传失败
**解决**：
- 检查图片路径是否正确
- 确保图片文件存在
- 尝试手动上传

### 问题：发布失败
**解决**：
- 检查网络连接
- 确认账号没有发布限制
- 查看 Instagram 是否有错误提示

## 安全说明

🔒 **隐私保护**：

- 脚本完全在本地运行，不会发送任何数据到外部服务器
- 用户名密码（如果配置）仅用于自动登录，不会被存储或传输
- 建议使用手动登录模式，更安全
- 可以在脚本运行后修改密码（如果使用自动登录）

## 自定义

### 修改发布内容

编辑 `instagram_automation.py`：

```python
# 修改图片目录
IMAGES_DIR = "/path/to/your/images"

# 修改文案
CAPTION = """你的文案内容

#标签 #标签2 #标签3
"""

# 修改账号信息
USERNAME = "your_username"  # 或留空使用手动登录
PASSWORD = "your_password"  # 或留空使用手动登录
```

### 调整等待时间

如果网络较慢，可以增加等待时间：

```python
# 在相关位置修改等待时间
await asyncio.sleep(5)  # 改为 10 或更高
```

## 技术说明

- **框架**：Playwright for Python
- **浏览器**：Chromium（Chrome 开源版本）
- **语言**：Python 3.7+
- **异步**：使用 asyncio 实现异步操作
- **选择器**：使用 CSS 选择器和文本选择器定位元素

## 更新日志

- 2024-03-12: 初始版本

## 许可证

本项目仅供学习和个人使用。使用自动化工具请遵守 Instagram 的服务条款。

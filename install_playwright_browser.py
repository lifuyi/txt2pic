#!/usr/bin/env python3
"""安装 Playwright 浏览器"""

from playwright.async_api import async_playwright
import asyncio

async def install_browser():
    print("正在安装 Playwright Chromium 浏览器...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        await browser.close()
    print("✅ 浏览器安装完成！")

if __name__ == "__main__":
    asyncio.run(install_browser())

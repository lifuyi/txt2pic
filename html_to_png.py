#!/usr/bin/env python3
"""Convert HTML files to PNG using Playwright"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import sys
import os

def html_to_png(html_path: str, output_path: str):
    """Convert a single HTML file to PNG"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_viewport_size({"width": 1536, "height": 2048})
        page.goto(f"file://{os.path.abspath(html_path)}")
        page.screenshot(path=output_path, full_page=False)
        browser.close()
        print(f"  ✓ {Path(output_path).name}")

def convert_folder(folder_path: str):
    """Convert all HTML files in a folder"""
    folder = Path(folder_path)
    html_files = sorted(folder.glob("*.html"))
    
    if not html_files:
        print(f"  No HTML files found in {folder_path}")
        return
    
    print(f"\n📁 {folder.name}")
    print(f"   Converting {len(html_files)} HTML files...")
    
    for html_file in html_files:
        png_name = html_file.stem + ".png"
        png_path = folder / png_name
        html_to_png(str(html_file), str(png_path))
    
    print(f"   ✅ Done!")

def convert_all_output_folders():
    """Convert HTML files in all output subfolders"""
    output_dir = Path("output")
    
    if not output_dir.exists():
        print("❌ Output directory not found!")
        return
    
    folders = [f for f in output_dir.iterdir() if f.is_dir()]
    
    if not folders:
        print("❌ No output folders found!")
        return
    
    print(f"\n{'='*60}")
    print(f"🖼️  HTML to PNG Converter")
    print(f"{'='*60}")
    
    for folder in sorted(folders):
        html_files = list(folder.glob("*.html"))
        if html_files:
            convert_folder(str(folder))
    
    print(f"\n{'='*60}")
    print("🎉 All conversions complete!")
    print(f"{'='*60}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--all":
            convert_all_output_folders()
        else:
            convert_folder(sys.argv[1])
    else:
        # Convert latest folder
        output_dir = Path("output")
        folders = [f for f in output_dir.iterdir() if f.is_dir()]
        if not folders:
            print("❌ No output folders found!")
            exit(1)
        latest_folder = max(folders, key=lambda x: x.stat().st_mtime)
        convert_folder(str(latest_folder))

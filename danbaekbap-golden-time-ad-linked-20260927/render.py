#!/usr/bin/env python3
"""Render each local HTML card to a review JPEG with a fixed viewport."""
import subprocess
from pathlib import Path
from PIL import Image

root=Path(__file__).resolve().parent
chrome='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for html in sorted(root.glob('0?_*.html')):
    png=root/(html.stem+'.png')
    jpg=root/(html.stem+'.jpg')
    cmd=[chrome,'--headless=new','--disable-gpu','--hide-scrollbars','--no-first-run','--no-default-browser-check',
         '--window-size=860,1600','--force-device-scale-factor=2','--virtual-time-budget=2500',
         f'--screenshot={png}',html.as_uri()]
    result=subprocess.run(cmd,capture_output=True,text=True,timeout=40)
    if result.returncode or not png.exists():
        raise RuntimeError(f'{html.name}: Chrome render failed: {result.stderr[-600:]}')
    with Image.open(png) as im:
        if im.size!=(1720,3200):
            raise RuntimeError(f'{html.name}: wrong image size {im.size}')
        im.convert('RGB').save(jpg,quality=88,optimize=True,subsampling=0)
    png.unlink()
    print(f'{jpg.name} {jpg.stat().st_size:,} bytes',flush=True)

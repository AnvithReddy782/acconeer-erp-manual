# scripts/assemble_manual.py
import os
import sys

# Ensure current directory is in path
sys.path.insert(0, os.path.dirname(__file__))

from generate_complete_manual import get_css
from pages_p01_p08 import (
    get_page_01, get_page_02, get_page_03, get_page_04,
    get_page_05, get_page_06, get_page_07, get_page_08
)
from pages_p09_p16 import (
    get_page_09, get_page_10, get_page_11, get_page_12,
    get_page_13, get_page_14, get_page_15, get_page_16
)
from pages_p17_p26 import (
    get_page_17, get_page_18, get_page_19, get_page_20,
    get_page_21, get_page_22, get_page_23, get_page_24,
    get_page_25, get_page_26
)

def build_full_html():
    css = get_css()
    
    pages = [
        get_page_01(),
        get_page_02(),
        get_page_03(),
        get_page_04(),
        get_page_05(),
        get_page_06(),
        get_page_07(),
        get_page_08(),
        get_page_09(),
        get_page_10(),
        get_page_11(),
        get_page_12(),
        get_page_13(),
        get_page_14(),
        get_page_15(),
        get_page_16(),
        get_page_17(),
        get_page_18(),
        get_page_19(),
        get_page_20(),
        get_page_21(),
        get_page_22(),
        get_page_23(),
        get_page_24(),
        get_page_25(),
        get_page_26()
    ]
    
    pages_html = "\n".join(pages)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Acconeer ERP — Enterprise Operations Manual (Volume I: Universal Standard)</title>
  <style>
{css}
  </style>
</head>
<body>
{pages_html}
</body>
</html>
"""
    
    output_path = "acconeer-user-manual.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    print(f"[Assembly Success] Wrote {len(full_html)} characters across {len(pages)} pages to {output_path}.")
    return output_path

if __name__ == "__main__":
    build_full_html()

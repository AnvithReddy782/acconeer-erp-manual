import fitz

doc = fitz.open("Acconeer_ERP_Operations_Manual.pdf")

for pno in range(len(doc)):
    page = doc[pno]
    rect = page.rect
    blocks = page.get_text("blocks")
    if not blocks:
        print(f"Page {pno+1}: EMPTY!")
        continue
    # find lowest y coordinate of text/block
    lowest_y = max(b[3] for b in blocks if not b[4].startswith("Page") and not "Currency: AED" in b[4])
    height = rect.height
    bottom_margin = height - lowest_y
    text_sample = blocks[0][4][:40].strip() if blocks else ""
    last_block = blocks[-1][4].strip()
    
    print(f"Page {pno+1:02d}: lowest_y={lowest_y:.1f}/{height:.1f} (bottom gap: {bottom_margin:.1f} pt) | Last line: '{last_block[:50]}'")

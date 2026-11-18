# scripts/compile_and_verify_pdf.py
import subprocess
import os
import time
import fitz

html_abs_path = os.path.abspath("acconeer-user-manual.html").replace("\\", "/")
pdf_abs_path = os.path.abspath("Acconeer_ERP_Operations_Manual.pdf").replace("\\", "/")
file_url = f"file:///{html_abs_path}"

browse_cli = r"C:\Users\anvit\.claude\skills\gstack\browse\dist\browse.exe"

print(f"[PDF Compiler] Navigating to: {file_url}")
res = subprocess.run([browse_cli, "goto", file_url], capture_output=True, text=True)
print(f"[PDF Compiler] Goto result: {res.stdout.strip()} {res.stderr.strip()}")

print("[PDF Compiler] Waiting for network idle...")
res_wait = subprocess.run([browse_cli, "wait", "--networkidle"], capture_output=True, text=True)
print(f"[PDF Compiler] Wait result: {res_wait.stdout.strip()}")

time.sleep(2)

print(f"[PDF Compiler] Generating PDF: {pdf_abs_path}")
res_pdf = subprocess.run([browse_cli, "pdf", pdf_abs_path], capture_output=True, text=True)
print(f"[PDF Compiler] PDF result: {res_pdf.stdout.strip()} {res_pdf.stderr.strip()}")

if os.path.exists(pdf_abs_path):
    size_mb = os.path.getsize(pdf_abs_path) / (1024 * 1024)
    print(f"[PDF Compiler] PDF successfully generated! File size: {size_mb:.2f} MB")
    
    doc = fitz.open(pdf_abs_path)
    total_pages = len(doc)
    print(f"[PDF Compiler] Total Pages in PDF: {total_pages}")
    
    os.makedirs("previews_v3", exist_ok=True)
    for pno in range(total_pages):
        page = doc[pno]
        pix = page.get_pixmap(dpi=150)
        preview_file = f"previews_v3/page_{pno+1:02d}.png"
        pix.save(preview_file)
    print(f"[PDF Compiler] Successfully rendered all {total_pages} page previews in previews_v3/")
else:
    print("[PDF Compiler] ERROR: PDF was not generated!")

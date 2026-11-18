# scripts/generate_complete_manual.py
import os
import base64

def get_base64_logo():
    if os.path.exists("spectrum-zestwings-logo.png"):
        with open("spectrum-zestwings-logo.png", "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def get_base64_shield():
    if os.path.exists("spectrum_shield.png"):
        with open("spectrum_shield.png", "rb") as f:
            return f"data:image/png;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def window_frame(img_path, caption, route, legend_items, tenant=""):
    legend_html = "".join([
        f'<div class="legend-item"><span class="legend-badge">{idx+1}</span> <span><strong>{item[0]}:</strong> {item[1]}</span></div>'
        for idx, item in enumerate(legend_items)
    ])
    return f"""
      <div class="screenshot-card">
        <div class="screenshot-viewport">
          <img src="{img_path}" alt="{caption}">
        </div>
        <div class="screenshot-caption">
          <span><strong>Interface Capture:</strong> {caption}</span>
          <span class="badge-mono">{route}</span>
        </div>
      </div>
      <div class="figure-legend">{legend_html}</div>
    """

def get_css():
    shield_b64 = get_base64_shield()
    watermark_css = f'--watermark-bg: url("{shield_b64}");' if shield_b64 else '--watermark-bg: none;'
    
    css_template = """
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

    :root {
      /* WATERMARK_VAR */
      --font-sans: "Poppins", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-mono: "JetBrains Mono", monospace;
      --font-display: "Poppins", -apple-system, BlinkMacSystemFont, sans-serif;

      --color-navy: #0F172A;
      --color-slate-900: #0F172A;
      --color-slate-800: #1E293B;
      --color-slate-700: #334155;
      --color-slate-600: #475569;
      --color-slate-500: #64748B;
      --color-slate-400: #94A3B8;
      --color-slate-300: #CBD5E1;
      --color-slate-200: #E2E8F0;
      --color-slate-100: #F1F5F9;
      --color-slate-50: #F8FAFC;

      --color-blue: #0052CC;
      --color-blue-dark: #0747A6;
      --color-blue-light: #F0F6FF;
      --color-blue-tint: #EBF3FE;

      --color-red: #DC2626;
      --color-red-light: #FEF2F2;

      --color-green: #15803D;
      --color-green-light: #DCFCE7;

      --color-amber: #B45309;
      --color-amber-light: #FEF3C7;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--font-sans);
      font-size: 8.2pt;
      line-height: 1.48;
      color: var(--color-slate-700);
      background-color: #FFFFFF;
      -webkit-font-smoothing: antialiased;
      print-color-adjust: exact;
      -webkit-print-color-adjust: exact;
    }

    @page {
      size: A4 portrait;
      margin: 11mm 13mm 13mm 13mm;
      @top-left {
        content: "Acconeer ERP — Enterprise Operations Manual (Volume I: Universal Edition)";
        font-family: var(--font-sans);
        font-size: 6.8pt;
        font-weight: 500;
        color: #64748B;
      }
      @top-right {
        content: "Spectrum Zestwings Technologies LLC";
        font-family: var(--font-sans);
        font-size: 6.8pt;
        font-weight: 600;
        color: #0052CC;
      }
      @bottom-left {
        content: "Enterprise Cloud ERP • UAE Statutory & GCC Standard • Currency: AED";
        font-family: var(--font-sans);
        font-size: 6.6pt;
        color: #94A3B8;
      }
      @bottom-right {
        content: "Page " counter(page);
        font-family: var(--font-mono);
        font-size: 6.8pt;
        font-weight: 600;
        color: #0F172A;
      }
    }

    @page:first {
      margin: 0;
      @top-left { content: normal; }
      @top-right { content: normal; }
      @bottom-left { content: normal; }
      @bottom-right { content: normal; }
    }

    .page {
      position: relative;
      height: 273mm;
      max-height: 273mm;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      page-break-after: always;
      break-after: page;
      box-sizing: border-box;
    }

    .page::before {
      content: "";
      position: absolute;
      top: 50%;
      left: 50%;
      width: 330px;
      height: 330px;
      transform: translate(-50%, -50%);
      background-image: var(--watermark-bg);
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      opacity: 0.038;
      pointer-events: none;
      z-index: 0;
    }

    .cover-page-wrapper::before {
      display: none !important;
    }

    .page > * {
      position: relative;
      z-index: 1;
    }

    @media screen {
      body {
        background-color: #F1F5F9;
        padding: 24px 0;
      }
      .page {
        width: 210mm;
        margin: 0 auto 24px auto;
        padding: 11mm 13mm 13mm 13mm;
        background: #FFFFFF;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.12);
        border-radius: 6px;
      }
      .cover-page-wrapper {
        padding: 0 !important;
      }
    }

    @media print {
      body {
        background: #FFFFFF;
      }
      .page {
        width: 100% !important;
        height: 273mm !important;
        max-height: 273mm !important;
        margin: 0 !important;
        padding: 0 !important;
        border: none !important;
        box-shadow: none !important;
        page-break-after: always;
        break-after: page;
      }
      .cover-page-wrapper {
        height: 297mm !important;
        max-height: 297mm !important;
      }
    }

    /* Headings */
    h1, h2, h3, h4 {
      font-family: var(--font-display);
      color: var(--color-navy);
      letter-spacing: -0.015em;
    }

    h1 {
      font-size: 15.5pt;
      font-weight: 700;
      line-height: 1.15;
      margin-bottom: 2pt;
    }

    h2 {
      font-size: 10pt;
      font-weight: 600;
      line-height: 1.25;
      margin-top: 5pt;
      margin-bottom: 3.5pt;
      padding-bottom: 1.5pt;
      border-bottom: 1px solid var(--color-slate-200);
      display: flex;
      align-items: center;
      gap: 5px;
    }

    p {
      margin-bottom: 4.5pt;
      color: var(--color-slate-700);
      font-size: 8pt;
      line-height: 1.48;
    }

    strong {
      color: var(--color-navy);
      font-weight: 600;
    }

    .brand-divider {
      display: inline-flex;
      height: 2.5px;
      border-radius: 2px;
      overflow: hidden;
      margin-bottom: 3pt;
    }
    .brand-divider-red { width: 20px; background: var(--color-red); }
    .brand-divider-blue { width: 35px; background: var(--color-blue); }

    .chapter-header {
      margin-bottom: 3pt;
      padding-bottom: 2.5pt;
      border-bottom: 2px solid var(--color-navy);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .chapter-pill {
      display: inline-block;
      background: var(--color-navy);
      color: #FFFFFF;
      font-family: var(--font-mono);
      font-size: 6.4pt;
      font-weight: 600;
      letter-spacing: 0.08em;
      padding: 1px 5px;
      border-radius: 3px;
      text-transform: uppercase;
      margin-bottom: 2pt;
    }
    .chapter-title {
      font-size: 13pt;
      font-weight: 700;
      color: var(--color-navy);
      line-height: 1.15;
    }
    .chapter-cat {
      font-family: var(--font-mono);
      font-size: 6.6pt;
      font-weight: 600;
      color: var(--color-blue);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .nav-breadcrumb {
      background: var(--color-slate-50);
      border: 1px solid var(--color-slate-200);
      border-left: 3px solid var(--color-blue);
      border-radius: 4px;
      padding: 2.5pt 5.5pt;
      margin-bottom: 3.5pt;
      font-size: 7pt;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .nav-breadcrumb strong { color: var(--color-navy); }

    .badge-mono {
      font-family: var(--font-mono);
      font-size: 6.4pt;
      font-weight: 600;
      padding: 1px 4pt;
      border-radius: 3px;
      background: var(--color-slate-100);
      color: var(--color-slate-800);
      border: 1px solid var(--color-slate-300);
      display: inline-block;
      white-space: nowrap;
    }
    .badge-blue { background: var(--color-blue-tint); color: var(--color-blue); border-color: #BFDBFE; }
    .badge-green { background: var(--color-green-light); color: var(--color-green); border-color: #BBF7D0; }
    .badge-amber { background: var(--color-amber-light); color: var(--color-amber); border-color: #FDE68A; }
    .badge-red { background: var(--color-red-light); color: var(--color-red); border-color: #FECACA; }

    /* Clean Enterprise Screenshot Card (No Desktop Window Chrome) */
    .screenshot-card, .window-frame {
      margin: 3.5pt 0 2.5pt 0;
      border: 1px solid var(--color-slate-200);
      border-radius: 4.5px;
      overflow: hidden;
      background: #FFFFFF;
      box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
    }
    .screenshot-viewport, .window-viewport {
      background: #FFFFFF;
      line-height: 0;
      padding: 0;
      border-bottom: 1px solid var(--color-slate-100);
      text-align: center;
    }
    .screenshot-viewport img, .window-viewport img {
      width: 100%;
      height: auto;
      max-height: 235px;
      object-fit: contain;
      display: block;
    }
    .screenshot-caption, .window-caption {
      background: var(--color-slate-50);
      border-top: 1px solid var(--color-slate-200);
      padding: 2.5pt 6pt;
      font-size: 6.7pt;
      color: var(--color-slate-600);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .screenshot-caption strong, .window-caption strong {
      color: var(--color-navy);
      font-weight: 600;
    }

    .figure-legend {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2.5pt 6pt;
      background: var(--color-slate-50);
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 4.5pt 7pt;
      margin-bottom: 4.5pt;
      font-size: 7.4pt;
      line-height: 1.4;
      color: var(--color-slate-700);
    }
    .legend-item { display: flex; align-items: flex-start; gap: 4px; }
    .legend-badge {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 11.5px;
      height: 11.5px;
      border-radius: 50%;
      background: var(--color-blue);
      color: #FFFFFF;
      font-family: var(--font-mono);
      font-size: 5.8pt;
      font-weight: 700;
      flex-shrink: 0;
      margin-top: 1px;
    }

    /* Standard Tables */
    .doc-table {
      width: 100%;
      border-collapse: collapse;
      margin: 4.5pt 0;
      font-size: 7.6pt;
      line-height: 1.42;
      background: #FFFFFF;
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      overflow: hidden;
    }
    .doc-table th {
      background: var(--color-slate-50);
      color: var(--color-navy);
      font-weight: 600;
      text-align: left;
      padding: 3.5pt 5.5pt;
      border-bottom: 1.2px solid var(--color-slate-300);
      font-size: 6.4pt;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }
    .doc-table td {
      padding: 3.5pt 5.5pt;
      border-bottom: 1px solid var(--color-slate-200);
      color: var(--color-slate-700);
      vertical-align: top;
    }
    .doc-table tr:last-child td { border-bottom: none; }
    .doc-table .col-field { font-family: var(--font-mono); font-weight: 600; color: var(--color-blue); width: 23%; }

    /* Custom Unique Cards Per Module */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3.5pt;
      margin: 5pt 0;
    }
    .kpi-card {
      background: var(--color-slate-50);
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 5.5pt 7.5pt;
    }
    .kpi-label { font-size: 6.2pt; font-family: var(--font-mono); text-transform: uppercase; color: var(--color-slate-500); font-weight: 600; }
    .kpi-val { font-size: 9pt; font-weight: 700; color: var(--color-navy); margin: 1pt 0; }
    .kpi-sub { font-size: 6.2pt; color: var(--color-slate-600); }

    .proc-box {
      background: #FFFFFF;
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 5.5pt 8pt;
      margin-top: 5pt;
    }
    .proc-title {
      font-size: 7.4pt;
      font-weight: 600;
      color: var(--color-navy);
      margin-bottom: 2pt;
      display: flex;
      align-items: center;
      gap: 4px;
    }
    .proc-steps { margin-left: 10pt; font-size: 7pt; line-height: 1.38; color: var(--color-slate-700); }
    .proc-steps li { margin-bottom: 1pt; }

    .note-card {
      background: var(--color-slate-50);
      border: 1px solid var(--color-slate-200);
      border-left: 3px solid var(--color-blue);
      border-radius: 4px;
      padding: 3.5pt 5.5pt;
      margin: 5pt 0;
      font-size: 7.6pt;
      line-height: 1.46;
    }
    .note-card-title {
      font-size: 6.6pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--color-blue);
      margin-bottom: 1pt;
    }

    .warning-card {
      background: #FFFBEB;
      border: 1px solid #FDE68A;
      border-left: 3px solid #F59E0B;
      border-radius: 4px;
      padding: 3.5pt 5.5pt;
      margin: 4pt 0;
      font-size: 7.4pt;
      line-height: 1.42;
      color: #92400E;
    }
    .warning-card strong { color: #78350F; }

    .sop-meta-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4pt;
      margin: 3pt 0 4pt 0;
      background: var(--color-slate-50);
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 3.5pt 6pt;
      font-size: 6.8pt;
    }
    .sop-meta-item { display: flex; flex-direction: column; }
    .sop-meta-title { font-family: var(--font-mono); font-size: 6.1pt; font-weight: 700; text-transform: uppercase; color: var(--color-slate-500); margin-bottom: 1px; }
    .sop-meta-desc { color: var(--color-slate-800); font-weight: 500; line-height: 1.32; }

    .reversal-card {
      background: #F8FAFC;
      border: 1px solid #CBD5E1;
      border-left: 3px solid #0052CC;
      border-radius: 4px;
      padding: 3.5pt 6pt;
      margin: 3.5pt 0;
      font-size: 7.2pt;
      line-height: 1.4;
      color: var(--color-slate-700);
    }
    .reversal-card strong { color: var(--color-navy); }
    .reversal-card-title {
      font-size: 6.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #0052CC;
      margin-bottom: 1.5pt;
    }

    .error-card {
      background: #FEF2F2;
      border: 1px solid #FECACA;
      border-left: 3px solid #DC2626;
      border-radius: 4px;
      padding: 3.5pt 6pt;
      margin: 3.5pt 0;
      font-size: 7.2pt;
      line-height: 1.4;
      color: #991B1B;
    }
    .error-card strong { color: #7F1D1D; }
    .error-card-title {
      font-size: 6.5pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #DC2626;
      margin-bottom: 1.5pt;
    }

    .matching-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3.5pt;
      margin: 5pt 0;
    }
    .matching-card {
      background: #FFFFFF;
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 3.5pt 5.5pt;
    }
    .matching-card h4 { font-size: 6.8pt; text-transform: uppercase; color: var(--color-blue); font-weight: 700; margin-bottom: 1.5pt; }
    .matching-card p { font-size: 6.6pt; line-height: 1.34; margin: 0; }

    .journal-demo-card {
      background: #FFFFFF;
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 4.5pt 6pt;
      margin: 5pt 0;
      font-family: var(--font-mono);
      font-size: 6.8pt;
    }
    .journal-demo-header {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px solid var(--color-slate-200);
      padding-bottom: 2pt;
      margin-bottom: 2.5pt;
      font-weight: 600;
      color: var(--color-navy);
    }
    .journal-demo-row {
      display: flex;
      justify-content: space-between;
      padding: 1.5pt 0;
      border-bottom: 1px dashed var(--color-slate-100);
    }
    .journal-demo-total {
      display: flex;
      justify-content: space-between;
      font-weight: 700;
      border-top: 1.5px solid var(--color-navy);
      padding-top: 2pt;
      margin-top: 2pt;
      color: var(--color-navy);
    }

    .process-strip {
      background: var(--color-slate-50);
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      padding: 3pt 5.5pt;
      margin: 3pt 0;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 2.5pt;
      font-size: 6.8pt;
    }
    .process-strip-title { font-family: var(--font-mono); font-weight: 600; font-size: 6.4pt; text-transform: uppercase; color: var(--color-slate-500); margin-right: 3px; }
    .process-node { background: #FFFFFF; border: 1px solid var(--color-slate-300); border-radius: 3px; padding: 1px 4pt; font-weight: 600; color: var(--color-slate-800); font-size: 6.6pt; }
    .process-node-active { background: var(--color-blue-tint); border-color: var(--color-blue); color: var(--color-blue); }
    .process-arrow { color: var(--color-slate-400); font-weight: 700; margin: 0 1px; }

    /* Cover Page */
    .cover-page-wrapper {
      min-height: 297mm;
      height: 297mm;
      max-height: 297mm;
      padding: 24mm 20mm 20mm 20mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
      background: linear-gradient(150deg, #070D1E 0%, #0F172A 48%, #172554 100%);
      color: #FFFFFF;
      page-break-after: always;
      break-after: page;
    }
    .cover-top { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255, 255, 255, 0.15); padding-bottom: 14px; }
    .cover-logo-box { background: #FFFFFF; padding: 7px 16px; border-radius: 6px; display: inline-flex; align-items: center; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.35); }
    .cover-logo-box img { height: 36px; width: auto; object-fit: contain; }
    .cover-badge-top { background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 20px; padding: 3.5px 9px; font-family: var(--font-mono); font-size: 6.6pt; font-weight: 600; letter-spacing: 0.06em; color: #93C5FD; text-transform: uppercase; display: flex; align-items: center; gap: 5px; }
    .cover-dot { width: 5px; height: 5px; background: #38BDF8; border-radius: 50%; }
    .cover-body { margin: 22px 0; }
    .cover-eyebrow { display: inline-block; background: var(--color-blue); color: #FFFFFF; font-family: var(--font-mono); font-size: 6.6pt; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; padding: 2px 7.5px; border-radius: 3.5px; margin-bottom: 9pt; }
    .cover-title { font-size: 34pt; font-weight: 700; line-height: 1.05; letter-spacing: -0.02em; color: #FFFFFF; margin-bottom: 4pt; }
    .cover-subtitle { font-size: 13.5pt; font-weight: 500; line-height: 1.35; color: #93C5FD; margin-bottom: 11pt; }
    .cover-rule { display: flex; height: 4px; border-radius: 2px; overflow: hidden; margin-bottom: 15pt; }
    .cover-rule-red { width: 36px; background: #DC2626; }
    .cover-rule-blue { width: 95px; background: #0052CC; }
    .cover-desc { font-size: 8.8pt; line-height: 1.55; color: #CBD5E1; max-width: 610px; margin-bottom: 18pt; }
    .cover-meta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 7.5px; max-width: 630px; }
    .cover-meta-card { background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.14); border-radius: 5px; padding: 5.5pt 9pt; }
    .cover-meta-label { font-family: var(--font-mono); font-size: 6.2pt; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #93C5FD; margin-bottom: 1.5px; }
    .cover-meta-val { font-size: 7.8pt; font-weight: 500; color: #FFFFFF; }
    .cover-footer { border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 9px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 6.6pt; color: #94A3B8; }
    .cover-footer strong { color: #FFFFFF; }

    /* TOC */
    .toc-card { background: var(--color-slate-50); border: 1px solid var(--color-slate-200); border-radius: 5px; padding: 7pt 10pt; margin: 5pt 0; }
    .toc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3.5pt 14pt; }
    .toc-row { display: flex; justify-content: space-between; align-items: center; padding: 2.2pt 0; border-bottom: 1px dashed var(--color-slate-200); font-size: 7.2pt; }
    .toc-num { font-family: var(--font-mono); font-weight: 600; color: var(--color-blue); margin-right: 5px; }
    .toc-name { font-weight: 500; color: var(--color-navy); flex: 1; }
    .toc-pnum { font-family: var(--font-mono); font-weight: 600; color: var(--color-slate-500); }
    """
    return css_template.replace("/* WATERMARK_VAR */", watermark_css)

print("Helper definitions initialized.")

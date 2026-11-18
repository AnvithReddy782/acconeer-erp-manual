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

def window_frame(img_path, caption, route, legend_items):
    """
    Minimalist enterprise screenshot frame:
    - Pure white background
    - Crisp 1px hairline border
    - Clean horizontal/2-column legend key without tinted container boxes
    """
    legend_html = "".join([
        f'<div class="legend-entry"><span class="legend-num">[{idx+1}]</span> <strong>{item[0]}:</strong> <span>{item[1]}</span></div>'
        for idx, item in enumerate(legend_items)
    ])
    return f"""
      <div class="screenshot-card">
        <div class="screenshot-viewport">
          <img src="{img_path}" alt="{caption}">
        </div>
        <div class="screenshot-caption">
          <span><strong>Screen Capture:</strong> {caption}</span>
          <span class="badge-route">{route}</span>
        </div>
      </div>
      <div class="screen-legend">{legend_html}</div>
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

      --color-amber: #B45309;
      --color-red: #DC2626;
      --color-green: #15803D;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--font-sans);
      font-size: 8.1pt;
      line-height: 1.45;
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
        content: "Acconeer ERP — User Operations Manual & Guide";
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
        content: "Universal Enterprise Edition • Cloud ERP • Currency: AED";
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
      background: #FFFFFF;
    }

    /* Subtle Authenticity Watermark (< 2.2% opacity) */
    .page::before {
      content: "";
      position: absolute;
      top: 50%;
      left: 50%;
      width: 320px;
      height: 320px;
      transform: translate(-50%, -50%);
      background-image: var(--watermark-bg);
      background-size: contain;
      background-repeat: no-repeat;
      background-position: center;
      opacity: 0.020;
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
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.08);
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

    /* Headings & Typography */
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
      font-size: 9.5pt;
      font-weight: 600;
      line-height: 1.25;
      margin-top: 5pt;
      margin-bottom: 2.5pt;
      padding-bottom: 1.5pt;
      border-bottom: 1px solid var(--color-slate-200);
      color: var(--color-navy);
    }

    h3 {
      font-size: 8.2pt;
      font-weight: 600;
      color: var(--color-blue);
      margin-top: 4pt;
      margin-bottom: 2pt;
    }

    p {
      margin-bottom: 4pt;
      color: var(--color-slate-700);
      font-size: 7.9pt;
      line-height: 1.45;
    }

    strong {
      color: var(--color-navy);
      font-weight: 600;
    }

    code {
      font-family: var(--font-mono);
      font-size: 7.2pt;
      color: var(--color-blue);
      background: #F8FAFC;
      padding: 0.5px 3.5px;
      border: 1px solid var(--color-slate-200);
      border-radius: 2.5px;
    }

    kbd {
      font-family: var(--font-mono);
      font-size: 6.8pt;
      font-weight: 600;
      color: var(--color-navy);
      background: #FFFFFF;
      padding: 1px 4px;
      border: 1px solid var(--color-slate-300);
      border-radius: 3px;
      box-shadow: 0 1px 0 rgba(15, 23, 42, 0.1);
      display: inline-block;
    }

    /* Chapter Header */
    .chapter-header {
      margin-bottom: 3.5pt;
      padding-bottom: 3pt;
      border-bottom: 1.5px solid var(--color-navy);
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
    }
    .chapter-category {
      font-family: var(--font-mono);
      font-size: 6.5pt;
      font-weight: 600;
      color: var(--color-blue);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1.5pt;
    }
    .chapter-title {
      font-size: 13pt;
      font-weight: 700;
      color: var(--color-navy);
      line-height: 1.15;
    }
    .chapter-right-meta {
      font-family: var(--font-mono);
      font-size: 6.6pt;
      color: var(--color-slate-500);
      text-align: right;
    }

    /* Minimalist Navigation Path (No Tinted Box) */
    .nav-path {
      font-family: var(--font-mono);
      font-size: 7pt;
      color: var(--color-slate-500);
      margin-bottom: 3.5pt;
      display: flex;
      align-items: center;
      gap: 5px;
    }
    .nav-path strong {
      color: var(--color-blue);
      text-transform: uppercase;
      font-size: 6.5pt;
    }

    /* Minimalist Screenshot Card */
    .screenshot-card {
      margin: 3.5pt 0 2pt 0;
      border: 1px solid var(--color-slate-200);
      border-radius: 4px;
      overflow: hidden;
      background: #FFFFFF;
    }
    .screenshot-viewport {
      background: #FFFFFF;
      line-height: 0;
      padding: 0;
      text-align: center;
    }
    .screenshot-viewport img {
      width: 100%;
      height: auto;
      max-height: 235px;
      object-fit: contain;
      display: block;
    }
    .screenshot-caption {
      border-top: 1px solid var(--color-slate-200);
      padding: 2.5pt 6pt;
      font-size: 6.7pt;
      color: var(--color-slate-600);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #FFFFFF;
    }
    .badge-route {
      font-family: var(--font-mono);
      font-size: 6.4pt;
      font-weight: 600;
      padding: 0.5px 4.5px;
      border-radius: 2px;
      color: var(--color-slate-700);
      border: 1px solid var(--color-slate-300);
      background: #FFFFFF;
    }

    /* Screen Legend (Clean Hairline Borders, No Grey Background) */
    .screen-legend {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 2pt 8pt;
      border-top: 1px solid var(--color-slate-200);
      border-bottom: 1px solid var(--color-slate-200);
      padding: 3pt 0;
      margin-bottom: 4pt;
      font-size: 7.2pt;
      line-height: 1.35;
      color: var(--color-slate-700);
    }
    .legend-entry {
      display: flex;
      align-items: baseline;
      gap: 4px;
    }
    .legend-num {
      font-family: var(--font-mono);
      font-weight: 700;
      font-size: 6.5pt;
      color: var(--color-blue);
      flex-shrink: 0;
    }

    /* Minimalist Hairline Tables */
    .doc-table {
      width: 100%;
      border-collapse: collapse;
      margin: 4pt 0;
      font-size: 7.5pt;
      line-height: 1.4;
      background: transparent;
      border-top: 1.5px solid var(--color-navy);
      border-bottom: 1.5px solid var(--color-navy);
    }
    .doc-table th {
      padding: 3pt 4.5pt;
      font-size: 6.3pt;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--color-navy);
      border-bottom: 1px solid var(--color-slate-300);
      text-align: left;
      background: transparent;
    }
    .doc-table td {
      padding: 3pt 4.5pt;
      border-bottom: 1px solid var(--color-slate-100);
      color: var(--color-slate-700);
      vertical-align: top;
    }
    .doc-table tr:last-child td {
      border-bottom: none;
    }
    .doc-table .col-field {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--color-blue);
      width: 24%;
    }

    /* Clean Numbered Step List (Operational Procedures) */
    .step-list {
      list-style: none;
      counter-reset: op-step;
      margin: 3.5pt 0;
      padding: 0;
    }
    .step-list li {
      counter-increment: op-step;
      position: relative;
      padding-left: 17pt;
      margin-bottom: 2.5pt;
      font-size: 7.5pt;
      line-height: 1.42;
      color: var(--color-slate-700);
    }
    .step-list li::before {
      content: counter(op-step);
      position: absolute;
      left: 0;
      top: 0.5pt;
      width: 12pt;
      height: 12pt;
      border: 1px solid var(--color-blue);
      border-radius: 50%;
      color: var(--color-blue);
      font-family: var(--font-mono);
      font-size: 6pt;
      font-weight: 700;
      display: flex;
      align-items: center;
      justify-content: center;
      line-height: 1;
    }

    /* Minimal Left-Border Callouts (Zero Colored Background Fills) */
    .callout {
      border-left: 2px solid var(--color-blue);
      padding: 2.5pt 0 2.5pt 7pt;
      margin: 4pt 0;
      font-size: 7.4pt;
      line-height: 1.42;
      color: var(--color-slate-700);
      background: transparent;
    }
    .callout-title {
      font-size: 6.4pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--color-blue);
      margin-bottom: 1.5pt;
    }

    .callout-warn {
      border-left-color: var(--color-amber);
    }
    .callout-warn .callout-title {
      color: var(--color-amber);
    }

    .callout-error {
      border-left-color: var(--color-red);
    }
    .callout-error .callout-title {
      color: var(--color-red);
    }

    /* Grid Layouts with Pure Borders */
    .grid-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 3.5pt 10pt;
      margin: 3.5pt 0;
    }
    .grid-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 3.5pt 8pt;
      margin: 3.5pt 0;
    }
    .grid-card {
      border: 1px solid var(--color-slate-200);
      border-radius: 3.5px;
      padding: 4pt 6pt;
      background: #FFFFFF;
    }
    .grid-card-label {
      font-family: var(--font-mono);
      font-size: 6.2pt;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--color-slate-500);
      margin-bottom: 1pt;
    }
    .grid-card-val {
      font-size: 9pt;
      font-weight: 700;
      color: var(--color-navy);
      margin-bottom: 1pt;
    }
    .grid-card-desc {
      font-size: 6.6pt;
      color: var(--color-slate-600);
      line-height: 1.35;
    }

    /* Divider */
    .hairline-divider {
      border-bottom: 1px solid var(--color-slate-200);
      margin: 4pt 0;
    }

    /* Cover Page (Pristine Executive Modernism) */
    .cover-page-wrapper {
      min-height: 297mm;
      height: 297mm;
      max-height: 297mm;
      padding: 24mm 20mm 20mm 20mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
      background: #FFFFFF;
      color: var(--color-navy);
      page-break-after: always;
      break-after: page;
      border: 1px solid var(--color-slate-200);
    }
    .cover-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--color-navy);
      padding-bottom: 14px;
    }
    .cover-logo-box img {
      height: 38px;
      width: auto;
      object-fit: contain;
    }
    .cover-badge-top {
      border: 1px solid var(--color-slate-300);
      border-radius: 4px;
      padding: 3.5px 10px;
      font-family: var(--font-mono);
      font-size: 6.8pt;
      font-weight: 600;
      letter-spacing: 0.06em;
      color: var(--color-blue);
      text-transform: uppercase;
    }
    .cover-body {
      margin: 24px 0;
    }
    .cover-eyebrow {
      font-family: var(--font-mono);
      font-size: 7.2pt;
      font-weight: 600;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--color-blue);
      margin-bottom: 8pt;
    }
    .cover-title {
      font-size: 36pt;
      font-weight: 700;
      line-height: 1.05;
      letter-spacing: -0.025em;
      color: var(--color-navy);
      margin-bottom: 6pt;
    }
    .cover-subtitle {
      font-size: 13.5pt;
      font-weight: 500;
      line-height: 1.35;
      color: var(--color-slate-600);
      margin-bottom: 12pt;
    }
    .cover-rule {
      display: flex;
      height: 3px;
      margin-bottom: 14pt;
    }
    .cover-rule-red { width: 32px; background: #DC2626; }
    .cover-rule-blue { width: 80px; background: #0052CC; }
    .cover-desc {
      font-size: 8.8pt;
      line-height: 1.55;
      color: var(--color-slate-600);
      max-width: 610px;
      margin-bottom: 18pt;
    }
    .cover-meta-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      max-width: 630px;
      border-top: 1px solid var(--color-slate-200);
      padding-top: 12pt;
    }
    .cover-meta-card {
      border-left: 2px solid var(--color-blue);
      padding: 2.5pt 0 2.5pt 8pt;
    }
    .cover-meta-label {
      font-family: var(--font-mono);
      font-size: 6.2pt;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-slate-500);
      margin-bottom: 1.5px;
    }
    .cover-meta-val {
      font-size: 7.8pt;
      font-weight: 600;
      color: var(--color-navy);
    }
    .cover-footer {
      border-top: 1px solid var(--color-slate-200);
      padding-top: 10px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      font-size: 6.8pt;
      color: var(--color-slate-500);
    }
    .cover-footer strong {
      color: var(--color-navy);
    }

    /* Table of Contents (Clean Border-Driven Directory) */
    .toc-container {
      margin: 4pt 0;
      border-top: 1.5px solid var(--color-navy);
      border-bottom: 1.5px solid var(--color-navy);
      padding: 6pt 0;
    }
    .toc-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4pt 16pt;
    }
    .toc-section-title {
      font-family: var(--font-mono);
      font-size: 6.8pt;
      font-weight: 700;
      color: var(--color-blue);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin: 3pt 0 2pt 0;
      border-bottom: 1px solid var(--color-slate-200);
      padding-bottom: 1pt;
    }
    .toc-row {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      padding: 1.8pt 0;
      border-bottom: 1px dotted var(--color-slate-200);
      font-size: 7.2pt;
    }
    .toc-row:last-child {
      border-bottom: none;
    }
    .toc-num {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--color-blue);
      margin-right: 5px;
    }
    .toc-name {
      font-weight: 500;
      color: var(--color-navy);
      flex: 1;
    }
    .toc-pnum {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--color-slate-500);
    }
    """
    return css_template.replace("/* WATERMARK_VAR */", watermark_css)

if __name__ == "__main__":
    print("CSS engine initialized successfully.")

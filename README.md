# Acconeer ERP — Enterprise Operations Manual
### Volume I: Universal Enterprise Standard Operating Manual
**Developer & Technology Owner:** Spectrum Zestwings Technologies LLC  
**Platform Portal:** `acconeer.zestwings.com`  
**Market & Operating Currency:** UAE & GCC Enterprise Markets • AED  
**Publication Revision:** Rev 3.0 (November 2026)  
**Target Format:** Exactly 26 Pages, ISO A4 Portrait  

---

## 1. Overview & Executive Summary

This package contains the official, publication-grade **Acconeer ERP Operations Manual**. It has been systematically authored and engineered to provide rigorous operational, financial, and regulatory guidance for enterprise operations across the UAE and GCC.

Unlike generic marketing overviews or single-tenant walkthroughs, this Universal Edition establishes:
1. **Multi-Entity Scoping & Row-Level Security (RLS)** across corporate organizational trees.
2. **Synchronous Double-Entry General Ledger Accounting** with balanced debits and credits ($0.00$ variance).
3. **End-to-End Commercial Order-to-Cash (O2C)** and **Procure-to-Pay (P2P)** 3-way matching.
4. **UAE Statutory Compliance**:
   - UAE Federal Tax Authority (FTA) VAT Form 201 filing and GL tax clearing accounts.
   - Central Bank of the UAE (CBUAE) Wages Protection System (WPS) encrypted SIF v1.2 generation.
   - UAE Federal Decree-Law No. 33 of 2021 (Labour Law) gratuity and statutory leave formulas.
   - UAE Corporate Tax (Federal Decree-Law No. 47 of 2022) 5-to-7-year immutable audit retention.
5. **Responsible Human-in-the-Loop AI Governance** within sovereign UAE private cloud inference enclaves.

---

## 2. Package Directory Structure

```
Acconeer_ERP_Operations_Manual/
├── Acconeer_ERP_Operations_Manual.pdf   # Official 26-Page Publication-Grade PDF (4.62 MB)
├── acconeer-user-manual.html            # Master Self-Contained HTML Document (260 KB)
├── README.md                            # Comprehensive Package Guide & Operational Reference
├── spectrum-zestwings-logo.png          # Official Corporate Header Logo Asset
├── spectrum_shield.png                  # Background Watermark Crest Asset (Embedded via Base64)
├── spectrum_zestwings_logo.png          # High-Res Vector Brand Asset
│
├── Acconeer_ERP_UserFlows/              # 21 High-Resolution Application Screenshot Captures
│   ├── Dashboard/                       # Executive KPI Cockpit
│   ├── Banking/                         # Bank Accounts & Statement Reconciliation
│   ├── Customer_Activity/               # Commercial Sales Invoices, Orders & Receipts
│   ├── Supplier_Activity/               # Vendor Bills, 3-Way Matching & Vendor Master
│   ├── General_Ledger/                  # Journal Entries & Voucher Reversals
│   ├── Chart_of_Accounts/               # 5-Digit Hierarchical Account Tree
│   ├── Inventory/                       # SKU Master, UOM Multipliers & GRN Intake
│   ├── Assets/                          # Fixed Asset Register & IAS 16 Depreciation
│   ├── Human_Resources/                 # Employee Master & WPS Payroll Engine
│   ├── Reports/                         # IFRS Financial Statements & Variance Switches
│   ├── VAT_Returns/                     # UAE FTA Form 201 Return & EmaraTax Settlement
│   ├── Document_Vault/                  # RBAC Vault & Statutory Document Retention
│   ├── Audit_Trail/                     # Append-Only SIEM Logs & Forensic Packages
│   ├── Budgeting/                       # Cost Center Variance Gateways & CapEx AFEs
│   └── AI_Operations/                   # Advisory AI Assistant & Accountant Verification
│
├── previews_v3/                         # 26 High-Resolution Page Previews (150 DPI PNGs)
│   ├── page_01.png                      # Full-Bleed Executive Cover Page
│   ├── page_02.png ... page_25.png      # Individual Module Pages with Watermarks
│   └── page_26.png                      # System Requirements & SLA Appendix
│
├── docs/                                # Engineering Specifications & Audit Remediation Blueprints
│   ├── 2026-11-18-acconeer-user-manual-redesign.md
│   └── 2026-11-18-acconeer-user-manual-redesign.md
│
└── scripts/                             # Complete Compilation & Automated Verification Pipeline
    ├── assemble_manual.py               # Assembles modular Python templates into master HTML
    ├── generate_complete_manual.py      # CSS design system, base64 watermark & component helpers
    ├── pages_p01_p08.py                 # Pages 01 to 08 layout & operational markup
    ├── pages_p09_p16.py                 # Pages 09 to 16 layout & operational markup
    ├── pages_p17_p26.py                 # Pages 17 to 26 layout & operational markup
    ├── compile_and_verify_pdf.py        # Automated headless browser PDF compilation & PNG rendering
    └── audit_page_gaps.py               # Optical margin auditor measuring vertical bottom gaps
```

---

## 3. 26-Page Master Chapter Sitemap

| Page | Section / Module | Focus & Core Standard Operating Procedure |
|:---:|:---|:---|
| **01** | Executive Cover | Title, Subtitle, Metadata Badge, Technology Ownership |
| **02** | System Architecture | Multi-Entity Hierarchy, Organization Scoping, Branch Isolation |
| **03** | System Navigation | Universal Toolbar Actions, Shortcuts, Segregation of Duties (SoD) |
| **04** | Master Sitemap & Key | Table of Contents, 5-Part Lifecycle Map, Document Governance |
| **05** | Ch. 01 · Dashboard | Multi-Entity Scope Selector, Executive Financial KPIs, Drill-down |
| **06** | Ch. 02 · Banking (Pt 1) | Corporate Accounts, UAE Central Bank IBANs, Bank Registry |
| **07** | Ch. 02 · Banking (Pt 2) | Bank Reconciliation Equation, Discrepancy Clearing, Variance $0.00$ |
| **08** | Ch. 03 · Customers (Pt 1)| Commercial Tax Invoicing, Mandatory TRN, Output VAT ($5\%$) |
| **09** | Ch. 03 · Customers (Pt 2)| Order-to-Cash (O2C) State Machine, Goods Issue, Cash Receipts |
| **10** | Ch. 04 · Suppliers (Pt 1)| Supplier Bills, Automated 3-Way Matching, Discrepancy Tolerances |
| **11** | Ch. 04 · Suppliers (Pt 2)| Vendor Directory, IBAN Callback Verification, Sanction Screening |
| **12** | Ch. 05 · General Ledger | Double-Entry Journal Vouchers, GL Immutability, Reversal Protocols |
| **13** | Ch. 06 · Chart of Accounts | Standard 5-Digit IFRS Tree, Control Account Locks, Sub-Account Mapping |
| **14** | Ch. 07 · Inventory (Pt 1)| Perpetual Inventory, Moving Weighted Average / FIFO, SKU Master |
| **15** | Ch. 07 · Inventory (Pt 2)| Goods Received Notes (GRN), Landed Costs (Customs/Freight), QC |
| **16** | Ch. 08 · Fixed Assets | Capital Fixed Asset Register, IAS 16 Useful Lives, Depreciation Runs |
| **17** | Ch. 09 · HR & Workforce | Employee Master, Emirates ID Format, UAE Labour Law Leave Rules |
| **18** | Ch. 09 · Payroll Engine | WPS SIF v1.2 File Generation, EOSB Gratuity, MOHRE Compliance |
| **19** | Ch. 10 · Reports | IFRS Financial Statements (P&L, Balance Sheet), Dynamic Variances |
| **20** | Ch. 11 · VAT Returns (Pt 1)| UAE FTA Form 201 Returns, 7 Emirates Breakdown, Tax Points |
| **21** | Ch. 11 · VAT Returns (Pt 2)| EmaraTax GL Settlement Vouchers, Filing Calendar, Form 211 |
| **22** | Ch. 12 · Document Vault | Controlled Document Registry, RBAC Access, Statutory Expirations |
| **23** | Ch. 13 · Audit Trail | Append-Only SIEM Logs, Cryptographic Timestamps, Forensic Dossiers |
| **24** | Ch. 14 · Budgeting | Departmental Cost Centers, Pre-Commitment Checking, CapEx Rules |
| **25** | Ch. 15 · AI Assistant | Private Cloud Enclave, Zero Model Training, Accountant Checklist |
| **26** | Appendix & Support | SLA Incident Response Tiers, High Availability, Disaster Recovery |

---

## 4. Visual Design & Quality Metrics

1. **Subtle Background Brand Watermark**:
   - Base64-injected official Spectrum Zestwings shield crest centered on `.page::before` at $3.8\%$ opacity.
   - Non-intrusive, fully legible typography and crisp diagram readability.
2. **Minimalist Screenshot Frames (Zero Desktop Window Chrome)**:
   - Eliminated simulated operating system chrome (titlebars, window dots, dark viewports).
   - Replaced with clean enterprise cards with subtle borders and numbered feature anchors.
3. **Zero White Voids / Perfectly Balanced Margins**:
   - All 26 pages maintain uniform bottom margins strictly between $31.7\text{ pt}$ and $74.7\text{ pt}$ (average $\approx 54\text{ pt}$).
   - Zero blank trailing pages or orphan lines.

---

## 5. Compilation & Build Verification

To recompile the HTML and generate the publication PDF locally:

```bash
# 1. Assemble HTML from modular components
python scripts/assemble_manual.py

# 2. Compile PDF and render page previews
python scripts/compile_and_verify_pdf.py

# 3. Audit bottom margins and page geometries
python scripts/audit_page_gaps.py
```

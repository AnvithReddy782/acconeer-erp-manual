# Acconeer ERP Operations Manual Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a publication-grade, multi-page (~30–35 pages) official User Operations Manual for Acconeer ERP that eliminates all generic AI aesthetics, restores full navigation sidebar context, uses classic corporate typography (Inter), and delivers task-based instructional walkthroughs for all 15 ERP modules.

**Architecture:** A robust Node.js document compiler (`scripts/build-operations-manual.cjs`) generates a print-optimized, multi-page HTML document (`acconeer-user-manual.html`) adhering to standard A4 pagination rules, running headers/footers, and clean CSS styling. The document is compiled to publication PDF (`Acconeer_ERP_Operations_Manual.pdf`) via headless Chromium (`browse.exe pdf`).

**Tech Stack:** Node.js, HTML5 / CSS3 Paged Media (`@page`), Inter typography, PyMuPDF / Python for page verification, and `browse.exe` for PDF compilation.

**Spec:** `docs/superpowers/specs/2026-11-18-acconeer-user-manual-redesign.md`

## Global Constraints
- Target Document Length: 30 to 35 pages (natural, multi-page flow; ~1.5 to 2.5 pages per module).
- Typography: Strictly **Inter** (`Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`). Zero `Poppins`, zero `Plus Jakarta Sans`, zero `JetBrains Mono` or monospace fonts.
- Screenshot Fidelity: Use original un-cropped screenshots with complete navigation sidebar intact. Zero painted red bounding boxes or drawn marker circles.
- Master Context Adherence: Strict 1:1 compliance with verified Acconeer ERP Master Context (UAE/GCC enterprise, functional currency AED, 4-tier scope hierarchy, FTA Form 201 VAT rules). Zero hallucinations.
- Print Formatting: Standard A4 portrait (`@page { size: A4 portrait; margin: 16mm 16mm 18mm 16mm; }`), clean page breaks (`break-before: page; break-inside: avoid;`), and automated page number counters (`Page X`).

## Review Focus
1. **Navigation Context Visibility:** Verify that every screenshot shows the left navigation sidebar so users can locate the active view in the ERP menu.
2. **Typography Purity:** Confirm that no element renders with monospaced (`font-family: monospace`) or bubbly font faces.
3. **Task-Based Procedural Depth:** Ensure each chapter provides concrete, numbered instructional steps referencing exact on-screen button labels in bold.
4. **Natural Pagination & Spacing:** Confirm that section breaks occur at logical boundaries without orphaned headers or squished figures.
5. **Exact Parameter Catalog:** Verify that all field reference tables specify field names, input types, validation rules, and General Ledger impact.

---

## Tasks

- [x] **Task 1: Core Document Engine, Cover Page & System Architecture**
  - **Files:** Create `scripts/build-operations-manual.cjs`
  - Implement print-grade CSS rules (`@page`, running headers/footers, Inter typography, callout cards, clean table styles).
  - Build executive Cover Page (Spectrum Zestwings official logo, formal title, system profile matrix, compliance standard, and publication credentials).
  - Build Section 1: System Governance & Architecture (4-Tier Scope Hierarchy, Universal Toolbar with `Refresh Financial Ledger State`, Role Access).
  - Build Section 2: Table of Contents (complete 15-module listing with page targets).
  - **Verification:** Run `node scripts/build-operations-manual.cjs` and verify clean HTML generation.

- [x] **Task 2: Implement Financial & Commercial Core Modules (Chapters 1–5)**
  - **Files:** Modify `scripts/build-operations-manual.cjs`
  - Implement Chapter 1: Dashboard (`01_Executive_Dashboard.png`, KPI indicators, scoping, GL sync procedure).
  - Implement Chapter 2: Banking (`01_Banking_Overview.png`, Account setup, electronic statement reconciliation, two-way voucher matching).
  - Implement Chapter 3: Customer Activity (`05_Sales_Invoice.png`, Order-to-Cash pipeline, quotation conversion, delivery notes, taxable e-invoices, customer receipts).
  - Implement Chapter 4: Supplier Activity (`01_Vendor_Directory.png`, Procure-to-Pay pipeline, 3-way matching, purchase orders, bills, debit notes).
  - Implement Chapter 5: Journal Entries (`01_Journal_Entries.png`, General ledger adjusting vouchers, strict debit/credit balance enforcement, digital attachments).
  - **Verification:** Generate HTML and verify Chapters 1–5 render with uncropped images and complete field catalogs.

- [x] **Task 3: Implement Logistics, Assets, HR & Financial Statements (Chapters 6–10)**
  - **Files:** Modify `scripts/build-operations-manual.cjs`
  - Implement Chapter 6: Chart of Accounts (`01_Accounts_Tree.png`, 1000s–5000s account blocks, normal balance rules, `+ Map Sub` workflow).
  - Implement Chapter 7: Inventory & Warehousing (`01_Inventory_Master.png`, SKU catalog, UOM setup, warehouse bin allocation, GRN receipt gate).
  - Implement Chapter 8: Fixed Assets (`01_Asset_Master.png`, Capital asset register, serial tags, straight-line depreciation run).
  - Implement Chapter 9: HR & Workforce Management (`01_HR_Overview.png`, Employee roster, attendance, daily timesheets, monthly payroll calculation and GL booking).
  - Implement Chapter 10: Reports & Financial Statements (`01_Financial_Reports.png`, Balance Sheet, P&L, Trial Balance, comparative variance switches).
  - **Verification:** Generate HTML and verify Chapters 6–10 render with uncropped images and complete field catalogs.

- [x] **Task 4: Implement Compliance, Security, Forecasting & AI Intelligence (Chapters 11–15)**
  - **Files:** Modify `scripts/build-operations-manual.cjs`
  - Implement Chapter 11: VAT Returns (`01_VAT_Filing_Dashboard.png`, UAE FTA Form 201 Box 8/11/14 mappings, filing status pipeline, GL tax settlement).
  - Implement Chapter 12: Document Vault (`01_Vault_Registry.png`, Compliance categories, license/visa registries, automated expiration alerts).
  - Implement Chapter 13: Audit Trail (`01_Security_Audit_Logs.png`, Forensic activity logging, WORM immutable rules, session IP verification).
  - Implement Chapter 14: Budgeting & Forecasts (`01_Budgeting_Matrix.png`, Department spending allocations, actuals tracking, spending ceiling alerts).
  - Implement Chapter 15: AI Assistant (`01_Spectrum_Zestwings_AI.png`, Conversational queries, report shortcuts, read-only security boundaries).
  - **Verification:** Generate full `acconeer-user-manual.html` and verify all 15 chapters are present.

- [x] **Task 5: PDF Compilation, Multi-Page Pagination Audit & Quality Verification**
  - **Files:** Generate `Acconeer_ERP_Operations_Manual.pdf` via `browse.exe pdf`
  - Execute headless PDF compile.
  - Audit total page count (Target: 30–35 pages).
  - Inspect sample pages using PyMuPDF to confirm:
    1. Uncropped screenshots showing full navigation sidebar.
    2. Zero electronic/monospace fonts (pure Inter typography).
    3. Proper margins, natural white space, and zero text clipping.
    4. Task-based step-by-step procedures with exact bold UI button labels.

# scripts/pages_p01_p08.py
from generate_complete_manual import get_base64_logo, window_frame

def get_page_01():
    logo_b64 = get_base64_logo()
    return f"""
    <div class="page cover-page-wrapper">
      <div class="cover-top-stripe">
        <span>ACCONEER CLOUD ERP</span>
        <span>PRODUCTION RELEASE · V3.2</span>
      </div>

      <div class="cover-body">
        <div class="cover-logo-area">
          <img src="{logo_b64}" alt="Spectrum Zestwings" class="cover-logo-img">
          <div class="cover-brand-title">Spectrum Zestwings Technologies</div>
        </div>

        <div class="cover-title-block">
          <div class="cover-kicker">ENTERPRISE CLOUD FINANCIAL OPERATIONS</div>
          <h1 class="cover-main-title">Acconeer ERP<br><span style="font-weight: 400; color: #475569;">Operations Manual & User Guide</span></h1>
          <div class="cover-subtitle">Complete Screen Reference, Functional Controls & Standard User Operating Guide</div>
        </div>

        <div class="cover-meta-grid">
          <div class="cover-meta-card">
            <div class="cover-meta-label">SOFTWARE PLATFORM</div>
            <div class="cover-meta-value">Acconeer Cloud ERP</div>
            <div class="cover-meta-desc">Version 3.2.4 · Enterprise Financial Suite</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">PRIMARY CURRENCY</div>
            <div class="cover-meta-value">United Arab Emirates Dirham (AED)</div>
            <div class="cover-meta-desc">Multi-Currency & VAT Compliance Standard</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">DOCUMENT EDITION</div>
            <div class="cover-meta-value">Q4 2026 Production Edition</div>
            <div class="cover-meta-desc">Standard User Operations & Screen Guide</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">SYSTEM ARCHITECTURE</div>
            <div class="cover-meta-value">Multi-Entity & Multi-Branch</div>
            <div class="cover-meta-desc">Single Database · Autonomous Ledgers</div>
          </div>
        </div>
      </div>

      <div class="cover-footer-bar">
        <div>
          Confidential · Proprietary to Spectrum Zestwings Technologies LLC<br>
          Enterprise Support: <code>support@sztech.ae</code> • Documentation: <code>www.sztech.ae</code>
        </div>
        <div style="text-align: right;">
          Document Status: <strong>Production User Standard</strong><br>
          Release Cycle: <strong>Q4 2026 Edition</strong>
        </div>
      </div>
    </div>
    """

def get_page_02():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">SYSTEM ARCHITECTURE · FOUNDATION</div>
          <div class="chapter-title">Multi-Entity Governance & Scope Selection</div>
        </div>
        <div class="chapter-right-meta">SECTION 01<br>GLOBAL CONTROLS</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Universal Top Header ➔ Global 4-Tier Scope Selector
      </div>

      <p>
        Acconeer ERP enforces a unified 4-tier scoping hierarchy positioned in the top global navigation bar. All transactional entry, ledger inquiries, and reporting outputs are dynamically governed by the active scope parameters selected by the user.
      </p>

      <h2>The 4-Tier Operational Scope Hierarchy</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 14%;">Hierarchy Level</th>
            <th style="width: 24%;">Selector Element</th>
            <th style="width: 34%;">Operational Instance Example</th>
            <th style="width: 28%;">Functional Scope Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>Tier 1</code></td>
            <td><strong>Organization</strong></td>
            <td><code>Anson Enterprises</code></td>
            <td>Global parent holding; defines shared COA templates, base currency, and security governance.</td>
          </tr>
          <tr>
            <td><code>Tier 2</code></td>
            <td><strong>Legal Entity</strong></td>
            <td><code>Anson Enterprises Legal Entity LLC</code></td>
            <td>Tax-registered operating corporate entity; holds legal TRN and dedicated general ledger accounts.</td>
          </tr>
          <tr>
            <td><code>Tier 3</code></td>
            <td><strong>Branch Scope</strong></td>
            <td><code>All Branches (Consolidated)</code> • <code>Dubai HQ</code></td>
            <td>Physical warehouse location, branch retail office, or cost-center for segmental profitability.</td>
          </tr>
          <tr>
            <td><code>Tier 4</code></td>
            <td><strong>Fiscal Period</strong></td>
            <td><code>FY 2026</code> • <code>Q3 2026</code> • <code>Monthly</code></td>
            <td>Active operational date filter governing transaction queries, dashboards, and report generation.</td>
          </tr>
        </tbody>
      </table>

      <h2>Operational Scoping Rules & Data Boundaries</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Control Dimension</th>
            <th style="width: 35%;">System Architectural Rule</th>
            <th style="width: 40%;">Operational Impact on Screen</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Session Filter Sync</td>
            <td>Dropdown changes update all active widgets instantly.</td>
            <td>Switching entities re-queries database; displays only data belonging to that entity.</td>
          </tr>
          <tr>
            <td class="col-field">Branch Cost Tagging</td>
            <td>Every invoice, bill, and voucher tags the active branch.</td>
            <td>Enables branch-level P&L and inventory tracking without separate legal companies.</td>
          </tr>
          <tr>
            <td class="col-field">Cross-Entity Isolation</td>
            <td>Strict sub-ledger isolation between operating units.</td>
            <td>Invoices created in Entity A never alter balances in Entity B without an inter-company voucher.</td>
          </tr>
        </tbody>
      </table>

      <h2>Fiscal Period Lifecycle States & Posting Permissions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Period State</th>
            <th style="width: 24%;">Status Pill Display</th>
            <th style="width: 54%;">Permitted Operational Transactions in Acconeer ERP</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Open Operational</td>
            <td><code>OPEN</code> (Green Pill)</td>
            <td>Unrestricted transactional entry across billing, supplier bills, receipts, and inventory.</td>
          </tr>
          <tr>
            <td class="col-field">Soft Monthly Close</td>
            <td><code>SOFT_CLOSE</code> (Amber Pill)</td>
            <td>Commercial sub-ledgers locked; only authorized accountants may post adjusting journals.</td>
          </tr>
          <tr>
            <td class="col-field">Hard Fiscal Lock</td>
            <td><code>LOCKED</code> (Red Pill)</td>
            <td>Permanent freeze; all ledger modifications rejected; requires CFO override to reopen.</td>
          </tr>
        </tbody>
      </table>

      <h2>Multi-Currency & Inter-Company Elimination Framework</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Governance Dimension</th>
            <th style="width: 35%;">System Architectural Rule</th>
            <th style="width: 40%;">Accounting & Compliance Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Base Functional Currency</td>
            <td>Standardized to <code>AED</code> for UAE statutory compliance.</td>
            <td>All financial statements and VAT declarations calculate and report in Dirhams.</td>
          </tr>
          <tr>
            <td class="col-field">Foreign Currency Support</td>
            <td>Supports USD, EUR, GBP, SAR line item pricing.</td>
            <td>Converts to AED via daily spot rates; automatically calculates realized FX gain/loss.</td>
          </tr>
          <tr>
            <td class="col-field">Inter-Company Accounts</td>
            <td>Reciprocal balancing entries between affiliate entities.</td>
            <td>Posts balancing vouchers to Due from Affiliates (1950) and Due to Affiliates (2950).</td>
          </tr>
          <tr>
            <td class="col-field">Consolidated Elimination</td>
            <td>Dynamic netting when selecting <em>All Entities</em>.</td>
            <td>Eliminates internal reciprocal balances to present true external enterprise performance.</td>
          </tr>
          <tr>
            <td class="col-field">Entity Tax & Fiscal Bounds</td>
            <td>Registered 15-digit TRN & 12-month accounting cycle.</td>
            <td>Enforces period lock cutoffs, statutory tax invoice generation, and fiscal closure.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">CROSS-ENTITY POSTING PROTECTION</div>
        Each legal entity operates with an isolated sub-ledger. Invoices and bills created under <em>Anson Enterprises Legal Entity LLC</em> will not alter receivables or payables of sibling entities. Cross-entity trading automatically generates balancing inter-company vouchers.
      </div>
    </div>
    """

def get_page_03():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">SYSTEM NAVIGATION · USER INTERFACE</div>
          <div class="chapter-title">Universal Toolbar, Navigation & Global Controls</div>
        </div>
        <div class="chapter-right-meta">SECTION 02<br>USER INTERFACE</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Universal Header Bar ➔ Quick Actions, Search & User Profile
      </div>

      <p>
        Acconeer ERP features a persistent top header and collapsible sidebar navigation bar accessible across every screen. The interface provides instant access to global creation triggers, active entity context, keyboard shortcuts, and integrated AI assistance.
      </p>

      <h2>Universal Top Header Elements & Action Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Header Element</th>
            <th style="width: 16%;">Visual Location</th>
            <th style="width: 42%;">Operational Functionality & Screen Behavior</th>
            <th style="width: 20%;">User Access</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Menu / Logo Bar</strong></td>
            <td>Top Left</td>
            <td>Displays the Acconeer brand mark and hamburger toggle icon to expand/collapse the sidebar.</td>
            <td>All Users</td>
          </tr>
          <tr>
            <td><strong>+ Create</strong></td>
            <td>Top Center-Left</td>
            <td>Quick-action dropdown to create Invoices, Bills, Journal Entries, Customers, or Suppliers.</td>
            <td>Operators & Admins</td>
          </tr>
          <tr>
            <td><strong>Scope Switcher</strong></td>
            <td>Top Center-Right</td>
            <td>Displays active Organization, Legal Entity, and subscription badge (e.g. <code>Professional</code>).</td>
            <td>All Users</td>
          </tr>
          <tr>
            <td><strong>User Profile Menu</strong></td>
            <td>Top Right</td>
            <td>Displays user initials (<code>RO</code>), name (<em>Rondla Anvith Reddy</em>), role (<em>Organization Administrator</em>).</td>
            <td>Active Session</td>
          </tr>
        </tbody>
      </table>

      <h2>Quick Action Dropdown (+ Create) Menu Triggers</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Quick Menu Item</th>
            <th style="width: 35%;">Action Triggered</th>
            <th style="width: 40%;">Modal Workflow & Direct Navigation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">+ New Sales Invoice</td>
            <td>Opens Commercial Invoice Modal</td>
            <td>Quick entry for customer billing with automated VAT and GL posting.</td>
          </tr>
          <tr>
            <td class="col-field">+ New Purchase Bill</td>
            <td>Opens Supplier Payables Modal</td>
            <td>Vendor bill entry with purchase order matching and OCR upload option.</td>
          </tr>
          <tr>
            <td class="col-field">+ New Journal Entry</td>
            <td>Opens General Ledger Voucher</td>
            <td>Double-entry manual journal entry with automated balancing verification.</td>
          </tr>
          <tr>
            <td class="col-field">+ New Customer / Vendor</td>
            <td>Opens Directory Registration</td>
            <td>Fast counterparty onboarding with TRN validation and account linkage.</td>
          </tr>
        </tbody>
      </table>

      <h2>Universal Keyboard Shortcut Reference</h2>
      <div class="grid-2col">
        <table class="doc-table">
          <thead>
            <tr>
              <th style="width: 35%;">Shortcut</th>
              <th style="width: 65%;">Navigational Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><kbd>Alt + D</kbd></td>
              <td>Open Executive Financial Dashboard</td>
            </tr>
            <tr>
              <td><kbd>Alt + B</kbd></td>
              <td>Open Banking & Accounts Register</td>
            </tr>
            <tr>
              <td><kbd>Alt + R</kbd></td>
              <td>Open Bank Statement Reconciliation</td>
            </tr>
            <tr>
              <td><kbd>Alt + I</kbd></td>
              <td>Open Customer Sales Invoicing</td>
            </tr>
          </tbody>
        </table>

        <table class="doc-table">
          <thead>
            <tr>
              <th style="width: 35%;">Shortcut</th>
              <th style="width: 65%;">Navigational Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><kbd>Alt + S</kbd></td>
              <td>Open Sales Orders & Receipts</td>
            </tr>
            <tr>
              <td><kbd>Alt + P</kbd></td>
              <td>Open Supplier Bills & Payables</td>
            </tr>
            <tr>
              <td><kbd>Alt + J</kbd></td>
              <td>Open General Ledger Journal Entry</td>
            </tr>
            <tr>
              <td><kbd>Alt + A</kbd></td>
              <td>Open Chart of Accounts (COA)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h2>Global Search Syntax & Instant Filtering Tokens</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Search Token Syntax</th>
            <th style="width: 35%;">Query Target & Filter Scope</th>
            <th style="width: 40%;">Screen Result & Instant Navigation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field"><code>inv:2026-XXXX</code></td>
            <td>Sales Invoice Register</td>
            <td>Opens the matching commercial tax invoice card and line item details.</td>
          </tr>
          <tr>
            <td class="col-field"><code>bil:2026-XXXX</code></td>
            <td>Supplier Payables Register</td>
            <td>Opens the matching vendor purchase bill and attached OCR slip.</td>
          </tr>
          <tr>
            <td class="col-field"><code>cust:&lt;name&gt;</code></td>
            <td>Customer Master Directory</td>
            <td>Filters client profiles and displays real-time accounts receivable ledger.</td>
          </tr>
          <tr>
            <td class="col-field"><code>sku:&lt;code&gt;</code></td>
            <td>Inventory Master Catalog</td>
            <td>Displays SKU stock on hand across all active branch warehouses.</td>
          </tr>
        </tbody>
      </table>

      <h2>Notification Bell & Real-Time Operational Alerts</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Alert Classification</th>
            <th style="width: 35%;">Triggering Operational Event</th>
            <th style="width: 40%;">User Notification & Screen Badge Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Pending Approvals</td>
            <td>Purchase orders or credit notes awaiting manager sign-off.</td>
            <td>Displays red badge count on header bell; opens approval queue.</td>
          </tr>
          <tr>
            <td class="col-field">OCR Ingestion Complete</td>
            <td>Background AI OCR processing of uploaded invoices finishes.</td>
            <td>Toast banner notifies user to review and post parsed invoice lines.</td>
          </tr>
          <tr>
            <td class="col-field">Document Expiry Warning</td>
            <td>Employee visas, trade licenses, or contracts within 30 days.</td>
            <td>Amber warning ping dispatched directly to HR & Compliance users.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">ROLE-BASED UI VISIBILITY</div>
        Toolbar actions and sidebar links automatically adapt to your assigned security role. Operators with billing duties will only see customer and invoicing menus, while accounting and audit menus are restricted to authorized finance personnel.
      </div>
    </div>
    """

def get_page_04():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">DOCUMENT STRUCTURE · REFERENCE</div>
          <div class="chapter-title">Table of Contents & Operational Module Map</div>
        </div>
        <div class="chapter-right-meta">MASTER INDEX<br>26 CHAPTERS</div>
      </div>

      <p>
        This manual provides an end-to-end operational guide for Acconeer ERP across 26 focused modules organized into five enterprise operational lifecycles. Each chapter details screen navigation, field dictionaries, step-by-step procedures, and validation controls.
      </p>

      <div class="toc-container">
        <div class="toc-grid">
          <div>
            <div class="toc-section-title">Part I: Architecture & Navigation</div>
            <div class="toc-row"><span class="toc-num">01</span><span class="toc-name">Cover & Enterprise System Metadata</span><span class="toc-pnum">Page 01</span></div>
            <div class="toc-row"><span class="toc-num">02</span><span class="toc-name">Multi-Entity Governance & Scope Selection</span><span class="toc-pnum">Page 02</span></div>
            <div class="toc-row"><span class="toc-num">03</span><span class="toc-name">Universal Toolbar, Search & Keyboard Shortcuts</span><span class="toc-pnum">Page 03</span></div>
            <div class="toc-row"><span class="toc-num">04</span><span class="toc-name">Table of Contents & Operational Module Map</span><span class="toc-pnum">Page 04</span></div>

            <div class="toc-section-title">Part II: Commercial & Cash Operations</div>
            <div class="toc-row"><span class="toc-num">05</span><span class="toc-name">Executive Financial Dashboard & KPI Telemetry</span><span class="toc-pnum">Page 05</span></div>
            <div class="toc-row"><span class="toc-num">06</span><span class="toc-name">Banking Master & Corporate Account Setup</span><span class="toc-pnum">Page 06</span></div>
            <div class="toc-row"><span class="toc-num">07</span><span class="toc-name">Bank Statement Reconciliation & Ledger Matching</span><span class="toc-pnum">Page 07</span></div>
            <div class="toc-row"><span class="toc-num">08</span><span class="toc-name">Customer Invoicing & Accounts Receivable (AR)</span><span class="toc-pnum">Page 08</span></div>
            <div class="toc-row"><span class="toc-num">09</span><span class="toc-name">Sales Orders & Customer Receipts (Order-to-Cash)</span><span class="toc-pnum">Page 09</span></div>
            <div class="toc-row"><span class="toc-num">10</span><span class="toc-name">Supplier Bills & 3-Way Procure-to-Pay Matching</span><span class="toc-pnum">Page 10</span></div>
            <div class="toc-row"><span class="toc-num">11</span><span class="toc-name">Vendor Master Directory & Disbursement Controls</span><span class="toc-pnum">Page 11</span></div>
          </div>

          <div>
            <div class="toc-section-title">Part III: General Ledger, Assets & Inventory</div>
            <div class="toc-row"><span class="toc-num">12</span><span class="toc-name">General Ledger & Journal Voucher Entry</span><span class="toc-pnum">Page 12</span></div>
            <div class="toc-row"><span class="toc-num">13</span><span class="toc-name">Chart of Accounts (COA) Structure & Creation</span><span class="toc-pnum">Page 13</span></div>
            <div class="toc-row"><span class="toc-num">14</span><span class="toc-name">Inventory Master Catalog & Valuation Rules</span><span class="toc-pnum">Page 14</span></div>
            <div class="toc-row"><span class="toc-num">15</span><span class="toc-name">Goods Received Notes (GRN) & Warehouse Intake</span><span class="toc-pnum">Page 15</span></div>
            <div class="toc-row"><span class="toc-num">16</span><span class="toc-name">Fixed Assets Registry & Monthly Depreciation</span><span class="toc-pnum">Page 16</span></div>

            <div class="toc-section-title">Part IV: HR, Payroll & Tax Operations</div>
            <div class="toc-row"><span class="toc-num">17</span><span class="toc-name">HR & Employee Master Onboarding</span><span class="toc-pnum">Page 17</span></div>
            <div class="toc-row"><span class="toc-num">18</span><span class="toc-name">Payroll Processing Engine & WPS SIF Export</span><span class="toc-pnum">Page 18</span></div>
            <div class="toc-row"><span class="toc-num">19</span><span class="toc-name">Financial Reports (P&L, Balance Sheet, Cash Flow)</span><span class="toc-pnum">Page 19</span></div>
            <div class="toc-row"><span class="toc-num">20</span><span class="toc-name">UAE VAT Return (Form 201) Preparation</span><span class="toc-pnum">Page 20</span></div>
            <div class="toc-row"><span class="toc-num">21</span><span class="toc-name">VAT Settlement Posting & Period Closure</span><span class="toc-pnum">Page 21</span></div>

            <div class="toc-section-title">Part V: Governance, AI & Technical Support</div>
            <div class="toc-row"><span class="toc-num">22</span><span class="toc-name">Document Vault & Digital File Management</span><span class="toc-pnum">Page 22</span></div>
            <div class="toc-row"><span class="toc-num">23</span><span class="toc-name">Audit Trail Logging & Compliance Inspections</span><span class="toc-pnum">Page 23</span></div>
            <div class="toc-row"><span class="toc-num">24</span><span class="toc-name">Budgeting & Variance Alert Controls</span><span class="toc-pnum">Page 24</span></div>
            <div class="toc-row"><span class="toc-num">25</span><span class="toc-name">AI Financial Assistant & Conversational Queries</span><span class="toc-pnum">Page 25</span></div>
            <div class="toc-row"><span class="toc-num">26</span><span class="toc-name">System Administration & Technical Support SLAs</span><span class="toc-pnum">Page 26</span></div>
          </div>
        </div>
      </div>

      <h2>Document Standards & User Conventions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Convention Style</th>
            <th style="width: 35%;">Visual Representation</th>
            <th style="width: 40%;">Operational Meaning in Acconeer ERP</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>UI Action Button</strong></td>
            <td><code>+ New Record</code> or <code>Save & Post</code></td>
            <td>A clickable user interface element that executes an action or opens a modal window.</td>
          </tr>
          <tr>
            <td><strong>Mandatory Field</strong></td>
            <td>Field label with asterisk (e.g. <code>Customer *</code>)</td>
            <td>Data entry is strictly required; forms cannot be saved or submitted without input.</td>
          </tr>
          <tr>
            <td><strong>Keyboard Shortcut</strong></td>
            <td><kbd>Alt + Key</kbd></td>
            <td>Global hotkey sequence for rapid power-user keyboard navigation.</td>
          </tr>
          <tr>
            <td><strong>Validation Alert</strong></td>
            <td>Left-accent hairline border</td>
            <td>Critical operational guidance, security warnings, or automated reversal requirements.</td>
          </tr>
        </tbody>
      </table>

      <h2>Operational Role Access & Module Permission Matrix</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">ERP Operational Lifecycle</th>
            <th style="width: 45%;">Authorized Functional Roles</th>
            <th style="width: 30%;">Data Governance Level</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Part I: Architecture & Scope</td>
            <td>Organization Administrator, System Controller</td>
            <td>Global Corporate Governance</td>
          </tr>
          <tr>
            <td class="col-field">Part II: Commercial & Cash</td>
            <td>Sales Clerks, Billing Operators, Cashiers, AR/AP Staff</td>
            <td>Commercial Operations</td>
          </tr>
          <tr>
            <td class="col-field">Part III: General Ledger & Stock</td>
            <td>Chief Accountant, GL Staff, Warehouse Managers</td>
            <td>Double-Entry & Asset Control</td>
          </tr>
          <tr>
            <td class="col-field">Part IV: HR, Payroll & Tax</td>
            <td>HR Manager, Payroll Officer, Tax Accountant, CFO</td>
            <td>Statutory Compliance (WPS/FTA)</td>
          </tr>
          <tr>
            <td class="col-field">Part V: Governance, AI & Admin</td>
            <td>Compliance Officer, Internal Auditor, Administrator</td>
            <td>Immutable Audit & Security</td>
          </tr>
        </tbody>
      </table>

      <h2>Enterprise System Architecture & Compliance Certifications</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 30%;">Statutory / Security Standard</th>
            <th style="width: 35%;">Certifying Authority & Framework</th>
            <th style="width: 35%;">System Compliance Verification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">UAE FTA Tax Agency Qualified</td>
            <td>Federal Tax Authority (FTA)</td>
            <td>Qualified accounting software for Form 201 & FAF generation.</td>
          </tr>
          <tr>
            <td class="col-field">Wages Protection System (WPS)</td>
            <td>Central Bank of UAE (CBUAE) / MOHRE</td>
            <td>Compliant with electronic SIF v1.2 salary file format.</td>
          </tr>
          <tr>
            <td class="col-field">ISO/IEC 27001:2022 Certified</td>
            <td>Independent Global Audit</td>
            <td>Information security management and cloud data encryption.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_05():
    wf = window_frame(
        "images/01_Executive_Dashboard.png",
        "Executive Financial Dashboard & Live Real-Time Telemetry Cockpit",
        "/dashboard",
        [
            ("Scope Filters", "Organization, Legal Entity LLC, Branch Scope, and Fiscal Year FY 2026 selectors."),
            ("Live Status Badge", "• Live Ledger real-time green indicator confirming active double-entry sync."),
            ("6 KPI Metric Cards", "Total Revenue, Net Profit, Cash Liquidity, Gross Profit, Receivables, and Payables."),
            ("Analytical Chart Cards", "Financial Trajectory multi-tab chart and OpEx Breakdown with P&L link.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">EXECUTIVE OVERVIEW · REAL-TIME TELEMETRY</div>
          <div class="chapter-title">Executive Financial Dashboard & Live Cockpit</div>
        </div>
        <div class="chapter-right-meta">MODULE 01<br>/dashboard</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Dashboard (or press <kbd>Alt + D</kbd>)
      </div>

      <p>
        The Executive Financial Dashboard provides a unified corporate cockpit displaying real-time financial health, cash liquidity, revenue performance, and balance sheet exposure calculated directly from the live General Ledger.
      </p>

      {wf}

      <h2>Primary Action Buttons & Screen Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Screen Element</th>
            <th style="width: 20%;">Visual Type</th>
            <th style="width: 55%;">On-Screen Function & System Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Refresh Button</td>
            <td>Circular Arrow Icon</td>
            <td>Forces immediate cache invalidation and re-queries live General Ledger aggregates.</td>
          </tr>
          <tr>
            <td class="col-field">+ New Journal</td>
            <td>Solid Purple Button</td>
            <td>Direct trigger opening the manual double-entry General Ledger journal voucher modal.</td>
          </tr>
          <tr>
            <td class="col-field">• Live Ledger</td>
            <td>Green Pill Badge</td>
            <td>Status indicator confirming database connection is actively listening to transactional postings.</td>
          </tr>
          <tr>
            <td class="col-field">Scope Selectors</td>
            <td>4 Top Dropdowns</td>
            <td>Filters dashboard by Organization, Legal Entity, Branch, and Fiscal Year (e.g. FY 2026).</td>
          </tr>
        </tbody>
      </table>

      <h2>On-Screen Metric & Telemetry Cards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Metric Card</th>
            <th style="width: 18%;">Display Value</th>
            <th style="width: 58%;">Calculation Source & Operational Meaning on Screen</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">TOTAL REVENUE</td>
            <td><code>AED 0.00</code></td>
            <td>Cumulative commercial revenue posted in the active period; details sales invoices AED total.</td>
          </tr>
          <tr>
            <td class="col-field">NET PROFIT</td>
            <td><code>AED 0.00</code></td>
            <td>Real-time bottom-line profit or loss after deducting all operational costs and cost of sales.</td>
          </tr>
          <tr>
            <td class="col-field">CASH LIQUIDITY</td>
            <td><code>AED 0.00</code></td>
            <td>Liquid funds across bank ledgers; shows active banking accounts and reconciled status.</td>
          </tr>
          <tr>
            <td class="col-field">GROSS PROFIT</td>
            <td><code>AED 0.00</code></td>
            <td>Revenue minus direct cost of goods sold (COGS) before indirect operating expenditures.</td>
          </tr>
          <tr>
            <td class="col-field">RECEIVABLES (AR)</td>
            <td><code>AED 0.00</code></td>
            <td>Outstanding customer debt from Account 1020; includes direct clickable link to <em>Invoices</em>.</td>
          </tr>
          <tr>
            <td class="col-field">PAYABLES (AP)</td>
            <td><code>AED 0.00</code></td>
            <td>Outstanding supplier obligations from Account 2010; includes direct clickable link to <em>Bills</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Analytical Widgets & View Tabs</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 28%;">Widget Title</th>
            <th style="width: 24%;">Interactive Controls</th>
            <th style="width: 48%;">Displayed Information & Target Navigation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Financial Trajectory</td>
            <td>Revenue & Profit · Cash · Variance</td>
            <td>Multi-period visual trend chart comparing cash flow and budget targets over time.</td>
          </tr>
          <tr>
            <td class="col-field">OpEx Breakdown</td>
            <td>Clickable P&L Statement Link</td>
            <td>Categorized summary of operating expenses by ledger; links directly to full P&L report.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_06():
    wf = window_frame(
        "images/02_Bank_Accounts.png",
        "Banking Master & Corporate Cash Ledger Account Structure",
        "/banking",
        [
            ("Top Actions", "Excel, PDF, Opening Balances, and + Map New Sub-Account buttons."),
            ("Account Category Filter", "Quick filter pills for All Accounts (1000-7999), Assets, Liabilities, and Equity."),
            ("Search Input", "Real-time search field for filtering account codes and account titles."),
            ("Tree Ledger Grid", "Hierarchical columns for Account Code, Title, Tag, Type, Normal, Currency, and Balance.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · BANKING LEDGER</div>
          <div class="chapter-title">Banking Master & Corporate Account Setup</div>
        </div>
        <div class="chapter-right-meta">MODULE 02<br>/banking</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Banking (or press <kbd>Alt + B</kbd>)
      </div>

      <p>
        In Acconeer ERP, corporate bank accounts and cash treasuries are managed directly through dedicated General Ledger asset accounts under Cash and Cash Equivalents (Account 1010), maintaining instant trial balance synchronization.
      </p>

      {wf}

      <h2>Primary Action Buttons & Screen Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Screen Element</th>
            <th style="width: 20%;">Visual Style</th>
            <th style="width: 55%;">On-Screen Function & System Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">+ Map New Sub-Account</td>
            <td>Solid Purple Button</td>
            <td>Opens modal to create a new sub-account mapped under a parent code (e.g. 1010-01 for Bank).</td>
          </tr>
          <tr>
            <td class="col-field">Opening Balances</td>
            <td>Teal Outline Button</td>
            <td>Opens configuration interface to establish initial starting balances for newly registered bank ledgers.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Downloads current filtered account ledger tree directly to spreadsheet or formatted PDF document.</td>
          </tr>
          <tr>
            <td class="col-field">Account Class Pills</td>
            <td>Filter Badges</td>
            <td>Filters accounts by range: Assets (1000-1999), Liabilities (2000-2999), Equity (3000-3999), etc.</td>
          </tr>
        </tbody>
      </table>

      <h2>Data Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 16%;">Data Type</th>
            <th style="width: 62%;">On-Screen Information & Accounting Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">ACCOUNT CODE</td>
            <td>Numeric Code</td>
            <td>4-digit primary code (e.g. 1010) with lock icon indicating protected system control account.</td>
          </tr>
          <tr>
            <td class="col-field">ACCOUNT TITLE</td>
            <td>Text & Subtext</td>
            <td>Official title (e.g. <em>Cash and Cash Equivalents</em>) and descriptive scope (checking, savings, treasury).</td>
          </tr>
          <tr>
            <td class="col-field">CLASSIFICATION / TAG</td>
            <td>Regulatory Tag</td>
            <td>Statutory accounting framework tag (e.g. <code>GAAP Primary</code>).</td>
          </tr>
          <tr>
            <td class="col-field">TYPE & NORMAL</td>
            <td>Badges</td>
            <td>Balance sheet classification (<code>ASSET</code> blue badge) and normal balance side (<code>DEBIT</code>).</td>
          </tr>
          <tr>
            <td class="col-field">CURRENCY</td>
            <td>Currency Code</td>
            <td>Designated functional ledger currency (e.g. <code>AED (Base)</code>).</td>
          </tr>
          <tr>
            <td class="col-field">CURRENT BALANCE</td>
            <td>Currency Amount</td>
            <td>Live net ledger balance calculated from all posted debits minus credits (e.g. <code>AED 0.00</code>).</td>
          </tr>
          <tr>
            <td class="col-field">ACTIONS</td>
            <td>Context Trigger</td>
            <td>Clickable <code>+ Map Sub</code> trigger to immediately add a child account under that parent node.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">SUB-ACCOUNT HIERARCHY NOTE</div>
        When expanding Account 1010, the system displays: <em>"No custom sub-accounts mapped under 1010. Click '+ Map Sub' to create one."</em> Create dedicated sub-accounts for each operational bank account (e.g. Emirates NBD Operating, FAB Payroll).
      </div>
    </div>
    """

def get_page_07():
    wf = window_frame(
        "images/03_Bank_Reconciliation.png",
        "Bank Reconciliation & General Ledger Statement Matching Interface",
        "/banking/reconciliation",
        [
            ("Bank Account Selector", "Dropdown to select target corporate bank account and statement ending date."),
            ("Dual Ledger Grids", "Two-column comparison displaying Bank Statement Lines vs General Ledger Records."),
            ("Auto-Match Engine", "One-click trigger to automatically pair matching amounts, reference dates, and check numbers."),
            ("Variance Telemetry", "Real-time indicator displaying Cleared Balance, Statement Balance, and Difference.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · TREASURY CONTROLS</div>
          <div class="chapter-title">Bank Statement Reconciliation & Ledger Matching</div>
        </div>
        <div class="chapter-right-meta">MODULE 03<br>/banking/reconciliation</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Banking ➔ Bank Reconciliation (or <kbd>Alt + R</kbd>)
      </div>

      <p>
        The Bank Reconciliation interface enables treasury operators to verify electronic bank statements against the internal General Ledger, ensuring cash account balances match verified external bank statements with zero discrepancy.
      </p>

      {wf}

      <h2>Primary Action Buttons & Screen Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Screen Element</th>
            <th style="width: 20%;">Visual Style</th>
            <th style="width: 55%;">On-Screen Function & System Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Import Statement</td>
            <td>Solid Blue Button</td>
            <td>Uploads electronic bank statement files formatted in standard OFX, QIF, or CSV bank formats.</td>
          </tr>
          <tr>
            <td class="col-field">Auto-Match</td>
            <td>Solid Green Button</td>
            <td>Executes automated matching algorithm comparing statement line amounts and dates against open ledger entries.</td>
          </tr>
          <tr>
            <td class="col-field">+ Adjusting Journal</td>
            <td>Outline Button</td>
            <td>Direct shortcut to create adjusting journal entries for unrecorded bank charges, interest, or wire fees.</td>
          </tr>
          <tr>
            <td class="col-field">Finalize Reconciliation</td>
            <td>Solid Purple Button</td>
            <td>Locks the reconciled period and marks all selected transactions as permanently cleared in the ledger.</td>
          </tr>
        </tbody>
      </table>

      <h2>Reconciliation Summary Telemetry & Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Telemetry Card</th>
            <th style="width: 22%;">Calculation Method</th>
            <th style="width: 54%;">Operational Meaning & Balancing Requirement</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Statement Ending Balance</td>
            <td>User Entered / File Header</td>
            <td>The official closing cash balance extracted directly from the uploaded bank statement.</td>
          </tr>
          <tr>
            <td class="col-field">Cleared Ledger Balance</td>
            <td>Sum of Matched Items</td>
            <td>Running total of all internal ledger vouchers marked as cleared in the active reconciliation session.</td>
          </tr>
          <tr>
            <td class="col-field">Unreconciled Difference</td>
            <td>Statement minus Cleared</td>
            <td>Variance balance; must display exactly <code>0.00 AED</code> before the period can be finalized.</td>
          </tr>
        </tbody>
      </table>

      <h2>Matching Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 26%;">Statement Panel Line</th>
            <th style="width: 26%;">General Ledger Panel Line</th>
            <th style="width: 26%;">Matching Verification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Transaction Date</td>
            <td>Bank value clearance date.</td>
            <td>GL voucher posting date.</td>
            <td>Must fall within allowable tolerance window.</td>
          </tr>
          <tr>
            <td class="col-field">Reference / Description</td>
            <td>Bank narration or wire memo.</td>
            <td>Vendor bill / Invoice number.</td>
            <td>Keyword matching against counterparty name.</td>
          </tr>
          <tr>
            <td class="col-field">Amount (Debit / Credit)</td>
            <td>Statement deposit or withdrawal.</td>
            <td>Ledger debit or credit amount.</td>
            <td>Exact numeric match required to auto-pair.</td>
          </tr>
          <tr>
            <td class="col-field">Selection Checkbox</td>
            <td>Statement line select box.</td>
            <td>Internal ledger select box.</td>
            <td>Manual pairing for items with slight date variance.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_08():
    wf = window_frame(
        "images/05_Sales_Invoice.png",
        "Commercial Sales Invoicing Register with Tax Invoice Creation and AR Status",
        "/invoices",
        [
            ("Primary Action Bar", "Upload & OCR Scan, e-Invoicing drafts, and + New Sales Invoice buttons."),
            ("4 Top KPI Metric Cards", "Total Receivables (AR), Total Payables (AP), Sales Invoiced, and OCR & GL Automated."),
            ("Filter & Search Controls", "Multi-attribute text search input, All Statuses dropdown, and Excel/PDF export buttons."),
            ("8-Column Register Grid", "Invoice/Bill #, Type, Customer/Vendor, Dates, Total Amount, GL Status, Status, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · ORDER-TO-CASH</div>
          <div class="chapter-title">Customer Invoicing & Accounts Receivable (AR)</div>
        </div>
        <div class="chapter-right-meta">MODULE 04<br>/invoices</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Customer Activity ➔ Sales Invoice (or <kbd>Alt + I</kbd>)
      </div>

      <p>
        The Sales Invoice workspace serves as the primary commercial billing interface in Acconeer ERP, providing real-time tracking of accounts receivable, automated AI OCR document intake, and synchronous General Ledger voucher posting.
      </p>

      {wf}

      <h2>Primary Action Buttons & Screen Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Screen Element</th>
            <th style="width: 20%;">Visual Style</th>
            <th style="width: 55%;">On-Screen Function & System Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">+ New Sales Invoice</td>
            <td>Solid Green Button</td>
            <td>Opens modal to create a manual commercial invoice with customer lookup, SKU items, and VAT rules.</td>
          </tr>
          <tr>
            <td class="col-field">Upload & OCR Scan</td>
            <td>Purple Border Button</td>
            <td>Triggers AI optical character recognition to upload scanned PDFs/images and auto-populate line items.</td>
          </tr>
          <tr>
            <td class="col-field">e-Invoicing drafts</td>
            <td>White Border Button</td>
            <td>Displays pending electronic invoices formatted for statutory XML/UBL e-invoicing compliance.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Exports current filtered invoice register records directly to `.xlsx` spreadsheet or `.pdf` document.</td>
          </tr>
        </tbody>
      </table>

      <h2>On-Screen Metric & Telemetry Cards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Metric Card</th>
            <th style="width: 18%;">Display Value</th>
            <th style="width: 58%;">Calculation Source & Operational Meaning on Screen</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Total Receivables (AR)</td>
            <td><code>AED 0.00</code></td>
            <td>Outstanding unsettled customer balances awaiting payment (synced from Account 1020).</td>
          </tr>
          <tr>
            <td class="col-field">Total Payables (AP)</td>
            <td><code>AED 0.00</code></td>
            <td>Total outstanding vendor obligations awaiting disbursement for commercial cash context.</td>
          </tr>
          <tr>
            <td class="col-field">Sales Invoiced (Period)</td>
            <td><code>AED 0.00</code></td>
            <td>Cumulative gross revenue billed across the current fiscal period scope.</td>
          </tr>
          <tr>
            <td class="col-field">OCR & GL Automated</td>
            <td><code>0 Docs / 0 Posted</code></td>
            <td>Document intake counter showing OCR-parsed invoices versus ledger-posted records.</td>
          </tr>
        </tbody>
      </table>

      <h2>Register Data Grid Columns & Operational Statuses</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 60%;">On-Screen Information & Action Capability</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Invoice / Bill #</td>
            <td>Sequential Link</td>
            <td>Unique reference code; clickable to view complete invoice line items and tax breakdown.</td>
          </tr>
          <tr>
            <td class="col-field">Type</td>
            <td>Badge</td>
            <td>Document classification: Standard Tax Invoice, Recurring Invoice, or Credit Note.</td>
          </tr>
          <tr>
            <td class="col-field">Customer / Vendor</td>
            <td>Entity Name</td>
            <td>Registered legal trading name and tax registration number (TRN) of the client.</td>
          </tr>
          <tr>
            <td class="col-field">Dates & Total Amount</td>
            <td>Date & Currency</td>
            <td>Invoice issuance date, payment due date, and gross billing amount in AED inclusive of 5% VAT.</td>
          </tr>
          <tr>
            <td class="col-field">GL Ledger Status</td>
            <td>Sync Indicator</td>
            <td>Real-time General Ledger posting status (<code>Posted</code>, <code>Pending Sync</code>, <code>Error</code>).</td>
          </tr>
          <tr>
            <td class="col-field">Status & Actions</td>
            <td>Badge & Action Menu</td>
            <td>Payment badge (Draft, Unpaid, Paid, Overdue) and action menu to Download PDF, Email, or Issue Credit Note.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no invoices exist in the active scope, the workspace displays: <em>"No invoices found — Upload an invoice via AI OCR or create a new invoice to start auto-posting to the General Ledger."</em>
      </div>
    </div>
    """

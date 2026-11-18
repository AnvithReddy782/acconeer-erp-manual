# scripts/pages_p01_p08.py
from generate_complete_manual import get_base64_logo, window_frame

def get_page_01():
    logo_base64 = get_base64_logo()
    return f"""
    <div class="page cover-page-wrapper">
      <div class="cover-top">
        <div class="cover-logo-box">
          <img src="{logo_base64}" alt="Spectrum Zestwings Technologies">
        </div>
        <div class="cover-badge-top">
          <span class="cover-dot"></span>
          <span>Enterprise System Documentation • Rev 3.0</span>
        </div>
      </div>

      <div class="cover-body">
        <div class="cover-eyebrow">Enterprise Operations Standard • Volume I</div>
        <h1 class="cover-title">ACCONEER ERP</h1>
        <div class="cover-subtitle">Universal Standard Operating Manual: Multi-Entity Governance, Financial Ledgers & UAE Statutory Compliance</div>
        <div class="cover-rule">
          <div class="cover-rule-red"></div>
          <div class="cover-rule-blue"></div>
        </div>
        <p class="cover-desc">
          The official operational standard for Acconeer ERP. Enforces multi-entity enterprise hierarchies, synchronous general ledger double-entry accounting, commercial order-to-cash workflows, procure-to-pay expenditure controls, UAE FTA VAT Form 201 statutory compliance, and governed human-in-the-loop AI assistance across UAE and GCC enterprise markets.
        </p>

        <div class="cover-meta-grid">
          <div class="cover-meta-card">
            <div class="cover-meta-label">System Platform & Portal</div>
            <div class="cover-meta-val">acconeer.zestwings.com</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Developer & Technology Owner</div>
            <div class="cover-meta-val">Spectrum Zestwings Technologies LLC</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Operating Currency & Market</div>
            <div class="cover-meta-val">UAE / GCC Market • Currency: AED</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Statutory Compliance Baseline</div>
            <div class="cover-meta-val">UAE FTA VAT Form 201 • CBUAE WPS SIF • IFRS</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Document Classification</div>
            <div class="cover-meta-val">Volume I: Universal Enterprise Manual</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Reference Tenant Implementation</div>
            <div class="cover-meta-val">Gulf Horizon General Trading LLC (AED)</div>
          </div>
        </div>
      </div>

      <div class="cover-footer">
        <div>
          <strong>Spectrum Zestwings Technologies LLC</strong> • Dubai Silicon Oasis, UAE<br>
          Enterprise Portal: <span class="badge-mono" style="background:rgba(255,255,255,0.1);color:#FFFFFF;border:none;">www.sztech.ae</span> • Inquiries: <span class="badge-mono" style="background:rgba(255,255,255,0.1);color:#FFFFFF;border:none;">support@sztech.ae</span>
        </div>
        <div style="text-align: right;">
          Document Control ID: <strong>DOC-ACC-OPS-V3.0</strong><br>
          Status: <strong>Production Enterprise Standard (Nov 2026)</strong>
        </div>
      </div>
    </div>
    """

def get_page_02():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">SYSTEM ARCHITECTURE</div>
          <div class="chapter-title">Multi-Entity Governance & Scope Hierarchy</div>
        </div>
        <div class="chapter-cat">ENTERPRISE FRAMEWORK</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Universal Header ➔ Global 4-Tier Scope Selector
      </div>

      <p>
        Acconeer ERP enforces a rigorous 4-tier relational hierarchy designed to guarantee strict data separation, consolidated financial reporting, and auditable accounting boundaries across diversified corporate groups operating in the UAE and GCC.
      </p>

      <div class="brand-divider">
        <div class="brand-divider-red"></div>
        <div class="brand-divider-blue"></div>
      </div>

      <h2>Unified 4-Tier Scope Selector Architecture</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 12%;">Tier Level</th>
            <th style="width: 24%;">Hierarchy Node</th>
            <th style="width: 38%;">Universal Reference Instance</th>
            <th style="width: 26%;">Accounting & Governance Scope</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="badge-mono">Tier 1</td>
            <td><strong>Organization</strong></td>
            <td><code>Gulf Horizon Group Holding Ltd</code></td>
            <td>Top-level holding entity; defines global Chart of Accounts templates, currency rules, and master security policies.</td>
          </tr>
          <tr>
            <td class="badge-mono">Tier 2</td>
            <td><strong>Legal Entity</strong></td>
            <td><code>Gulf Horizon General Trading LLC (AED)</code></td>
            <td>Tax-registered legal entity holding the official UAE FTA Tax Registration Number (TRN <code>100999900000003</code>).</td>
          </tr>
          <tr>
            <td class="badge-mono">Tier 3</td>
            <td><strong>Branch Scope</strong></td>
            <td><code>Main Operations Branch (Dubai)</code> • <code>Abu Dhabi Depot</code></td>
            <td>Physical operating location, warehouse facility, and cost-center boundary for departmental profit-and-loss reporting.</td>
          </tr>
          <tr>
            <td class="badge-mono">Tier 4</td>
            <td><strong>Fiscal Period Scope</strong></td>
            <td><code>FY 2026</code> • <code>Q3 2026</code> • <code>September 2026</code></td>
            <td>Active operational filter determining which posted transactions appear in registers, reports, and tax declarations.</td>
          </tr>
        </tbody>
      </table>

      <h2>Posting Boundaries & Accounting Scope Controls</h2>
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
            <td class="col-field">Session Filter vs. Period Lock</td>
            <td>Top-bar selector is a view filter, not an administrative lock</td>
            <td>Selecting <em>Q3 2026</em> restricts on-screen data. Locking a period is a separate GL control preventing retroactive entries.</td>
          </tr>
          <tr>
            <td class="col-field">Entity Posting Boundary</td>
            <td>Sub-ledgers post strictly to the active Legal Entity</td>
            <td>Invoices, bills, and payments write directly to the selected Legal Entity's general ledger accounts (Class 1000–6000).</td>
          </tr>
          <tr>
            <td class="col-field">Inter-Company Transactions</td>
            <td>Automated reciprocal Due-To / Due-From entries</td>
            <td>Cross-entity billing automatically generates balancing vouchers between entities (Account 1950 Intercompany Due From / 2950 Due To).</td>
          </tr>
          <tr>
            <td class="col-field">Consolidated Reporting</td>
            <td>Dynamic elimination of inter-company balances</td>
            <td>Selecting <em>All entities</em> provides consolidated P&L and Balance Sheet with inter-entity balances eliminated.</td>
          </tr>
        </tbody>
      </table>

      <h2>Relational Scope Isolation & Fiscal Integrity Controls</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Row-Level Tenant Isolation</h4>
          <p>Database queries strictly enforce organization and legal entity IDs via Row-Level Security (RLS), preventing cross-tenant data exposure.</p>
        </div>
        <div class="matching-card">
          <h4>Branch Cost Center Tagging</h4>
          <p>Every commercial invoice and vendor bill carries a mandatory Branch ID, enabling segmental P&L reporting across Dubai and Abu Dhabi.</p>
        </div>
        <div class="matching-card">
          <h4>Administrative Period Locking</h4>
          <p>Closed fiscal periods reject new transaction postings. Reopening requires Chief Accountant approval and logs a permanent audit entry.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Establishing Active Operational Scope</div>
        <ol class="proc-steps">
          <li>Upon signing into <code>acconeer.zestwings.com</code>, confirm your assigned Organization in the upper-left navigation header.</li>
          <li>Select the operational <strong>Legal Entity</strong> (e.g., <em>Gulf Horizon General Trading LLC</em>). For consolidated group review, choose <em>All entities</em>.</li>
          <li>Select the target <strong>Branch Scope</strong> to isolate local operations or perform warehouse-specific allocations.</li>
          <li>Set the active <strong>Fiscal Reporting Period</strong> to match the transaction date range under review.</li>
          <li>Confirm that the active period status displays <span class="badge-mono badge-green">OPEN</span> prior to processing financial transactions.</li>
        </ol>
      </div>
    </div>
    """

def get_page_03():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">SYSTEM GOVERNANCE</div>
          <div class="chapter-title">Universal System Toolbar & Segregation of Duties</div>
        </div>
        <div class="chapter-cat">GLOBAL NAVIGATION & SECURITY</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Global Header Navigation Bar ➔ Universal Toolbar
      </div>

      <p>
        The Universal System Toolbar is persistently positioned at the top of every Acconeer ERP workspace. It hosts primary transactional dispatchers, ledger balance synchronization triggers, and administrative governance controls.
      </p>

      <div class="brand-divider">
        <div class="brand-divider-red"></div>
        <div class="brand-divider-blue"></div>
      </div>

      <h2 style="margin-top: 3pt; margin-bottom: 2pt;">Universal Header Action Triggers & System Capabilities</h2>
      <table class="doc-table" style="margin: 2.5pt 0; font-size: 7.2pt;">
        <thead>
          <tr>
            <th style="width: 24%;">Toolbar Action Button</th>
            <th style="width: 20%;">Execution Shortcut</th>
            <th style="width: 32%;">Primary Operational Function</th>
            <th style="width: 24%;">Minimum Authorized Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="badge-mono badge-blue">Create</span></td>
            <td>Global Action Modal</td>
            <td>Opens instant creation drawer for Invoices, Bills, Journal Entries, and SKUs without navigating away.</td>
            <td>Operational Staff / Clerks</td>
          </tr>
          <tr>
            <td><span class="badge-mono">Dashboard</span></td>
            <td>Alt + D</td>
            <td>Returns immediately to the consolidated executive financial overview and KPI metrics.</td>
            <td>All Authorized Users</td>
          </tr>
          <tr>
            <td><span class="badge-mono">Manage Organization</span></td>
            <td>Admin Console</td>
            <td>Configuration of Legal Entities, trade licenses, UAE VAT TRNs, and branch tax registration.</td>
            <td>System Administrator</td>
          </tr>
          <tr>
            <td><span class="badge-mono">Manage Users</span></td>
            <td>Security Portal</td>
            <td>User invitation, role assignment, multi-factor authentication (MFA), and session management.</td>
            <td>Security Administrator</td>
          </tr>
          <tr>
            <td><span class="badge-mono badge-red">Refresh Ledger State</span></td>
            <td>Administrative Trigger</td>
            <td>Executes a real-time ledger balance recalculation sweep across all journal vouchers and accounts.</td>
            <td>Chief Accountant / Finance Lead</td>
          </tr>
          <tr>
            <td><span class="badge-mono badge-green">New Journal</span></td>
            <td>Alt + J</td>
            <td>Direct trigger opening the double-entry journal voucher creation interface with auto-balancing.</td>
            <td>General Ledger Accountants</td>
          </tr>
          <tr>
            <td><span class="badge-mono badge-blue">Invoices</span></td>
            <td>Alt + I</td>
            <td>Quick jump to the commercial sales invoicing ledger and customer accounts receivable directory.</td>
            <td>Billing & AR Specialists</td>
          </tr>
        </tbody>
      </table>

      <h2 style="margin-top: 3pt; margin-bottom: 2pt;">Segregation of Duties (SoD) & Role Governance Matrix</h2>
      <table class="doc-table" style="margin: 2.5pt 0; font-size: 7.2pt;">
        <thead>
          <tr>
            <th style="width: 25%;">Enterprise Role Category</th>
            <th style="width: 40%;">Authorized Functional Scope</th>
            <th style="width: 35%;">Strict Internal Control Restrictions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Finance Director / CFO</td>
            <td>Period closure, financial statements, bank mandate release, tax sign-off.</td>
            <td><strong>Restricted from operational data entry:</strong> cannot originate vendor bills, sales invoices, or clerical journals.</td>
          </tr>
          <tr>
            <td class="col-field">Chief Accountant</td>
            <td>GL adjustments, manual JVs, bank reconciliation, 3-way match exceptions.</td>
            <td><strong>Restricted from disbursement release:</strong> cannot approve outbound bank transfers or release payment files.</td>
          </tr>
          <tr>
            <td class="col-field">Operational Clerks (AR/AP)</td>
            <td>Data entry of invoices, bills, inventory intake, and employee timesheets.</td>
            <td><strong>Restricted from GL postings:</strong> cannot post manual journal vouchers or alter chart of accounts mapping.</td>
          </tr>
          <tr>
            <td class="col-field">System Administrator</td>
            <td>User lifecycle, RBAC assignments, security policies, system configuration.</td>
            <td><strong>Zero transactional authority:</strong> cannot create, edit, or approve financial transactions or view financial data.</td>
          </tr>
        </tbody>
      </table>

      <h2 style="margin-top: 3pt; margin-bottom: 2pt;">Synchronous Posting vs. Administrative Recalculation</h2>
      <div class="matching-grid" style="margin: 3pt 0;">
        <div class="matching-card">
          <h4>Synchronous Posting</h4>
          <p>All approved transactions (invoices, receipts, bills, journals) write immediately and synchronously to the General Ledger upon submission.</p>
        </div>
        <div class="matching-card">
          <h4>Reporting Balance Cache</h4>
          <p>Dashboard cards and summary reports draw from pre-aggregated balance rollups for instantaneous sub-second query performance.</p>
        </div>
        <div class="matching-card">
          <h4>Ledger Integrity Sweep</h4>
          <p>The <em>Refresh Ledger State</em> tool validates debits against credits, clears report caches, and confirms zero variance across accounts.</p>
        </div>
      </div>

      <div class="proc-box" style="margin-top: 3pt;">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Running an Administrative Ledger Balance Sweep</div>
        <ol class="proc-steps">
          <li>Ensure all operational batch postings (invoices, payments, payroll) are completed for the session.</li>
          <li>Verify the active Legal Entity and Fiscal Reporting Period in the global scope selector.</li>
          <li>Click <strong>Refresh Ledger State</strong> in the universal top toolbar (restricted to Chief Accountant).</li>
          <li>Await confirmation prompt: <em>"General Ledger Synchronized — Debits Equal Credits (0.00 Variance)."</em></li>
        </ol>
      </div>
    </div>
    """

def get_page_04():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">DOCUMENT STRUCTURE</div>
          <div class="chapter-title">Table of Contents & 5-Part Enterprise Lifecycle Map</div>
        </div>
        <div class="chapter-cat">MASTER MANUAL SITEMAP</div>
      </div>

      <p>
        This manual is structured into five cohesive enterprise lifecycle sections encompassing all Acconeer ERP operational modules. Each chapter provides step-by-step operating procedures, data dictionaries, validation rules, error handling, and accounting posting impacts.
      </p>

      <div class="brand-divider">
        <div class="brand-divider-red"></div>
        <div class="brand-divider-blue"></div>
      </div>

      <div class="toc-card">
        <div class="toc-grid">
          <div>
            <div style="font-family: var(--font-mono); font-size: 6.8pt; font-weight: 700; color: var(--color-blue); text-transform: uppercase; margin-bottom: 2pt;">Part I: Architecture & System Controls</div>
            <div class="toc-row"><span class="toc-num">01</span><span class="toc-name">System Architecture & Multi-Entity Scope</span><span class="toc-pnum">Page 02</span></div>
            <div class="toc-row"><span class="toc-num">02</span><span class="toc-name">Universal Toolbar & Segregation of Duties</span><span class="toc-pnum">Page 03</span></div>
            <div class="toc-row"><span class="toc-num">03</span><span class="toc-name">Table of Contents & Enterprise Lifecycle Map</span><span class="toc-pnum">Page 04</span></div>

            <div style="font-family: var(--font-mono); font-size: 6.8pt; font-weight: 700; color: var(--color-blue); text-transform: uppercase; margin-top: 4pt; margin-bottom: 2pt;">Part II: Commercial & Operational Cycles</div>
            <div class="toc-row"><span class="toc-num">04</span><span class="toc-name">Executive Financial Dashboard & KPI Telemetry</span><span class="toc-pnum">Page 05</span></div>
            <div class="toc-row"><span class="toc-num">05</span><span class="toc-name">Banking & Corporate Account Management</span><span class="toc-pnum">Page 06</span></div>
            <div class="toc-row"><span class="toc-num">06</span><span class="toc-name">Bank Statement Reconciliation & Clearing</span><span class="toc-pnum">Page 07</span></div>
            <div class="toc-row"><span class="toc-num">07</span><span class="toc-name">Customer Activity: Commercial Invoicing</span><span class="toc-pnum">Page 08</span></div>
            <div class="toc-row"><span class="toc-num">08</span><span class="toc-name">Order-to-Cash Lifecycle: Orders & Receipts</span><span class="toc-pnum">Page 09</span></div>
            <div class="toc-row"><span class="toc-num">09</span><span class="toc-name">Supplier Activity: Bills & 3-Way Matching</span><span class="toc-pnum">Page 10</span></div>
            <div class="toc-row"><span class="toc-num">10</span><span class="toc-name">Vendor Directory & Disbursement Governance</span><span class="toc-pnum">Page 11</span></div>
          </div>

          <div>
            <div style="font-family: var(--font-mono); font-size: 6.8pt; font-weight: 700; color: var(--color-blue); text-transform: uppercase; margin-bottom: 2pt;">Part III: General Ledger, Assets & Inventory</div>
            <div class="toc-row"><span class="toc-num">11</span><span class="toc-name">General Ledger & Manual Journal Entries</span><span class="toc-pnum">Page 12</span></div>
            <div class="toc-row"><span class="toc-num">12</span><span class="toc-name">Chart of Accounts (COA Master)</span><span class="toc-pnum">Page 13</span></div>
            <div class="toc-row"><span class="toc-num">13</span><span class="toc-name">Inventory Master Catalog & Valuation</span><span class="toc-pnum">Page 14</span></div>
            <div class="toc-row"><span class="toc-num">14</span><span class="toc-name">Goods Received Notes (GRN) & Intake</span><span class="toc-pnum">Page 15</span></div>
            <div class="toc-row"><span class="toc-num">15</span><span class="toc-name">Fixed Assets & Depreciation Accounting</span><span class="toc-pnum">Page 16</span></div>

            <div style="font-family: var(--font-mono); font-size: 6.8pt; font-weight: 700; color: var(--color-blue); text-transform: uppercase; margin-top: 4pt; margin-bottom: 2pt;">Part IV: HR, Payroll & Statutory Tax</div>
            <div class="toc-row"><span class="toc-num">16</span><span class="toc-name">HR & Workforce Management</span><span class="toc-pnum">Page 17</span></div>
            <div class="toc-row"><span class="toc-num">17</span><span class="toc-name">Payroll Engine & UAE WPS Compliance</span><span class="toc-pnum">Page 18</span></div>
            <div class="toc-row"><span class="toc-num">18</span><span class="toc-name">Financial Reporting & Comparative Variance</span><span class="toc-pnum">Page 19</span></div>
            <div class="toc-row"><span class="toc-num">19</span><span class="toc-name">VAT Returns: UAE FTA Form 201 Engine</span><span class="toc-pnum">Page 20</span></div>
            <div class="toc-row"><span class="toc-num">20</span><span class="toc-name">VAT Settlement & EmaraTax Calendar</span><span class="toc-pnum">Page 21</span></div>

            <div style="font-family: var(--font-mono); font-size: 6.8pt; font-weight: 700; color: var(--color-blue); text-transform: uppercase; margin-top: 4pt; margin-bottom: 2pt;">Part V: Governance, Security, AI & Support</div>
            <div class="toc-row"><span class="toc-num">21</span><span class="toc-name">Document Vault & Retention Governance</span><span class="toc-pnum">Page 22</span></div>
            <div class="toc-row"><span class="toc-num">22</span><span class="toc-name">Audit Trail & Security Telemetry</span><span class="toc-pnum">Page 23</span></div>
            <div class="toc-row"><span class="toc-num">23</span><span class="toc-name">Budgeting & Fiscal Variance Controls</span><span class="toc-pnum">Page 24</span></div>
            <div class="toc-row"><span class="toc-num">24</span><span class="toc-name">AI Assistant & Responsible Use Controls</span><span class="toc-pnum">Page 25</span></div>
            <div class="toc-row"><span class="toc-num">25</span><span class="toc-name">Document Control, Requirements & Support</span><span class="toc-pnum">Page 26</span></div>
          </div>
        </div>
      </div>

      <h2>Document Typography & Visual Syntax Key</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Visual Syntax</th>
            <th style="width: 30%;">Semantic Meaning</th>
            <th style="width: 50%;">Operational Reading Guideline</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="badge-mono badge-blue">Blue Badge</span></td>
            <td>Primary Action / State Trigger</td>
            <td>Interactive UI button, command trigger, or active filter selection.</td>
          </tr>
          <tr>
            <td><span class="badge-mono badge-red">Red Badge</span></td>
            <td>Irreversible / Financial Action</td>
            <td>Irreversible general ledger commit, period closure, or statutory submission.</td>
          </tr>
          <tr>
            <td><span class="badge-mono"><code>Mono Code</code></span></td>
            <td>System Identifiers & Routes</td>
            <td>Database account code, transaction number, UAE TRN string, or API route.</td>
          </tr>
          <tr>
            <td><span class="legend-badge" style="width:14px;height:14px;font-size:7pt;">1</span></td>
            <td>Numbered UI Anchor</td>
            <td>Correlates the authentic screenshot frame with the contextual feature breakdown.</td>
          </tr>
        </tbody>
      </table>

      <h2>Statutory & Regulatory Compliance Baselines</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>UAE Federal Tax Authority (FTA)</h4>
          <p>Federal Decree-Law No. 8 on Value Added Tax, Cabinet Decision No. 52 (Executive Regulations), and official Form 201 declarations.</p>
        </div>
        <div class="matching-card">
          <h4>UAE Central Bank WPS</h4>
          <p>Ministry of Human Resources and Emiratisation (MOHRE) Wages Protection System compliance via encrypted SIF v1.2 file exports.</p>
        </div>
        <div class="matching-card">
          <h4>IFRS & UAE Corporate Tax</h4>
          <p>IAS 16 asset depreciation, double-entry general ledger balancing, and Federal Decree-Law No. 47 of 2022 accounting record compliance.</p>
        </div>
      </div>

      <h2>Enterprise Documentation Governance & Lifecycle Standard</h2>
      <div class="sop-meta-grid" style="margin-top: 4pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Volume I Scope: Universal Standard</div>
          <div class="sop-meta-desc">Establishes universal software operation, ledger architecture, and statutory baselines. Tenant-specific configuration parameters are maintained in Volume II addenda.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Revision Governance & Versioning</div>
          <div class="sop-meta-desc">Major version changes (e.g. 3.0) denote statutory schema revisions; minor increments reflect UI field updates. All operational staff must operate against current published manuals.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Internal Audit & Evidence Retention</div>
          <div class="sop-meta-desc">Mandatory 5-year retention for all accounting records, electronic tax invoices, and bank clearing files pursuant to UAE Federal Law No. 47 of 2022.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Authorized System Administrators</div>
          <div class="sop-meta-desc">Annual operational manual reviews are conducted by the Chief Financial Officer and certified by Spectrum Zestwings Technologies LLC.</div>
        </div>
      </div>
    </div>
    """

def get_page_05():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Dashboard/01_Executive_Dashboard.png",
        "Executive Dashboard with Multi-Entity Scoping and Financial KPI Cards",
        "/dashboard",
        [
            ("4-Tier Scope Selector", "Filters financial telemetry by Organization, Legal Entity, Branch, and Period."),
            ("Primary Action Bar", "Direct triggers for Refresh Ledger State, + New Journal, and Invoices."),
            ("Executive KPI Cards", "Displays Total Revenue, Gross Profit, Cash Liquidity, Receivables, and Payables in AED."),
            ("Trend Charts & Ledger Drill", "Cash trajectory, operational expense breakdown, and one-click sub-ledger drill-down.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 01 · MODULE 01</div>
          <div class="chapter-title">Executive Financial Dashboard & KPI Telemetry</div>
        </div>
        <div class="chapter-cat">EXECUTIVE OPERATIONS</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Dashboard
      </div>

      <p>
        The Executive Financial Dashboard provides consolidated visibility into revenue generation, gross and net profitability, available cash liquidity, customer receivables (AR), and supplier payables (AP) across all selected legal entities and branches.
      </p>

      {wf}

      <h2>Core Financial KPI Metrics & Performance Cockpit</h2>
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-label">Total Revenue (YTD)</div>
          <div class="kpi-val">AED 1,248,500</div>
          <div class="kpi-sub">Account Class 4000 • Net of Credit Notes</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Net Profit Margin</div>
          <div class="kpi-val" style="color: var(--color-green);">18.4%</div>
          <div class="kpi-sub">AED 229,724 • Post OpEx & Tax</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Cash & Bank Liquidity</div>
          <div class="kpi-val" style="color: var(--color-blue);">AED 842,100</div>
          <div class="kpi-sub">Class 1010 • Reconciled Bank Balances</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Gross Profit Rate</div>
          <div class="kpi-val">32.1%</div>
          <div class="kpi-sub">Revenue minus Direct COGS (5000)</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Receivables (AR)</div>
          <div class="kpi-val" style="color: var(--color-amber);">AED 312,400</div>
          <div class="kpi-sub">Class 1200 • Open Customer Invoices</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Payables (AP)</div>
          <div class="kpi-val" style="color: var(--color-red);">AED 184,600</div>
          <div class="kpi-sub">Class 2100 • Pending Supplier Bills</div>
        </div>
      </div>

      <h2>Executive KPI Master Dictionary & Calculation Bases</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Executive Metric</th>
            <th style="width: 32%;">General Ledger Calculation Formula</th>
            <th style="width: 26%;">Sub-Ledger Source Data</th>
            <th style="width: 20%;">Refresh Frequency</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Total Revenue</td>
            <td><code>Sum(Credits 4000) - Sum(Debits 4000)</code></td>
            <td>Posted Sales Invoices net of Credit Notes</td>
            <td>Real-Time Synchronous</td>
          </tr>
          <tr>
            <td class="col-field">Net Profit Margin</td>
            <td><code>(Sales 4000 - COGS 5000 - OpEx 6000) / Sales 4000</code></td>
            <td>Full P&L Account Rollups</td>
            <td>Cached / 5-Min Sweep</td>
          </tr>
          <tr>
            <td class="col-field">Cash Liquidity</td>
            <td><code>Sum(Debits 1010) - Sum(Credits 1010)</code></td>
            <td>Reconciled Bank Accounts & Petty Cash</td>
            <td>Real-Time Synchronous</td>
          </tr>
          <tr>
            <td class="col-field">Working Capital</td>
            <td><code>Current Assets (1000) / Current Liabilities (2000)</code></td>
            <td>Balance Sheet Asset/Liability Rollups</td>
            <td>Real-Time Synchronous</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Operational Procedure: Setting Scope & Drilling Down into KPI Balances</div>
        <ol class="proc-steps">
          <li>Select the operational Legal Entity (e.g. <em>Gulf Horizon General Trading LLC</em>) and target Branch from the top scope bar.</li>
          <li>Set the active Fiscal Period (e.g. <em>Q3 2026</em>) to align dashboard telemetry with the financial reporting window.</li>
          <li>Click any KPI Card (e.g., <strong>Receivables AED 312,400</strong>) to open the underlying sub-ledger transaction drill-down.</li>
          <li>Inspect real-time line-item vouchers, debtor aging buckets, and customer tax registration numbers directly from the drill-down grid.</li>
          <li>Operational clerks are restricted to branch operational cards; executive profitability cards require Chief Accountant or CFO permissions.</li>
        </ol>
      </div>

      <div class="note-card" style="margin-top: 3.5pt; margin-bottom: 0;">
        <div class="note-card-title">Executive Telemetry & Row-Level Data Security</div>
        <strong>Dynamic Multi-Entity Rollup:</strong> Changing the Legal Entity selector dynamically recompiles all dashboard aggregates within &lt; 350ms using PostgreSQL Row-Level Security (RLS). Users with single-branch clearance are automatically prevented from viewing group-consolidated liquidity balances.
      </div>
    </div>
    """

def get_page_06():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Banking/02_Bank_Accounts.png",
        "Registered Corporate Bank Accounts with Cleared Ledger Balances",
        "/banking/accounts",
        [
            ("View Switcher", "Toggle between Registered Bank Accounts and Statement Reconciliation workspaces."),
            ("Bank Registry Table", "Lists registered banking institutions, account numbers, IBANs, and current cleared balances in AED."),
            ("Add Bank Account Action", "Opens creation modal to register new banking relationships and assign GL account codes."),
            ("Reconciliation Trigger", "Direct action button to initiate period-end bank statement clearing.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 02 · MODULE 02 (PART 1)</div>
          <div class="chapter-title">Banking & Corporate Account Management</div>
        </div>
        <div class="chapter-cat">TREASURY & LIQUIDITY</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Banking ➔ Accounts
      </div>

      <p>
        The Banking module manages corporate bank accounts, petty cash registers, and electronic statement reconciliation. It ensures that internal ledger cash balances (Account Class 1010) match external bank balances reported by UAE financial institutions.
      </p>

      {wf}

      <h2>UAE Central Bank IBAN & Corporate Account Master Parameters</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Master Parameter</th>
            <th style="width: 25%;">System Specification</th>
            <th style="width: 50%;">Operational Governance & Accounting Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Bank Institution</td>
            <td>Financial Entity Name</td>
            <td>Licensed UAE commercial bank (e.g., Emirates NBD, Abu Dhabi Commercial Bank, First Abu Dhabi Bank).</td>
          </tr>
          <tr>
            <td class="col-field">IBAN Structure</td>
            <td>23-Character UAE IBAN</td>
            <td>Format: <code>AE</code> + 2 check digits + 3 bank code digits + 16 account digits. Strictly validated on save.</td>
          </tr>
          <tr>
            <td class="col-field">GL Mapping Code</td>
            <td>Class 1010 Sub-Account</td>
            <td>Links bank profile to a unique dedicated child ledger account (e.g., <code>1010-01 Operating Account AED</code>).</td>
          </tr>
          <tr>
            <td class="col-field">Operating Currency</td>
            <td>ISO Currency Code</td>
            <td>Defaults to AED. Multi-currency USD accounts apply the UAE Central Bank fixed rate (3.6725); EUR/GBP use daily spot rates.</td>
          </tr>
        </tbody>
      </table>

      <h2>Corporate Banking Mandates & Internal Fraud Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Treasury Policy</th>
            <th style="width: 35%;">System Security Enforcement</th>
            <th style="width: 40%;">Statutory Fraud Prevention Standard</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Dual Signatory Mandate</td>
            <td>Transfers &gt; AED 100,000 require two approvals</td>
            <td>Mandatory joint sign-off by Finance Director and Chief Executive Officer prior to bank file generation.</td>
          </tr>
          <tr>
            <td class="col-field">Positive Pay Verification</td>
            <td>Automated electronic check pre-clearing</td>
            <td>Uploads issued check numbers and amounts to the corporate bank portal, preventing check alteration fraud.</td>
          </tr>
          <tr>
            <td class="col-field">ISO 20022 Host-to-Host</td>
            <td>Encrypted direct bank messaging channel</td>
            <td>Secures automated salary SIF file uploads and corporate wire transmissions with end-to-end payload signing.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Operational Procedure: Registering and Mapping a Corporate Bank Account</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Banking ➔ Accounts</strong> and click <strong>+ Add Bank Account</strong> (requires Chief Accountant role).</li>
          <li>Enter the official Bank Name, branch location, currency (AED/USD), and verified 23-character UAE IBAN.</li>
          <li>Map the account to an active child code in the Chart of Accounts under Class 1010 (e.g. <code>1010-02</code>).</li>
          <li>Enter the verified opening statement balance and attach the bank confirmation letter or statement header.</li>
          <li>Click <strong>Save & Authorize</strong> to activate the account for payments, customer collections, and reconciliation.</li>
        </ol>
      </div>
    </div>
    """

def get_page_07():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Banking/03_Bank_Reconciliation.png",
        "Bank Statement Reconciliation Workspace with Matched Ledger Records",
        "/banking/reconciliation",
        [
            ("Bank Account Dropdown", "Isolate statement clearing workspace by individual registered corporate bank account."),
            ("Statement Balance Match", "Header summary comparing uploaded bank statement ending balance against current GL balance."),
            ("Matched Transaction Table", "Itemized ledger vouchers paired against electronic statement records with tick-and-tie checkboxes."),
            ("Finalize Reconciliation Trigger", "Commits reconciled statement period and locks reconciled vouchers from further edits.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 02 · MODULE 02 (PART 2)</div>
          <div class="chapter-title">Bank Statement Reconciliation & Clearing</div>
        </div>
        <div class="chapter-cat">TREASURY & AUDIT CONTROL</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Banking ➔ Reconciliation
      </div>

      <p>
        The Bank Reconciliation workspace enforces electronic statement clearing to resolve timing differences between internal accounting records and bank balance confirmations. Periodic reconciliation is mandatory prior to fiscal month-end closing.
      </p>

      {wf}

      <h2>4-Quadrant Bank Reconciliation Accounting Equation</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>1. Bank Statement Balance</h4>
          <p>Closing balance reported on the official bank statement as of the cut-off date (e.g., AED 842,100.00).</p>
        </div>
        <div class="matching-card">
          <h4>2. In-Transit Timing Items</h4>
          <p><strong>+ Deposits in Transit:</strong> customer payments received in ledger not yet credited by bank.<br><strong>− Uncleared Checks:</strong> issued checks unpresented.</p>
        </div>
        <div class="matching-card">
          <h4>3. Adjusted GL Cash Balance</h4>
          <p><strong>± Bank Adjustments:</strong> service fees, loan interest, or foreign exchange differences posted via direct adjustment vouchers.</p>
        </div>
      </div>

      <h2>Bank Statement Discrepancy Resolution & Audit Handling</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Discrepancy Condition</th>
            <th style="width: 35%;">Root Cause & Diagnostic</th>
            <th style="width: 40%;">System Remediation & Journal Adjustment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Unmatched Bank Debit</td>
            <td>Bank service fees, wire charges, interest</td>
            <td>Click <em>Post Fee</em>: Dr. 6600 Bank Charges / Cr. 1010 Corporate Bank Account.</td>
          </tr>
          <tr>
            <td class="col-field">Unidentified Credit</td>
            <td>Direct customer deposit without invoice ref</td>
            <td>Posts to Account 2190 Customer Clearing Suspense pending remittance advice verification.</td>
          </tr>
          <tr>
            <td class="col-field">Stale Outbound Check</td>
            <td>Check unpresented for &gt; 180 calendar days</td>
            <td>Void check voucher: Dr. 1010 Bank / Cr. 2100 Accounts Payable (restores liability).</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Operational Procedure: Executing Bank Statement Reconciliation</div>
        <ol class="proc-steps">
          <li>Select the corporate bank account from the dropdown selector and set the reconciliation statement cut-off date.</li>
          <li>Upload the electronic bank statement (CSV, MT940, or CAMT.053 format) or input ending statement balance.</li>
          <li>Review auto-matched entries; check unmatched transactions and post required bank fee adjustment vouchers.</li>
          <li>Verify that the <strong>Unreconciled Variance</strong> displays exactly <code>AED 0.00</code>.</li>
          <li>Click <strong>Finalize Reconciliation</strong> (Chief Accountant sign-off required) to lock reconciled records.</li>
        </ol>
      </div>

      <div class="note-card" style="margin-top: 4pt; margin-bottom: 0;">
        <div class="note-card-title">Treasury Audit Governance & Statement Lock Policy</div>
        <strong>Period Closing Prerequisite:</strong> Fiscal period closing is strictly blocked until all registered corporate bank accounts achieve certified reconciliation with <code>AED 0.00</code> unallocated variance. Finalizing reconciliation permanently seals matched vouchers; reversals require CFO dual-key authorization and generate an immutable entry in the system audit trail. Uploaded statement files (MT940/CAMT.053) are archived with SHA-256 checksums in the Document Vault.
      </div>
    </div>
    """

def get_page_08():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Customer_Activity/05_Sales_Invoice.png",
        "Commercial Tax Invoicing Directory with VAT Breakdown and Settlement Status",
        "/customers/invoices",
        [
            ("Customer Invoice Table", "Lists invoice numbers, customer names, issue dates, taxable totals, 5% VAT amounts, and payment statuses."),
            ("New Invoice Action", "Opens the full-screen invoice creation workflow with customer TRN auto-population."),
            ("Status Filter Pipeline", "Filter invoices by Draft, Approved, Issued, Overdue, and Paid."),
            ("Export & FTA Transmission", "Generate official bilingual Arabic/English PDF tax invoices and export statutory XML.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 03 · MODULE 03 (PART 1)</div>
          <div class="chapter-title">Customer Activity: Commercial Invoicing</div>
        </div>
        <div class="chapter-cat">ORDER-TO-CASH & E-INVOICING</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Customer Activity ➔ Sales Invoice
      </div>

      <p>
        The Commercial Invoicing engine generates fully compliant electronic tax invoices in accordance with UAE Federal Tax Authority (FTA) regulations. It manages customer billing terms, line-item VAT calculations, and automatic general ledger postings.
      </p>

      {wf}

      <div class="sop-meta-grid">
        <div class="sop-meta-item">
          <span class="sop-meta-title">Prerequisites & Master Data</span>
          <span class="sop-meta-desc">Active Customer Record • Validated 15-Digit TRN (if UAE entity) • Open AR Accounting Period • Active SKU with Tax Code</span>
        </div>
        <div class="sop-meta-item">
          <span class="sop-meta-title">Authorized Roles & SoD Policy</span>
          <span class="sop-meta-desc">Creation: AR Clerk • Approval (> AED 50,000): Chief Accountant • Creator cannot authorize credit notes or write-offs</span>
        </div>
      </div>

      <h2>Automated Double-Entry Accounting Posting Impact</h2>
      <div class="journal-demo-card">
        <div class="journal-demo-header">
          <span>TRANSACTION POSTING: Commercial Tax Invoice #INV-2026-0188</span>
          <span class="badge-mono badge-blue">POSTED TO GL</span>
        </div>
        <div class="journal-demo-row">
          <span>Dr. 1200-01 Accounts Receivable Control (Reference Customer LLC)</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 10,500.00</span>
          <span>AED 0.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Cr. 4000-01 Commercial Sales Revenue (Dubai Branch)</span>
          <span>AED 0.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 10,000.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Cr. 2210-01 Output VAT Payable (UAE Standard 5% Rate — Form 201 Box 1)</span>
          <span>AED 0.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 500.00</span>
        </div>
        <div class="journal-demo-total">
          <span>Balanced Journal Total</span>
          <span>Debit: AED 10,500.00</span>
          <span>Credit: AED 10,500.00 (Variance: AED 0.00)</span>
        </div>
      </div>

      <h2>Field Data Dictionary & Statutory Validations</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Name</th>
            <th style="width: 18%;">Constraint</th>
            <th style="width: 32%;">System Validation Rule</th>
            <th style="width: 28%;">Statutory / Accounting Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Customer Name</td>
            <td>Mandatory</td>
            <td>Must select from active customer directory</td>
            <td>Assigns receivable to customer sub-ledger.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Treatment / TRN</td>
            <td>Conditional</td>
            <td>Must be 15 numeric digits starting with <code>100</code></td>
            <td>Mandatory on tax invoices exceeding AED 10,000.</td>
          </tr>
          <tr>
            <td class="col-field">Invoice Date</td>
            <td>Mandatory</td>
            <td>Cannot fall in a locked fiscal period</td>
            <td>Establishes the quarterly VAT return tax period.</td>
          </tr>
          <tr>
            <td class="col-field">Line Item Tax Code</td>
            <td>Mandatory</td>
            <td>Standard 5%, Zero Rated 0%, or Exempt</td>
            <td>Determines Form 201 box allocation (Box 1 or 4).</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Issuing an Official UAE Tax Invoice</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Customer Activity ➔ Sales Invoice</strong> and click <strong>+ New Invoice</strong>.</li>
          <li>Select Customer; confirm customer TRN and billing address populate. Verify payment terms (e.g. Net 30).</li>
          <li>Add line items, entering SKU, quantity, and unit price (exclusive of VAT). The system automatically computes 5% VAT.</li>
          <li>Confirm Branch allocation (e.g. <em>Main Operations Branch (Dubai)</em>) for cost center attribution.</li>
          <li>Click <strong>Issue Invoice</strong>. System assigns sequential number <code>INV-YYYY-XXXXX</code>, generates PDF, and posts double-entry GL journal.</li>
        </ol>
      </div>

      <div class="reversal-card">
        <div class="reversal-card-title">Correction & Reversal Protocol: Issued Invoices</div>
        Posted invoices cannot be modified or deleted under UAE statutory recordkeeping rules. If an error occurs, click <strong>Actions ➔ Create Credit Note</strong> to issue a linked Credit Note (referencing the original invoice number), which reverses GL postings: <em>Dr. 4000 Sales Revenue / Dr. 2210 Output VAT / Cr. 1200 AR Control</em>.
      </div>
    </div>
    """

print("Pages 01-08 module finalized.")

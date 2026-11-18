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
          Enterprise User Guide • Rev 3.0
        </div>
      </div>

      <div class="cover-body">
        <div class="cover-eyebrow">Enterprise Operations Standard • Volume I</div>
        <h1 class="cover-title">ACCONEER ERP</h1>
        <div class="cover-subtitle">Universal User Operations Manual: Screen Navigation, Transaction Workflows & Operational Controls</div>
        <div class="cover-rule">
          <div class="cover-rule-red"></div>
          <div class="cover-rule-blue"></div>
        </div>
        <p class="cover-desc">
          The definitive operational user guide for Acconeer ERP. Provides comprehensive step-by-step procedures for daily enterprise workflows, screen navigation, data entry validation, automated double-entry postings, bank clearing, order-to-cash, procure-to-pay, inventory management, payroll processing, and statutory tax reporting across UAE and GCC commercial environments.
        </p>

        <div class="cover-meta-grid">
          <div class="cover-meta-card">
            <div class="cover-meta-label">Cloud ERP Application Portal</div>
            <div class="cover-meta-val">acconeer.zestwings.com</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">System Developer & Vendor</div>
            <div class="cover-meta-val">Spectrum Zestwings Technologies LLC</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Operating Currency & Region</div>
            <div class="cover-meta-val">UAE / GCC Market • Functional Currency: AED</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Target Audience & User Scope</div>
            <div class="cover-meta-val">Finance Directors, Accountants, AR/AP Clerks & Operations Staff</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Standard Document ID</div>
            <div class="cover-meta-val">DOC-ACC-OPS-V3.0 (Universal Edition)</div>
          </div>
          <div class="cover-meta-card">
            <div class="cover-meta-label">Reference Implementation Tenant</div>
            <div class="cover-meta-val">Gulf Horizon General Trading LLC (AED)</div>
          </div>
        </div>
      </div>

      <div class="cover-footer">
        <div>
          <strong>Spectrum Zestwings Technologies LLC</strong> • Dubai Silicon Oasis, Dubai, UAE<br>
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
        <strong>NAVIGATION:</strong> Universal Header ➔ Global 4-Tier Scope Selector
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
            <td><code>Gulf Horizon Group Holding Ltd</code></td>
            <td>Global parent holding; defines shared COA templates, base currency, and security governance.</td>
          </tr>
          <tr>
            <td><code>Tier 2</code></td>
            <td><strong>Legal Entity</strong></td>
            <td><code>Gulf Horizon General Trading LLC (AED)</code></td>
            <td>Tax-registered operating corporate entity; holds legal TRN and dedicated general ledger accounts.</td>
          </tr>
          <tr>
            <td><code>Tier 3</code></td>
            <td><strong>Branch Scope</strong></td>
            <td><code>Main Branch (Dubai)</code> • <code>Abu Dhabi Depot</code></td>
            <td>Physical warehouse location, branch retail office, or cost-center for segmental profitability.</td>
          </tr>
          <tr>
            <td><code>Tier 4</code></td>
            <td><strong>Fiscal Period</strong></td>
            <td><code>FY 2026</code> • <code>Q3 2026</code> • <code>September 2026</code></td>
            <td>Active operational date filter governing transaction queries, dashboards, and report generation.</td>
          </tr>
        </tbody>
      </table>

      <h2>Operational Scoping Rules & Data Boundaries</h2>
      <div class="grid-2col">
        <div>
          <h3>Session Filtering vs Period Locking</h3>
          <p>
            The top-bar period selector is an active view filter for your current session. Selecting <em>Q3 2026</em> displays transactions posted within that date window. Period locking is an administrative control executed in General Ledger settings to prevent postings to closed months.
          </p>
        </div>
        <div>
          <h3>Branch Cost-Center Tagging</h3>
          <p>
            Every sales invoice, purchase bill, and inventory intake document captures the active Branch ID. This enables granular branch-level trial balances and warehouse inventory segregation without requiring separate legal entities.
          </p>
        </div>
      </div>

      <h2>Standard Operating Procedure: Setting Your Active Work Scope</h2>
      <ol class="step-list">
        <li>Sign in to the Acconeer ERP portal (<code>acconeer.zestwings.com</code>) using your corporate credentials.</li>
        <li>Inspect the top-left navigation bar to verify your assigned <strong>Organization</strong> name.</li>
        <li>Click the <strong>Legal Entity</strong> dropdown and select the operating company you are transacting for (e.g. <em>Gulf Horizon General Trading LLC</em>). For consolidated group reports, select <em>All Entities</em>.</li>
        <li>Select the target <strong>Branch Scope</strong> (e.g. <em>Dubai Head Office</em> or <em>Warehouse 01</em>).</li>
        <li>Choose the active <strong>Fiscal Reporting Period</strong> (e.g. <em>Q3 2026</em>) to ensure your workspace aligns with the current transaction cycle.</li>
        <li>Verify that the status pill displays <code>OPEN</code>. If the period displays <code>CLOSED</code>, new transaction postings are disabled.</li>
      </ol>

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
            <td class="col-field">Functional Base Currency</td>
            <td>Fixed to <code>AED</code> for UAE statutory compliance.</td>
            <td>All financial statements and VAT declarations calculate in Dirhams.</td>
          </tr>
          <tr>
            <td class="col-field">Multi-Currency Invoicing</td>
            <td>Supports USD, EUR, GBP, SAR line item pricing.</td>
            <td>Converts to AED via daily spot rates; tracks realized FX gain/loss.</td>
          </tr>
          <tr>
            <td class="col-field">Inter-Company Due To/From</td>
            <td>Automated reciprocal entries between affiliate entities.</td>
            <td>Posts to Account 1950 (Due from Affiliates) and 2950 (Due to Affiliates).</td>
          </tr>
          <tr>
            <td class="col-field">Consolidation Elimination</td>
            <td>Dynamic netting when selecting <em>All Entities</em>.</td>
            <td>Eliminates inter-company balances to present true external group profit.</td>
          </tr>
        </tbody>
      </table>

      <h2>Fiscal Year-End Closing & Period Lock Hierarchy</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Closing Level</th>
            <th style="width: 35%;">System Operational Trigger</th>
            <th style="width: 40%;">Accounting Immutability Standard</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Soft Monthly Close</td>
            <td>Sub-ledger lock preventing operational billing edits.</td>
            <td>General Ledger adjusting journals remain permitted for accountants.</td>
          </tr>
          <tr>
            <td class="col-field">Hard Period Lock</td>
            <td>Period status switched to <code>LOCKED</code> in GL settings.</td>
            <td>Rejects all transaction postings; requires CFO override to reopen.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">OPERATIONAL TIP: CROSS-ENTITY POSTING PROTECTION</div>
        Each legal entity operates with an isolated sub-ledger. Invoices and bills created under <em>Gulf Horizon General Trading LLC</em> will not alter receivables or payables of sibling entities. Cross-entity trading automatically generates balancing inter-company vouchers (Accounts 1950/2950).
      </div>
    </div>
    """

def get_page_03():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">SYSTEM NAVIGATION · USER INTERFACE</div>
          <div class="chapter-title">Universal Toolbar, Search & Keyboard Shortcuts</div>
        </div>
        <div class="chapter-right-meta">SECTION 02<br>USER INTERFACE</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Universal Header Bar ➔ Quick Actions, Search & User Menu
      </div>

      <p>
        Acconeer ERP features a persistent top header bar accessible across every screen. The header provides rapid access to global search, instant transaction dispatchers, ledger synchronization, and user session management.
      </p>

      <h2>Universal Header Action Triggers</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Header Element</th>
            <th style="width: 16%;">Trigger Method</th>
            <th style="width: 42%;">Operational Functionality</th>
            <th style="width: 20%;">Authorized Roles</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Global Search</strong></td>
            <td><kbd>Alt + K</kbd> or Click</td>
            <td>Instant modal search across customers, vendors, invoices, voucher numbers, and SKUs.</td>
            <td>All Authenticated Users</td>
          </tr>
          <tr>
            <td><strong>+ New Journal</strong></td>
            <td><kbd>Alt + J</kbd> or Button</td>
            <td>Direct shortcut opening the manual General Ledger journal entry modal with auto-balancing.</td>
            <td>General Ledger Accountants</td>
          </tr>
          <tr>
            <td><strong>Invoices</strong></td>
            <td><kbd>Alt + I</kbd> or Button</td>
            <td>Quick jump to the sales invoicing ledger and customer accounts receivable directory.</td>
            <td>Billing Clerks, AR Staff</td>
          </tr>
          <tr>
            <td><strong>Refresh Ledger State</strong></td>
            <td>Header Button</td>
            <td>Forces immediate cache invalidation and re-computes real-time GL balance aggregates.</td>
            <td>Chief Accountant, CFO</td>
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

      <h2>Standard Operating Procedure: Universal Fast Search</h2>
      <ol class="step-list">
        <li>From any workspace in Acconeer ERP, press <kbd>Alt + K</kbd> on your keyboard (or click the search input bar in the header).</li>
        <li>Type any search query: an invoice number (e.g. <code>INV-2026-0042</code>), customer name (e.g. <code>Al-Futtaim</code>), vendor name, or SKU code.</li>
        <li>The system dynamically displays categorized search results grouped by Invoices, Customers, Vendors, and Journal Vouchers.</li>
        <li>Use the arrow keys to highlight the desired record and press <kbd>Enter</kbd> to open the document directly.</li>
      </ol>

      <h2>Left Sidebar Navigation Module Taxonomy</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Navigation Pillar</th>
            <th style="width: 35%;">Direct Child Sub-Menus</th>
            <th style="width: 40%;">Core Operational Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Commercial Operations</td>
            <td>Invoices, Sales Orders, Customer Directory, Receipts.</td>
            <td>Manages full client billing, order fulfillment, and cash collection.</td>
          </tr>
          <tr>
            <td class="col-field">Procure-to-Pay (AP)</td>
            <td>Bills, Purchase Orders, Vendor Directory, Payments.</td>
            <td>Controls supplier intake, 3-way matching, and disbursements.</td>
          </tr>
          <tr>
            <td class="col-field">General Ledger & Assets</td>
            <td>Journals, Chart of Accounts, Product Master, GRN, Assets.</td>
            <td>Core double-entry accounting, physical stock, and capitalization.</td>
          </tr>
          <tr>
            <td class="col-field">Workforce & Compliance</td>
            <td>HR Master, Payroll & WPS, Financials, VAT Return, Audit.</td>
            <td>Labour compliance, statutory tax filing, and security audit logs.</td>
          </tr>
        </tbody>
      </table>

      <h2>Role-Based Navigation Permissions & Access Boundaries</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Enterprise User Role</th>
            <th style="width: 35%;">Visible Workspaces & Menus</th>
            <th style="width: 40%;">Restricted Actions & Governance Safeguards</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Finance Director / CFO</td>
            <td>Full system visibility; financial statements, approvals, period locking.</td>
            <td>Restricted from operational invoice/bill data entry to preserve segregation of duties.</td>
          </tr>
          <tr>
            <td class="col-field">Chief Accountant</td>
            <td>General Ledger, Banking, Bank Reconciliation, Asset Depreciation.</td>
            <td>Restricted from outbound bank transfer file release without CFO dual-authorization.</td>
          </tr>
          <tr>
            <td class="col-field">Billing & AR Specialist</td>
            <td>Customer Invoices, Sales Orders, Customer Directory, Payment Receipts.</td>
            <td>Zero access to manual GL journal entry, payroll calculations, or system audit logs.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">SEGREGATION OF DUTIES (SOD) ENFORCEMENT</div>
        Button visibility in the universal toolbar automatically reflects your user role permissions. Users assigned operational billing roles will not see the <strong>Refresh Ledger State</strong> or manual GL posting buttons.
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
            <td>Field label with asterisk (e.g. <code>IBAN *</code>)</td>
            <td>Data entry is strictly required; forms cannot be saved or submitted without input.</td>
          </tr>
          <tr>
            <td><strong>Keyboard Shortcut</strong></td>
            <td><kbd>Alt + Key</kbd></td>
            <td>Global hotkey sequence for rapid power-user keyboard navigation.</td>
          </tr>
          <tr>
            <td><strong>Validation Alert</strong></td>
            <td>Left-accent callout line</td>
            <td>Critical operational guidance, security warnings, or automated reversal requirements.</td>
          </tr>
        </tbody>
      </table>

      <h2>Quick-Start User Onboarding Checklist</h2>
      <ol class="step-list">
        <li>Sign in at <code>acconeer.zestwings.com</code> using your corporate email and temporary credentials.</li>
        <li>Navigate to <strong>User Profile</strong> (<kbd>Alt + P</kbd>) and immediately establish your personal secure password and 2FA.</li>
        <li>Inspect the 4-Tier Scope Selector in the top bar to verify that your active <strong>Legal Entity</strong> and <strong>Branch</strong> are correct.</li>
        <li>Review your module permissions: confirm that relevant sidebars (e.g. Invoices, Banking, Inventory) appear in your workspace.</li>
        <li>Refer to the respective chapters in this manual for detailed step-by-step transaction instructions.</li>
      </ol>

      <h2>System Security & Compliance Governance Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Security Dimension</th>
            <th style="width: 35%;">System Policy Parameter</th>
            <th style="width: 40%;">Operational Implementation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Inactivity Timeout</td>
            <td>Automatic session termination after 15 minutes of idle time.</td>
            <td>Prevents unauthorized access on open workstations.</td>
          </tr>
          <tr>
            <td class="col-field">Password Complexity</td>
            <td>Minimum 12 characters, uppercase, numbers, and symbols.</td>
            <td>Mandatory 90-day password rotation enforced system-wide.</td>
          </tr>
          <tr>
            <td class="col-field">Concurrent Sessions</td>
            <td>Restricted to single active browser session per user license.</td>
            <td>New logins automatically invalidate previous browser sessions.</td>
          </tr>
          <tr>
            <td class="col-field">Audit Trail Retention</td>
            <td>Immutable write-only database event log; 5-year retention.</td>
            <td>Satisfies UAE statutory compliance and independent auditor reviews.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_05():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Dashboard/01_Executive_Dashboard.png",
        "Executive Dashboard with Multi-Entity Scoping and Financial Telemetry",
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
          <div class="chapter-category">COMMERCIAL & CASH · EXECUTIVE COCKPIT</div>
          <div class="chapter-title">Executive Financial Dashboard & KPI Telemetry</div>
        </div>
        <div class="chapter-right-meta">MODULE 01<br>/dashboard</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Dashboard (or press <kbd>Alt + D</kbd>)
      </div>

      <p>
        The Executive Financial Dashboard is the primary operational landing cockpit in Acconeer ERP. It delivers consolidated, real-time visibility into revenue generation, gross margin, cash balances, accounts receivable (AR), and supplier payables (AP) across selected entities.
      </p>

      {wf}

      <h2>Executive KPI Telemetry Master Dictionary</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Metric Card</th>
            <th style="width: 32%;">General Ledger Balance Source</th>
            <th style="width: 26%;">Sub-Ledger Input Origin</th>
            <th style="width: 20%;">Refresh Cadence</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Total Revenue</td>
            <td><code>Class 4000 (Operating Revenue)</code></td>
            <td>Posted Sales Invoices less Credit Notes</td>
            <td>Real-Time Synchronous</td>
          </tr>
          <tr>
            <td class="col-field">Net Profit Margin</td>
            <td><code>(Revenue - COGS - OpEx) / Revenue</code></td>
            <td>Comprehensive P&L Statement aggregate</td>
            <td>Dynamic on query</td>
          </tr>
          <tr>
            <td class="col-field">Cash & Bank Liquidity</td>
            <td><code>Class 1010 (Bank Current Accounts)</code></td>
            <td>Reconciled bank ledger balances (AED)</td>
            <td>Real-Time Synchronous</td>
          </tr>
          <tr>
            <td class="col-field">Receivables (AR)</td>
            <td><code>Account 1200 (Accounts Receivable)</code></td>
            <td>Open, unpaid customer sales invoices</td>
            <td>Real-Time Synchronous</td>
          </tr>
          <tr>
            <td class="col-field">Payables (AP)</td>
            <td><code>Account 2100 (Accounts Payable)</code></td>
            <td>Pending, approved supplier bills</td>
            <td>Real-Time Synchronous</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Navigating the Executive Dashboard</h2>
      <ol class="step-list">
        <li>Log into Acconeer ERP and confirm your target Legal Entity and Period in the top-bar scope selector.</li>
        <li>Review the top row of KPI cards for immediate liquidity and outstanding receivables/payables balances.</li>
        <li>Click directly on any metric card (e.g. <strong>Receivables</strong>) to instantly navigate to the filtered sub-ledger listing.</li>
        <li>Inspect the <strong>Cash Flow Trend</strong> chart to review rolling 30-day inflows versus outflows.</li>
        <li>If bulk transactions or payroll vouchers were posted during the session, click <strong>Refresh Ledger State</strong> in the action bar to refresh dashboard aggregate caches.</li>
      </ol>

      <h2>Executive Telemetry Filters & Analytical Insights</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Dashboard View Mode</th>
            <th style="width: 35%;">Filter Parameter & Selector</th>
            <th style="width: 40%;">Executive Analytical Insight</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Consolidated Group View</td>
            <td>Legal Entity: <em>All Entities</em></td>
            <td>Group-wide liquidity, total turnover, and aggregated profitability with inter-company eliminations.</td>
          </tr>
          <tr>
            <td class="col-field">Branch Segmental View</td>
            <td>Branch Scope: <em>Dubai</em> vs <em>Abu Dhabi</em></td>
            <td>Regional revenue performance and operating margin comparison across commercial branch depots.</td>
          </tr>
          <tr>
            <td class="col-field">Quarterly Comparative</td>
            <td>Fiscal Period: <em>Q3 2026 vs Q2 2026</em></td>
            <td>Quarter-over-quarter percentage variance on gross margin and operating overhead expenses.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">OPERATIONAL TIP: DRILL-DOWN CAPABILITY</div>
        Every chart bar and metric widget in the dashboard is an active interactive link. Clicking a monthly revenue bar opens the underlying Sales Register pre-filtered for that specific calendar month.
      </div>
    </div>
    """

def get_page_06():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Banking/02_Bank_Accounts.png",
        "Corporate Banking Master Registry with Account Setup and Ledger Balances",
        "/banking",
        [
            ("Bank Account Directory", "Comprehensive listing of all active corporate bank accounts, IBANs, and currencies."),
            ("+ Add Account Button", "Primary trigger modal to register and configure a new commercial bank account."),
            ("Real-Time Ledger Balances", "Book Balance versus Statement Balance with reconciliation status indicators."),
            ("Action Dropdown Menu", "Direct access to View Ledger, Import Statement, and Initiate Transfer.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · TREASURY</div>
          <div class="chapter-title">Banking Master & Corporate Account Setup</div>
        </div>
        <div class="chapter-right-meta">MODULE 02<br>/banking</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Banking (or press <kbd>Alt + B</kbd>)
      </div>

      <p>
        The Banking Master module serves as the central treasury directory in Acconeer ERP. It maintains corporate bank accounts, manages multi-currency holdings, tracks book balances against reconciled statements, and controls disbursement authorizations.
      </p>

      {wf}

      <h2>Bank Account Data Dictionary & Validation Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Name</th>
            <th style="width: 14%;">Field Type</th>
            <th style="width: 38%;">Description & Required Format</th>
            <th style="width: 26%;">Validation Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Account Name *</td>
            <td>Text</td>
            <td>Friendly descriptive title (e.g. <code>Emirates NBD - AED Operating</code>).</td>
            <td>Mandatory; minimum 3 characters.</td>
          </tr>
          <tr>
            <td class="col-field">Bank Name *</td>
            <td>Dropdown</td>
            <td>Commercial bank institution (e.g. <em>Emirates NBD</em>, <em>ADCB</em>, <em>FAB</em>, <em>Mashreq</em>).</td>
            <td>Mandatory; selected from master list.</td>
          </tr>
          <tr>
            <td class="col-field">IBAN Number *</td>
            <td>Text</td>
            <td>International Bank Account Number (e.g. <code>AE250260001012345678901</code>).</td>
            <td>UAE standard: 23 characters; begins with AE.</td>
          </tr>
          <tr>
            <td class="col-field">Currency *</td>
            <td>Dropdown</td>
            <td>Operating currency (defaults to <code>AED</code>; supports USD, EUR, GBP).</td>
            <td>Mandatory; fixed once transactions exist.</td>
          </tr>
          <tr>
            <td class="col-field">GL Account Link *</td>
            <td>Lookup</td>
            <td>General Ledger asset account (e.g. <code>1010 - Cash at Bank ENBD</code>).</td>
            <td>Mandatory; must be an active Asset account.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Adding a New Corporate Bank Account</h2>
      <ol class="step-list">
        <li>Navigate to the Banking workspace by clicking <strong>Banking</strong> in the sidebar or pressing <kbd>Alt + B</kbd>.</li>
        <li>Click the blue <strong>+ Add Account</strong> button located in the top-right corner of the screen.</li>
        <li>In the modal window, enter the <strong>Account Name</strong> and select the <strong>Bank Name</strong> from the master list.</li>
        <li>Type the official 23-character UAE <strong>IBAN Number</strong>. The system will perform an automated checksum validation.</li>
        <li>Select the dedicated <strong>GL Account Link</strong> from the Chart of Accounts (Account Class 1010).</li>
        <li>Enter the verified <strong>Opening Balance</strong> and effective opening balance date from your bank statement.</li>
        <li>Click <strong>Save & Activate</strong> to register the account in the corporate treasury directory.</li>
      </ol>

      <h2>Treasury Fund Transfers & Currency Handling</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Treasury Operation</th>
            <th style="width: 35%;">Action Trigger & Inputs</th>
            <th style="width: 40%;">System General Ledger Posting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Inter-Bank Transfer</td>
            <td>Click <em>Initiate Transfer</em>; select Source Account, Destination Account, and Amount.</td>
            <td>Dr. Receiving Bank (1010-02) / Cr. Disbursing Bank (1010-01).</td>
          </tr>
          <tr>
            <td class="col-field">Foreign Currency Exchange</td>
            <td>Transfer between AED and USD account; input realized spot exchange rate.</td>
            <td>Dr. Foreign Bank / Cr. Local Bank / Dr./Cr. FX Realized Gain/Loss (6350/4350).</td>
          </tr>
          <tr>
            <td class="col-field">Petty Cash Replenishment</td>
            <td>Record cash withdrawal check disbursed to custodian.</td>
            <td>Dr. Petty Cash Imprest (1020) / Cr. Bank Current Account (1010).</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">VALIDATION WARNING: IBAN INTEGRITY ENFORCEMENT</div>
        Acconeer ERP strictly blocks duplicate IBAN registrations within the same organization. Ensure the IBAN matches your official bank confirmation letter before saving to avoid WPS disbursement rejections.
      </div>
    </div>
    """

def get_page_07():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Banking/03_Bank_Reconciliation.png",
        "Bank Reconciliation Workspace with Automated Matching and Discrepancy Clearance",
        "/reconciliation",
        [
            ("Bank Account & Period Selector", "Select target bank account, statement closing date, and statement ending balance."),
            ("Unmatched Statement Items", "Imported bank statement feed awaiting matching against general ledger entries."),
            ("General Ledger Transactions", "Internal book transactions awaiting clearing against verified bank statement lines."),
            ("Auto-Match & Reconcile Bar", "One-click rule engine execution, statement difference counter, and Final Reconcile button.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · TREASURY</div>
          <div class="chapter-title">Bank Statement Reconciliation & Ledger Matching</div>
        </div>
        <div class="chapter-right-meta">MODULE 03<br>/reconciliation</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Reconciliation (or press <kbd>Alt + R</kbd>)
      </div>

      <p>
        The Bank Reconciliation module ensures complete alignment between company general ledger records and official external bank statements. The built-in rule engine matches transactions by date, reference, and amount to resolve outstanding timing differences.
      </p>

      {wf}

      <h2>Reconciliation Interface Fields & Balancing Calculations</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Interface Field</th>
            <th style="width: 38%;">Description & Operating Rule</th>
            <th style="width: 38%;">System Validation & Balancing Formula</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Statement Ending Balance</td>
            <td>The exact closing balance displayed on the official bank statement.</td>
            <td>Manually entered by user; must match statement PDF/feed.</td>
          </tr>
          <tr>
            <td class="col-field">Book Balance</td>
            <td>The current closing balance of the linked GL bank account.</td>
            <td>Calculated dynamically: <code>Class 1010 Account Net Balance</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Cleared Balance</td>
            <td>Sum of all checked and matched debits less credits.</td>
            <td>Calculated: <code>Opening Cleared + Matched Receipts - Matched Payments</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Unreconciled Difference</td>
            <td>Variance between Statement Ending Balance and Cleared Balance.</td>
            <td>Formula: <code>Statement Ending Balance - Cleared Balance = 0.00 AED</code>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Executing Bank Reconciliation</h2>
      <ol class="step-list">
        <li>Select the corporate <strong>Bank Account</strong> from the top dropdown (e.g. <em>Emirates NBD - AED Operating</em>).</li>
        <li>Enter the official <strong>Statement Ending Date</strong> and <strong>Statement Ending Balance</strong> from your bank statement.</li>
        <li>Click <strong>Import Statement</strong> to upload an electronic bank statement file (OFX, QIF, or standardized CSV).</li>
        <li>Click the green <strong>Auto-Match</strong> button. The system scans entries and automatically pairs identical amounts and reference dates.</li>
        <li>For remaining unmatched items, manually check the corresponding checkboxes in the Statement and Ledger panels.</li>
        <li>Verify that the <strong>Unreconciled Difference</strong> displays exactly <code>0.00 AED</code>.</li>
        <li>Click <strong>Finalize Reconciliation</strong> to lock the statement period and mark entries as permanently cleared.</li>
      </ol>

      <h2>Common Reconciliation Discrepancies & Resolution Protocols</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Discrepancy Category</th>
            <th style="width: 35%;">Root Operational Cause</th>
            <th style="width: 40%;">System Resolution Action in Acconeer ERP</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Unrecorded Bank Charges</td>
            <td>Monthly maintenance fee or transfer charges debited by bank.</td>
            <td>Click <em>+ Adjusting Journal</em>: Dr. Bank Fees (6400) / Cr. Bank (1010).</td>
          </tr>
          <tr>
            <td class="col-field">Unpresented Supplier Checks</td>
            <td>Check issued by company but not yet deposited by vendor.</td>
            <td>Leave item unchecked in Ledger panel; clears automatically next cycle.</td>
          </tr>
          <tr>
            <td class="col-field">Direct Customer Inward Remittance</td>
            <td>Customer paid directly via wire without submitting remittance advice.</td>
            <td>Click <em>+ Create Customer Receipt</em> directly from unmatched statement row.</td>
          </tr>
          <tr>
            <td class="col-field">Foreign Exchange Rounding</td>
            <td>Fractional cent rounding discrepancy on international transfers.</td>
            <td>Post minor rounding difference voucher to FX Rounding Variance (6360).</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">DISCREPANCY HANDLING: UNRECONCILED VARIANCES</div>
        If a difference persists, inspect for unrecorded bank charges, interest credits, or timing delays on outbound supplier checks. Click <strong>+ Create Adjusting Journal</strong> to post bank fee vouchers directly from the reconciliation screen.
      </div>
    </div>
    """

def get_page_08():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Customer_Activity/05_Sales_Invoice.png",
        "Commercial Sales Invoicing Register with Tax Invoice Creation and AR Status",
        "/invoices",
        [
            ("Invoice Status Filters", "Filter customer billing records by All, Draft, Posted, Paid, and Overdue."),
            ("+ New Invoice Button", "Primary action trigger to generate a new commercial tax invoice."),
            ("Invoice Register Table", "Detailed columns for Invoice #, Customer, Date, Due Date, Tax Amount, and Total (AED)."),
            ("Document Action Menu", "One-click options to View PDF, Send Email, Record Payment, and Issue Credit Note.")
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
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Invoices (or press <kbd>Alt + I</kbd>)
      </div>

      <p>
        The Customer Invoicing module manages commercial billing, electronic tax invoice generation, accounts receivable aging, and customer payment tracking. Posting an invoice synchronously records double-entry ledger vouchers and updates VAT liability.
      </p>

      {wf}

      <h2>Invoice Creation Field Dictionary & Validation Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Name</th>
            <th style="width: 14%;">Field Type</th>
            <th style="width: 38%;">Description & Required Format</th>
            <th style="width: 26%;">Validation & Accounting Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Customer *</td>
            <td>Lookup</td>
            <td>Select registered client from Customer Master (e.g. <code>Al-Futtaim Trading LLC</code>).</td>
            <td>Mandatory; auto-populates TRN and payment terms.</td>
          </tr>
          <tr>
            <td class="col-field">Invoice Date *</td>
            <td>Date Picker</td>
            <td>Official commercial supply date (tax point).</td>
            <td>Mandatory; must fall within an open fiscal period.</td>
          </tr>
          <tr>
            <td class="col-field">Payment Terms *</td>
            <td>Dropdown</td>
            <td>Credit period (e.g. <em>Net 30 Days</em>, <em>Due on Receipt</em>).</td>
            <td>Calculates statutory <strong>Due Date</strong> automatically.</td>
          </tr>
          <tr>
            <td class="col-field">Line Items *</td>
            <td>Item Grid</td>
            <td>Select Item/Service SKU, Quantity, Unit Price (AED), and Discount %.</td>
            <td>Requires at least one line item with valid GL revenue link.</td>
          </tr>
          <tr>
            <td class="col-field">VAT Treatment *</td>
            <td>Dropdown</td>
            <td>Tax classification: <code>Standard Rated (5%)</code>, <code>Zero Rated (0%)</code>, or <code>Exempt</code>.</td>
            <td>Computes 5% VAT and maps to Output VAT Account 2200.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Generating and Posting a Sales Invoice</h2>
      <ol class="step-list">
        <li>Navigate to the Invoices workspace (<kbd>Alt + I</kbd>) and click the blue <strong>+ New Invoice</strong> button.</li>
        <li>Select the <strong>Customer Name</strong>. Verify that the client's TRN and billing address populate correctly.</li>
        <li>Confirm the <strong>Invoice Date</strong> and verify the assigned credit <strong>Payment Terms</strong>.</li>
        <li>In the Line Items table, click <strong>+ Add Item</strong>, choose the catalog SKU, enter the <strong>Quantity</strong> and <strong>Unit Price</strong>.</li>
        <li>Ensure the tax column indicates <strong>5% Standard Rate</strong> (or applicable exemption code).</li>
        <li>Review the subtotal, calculated 5% VAT, and final invoice total at the bottom right.</li>
        <li>Click <strong>Save & Post</strong>. The system generates an immutable sequential invoice number and writes the GL voucher.</li>
      </ol>

      <h2>Post-Billing Actions & Accounts Receivable Management</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Action Trigger</th>
            <th style="width: 36%;">Operational Procedure</th>
            <th style="width: 40%;">System Accounting & Document Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Download / Print PDF</td>
            <td>Click <em>View PDF</em> from the invoice action menu.</td>
            <td>Generates official tax invoice compliant with FTA bilingual rules.</td>
          </tr>
          <tr>
            <td class="col-field">Email Invoice to Client</td>
            <td>Click <em>Send Email</em>; select contact and verify PDF attachment.</td>
            <td>Dispatches invoice directly; logs sent timestamp in audit history.</td>
          </tr>
          <tr>
            <td class="col-field">Issue Credit Note</td>
            <td>Click <em>Issue Credit Note</em> on posted invoice for returns or price fixes.</td>
            <td>Generates linked credit note: Dr. Sales 4000 / Dr. VAT 2200 / Cr. AR 1200.</td>
          </tr>
          <tr>
            <td class="col-field">Customer Statement</td>
            <td>Navigate to Customer profile and click <em>Generate Statement</em>.</td>
            <td>Produces running aging statement (Current, 30, 60, 90+ days overdue).</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">ACCOUNTING IMPACT: POSTING AN INVOICE</div>
        Posting immediately creates a balanced general ledger entry: <strong>Debit Account 1200 (Accounts Receivable)</strong> for the gross total, <strong>Credit Account 4000 (Sales Revenue)</strong> for the net subtotal, and <strong>Credit Account 2200 (Output VAT Payable)</strong> for the 5% tax amount.
      </div>
    </div>
    """

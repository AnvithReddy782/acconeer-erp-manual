# scripts/pages_p17_p26.py
from generate_complete_manual import window_frame

def get_page_17():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Human_Resources/01_Employees.png",
        "Employee Master Directory with UAE Labour Card and Contract Details",
        "/hr/employees",
        [
            ("Employee Directory Table", "Employee IDs, legal names, job titles, departments, visa statuses, and monthly basic pay in AED."),
            ("New Employee Onboarding", "Multi-tab registration capturing personal info, emergency contacts, and MOHRE contract details."),
            ("Department Filter", "Filter by Executive, Finance, Sales, Logistics, and Field Operations."),
            ("Document Expiry Alerts", "Monitors expiration dates for Emirates IDs, passports, and UAE residency visas.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 09 · MODULE 09 (PART 1)</div>
          <div class="chapter-title">HR & Workforce Management</div>
        </div>
        <div class="chapter-cat">HUMAN CAPITAL & COMPLIANCE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ HR & Workforce ➔ Employees
      </div>

      <p>
        The Human Resources module manages the complete workforce lifecycle, employee master data, statutory MOHRE employment contract details, biometric attendance, and leave entitlements in compliance with UAE Labour Law.
      </p>

      {wf}

      <h2>UAE Statutory Employee Master Data Parameters</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Master Parameter</th>
            <th style="width: 35%;">Statutory System Requirement</th>
            <th style="width: 40%;">Regulatory Compliance & Audit Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Emirates ID (EID)</td>
            <td>15-Digit Format: <code>784-YYYY-XXXXXXX-Z</code></td>
            <td>Federal identity card number required for all legal residents; validated on entry.</td>
          </tr>
          <tr>
            <td class="col-field">MOHRE Labour Card ID</td>
            <td>14-Digit Ministry Labour ID</td>
            <td>Mandatory unique identifier for CBUAE Wages Protection System (WPS) salary routing.</td>
          </tr>
          <tr>
            <td class="col-field">Employee UAE IBAN</td>
            <td>23-Character Personal IBAN</td>
            <td>Bank account registered in the employee's legal name for electronic payroll disbursement.</td>
          </tr>
          <tr>
            <td class="col-field">Contract Classification</td>
            <td>Fixed-Term Contract (UAE Labour Law)</td>
            <td>Standardized fixed-term employment contract per Federal Decree-Law No. 33 of 2021.</td>
          </tr>
        </tbody>
      </table>

      <h2>Workforce Attendance, Leave & Timesheet Locking</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Biometric Time-Clock Sync</h4>
          <p>Integrates daily biometric fingerprint and facial scans from Dubai and Abu Dhabi branch terminals, recording precise work hours.</p>
        </div>
        <div class="matching-card">
          <h4>Statutory Leave Ledger</h4>
          <p>Automates statutory leave balances: 30 calendar days annual leave, sick leave provisions, and maternity leave per UAE Labour Law.</p>
        </div>
        <div class="matching-card">
          <h4>Payroll Timesheet Lock</h4>
          <p>At month-end (25th), timesheets are locked against further edits, providing verified attendance records to the payroll calculation engine.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Onboarding an Employee into Acconeer ERP</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>HR & Workforce ➔ Employees</strong> and click <strong>+ Add Employee</strong>.</li>
          <li>Enter personal data, verified Emirates ID, passport number, and 14-digit MOHRE Labour Card identifier.</li>
          <li>Assign Department, Branch Cost Center, and direct supervisor for leave authorization routing.</li>
          <li>Input contractual compensation terms (Basic Wage and itemized allowances) and 23-character personal UAE IBAN.</li>
          <li>Attach scanned contract and Emirates ID documents; click <strong>Save & Activate</strong> to enroll in payroll.</li>
        </ol>
      </div>

      <h2>UAE Statutory Leave Entitlements (Federal Decree-Law No. 33 of 2021)</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Leave Category</th>
            <th style="width: 35%;">Statutory System Allowance</th>
            <th style="width: 40%;">Compensation & Accrual Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Annual Leave</td>
            <td>30 Calendar Days per completed year</td>
            <td>Accrues at 2.5 days per month; calculated on full gross wage per Article 29.</td>
          </tr>
          <tr>
            <td class="col-field">Statutory Sick Leave</td>
            <td>Up to 90 continuous or intermittent days</td>
            <td>First 15 days full pay; next 30 days half pay; remaining 45 days unpaid.</td>
          </tr>
          <tr>
            <td class="col-field">Maternity & Parental Leave</td>
            <td>60 Days Maternity (45 full / 15 half pay)</td>
            <td>Plus 5 working days paid parental leave for either parent within 6 months.</td>
          </tr>
        </tbody>
      </table>

      <h2>Biometric Time-Clock Hardware Sync & Attendance Rules</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Terminal Auto-Sync (15-Min Intervals)</div>
          <div class="sop-meta-desc">Biometric devices at Dubai and Abu Dhabi branch gates stream clock-in/out records directly to employee attendance logs.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Grace Periods & Shift Rules</div>
          <div class="sop-meta-desc">Configurable 15-minute grace period on shift starts; unapproved late arrivals flag automatically in supervisor timesheet reviews.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Overtime Calculation (Article 19)</div>
          <div class="sop-meta-desc">Approved overtime computes automatically: standard day + 25% hourly rate; night shift (9pm–4am) or rest days + 50% hourly rate.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">WPS Payroll Integration</div>
          <div class="sop-meta-desc">Validated monthly attendance summaries feed gross-to-net payroll calculations without manual re-entry.</div>
        </div>
      </div>
    </div>
    """

def get_page_18():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Human_Resources/07_Payroll.png",
        "Monthly Payroll Processing Register with UAE Central Bank WPS Integration",
        "/hr/payroll",
        [
            ("Payroll Processing Register", "Monthly compensation summary, itemized basic pay, allowances, and statutory deductions in AED."),
            ("Generate SIF Action", "Creates encrypted UAE Central Bank Wages Protection System (WPS) Salary Information File."),
            ("Post to GL Action", "Commits monthly payroll journal voucher to General Ledger salary expense accounts."),
            ("Payslip Distribution", "Automated distribution of bilingual electronic payslips to employee document repository.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 09 · MODULE 09 (PART 2)</div>
          <div class="chapter-title">Payroll Engine & UAE WPS Compliance</div>
        </div>
        <div class="chapter-cat">COMPENSATION & LABOUR LAW</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ HR & Workforce ➔ Payroll
      </div>

      <p>
        The Payroll Engine executes monthly gross-to-net salary calculations, end-of-service gratuity (EOSB) statutory provisions, and electronic Salary Information File (.SIF) generation for the UAE Central Bank Wages Protection System (WPS).
      </p>

      {wf}

      <h2>UAE Federal Labour Law Gratuity & Compensation Structure</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Compensation / Benefit</th>
            <th style="width: 35%;">System Calculation Basis</th>
            <th style="width: 40%;">UAE Labour Law Legal Reference (Law No. 33 of 2021)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Basic Wage</td>
            <td>Contractual basic salary component</td>
            <td><strong>Sole legal basis</strong> for computing End of Service Gratuity (EOSB). Excludes all allowances.</td>
          </tr>
          <tr>
            <td class="col-field">Contractual Allowances</td>
            <td>Housing, Transport, Utilities, Mobile</td>
            <td>Defined by employment agreement; paid monthly as part of gross remuneration; exempt from gratuity.</td>
          </tr>
          <tr>
            <td class="col-field">Gratuity (1 to 5 Years)</td>
            <td><strong>21 Days' Basic Wage</strong> per year of service</td>
            <td>Article 51: Accrues monthly in general ledger: <code>Dr. 63500 Gratuity Exp / Cr. 22500 Gratuity Provision</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Gratuity (> 5 Years)</td>
            <td><strong>30 Days' Basic Wage</strong> per additional year</td>
            <td>Article 51: Maximum total cumulative gratuity is strictly capped at <strong>two full years' basic wage</strong>.</td>
          </tr>
          <tr>
            <td class="col-field">Unpaid Leave Exclusion</td>
            <td>Deducted from total service days</td>
            <td>Unpaid leave periods are legally excluded from total service duration calculations.</td>
          </tr>
        </tbody>
      </table>

      <h2>CBUAE Wages Protection System (WPS) SIF v1.2 Specifications</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Header Record (SCR)</h4>
          <p>Contains 13-digit MOHRE Employer ID, 9-digit Bank Routing Code, file creation date, and total monthly payroll value in AED.</p>
        </div>
        <div class="matching-card">
          <h4>Employee Record (EDR)</h4>
          <p>Contains 14-digit Labour Card ID, personal IBAN, basic wage, variable pay, leave deductions, and net AED transfer amount.</p>
        </div>
        <div class="matching-card">
          <h4>General Ledger Post</h4>
          <p><strong>Dr. 63000 Salaries Expense / Dr. 63500 Gratuity / Cr. 21500 Payroll Clearing / Cr. 22500 Gratuity Liability</strong>.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Running Monthly Payroll and Exporting WPS SIF</div>
        <ol class="proc-steps">
          <li>Ensure all biometric attendance records and approved leave requests are locked for the current calendar month.</li>
          <li>Navigate to <strong>HR & Workforce ➔ Payroll</strong> and click <strong>Run Monthly Payroll Calculation</strong>.</li>
          <li>Review itemized gross-to-net calculations, overtime hours, unpaid leave deductions, and net payouts in AED.</li>
          <li>Click <strong>Generate WPS SIF File</strong>. The system validates all 14-digit Labour IDs and 23-character IBANs before export.</li>
          <li>Click <strong>Post Payroll to GL</strong> to record the salary expense voucher, then transmit the SIF file via corporate banking portal.</li>
        </ol>
      </div>

      <div class="note-card" style="margin-top: 4pt; margin-bottom: 0;">
        <div class="note-card-title">MOHRE Wages Protection System (WPS) Statutory Compliance</div>
        <strong>Cabinet Resolution No. 43 of 2022 Mandate:</strong> UAE employers must disburse at least 80% of total employee wages within 10 days of the due date via certified CBUAE WPS banking channels. Failure to disburse within 17 days results in automated work permit suspension and statutory ministry fines. Acconeer ERP enforces pre-export SIF validation against the Central Bank formatting specification.
      </div>
    </div>
    """

def get_page_19():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Reports/01_Financial_Reports.png",
        "Executive Financial Statements Suite with Multi-Period Variance Controls",
        "/reports/financial",
        [
            ("Financial Report Selector", "Generate Profit & Loss, Balance Sheet, Cash Flow Statement, and Trial Balance."),
            ("Period & Comparison Controls", "Toggle comparison with prior month, prior quarter, or prior fiscal year."),
            ("Variance Switches", "Activate [x] Show Variance (AED) and [x] Show Variance (%) delta columns."),
            ("Export Actions", "Generate board-ready bilingual PDF reports and auditable Excel balance sheets.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 10 · MODULE 10</div>
          <div class="chapter-title">Financial Reporting & Comparative Variance</div>
        </div>
        <div class="chapter-cat">FINANCIAL INTELLIGENCE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Reports ➔ Financial Statements
      </div>

      <p>
        The Financial Reporting suite generates publication-grade financial statements in strict accordance with International Financial Reporting Standards (IFRS). It provides dynamic variance switches and complete sub-ledger drill-down capabilities.
      </p>

      {wf}

      <h2>Standard Financial Statement Suite & Reporting Cadence</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Financial Statement</th>
            <th style="width: 35%;">IFRS Accounting Standard</th>
            <th style="width: 40%;">Primary Executive Purpose & Stakeholders</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Profit & Loss Statement (P&L)</td>
            <td>IAS 1 Presentation of Financial Statements</td>
            <td>Itemizes revenues (40000), direct costs (50000), and OpEx (60000); reveals operating profit and net margin.</td>
          </tr>
          <tr>
            <td class="col-field">Balance Sheet</td>
            <td>IAS 1 Financial Position Statement</td>
            <td>Assets = Liabilities + Equity. Summarizes working capital, bank liquidity, and net asset value.</td>
          </tr>
          <tr>
            <td class="col-field">Cash Flow Statement</td>
            <td>IAS 7 Statement of Cash Flows</td>
            <td>Categorizes cash into Operating, Investing, and Financing activities; reconciles bank balances.</td>
          </tr>
          <tr>
            <td class="col-field">Trial Balance</td>
            <td>IFRS Double-Entry Audit Standard</td>
            <td>Itemizes opening balance, period debit/credit movements, and closing balance for every active account.</td>
          </tr>
        </tbody>
      </table>

      <h2>Comparative Financial Switches & Variance Thresholds</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Variance Switch</th>
            <th style="width: 35%;">Operational Functionality</th>
            <th style="width: 40%;">Management Action Threshold</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">[x] Enable Comparison</td>
            <td>Compares active period against prior period or prior year</td>
            <td>Essential for board meetings, quarterly investor decks, and statutory audit reviews.</td>
          </tr>
          <tr>
            <td class="col-field">[x] Show Variance (AED)</td>
            <td>Calculates exact monetary difference column</td>
            <td>Monetary variances &gt; AED 50,000 trigger automated variance explanation flags.</td>
          </tr>
          <tr>
            <td class="col-field">[x] Show Variance (%)</td>
            <td>Displays relative percentage growth or contraction</td>
            <td>Cost expansions &gt; 10% highlight budgetary overruns across departmental cost centers.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Generating a Comparative Financial Statement</div>
        <ol class="proc-steps">
          <li>Select the desired report from the directory (e.g., <em>Profit & Loss Statement</em>).</li>
          <li>Set the primary reporting period (e.g. <em>Q3 2026 Consolidated</em>) and ensure all journals are posted.</li>
          <li>Check <strong>[x] Enable Comparison</strong> and select the comparison baseline (e.g. <em>Previous Quarter Q2 2026</em>).</li>
          <li>Activate <strong>[x] Show Variance (AED)</strong> and <strong>[x] Show Variance (%)</strong> to render variance delta columns.</li>
          <li>Click <strong>Generate Report</strong>. Inspect line-item drill-downs or click <strong>Export to PDF</strong> for board distribution.</li>
        </ol>
      </div>
    </div>
    """

def get_page_20():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/VAT_Returns/01_VAT_Filing_Dashboard.png",
        "UAE FTA VAT Returns Workspace with Automated Form 201 Box Mapping",
        "/vat/dashboard",
        [
            ("VAT Return Register", "Tax filing reference, quarterly tax period, filing due date, and statutory status."),
            ("FTA Form 201 Box Headers", "Standard Rated Outputs, Box 8 Output Tax, Box 11 Input Tax, and Box 14 Net Due."),
            ("Filing Status Pipeline", "Visual workflow tracker: All Statuses ➔ Draft ➔ Under Review ➔ Submitted ➔ Settled in GL."),
            ("EmaraTax XML Export", "Generates official schema-compliant XML file for direct upload to UAE FTA EmaraTax portal.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 11 · MODULE 11 (PART 1)</div>
          <div class="chapter-title">VAT Returns: UAE FTA Form 201 Engine</div>
        </div>
        <div class="chapter-cat">TAX COMPLIANCE & STATUTORY FILINGS</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ VAT Returns
      </div>

      <p>
        The UAE VAT Returns module is a statutory tax engine that calculates periodic tax liabilities in strict compliance with UAE Federal Decree-Law No. 8 on Value Added Tax. It automates exact box mappings for UAE FTA Form 201 declarations.
      </p>

      {wf}

      <h2>Official UAE FTA Form 201 Statutory Declaration Card (Q3 2026)</h2>
      <div class="journal-demo-card">
        <div class="journal-demo-header">
          <span>UAE FTA VAT FORM 201 DECLARATION SUMMARY • TRN: 100999900000003</span>
          <span class="badge-mono badge-blue">STATUS: UNDER REVIEW</span>
        </div>
        <div class="journal-demo-row">
          <span>Box 1: Standard Rated Supplies (Emirate of Dubai — 5%)</span>
          <span>AED 1,248,500.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">VAT: AED 62,425.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Box 8: Total Output Tax Due for Current Tax Period</span>
          <span>—</span>
          <span style="font-weight: 700; color: var(--color-navy);">AED 62,425.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Box 9: Standard Rated Expenses (Dubai Operations — 5% Recoverable)</span>
          <span>AED 823,600.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">VAT: AED 41,180.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Box 11: Total Recoverable Input Tax for Current Tax Period</span>
          <span>—</span>
          <span style="font-weight: 700; color: var(--color-navy);">AED 41,180.00</span>
        </div>
        <div class="journal-demo-total">
          <span>Box 14: Net VAT Payable to Federal Tax Authority (Box 8 − Box 11)</span>
          <span style="color: var(--color-red);">TOTAL NET DUE: AED 21,245.00</span>
        </div>
      </div>

      <h2>UAE FTA Form 201 Statutory Box Mapping Specifications</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Form 201 Box</th>
            <th style="width: 35%;">Statutory Tax Description</th>
            <th style="width: 45%;">Acconeer General Ledger Source & Rule</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>Boxes 1a - 1g</code></td>
            <td>Standard Rated Supplies by Emirate (5%)</td>
            <td>Mapped to Account 40000; segregated by delivering branch facility location (Abu Dhabi 1a, Dubai 1b, Sharjah 1c, etc.).</td>
          </tr>
          <tr>
            <td><code>Box 3</code></td>
            <td>Supplies Subject to Reverse Charge (RCM)</td>
            <td>Cross-border imported services/goods under Article 48; generates simultaneous output tax and input tax.</td>
          </tr>
          <tr>
            <td><code>Box 4 & 5</code></td>
            <td>Zero-Rated Supplies (0%) & Exempt Supplies</td>
            <td>Box 4: Qualifying commercial exports. Box 5: Exempt financial services, local passenger transport.</td>
          </tr>
          <tr>
            <td><code>Box 8</code></td>
            <td>Total Output Tax Due for Period</td>
            <td>Sum of output tax across Boxes 1–7. Credit balance in Account 22100 Output VAT Payable.</td>
          </tr>
          <tr>
            <td><code>Box 9 & 10</code></td>
            <td>Standard Expenses & Reverse Charge Inputs</td>
            <td>Box 9: 5% input tax paid to registered suppliers. Box 10: Input tax recoverable under reverse charge.</td>
          </tr>
          <tr>
            <td><code>Box 11</code></td>
            <td>Total Recoverable Input Tax</td>
            <td>Sum of input tax across Boxes 9–10. Debit balance in Account 22200 Input VAT Recoverable.</td>
          </tr>
          <tr>
            <td><code>Box 14</code></td>
            <td>Net VAT Payable / (Recoverable)</td>
            <td>Box 8 Output Tax minus Box 11 Input Tax. Net tax payable settled to FTA clearing account.</td>
          </tr>
          <tr>
            <td><code>Box 15</code></td>
            <td>Bad Debt Relief & Corrections</td>
            <td>Statutory adjustments for bad debts written off (&gt; 6 months overdue) or voluntary disclosures.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Auditing and Generating UAE VAT Form 201</div>
        <ol class="proc-steps">
          <li>Ensure all sales invoices, credit notes, and supplier bills for the quarterly tax period are approved and posted.</li>
          <li>Navigate to <strong>VAT Returns</strong> and click <strong>+ Generate Period Return</strong> for the active quarter (e.g. <em>Q3 2026</em>).</li>
          <li>Drill down into Box 1 (Standard Supplies by Emirate) and Box 9 (Standard Expenses) to verify line-item tax details.</li>
          <li>Verify that zero-rated exports map to Box 4, exempt supplies to Box 5, and import reverse charges to Boxes 3 & 10.</li>
          <li>Click <strong>Export EmaraTax XML</strong>. Transition status to <em>Under Review</em> for CFO sign-off prior to portal submission.</li>
        </ol>
      </div>
    </div>
    """

def get_page_21():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/VAT_Returns/01_VAT_Filing_Dashboard.png",
        "UAE VAT Return General Ledger Settlement and Statutory EmaraTax Status",
        "/vat/settlement",
        [
            ("Settlement Action Trigger", "Direct action button to execute statutory general ledger tax account zeroing."),
            ("GL Settlement Voucher Preview", "Shows journal voucher clearing Output VAT (22100) against Input VAT (22200)."),
            ("EmaraTax Reference Link", "Stores official FTA submission acknowledgment number and filing timestamp."),
            ("Settled Status Badge", "Locks tax period from future invoice allocations once settled in general ledger.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 11 · MODULE 11 (PART 2)</div>
          <div class="chapter-title">VAT Filing Pipeline & General Ledger Settlement</div>
        </div>
        <div class="chapter-cat">STATUTORY SETTLEMENT & TAX CALENDAR</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ VAT Returns ➔ Settlement
      </div>

      <p>
        Following official submission to the UAE FTA EmaraTax portal, the VAT return must be settled within the General Ledger. The settlement voucher offsets Output VAT against Input VAT, moving net payable amounts into the FTA settlement clearing account.
      </p>

      {wf}

      <h2>Automated Statutory GL VAT Settlement Voucher Simulation</h2>
      <div class="journal-demo-card">
        <div class="journal-demo-header">
          <span>VAT SETTLEMENT VOUCHER: JV-VAT-2026-Q3 (Period Settlement)</span>
          <span class="badge-mono badge-green">SETTLED IN GL</span>
        </div>
        <div class="journal-demo-row">
          <span>Dr. 22100-01 Output VAT Payable (Clearing Box 8 Tax Liability)</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 62,425.00</span>
          <span>AED 0.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Cr. 22200-01 Input VAT Recoverable (Clearing Box 11 Tax Asset)</span>
          <span>AED 0.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 41,180.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Cr. 22300-01 FTA VAT Settlement Clearing (Box 14 Net Due to FTA)</span>
          <span>AED 0.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 21,245.00</span>
        </div>
        <div class="journal-demo-total">
          <span>Balanced Tax Settlement Total</span>
          <span>Debit: AED 62,425.00</span>
          <span>Credit: AED 62,425.00 (Variance: AED 0.00)</span>
        </div>
      </div>

      <h2>UAE FTA Statutory Filing Calendar & Regulatory Penalties</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Compliance Event</th>
            <th style="width: 35%;">Statutory Deadline (UAE FTA)</th>
            <th style="width: 40%;">Regulatory Penalty for Non-Compliance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Quarterly VAT 201 Filing</td>
            <td>28th day following the end of the tax quarter</td>
            <td>Late filing penalty: AED 1,000 for the first offense; AED 2,000 for repetition within 24 months.</td>
          </tr>
          <tr>
            <td class="col-field">Statutory Tax Payment</td>
            <td>28th day following the end of the tax quarter</td>
            <td>Late payment penalty: 2% of unpaid tax immediately, plus 4% monthly penalty thereafter.</td>
          </tr>
          <tr>
            <td class="col-field">Record Retention (Article 78)</td>
            <td>Strict minimum of <strong>5 years</strong> from year-end</td>
            <td>Failure to maintain accounting records: AED 10,000 for first occurrence; AED 20,000 for repetition.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Settling VAT in General Ledger & Disbursing to FTA</div>
        <ol class="proc-steps">
          <li>Upload the approved EmaraTax submission acknowledgment receipt PDF and input the official FTA Reference Number.</li>
          <li>Click <strong>Settle in GL</strong>. The system posts the settlement voucher, zeroing out Accounts 22100 and 22200.</li>
          <li>Confirm that net payable moves to <code>22300 FTA VAT Settlement Clearing</code> (AED 21,245.00).</li>
          <li>Initiate corporate bank payment to FTA via GIBAN wire transfer, clearing Account 22300 against Bank (10100).</li>
          <li>The quarterly tax period transitions to <span class="badge-mono badge-green">LOCKED & SETTLED</span>, permanently preventing retroactive postings.</li>
        </ol>
      </div>

      <div class="note-card" style="margin-top: 4pt; margin-bottom: 0;">
        <div class="note-card-title">FTA Voluntary Disclosures (Form 211) & Penalty Safeguards</div>
        <strong>Statutory Adjustment Protocol:</strong> If an error resulting in a tax variance exceeding AED 10,000 is discovered in a locked period, UAE Federal Tax Law requires submission of a Voluntary Disclosure (Form 211) within 20 business days. Acconeer ERP generates automated audit delta reports comparing the locked return with corrected sub-ledger records to calculate the voluntary disclosure amount and minimize administrative penalties.
      </div>
    </div>
    """

def get_page_22():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Document_Vault/01_Document_Directory.png",
        "Enterprise Document Vault with Automated Expiry Tracking and RBAC Access",
        "/vault/documents",
        [
            ("Document Registry Table", "Document titles, categories, upload dates, expiration alerts, and verified attachment links."),
            ("Upload Document Action", "Upload commercial trade licenses, tenancy contracts, VAT certificates, and audit reports."),
            ("Expiry Alert Threshold", "Flags legal documents expiring within 30, 60, or 90 days with email alerts."),
            ("Access Permission Tag", "Restricts document viewing by user role (Executive, Finance, HR, or Legal).")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 12 · MODULE 12</div>
          <div class="chapter-title">Document Vault & Retention Governance</div>
        </div>
        <div class="chapter-cat">RECORDS MANAGEMENT & COMPLIANCE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Document Vault
      </div>

      <p>
        The Enterprise Document Vault manages corporate trade licenses, lease contracts, statutory certificates, and financial audit artifacts. It enforces regulatory record-retention policies and automated expiration warnings.
      </p>

      {wf}

      <h2>UAE Statutory Record Retention & Governance Policies</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Document Category</th>
            <th style="width: 35%;">Statutory Retention Period</th>
            <th style="width: 40%;">Governing UAE Legal Authority & Regulation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Tax Invoices & Credit Notes</td>
            <td>Minimum <strong>5 Years</strong> from end of tax period</td>
            <td>Article 78 of UAE Federal Decree-Law No. 8 on Value Added Tax.</td>
          </tr>
          <tr>
            <td class="col-field">Corporate Tax Records</td>
            <td>Minimum <strong>7 Years</strong> following tax year</td>
            <td>Article 56 of UAE Federal Decree-Law No. 47 of 2022 on Corporate Taxation.</td>
          </tr>
          <tr>
            <td class="col-field">Capital Real Estate Assets</td>
            <td>Minimum <strong>15 Years</strong> from acquisition</td>
            <td>Statutory capital asset scheme records for commercial property and land.</td>
          </tr>
          <tr>
            <td class="col-field">Employee Labour Contracts</td>
            <td>Minimum <strong>2 Years</strong> following termination</td>
            <td>Ministry of Human Resources & Emiratisation (MOHRE) workforce compliance.</td>
          </tr>
        </tbody>
      </table>

      <h2>Automated Expiration Monitoring & Alert Thresholds</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>90-Day Early Warning</h4>
          <p>Sends notification to Department Head upon detection of commercial license or lease expiration within 90 days.</p>
        </div>
        <div class="matching-card">
          <h4>30-Day Critical Escalation</h4>
          <p>Flags document status in red across the executive dashboard and alerts General Counsel and Managing Director.</p>
        </div>
        <div class="matching-card">
          <h4>Expired Document Lockout</h4>
          <p>Expired trade licenses or tax certificates trigger automated warnings on outbound customer invoicing workflows.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Uploading and Tagging a Controlled Enterprise Document</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Document Vault</strong> and click <strong>+ Upload Document</strong>.</li>
          <li>Select the Document Category (e.g. <em>Commercial Trade License</em> or <em>VAT Certificate</em>).</li>
          <li>Enter document title, issuing government authority (e.g. <em>Dubai DED</em>), effective date, and expiration date.</li>
          <li>Attach the verified original PDF scan and configure RBAC access permissions (e.g. <em>Finance & Legal Only</em>).</li>
          <li>Click <strong>Save Document</strong> to activate automated lifecycle monitoring and statutory retention tagging.</li>
        </ol>
      </div>

      <h2>Document Access Governance & Role-Based Permissions (RBAC)</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Access Security Tier</th>
            <th style="width: 35%;">Authorized Document Scopes</th>
            <th style="width: 40%;">Strict Security Controls & Redactions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Executive & Legal</td>
            <td>Trade licenses, tenancy contracts, board resolutions, tax audits</td>
            <td>Unrestricted access; downloads watermarked with viewer user ID and timestamp.</td>
          </tr>
          <tr>
            <td class="col-field">Finance & Treasury</td>
            <td>Bank confirmation letters, VAT returns, audited financial statements</td>
            <td>Restricted from viewing executive compensation contracts and HR personnel files.</td>
          </tr>
          <tr>
            <td class="col-field">Human Resources</td>
            <td>Employee MOHRE contracts, Emirates IDs, passport scans, visas</td>
            <td>Encrypted at rest (AES-256); personal identity documents masked from operational staff.</td>
          </tr>
        </tbody>
      </table>

      <h2>Statutory Expiration Action Checklist & Archival Protocol</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Automated Renewal Task Creation</div>
          <div class="sop-meta-desc">At 60 days to expiry, the system auto-assigns an administrative renewal ticket to the corporate PRO or legal officer.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Cryptographic SHA-256 Checksums</div>
          <div class="sop-meta-desc">Uploaded PDFs generate immutable SHA-256 hashes upon ingestion to guarantee evidence integrity during forensic audits.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Litigation & Legal Holds</div>
          <div class="sop-meta-desc">Chief Legal Officer can place an immediate <em>Legal Hold</em> on any document container, suspending automatic lifecycle purges.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Post-Retention Certified Purge</div>
          <div class="sop-meta-desc">Upon expiration of the statutory 5/7-year retention limit, documents enter a certified shredding queue requiring dual sign-off.</div>
        </div>
      </div>
    </div>
    """

def get_page_23():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Audit_Trail/01_Audit_Logs.png",
        "Tamper-Evident System Audit Trail with Cryptographic Timestamps",
        "/security/audit",
        [
            ("Audit Log Directory", "Chronological record of system events, operator IDs, event categories, IP addresses, and actions."),
            ("Search & Event Filter", "Filter logs by user ID, transaction number, module, or risk classification."),
            ("Diff Viewer Trigger", "Opens side-by-side JSON comparison showing pre-change and post-change database values."),
            ("Forensic Export Action", "Generates signed audit log package for external financial and compliance auditors.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 13 · MODULE 13</div>
          <div class="chapter-title">Audit Trail & Security Telemetry</div>
        </div>
        <div class="chapter-cat">SECURITY, FORENSICS & AUDIT</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Audit Trail
      </div>

      <p>
        The Audit Trail engine captures an append-only chronological record of all transactional, administrative, and security events across Acconeer ERP. It provides forensic proof of data integrity for statutory financial audits.
      </p>

      {wf}

      <h2>Append-Only Forensic Audit Logging Specifications</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Logged Event Category</th>
            <th style="width: 35%;">Captured Telemetry Fields</th>
            <th style="width: 40%;">Forensic Purpose & Compliance Mandate</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Financial Transactions</td>
            <td>User ID, timestamp, voucher ID, Dr/Cr accounts, amounts</td>
            <td>Traces origin of every journal voucher, invoice, bill, and payment. Cannot be altered or purged.</td>
          </tr>
          <tr>
            <td class="col-field">Master Data Modifications</td>
            <td>Pre-change value, post-change value, field modified</td>
            <td>Detects unauthorized alterations to customer credit limits, vendor bank IBANs, or tax rates.</td>
          </tr>
          <tr>
            <td class="col-field">Authentication & Access</td>
            <td>Login success/failure, IP address, user-agent, MFA method</td>
            <td>Identifies brute-force credential stuffing, suspicious geographical access, or privilege abuse.</td>
          </tr>
          <tr>
            <td class="col-field">Administrative Actions</td>
            <td>Period opening/closing, role assignment, system setting changes</td>
            <td>Guarantees that administrative overrides are attributed to specific authorized personnel.</td>
          </tr>
        </tbody>
      </table>

      <h2>Tamper-Evident Architecture & Non-Repudiation Controls</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Append-Only Storage</h4>
          <p>Audit tables are write-only. Database permissions strictly prohibit UPDATE or DELETE operations by any user, including admins.</p>
        </div>
        <div class="matching-card">
          <h4>Cryptographic Timestamping</h4>
          <p>Every event is stamped with an immutable UTC timestamp synchronized via NTP with certified time authority sources.</p>
        </div>
        <div class="matching-card">
          <h4>Audit Isolation</h4>
          <p>Audit records are isolated in an independent query layer; audit export packages carry SHA-256 integrity checksums.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Conducting a Forensic Audit Investigation</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Audit Trail</strong> and enter the transaction reference (e.g. <code>INV-2026-0188</code>).</li>
          <li>Review the chronological lifecycle: creation timestamp, approving manager ID, and journal release timestamp.</li>
          <li>Click <strong>View Diff</strong> on any modification event to compare original versus amended field values.</li>
          <li>Verify operator IP address and session token against registered corporate VPN and office network gateways.</li>
          <li>Click <strong>Export Audit Package</strong> to generate an encrypted, digitally signed audit dossier for external auditors.</li>
        </ol>
      </div>

      <h2>SIEM Integration & Real-Time Security Incident Telemetry</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Security Dimension</th>
            <th style="width: 35%;">System Telemetry & Protocol</th>
            <th style="width: 40%;">Incident Escalation & Forensic Trigger</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">SIEM Syslog Forwarding</td>
            <td>RFC 5424 TLS stream to corporate SOC</td>
            <td>Real-time streaming of all authentication, authorization, and administrative events.</td>
          </tr>
          <tr>
            <td class="col-field">Privileged Access Monitor</td>
            <td>Tracks super-user and admin console activity</td>
            <td>Automated alert triggered when admin accounts access transactional database tables.</td>
          </tr>
          <tr>
            <td class="col-field">Geographical Anomaly Detection</td>
            <td>IP geolocation against UAE office boundaries</td>
            <td>Logins from unrecognized overseas IP ranges require step-up MFA and trigger CISO alerts.</td>
          </tr>
        </tbody>
      </table>

      <h2>External Auditor Evidence Dossier & Forensic Package Protocol</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Auditor-Specific Role Profile</div>
          <div class="sop-meta-desc">Temporary read-only auditor credentials provide access to drill-down sub-ledgers without data export permissions.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Cryptographic Evidence Dossier</div>
          <div class="sop-meta-desc">Exported audit packages generate an encrypted ZIP archive containing all linked vouchers, approvals, and an SHA-256 manifest.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Chain of Custody Certification</div>
          <div class="sop-meta-desc">Each exported dossier embeds a digitally signed certificate verifying that the audit trail has not been altered or truncated.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Statutory Tax Authority Audits</div>
          <div class="sop-meta-desc">Generates the official UAE FTA Audit File (FAF) text format required during formal tax authority inspections.</div>
        </div>
      </div>
    </div>
    """

def get_page_24():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Budgeting/01_Budget_Management.png",
        "Corporate Budget Management Directory with Cost Center Variance Tracking",
        "/budgeting/overview",
        [
            ("Budget Matrix Table", "Departmental cost centers, approved annual allocations, committed spend, and remaining balance in AED."),
            ("New Budget Action", "Opens creation modal to establish annual operational and capital expenditure budgets."),
            ("Variance Alert Indicator", "Visual indicator flagging cost centers exceeding 80% (Amber) or 100% (Red) utilization."),
            ("Lock & Activate Trigger", "Freezes approved budget parameters and activates automated procurement spend controls.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 14 · MODULE 14</div>
          <div class="chapter-title">Budgeting & Fiscal Variance Controls</div>
        </div>
        <div class="chapter-cat">FINANCIAL PLANNING & CONTROL</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Budgeting ➔ Budget Management
      </div>

      <p>
        The Budget Management module enforces fiscal discipline by establishing annual expenditure allocations across departmental cost centers. It integrates with procure-to-pay workflows to block unauthorized spending before commitments are made.
      </p>

      {wf}

      <h2>Budget Enforcement Controls & Procurement Gateways</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Budget Control Level</th>
            <th style="width: 35%;">System Enforcement Mechanism</th>
            <th style="width: 40%;">Operational Impact on Business Operations</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Pre-Commitment Checking</td>
            <td>Purchase Requisitions check available budget in real-time</td>
            <td>Prevents creation of purchase orders if the cost center allocation lacks sufficient funds.</td>
          </tr>
          <tr>
            <td class="col-field">Soft Warning Threshold (80%)</td>
            <td>Alerts purchaser and cost center manager upon reaching 80%</td>
            <td>Advisory warning; allows transactions to proceed but notifies department head of run-rate.</td>
          </tr>
          <tr>
            <td class="col-field">Hard Stop Threshold (100%)</td>
            <td>System blocks purchase order release at 100% utilization</td>
            <td>Requires formal supplemental budget appropriation or Finance Director variance approval.</td>
          </tr>
        </tbody>
      </table>

      <h2>Budget Revision Governance & Transfer Rules</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Inter-Departmental Transfer</h4>
          <p>Reallocating funds between cost centers requires mutual sign-off by both Department Heads and Chief Accountant.</p>
        </div>
        <div class="matching-card">
          <h4>Supplemental Appropriations</h4>
          <p>Mid-year budget increases require formal executive justification and approval by the Finance Director or CFO.</p>
        </div>
        <div class="matching-card">
          <h4>Audit Trail Tracking</h4>
          <p>Every budget baseline modification, transfer, and override is permanently logged with timestamp and authorizer.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Establishing and Activating a Departmental Budget</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Budgeting ➔ Overview</strong> and click <strong>+ Add Budget Allocation</strong>.</li>
          <li>Select the operational Legal Entity, Branch Scope, and target Department Cost Center (e.g. <em>Sales & Marketing</em>).</li>
          <li>Enter approved quarterly and annual budget allocations in AED against specific expense accounts (Class 60000).</li>
          <li>Attach the board-approved annual budget schedule PDF as supporting documentation.</li>
          <li>Click <strong>Lock & Activate Budget</strong> (CFO authorization required) to enforce automated procurement spend controls.</li>
        </ol>
      </div>

      <h2>Budget Variance Escalation Tiers & Exception Routing</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Utilization Level</th>
            <th style="width: 35%;">System Gateway Status</th>
            <th style="width: 40%;">Operational Protocol & Approval Routing</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Normal (&lt; 80%)</td>
            <td><span class="badge-mono badge-green">Green · Open</span></td>
            <td>Purchase requisitions flow through standard departmental approval queues.</td>
          </tr>
          <tr>
            <td class="col-field">Advisory (80% - 99%)</td>
            <td><span class="badge-mono badge-amber">Amber · Warning</span></td>
            <td>Automatic notifications sent to Cost Center Manager; run-rate review triggered.</td>
          </tr>
          <tr>
            <td class="col-field">Lockout (&ge; 100%)</td>
            <td><span class="badge-mono badge-red">Red · Blocked</span></td>
            <td>Requisition submission completely blocked; requires formal budget reallocation.</td>
          </tr>
        </tbody>
      </table>

      <h2>CapEx Project Budgeting & Capitalization Thresholds</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Capitalization Minimum Threshold</div>
          <div class="sop-meta-desc">Tangible assets exceeding <strong>AED 5,000</strong> with useful life &gt; 1 year capitalize into Class 15000; minor items expense immediately.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">CapEx Project Codes</div>
          <div class="sop-meta-desc">Capital projects (e.g. warehouse automation) carry distinct project numbers tracking commitments against approved AFEs.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Inter-Cost Center Reallocation</div>
          <div class="sop-meta-desc">Transfers between operational cost centers require mutual agreement between department heads and Chief Accountant certification.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Contingency Reserve Drawdown</div>
          <div class="sop-meta-desc">Drawing down executive contingency reserves (Account 69000) requires formal authorization by the Chief Financial Officer.</div>
        </div>
      </div>
    </div>
    """

def get_page_25():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/AI_Operations/01_AI_Assistant_Prompt.png",
        "Embedded AI Assistant Prompt Console with Financial Intelligence Telemetry",
        "/ai/assistant",
        [
            ("AI Prompt Console", "Conversational interface accepting natural language queries regarding receivables, payables, and variances."),
            ("Suggested Prompts Bar", "Quick execution chips: Top 5 Overdue AR, Cash Flow Forecast, VAT 201 Summary, Budget Variance."),
            ("Generated Response Panel", "Structured tabular telemetry, financial insights, and automated draft journal vouchers."),
            ("Human Review & Commit Action", "Saves AI-drafted vouchers to standard review queue for mandatory accountant sign-off.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 15 · MODULE 15</div>
          <div class="chapter-title">AI Assistant & Responsible Use Controls</div>
        </div>
        <div class="chapter-cat">ENTERPRISE ARTIFICIAL INTELLIGENCE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ AI Assistant (or Press <code>Alt + A</code>)
      </div>

      <p>
        The Acconeer AI Assistant provides conversational intelligence for financial analytics, cash flow forecasting, and draft journal preparation. It operates within strict security boundaries governed by enterprise responsible-use policies.
      </p>

      {wf}

      <h2>Responsible AI Policy: Human-in-the-Loop Governance</h2>
      <div class="warning-card">
        <strong>Mandatory Accounting Policy:</strong> The AI Assistant functions exclusively in an <strong>Advisory & Drafting Capacity</strong>. Under no circumstances does the system permit AI models to post directly or autonomously to the General Ledger. All AI-prepared journal vouchers, tax allocations, or billing adjustments are saved to the standard draft queue and require independent verification and approval by an authorized accountant.
      </div>

      <h2>AI Assistant Capabilities & Data Privacy Enclave Architecture</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">AI Capability</th>
            <th style="width: 35%;">Supported Workflow</th>
            <th style="width: 40%;">Data Protection & Security Boundary</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Financial Query Telemetry</td>
            <td>Natural language queries on AR aging, bank liquidity, and budget variance</td>
            <td>Inherits active user's RBAC role; clerks cannot query executive profitability metrics.</td>
          </tr>
          <tr>
            <td class="col-field">Draft Journal Preparation</td>
            <td>Drafts balanced double-entry vouchers from invoices or expense statements</td>
            <td>Routes to <em>Pending Review</em> queue; requires authorized accountant sign-off before GL commit.</td>
          </tr>
          <tr>
            <td class="col-field">Zero Model Training</td>
            <td>Enterprise inference endpoints with zero prompt or output retention</td>
            <td>Customer financial data is never utilized for public model training or stored outside the enclave.</td>
          </tr>
          <tr>
            <td class="col-field">Prompt Injection Defense</td>
            <td>Automated sanitization of natural language inputs and document text</td>
            <td>Prevents malicious prompt payloads from bypassing business logic or leaking master data.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Utilizing the AI Assistant and Committing Draft JVs</div>
        <ol class="proc-steps">
          <li>Open the AI Assistant prompt console from the navigation header or press shortcut <code>Alt + A</code>.</li>
          <li>Enter natural language queries (e.g. <em>"Show top 5 overdue customer receivables"</em> or <em>"Draft prepaid rent JV"</em>).</li>
          <li>Review the AI-generated tabular data, statutory box calculations, or draft double-entry journal vouchers.</li>
          <li>Verify account codes, debit/credit balance equality (0.00 variance), and supporting business documentation.</li>
          <li>Click <strong>Save Draft Voucher</strong>. The voucher lands in the General Ledger review queue for standard managerial approval.</li>
        </ol>
      </div>

      <h2>AI Architecture & Data Processing Security Specifications</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Governance Dimension</th>
            <th style="width: 35%;">Technical Implementation Architecture</th>
            <th style="width: 40%;">Contractual & Security Assurance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Inference Enclave Hosting</td>
            <td>Dedicated UAE cloud region container instance</td>
            <td>Inference executes inside an isolated virtual private cloud (VPC); no external API hops.</td>
          </tr>
          <tr>
            <td class="col-field">Data Retention Policy</td>
            <td>Strict Ephemeral In-Memory Processing (Zero-Retention)</td>
            <td>Prompts and completions are discarded immediately after response delivery; zero disk storage.</td>
          </tr>
          <tr>
            <td class="col-field">Zero Model Training</td>
            <td>Statutory guarantee in Enterprise MSA</td>
            <td>Customer financial telemetry and vouchers are strictly excluded from AI model re-training.</td>
          </tr>
        </tbody>
      </table>

      <h2>Accountant Verification Checklist: AI-Drafted Vouchers</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">1. COA Account Mapping Audit</div>
          <div class="sop-meta-desc">Confirm that proposed debit and credit lines map to active, posting-eligible child codes in the Chart of Accounts.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">2. Mathematical Balancing Check</div>
          <div class="sop-meta-desc">Verify that debit and credit column totals calculate to identical amounts with exactly <code>AED 0.00</code> variance.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">3. UAE VAT Box Compatibility</div>
          <div class="sop-meta-desc">Confirm whether VAT lines map to 5% standard rate (Box 9) and verify supplier TRN validity on supporting tax invoice.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">4. Mandatory Supporting Evidence</div>
          <div class="sop-meta-desc">Attach verified original supplier invoice or contract PDF to voucher prior to submitting for managerial sign-off.</div>
        </div>
      </div>
    </div>
    """

def get_page_26():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">SYSTEM APPENDIX</div>
          <div class="chapter-title">Document Control, Requirements & Support</div>
        </div>
        <div class="chapter-cat">DOCUMENT GOVERNANCE & LIFECYCLE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Documentation Control ➔ Enterprise Support Directory
      </div>

      <p>
        This official operations manual is governed under Spectrum Zestwings corporate quality standards. Revisions are versioned systematically in synchronization with cloud software updates deployed to <code>acconeer.zestwings.com</code>.
      </p>

      <div class="brand-divider">
        <div class="brand-divider-red"></div>
        <div class="brand-divider-blue"></div>
      </div>

      <h2>Document Revision History & Quality Approvals</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 14%;">Revision #</th>
            <th style="width: 18%;">Release Date</th>
            <th style="width: 32%;">Scope of Changes</th>
            <th style="width: 20%;">Approved By</th>
            <th style="width: 16%;">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>v1.0.0</code></td>
            <td>15 Jan 2026</td>
            <td>Initial production baseline release for UAE enterprise market.</td>
            <td>Technology Director</td>
            <td><span class="badge-mono">Archived</span></td>
          </tr>
          <tr>
            <td><code>v2.0.0</code></td>
            <td>01 Jul 2026</td>
            <td>Multi-Entity Architecture & AI Assistant operations.</td>
            <td>Chief Solutions Architect</td>
            <td><span class="badge-mono">Archived</span></td>
          </tr>
          <tr>
            <td><code>v2.1.0</code></td>
            <td>18 Sep 2026</td>
            <td>Preliminary tenant operations draft.</td>
            <td>Lead Systems Auditor</td>
            <td><span class="badge-mono">Superseded</span></td>
          </tr>
          <tr>
            <td><code>v3.0.0</code></td>
            <td>18 Nov 2026</td>
            <td>Volume I: Universal Enterprise Standard Operating Manual.</td>
            <td>Documentation Board</td>
            <td><span class="badge-mono badge-green">Production</span></td>
          </tr>
        </tbody>
      </table>

      <h2>Technical Environment Prerequisites & System Requirements</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">System Dimension</th>
            <th style="width: 35%;">Supported Enterprise Standard</th>
            <th style="width: 40%;">Operational Recommendation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Supported Web Browsers</td>
            <td>Google Chrome, Microsoft Edge, Mozilla Firefox, Safari</td>
            <td>Current release and prior two major versions; JavaScript enabled.</td>
          </tr>
          <tr>
            <td class="col-field">Display Resolution</td>
            <td>1920 &times; 1080 (Full HD) recommended</td>
            <td>Minimum supported: 1366 &times; 768. Multi-column financial views optimized for 1080p+.</td>
          </tr>
          <tr>
            <td class="col-field">Network Bandwidth</td>
            <td>Minimum 2.0 Mbps dedicated per concurrent operator</td>
            <td>HTTPS TLS 1.3 encrypted connection; latency &lt; 50ms to UAE cloud region.</td>
          </tr>
          <tr>
            <td class="col-field">Contractual SLA Scope</td>
            <td>Governed by customer Master Services Agreement (MSA)</td>
            <td>Uptime guarantees, RPO/RTO metrics, and service credits are legally defined in client MSA.</td>
          </tr>
        </tbody>
      </table>

      <h2>Enterprise Escalation & Mission-Critical Support Tiers</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Support Tier Level</th>
            <th style="width: 38%;">Scope of Incident Management</th>
            <th style="width: 20%;">Direct Contact Channel</th>
            <th style="width: 20%;">Target Response SLA</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Tier 1: Frontline Helpdesk</td>
            <td>User login issues, role assignment, basic navigation inquiries.</td>
            <td><code>support@sztech.ae</code></td>
            <td>&lt; 2 Business Hours</td>
          </tr>
          <tr>
            <td class="col-field">Tier 2: Financial Systems</td>
            <td>GL balance inquiries, VAT box mapping, WPS SIF export validations.</td>
            <td><code>finance-support@sztech.ae</code></td>
            <td>&lt; 1 Hour (Priority)</td>
          </tr>
          <tr>
            <td class="col-field">Tier 3: Cloud Operations</td>
            <td>System availability, database failover, disaster recovery.</td>
            <td><code>ops@sztech.ae</code></td>
            <td>&lt; 15 Minutes (24/7/365)</td>
          </tr>
        </tbody>
      </table>

      <h2>High Availability, Cloud Disaster Recovery & MSA Precedence</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Infrastructure Dimension</th>
            <th style="width: 35%;">Architecture Specification (UAE Region)</th>
            <th style="width: 40%;">Contractual Governance & MSA Binding Rule</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Cloud Availability Zones</td>
            <td>Active-Passive Multi-Zone (Dubai & Abu Dhabi)</td>
            <td>Automated database failover ensures operational resilience across regional data centers.</td>
          </tr>
          <tr>
            <td class="col-field">Disaster Recovery (RPO / RTO)</td>
            <td>Target RPO &lt; 1 Hour • Target RTO &lt; 15 Minutes</td>
            <td>Binding uptime commitments, service credits, and custom SLAs are governed by client MSA.</td>
          </tr>
          <tr>
            <td class="col-field">Data Sovereignty & Encryption</td>
            <td>In-country UAE data residency (AES-256 / TLS 1.3)</td>
            <td>Guarantees that financial records never leave the UAE statutory jurisdiction.</td>
          </tr>
        </tbody>
      </table>

      <h2>Incident Severity Classification & Response Cadence</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Severity 1: Critical (Outage)</div>
          <div class="sop-meta-desc">Core system inaccessible; business halt. Response: &lt; 15 mins. 24/7 executive bridge & continuous engineer engagement.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Severity 2: High (Feature Degraded)</div>
          <div class="sop-meta-desc">Critical module impacted (e.g. VAT export or WPS payroll) without immediate workaround. Response: &lt; 1 hour.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Severity 3: Medium (Standard)</div>
          <div class="sop-meta-desc">Operational issue with available manual procedural workaround. Response: &lt; 4 business hours.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Severity 4: Low (Informational)</div>
          <div class="sop-meta-desc">Minor cosmetic inquiry, report formatting question, or feature enhancement request. Response: &lt; 1 business day.</div>
        </div>
      </div>
    </div>
    """

print("Pages 17-26 module finalized.")

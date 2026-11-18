# scripts/pages_p17_p26.py
from generate_complete_manual import window_frame

def get_page_17():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Human_Resources/02_Employee_Directory.png",
        "Employee Master Directory with UAE Labour Card and Contract Profiles",
        "/hr/employees",
        [
            ("Employee Directory Table", "Employee IDs, legal names, job titles, departments, visa statuses, and basic salary in AED."),
            ("+ Add Employee Button", "Primary action trigger opening multi-tab employee registration modal."),
            ("Department & Branch Filter", "Filter staff by Executive, Finance, Sales, Logistics, or Warehouse Branch."),
            ("Document Expiry Alerts", "Color-coded indicators tracking expiration of Emirates IDs, Passports, and Residency Visas.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">HR & WORKFORCE · HUMAN CAPITAL</div>
          <div class="chapter-title">HR & Employee Master Onboarding</div>
        </div>
        <div class="chapter-right-meta">MODULE 13<br>/hr/employees</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ HR & Workforce ➔ Employees
      </div>

      <p>
        The Human Resources module manages the complete employee lifecycle, workforce master profiles, statutory MOHRE employment contract details, personal UAE banking coordinates, and document expiration tracking in compliance with UAE Labour regulations.
      </p>

      {wf}

      <h2>Employee Profile Data Dictionary & Mandatory Parameters</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Parameter</th>
            <th style="width: 14%;">Field Type</th>
            <th style="width: 38%;">Description & Required Format</th>
            <th style="width: 26%;">Validation Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Full Legal Name *</td>
            <td>Text</td>
            <td>Full name matching passport and Emirates ID.</td>
            <td>Mandatory; minimum 3 characters.</td>
          </tr>
          <tr>
            <td class="col-field">Emirates ID (EID) *</td>
            <td>Text (15 digits)</td>
            <td>Standard UAE federal identity number (<code>784-YYYY-XXXXXXX-Z</code>).</td>
            <td>Validated format; must be unique in organization.</td>
          </tr>
          <tr>
            <td class="col-field">MOHRE Labour Card *</td>
            <td>Text (14 digits)</td>
            <td>Ministry of Human Resources unique employee identifier.</td>
            <td>Mandatory for Wages Protection System (WPS) routing.</td>
          </tr>
          <tr>
            <td class="col-field">Personal UAE IBAN *</td>
            <td>Text (23 chars)</td>
            <td>Employee's personal bank account registered in UAE (<code>AE...</code>).</td>
            <td>Validated: 23 characters; matches employee legal name.</td>
          </tr>
          <tr>
            <td class="col-field">Basic Salary *</td>
            <td>Numeric (AED)</td>
            <td>Contractual monthly basic pay specified in MOHRE contract.</td>
            <td>Mandatory; must be greater than zero.</td>
          </tr>
          <tr>
            <td class="col-field">Allowances (Housing/Trans)</td>
            <td>Numeric (AED)</td>
            <td>Itemized monthly fixed allowances for housing, transport, or food.</td>
            <td>Summed with Basic Salary for gross payroll calculation.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Onboarding a New Employee</h2>
      <ol class="step-list">
        <li>Navigate to <strong>HR & Workforce ➔ Employees</strong> and click the blue <strong>+ Add Employee</strong> button.</li>
        <li>Enter the employee's personal details, date of birth, nationality, and 15-digit <strong>Emirates ID</strong>.</li>
        <li>Under the Employment tab, select the assigned <strong>Department</strong> and operating <strong>Branch Cost Center</strong>.</li>
        <li>Input the 14-digit <strong>MOHRE Labour Card Number</strong> and select the contract start and end dates.</li>
        <li>In the Compensation tab, enter the monthly <strong>Basic Salary</strong> and breakdown of contractual allowances.</li>
        <li>Under Bank Coordinates, enter the employee's personal 23-character <strong>UAE IBAN</strong> and bank name.</li>
        <li>Upload scanned PDF copies of the Emirates ID, passport, and signed contract in the Documents tab, then click <strong>Save & Activate</strong>.</li>
      </ol>

      <h2>Statutory Leave Entitlements & Approval Routing</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Leave Classification</th>
            <th style="width: 35%;">Statutory Accrual & Entitlement</th>
            <th style="width: 40%;">System Approval & Payroll Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Annual Leave</td>
            <td>30 calendar days per completed year of service (2.5 days/month).</td>
            <td>Requires supervisor approval; paid at full basic salary + allowances.</td>
          </tr>
          <tr>
            <td class="col-field">Sick Leave</td>
            <td>Up to 90 days per year (15 full pay, 30 half pay, 45 unpaid).</td>
            <td>Medical certificate required; payroll engine auto-adjusts daily wage.</td>
          </tr>
          <tr>
            <td class="col-field">Maternity Leave</td>
            <td>60 days (45 days full pay, 15 days half pay).</td>
            <td>Requires HR documentation; protected under UAE Labour regulations.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">DOCUMENT EXPIRY MONITORING</div>
        Acconeer ERP automatically monitors passport, residency visa, and Emirates ID expiration dates. When a document is within 30 days of expiry, the employee record displays an amber badge and notifies the HR Manager via dashboard alerts.
      </div>
    </div>
    """

def get_page_18():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Human_Resources/07_Payroll.png",
        "Monthly Payroll Processing Engine with Timesheet Locking and WPS SIF Export",
        "/hr/payroll",
        [
            ("Payroll Batch Header", "Current payroll month (e.g. September 2026), employee head count, and gross payroll total."),
            ("Run Payroll Batch", "Primary action trigger to execute automated salary, allowance, and deduction calculations."),
            ("WPS SIF Export Trigger", "Generates encrypted CBUAE-compliant Salary Information File (SIF v1.2) for corporate bank upload."),
            ("Post Salary Voucher", "One-click generation of balanced double-entry payroll accrual journal in General Ledger.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">HR & WORKFORCE · PAYROLL ENGINE</div>
          <div class="chapter-title">Payroll Processing Engine & WPS SIF Export</div>
        </div>
        <div class="chapter-right-meta">MODULE 14<br>/hr/payroll</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ HR & Workforce ➔ Payroll & WPS
      </div>

      <p>
        The Payroll Processing Engine automates monthly compensation calculations, verifies biometric attendance timesheets, deducts statutory absences, posts balanced general ledger payroll accruals, and exports official CBUAE Wages Protection System (WPS) SIF v1.2 files.
      </p>

      {wf}

      <h2>Payroll Line Component Architecture & Calculation Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Payroll Component</th>
            <th style="width: 18%;">Classification</th>
            <th style="width: 38%;">Operational Calculation Rule</th>
            <th style="width: 22%;">GL Posting Mapping</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Basic Wage</td>
            <td>Earning (Fixed)</td>
            <td>Contractual fixed basic monthly pay from employee profile.</td>
            <td>Debit: <code>6010 Staff Salaries</code></td>
          </tr>
          <tr>
            <td class="col-field">Housing Allowance</td>
            <td>Earning (Fixed)</td>
            <td>Contractual monthly housing allowance.</td>
            <td>Debit: <code>6020 Housing Allowance</code></td>
          </tr>
          <tr>
            <td class="col-field">Transport Allowance</td>
            <td>Earning (Fixed)</td>
            <td>Contractual monthly travel and transport allowance.</td>
            <td>Debit: <code>6030 Transport Expense</code></td>
          </tr>
          <tr>
            <td class="col-field">Unpaid Leave Deductions</td>
            <td>Deduction</td>
            <td>Calculated: <code>(Basic Salary / 30 Days) * Unapproved Days Absent</code>.</td>
            <td>Credit: Offsets Salary Expense</td>
          </tr>
          <tr>
            <td class="col-field">Net Salary Payable</td>
            <td>Net Disbursement</td>
            <td>Formula: <code>Basic + Allowances - Deductions</code>.</td>
            <td>Credit: <code>2300 Accrued Salaries</code></td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Running Monthly Payroll & WPS Export</h2>
      <ol class="step-list">
        <li>Confirm that all employee attendance and approved leave requests are locked for the month (typically on the 25th).</li>
        <li>Navigate to <strong>HR & Workforce ➔ Payroll & WPS</strong> and click <strong>+ Run Monthly Payroll Batch</strong>.</li>
        <li>Select the payroll month and year, then click <strong>Calculate Payroll</strong>.</li>
        <li>Review the pre-calculated payroll register: verify employee head count, gross payroll, and individual net pay.</li>
        <li>Click <strong>Post Payroll to General Ledger</strong> to generate the salary accrual voucher: <em>Dr. Salary Expense (6010) / Cr. Accrued Salaries (2300)</em>.</li>
        <li>Click the green <strong>Export WPS SIF File</strong> button. The system generates the encrypted <code>.SIF</code> file for upload to corporate banking portals (e.g. ENBD, ADCB, FAB).</li>
      </ol>

      <h2>CBUAE Wages Protection System (WPS) Validation Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">WPS File Parameter</th>
            <th style="width: 35%;">Central Bank Format Standard</th>
            <th style="width: 40%;">System Verification Safeguard</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Employer ID / MOL Code</td>
            <td>13-digit corporate establishment number.</td>
            <td>Auto-populated from Legal Entity settings; verified against MOHRE.</td>
          </tr>
          <tr>
            <td class="col-field">Bank Routing Code</td>
            <td>9-digit CBUAE clearing code for paying bank.</td>
            <td>Linked to disbursing corporate bank account in Banking Master.</td>
          </tr>
          <tr>
            <td class="col-field">Salary Disbursement Date</td>
            <td>File creation date must precede payment date by &le; 14 days.</td>
            <td>Prevents late submission penalties under Ministerial Decree No. 43.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">WPS COMPLIANCE DEADLINE</div>
        Under UAE Ministry of Human Resources & Emiratisation (MOHRE) regulations, private sector salaries must be transferred through an approved WPS agent within 15 days of the month-end date to maintain statutory corporate compliance.
      </div>
    </div>
    """

def get_page_19():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Reports/01_Financial_Reports.png",
        "Financial Reports Workspace with Interactive Statements and Sub-Ledger Drill-Down",
        "/reports/financials",
        [
            ("Report Type Selector", "Select between Balance Sheet, Profit & Loss (P&L), Trial Balance, and Cash Flow Statement."),
            ("Entity & Comparative Filter", "Filter by Legal Entity, Branch, and set comparative periods (Prior Month or Prior Year)."),
            ("Interactive Account Tree", "Clickable account rows that expand to show sub-accounts and underlying journal vouchers."),
            ("Export Actions Bar", "One-click export of verified financial statements to publication-grade PDF or structured Excel.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">REPORTS & INTELLIGENCE · FINANCIAL STATEMENTS</div>
          <div class="chapter-title">Financial Reports (P&L, Balance Sheet, Trial Balance)</div>
        </div>
        <div class="chapter-right-meta">MODULE 15<br>/reports/financials</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Reports ➔ Financial Statements
      </div>

      <p>
        The Financial Reports module delivers comprehensive statutory and managerial financial statements compliant with IFRS standards. All statements feature real-time sub-ledger drill-down, multi-currency reporting, and multi-entity consolidation.
      </p>

      {wf}

      <h2>Standard Financial Reports Master Directory</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Financial Statement</th>
            <th style="width: 36%;">Accounting Framework & Content</th>
            <th style="width: 40%;">Primary Operational Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Profit & Loss (P&L)</td>
            <td>Revenue (4000), COGS (5000), and Operating Expenses (6000).</td>
            <td>Measures commercial performance, gross margin, operating profit, and net profit for any selected period.</td>
          </tr>
          <tr>
            <td class="col-field">Balance Sheet</td>
            <td>Assets (1000), Liabilities (2000), and Shareholders' Equity (3000).</td>
            <td>Presents financial position at a specific point in time; verifies <em>Assets = Liabilities + Equity</em>.</td>
          </tr>
          <tr>
            <td class="col-field">Trial Balance (TB)</td>
            <td>Complete listing of all active COA accounts with debit and credit totals.</td>
            <td>Used by accountants for month-end reconciliation to verify that total debits equal total credits.</td>
          </tr>
          <tr>
            <td class="col-field">Cash Flow Statement</td>
            <td>Operating activities, investing activities, and financing activities.</td>
            <td>Tracks actual physical cash inflows and outflows across corporate bank accounts and petty cash.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Generating and Exporting Financial Statements</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Reports ➔ Financial Statements</strong>.</li>
        <li>In the top report bar, click the tab for the statement you require (e.g. <strong>Profit & Loss</strong>).</li>
        <li>Select the reporting <strong>Legal Entity</strong> (or choose <em>All Entities</em> for consolidated group results).</li>
        <li>Set the target <strong>Date Range</strong> (e.g. <em>Current Fiscal Year YTD</em> or <em>Q3 2026</em>).</li>
        <li>Enable <strong>Comparative Period</strong> if you wish to display variance columns against the prior period or prior year.</li>
        <li>Click directly on any account row with an underline (e.g. <code>4000 Commercial Sales</code>) to drill down into the underlying transactions.</li>
        <li>Click <strong>Export PDF</strong> to download an official publication-grade report, or click <strong>Export Excel</strong> for data modeling.</li>
      </ol>

      <h2>Key Financial Health Indicators & Ledger Ratios</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Financial Health Metric</th>
            <th style="width: 35%;">Underlying General Ledger Formula</th>
            <th style="width: 40%;">Target Enterprise Benchmark</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Current Ratio</td>
            <td>Current Assets (1000–1400) / Current Liabilities (2000–2300)</td>
            <td>&gt; 1.50 (Indicates healthy short-term solvency).</td>
          </tr>
          <tr>
            <td class="col-field">Quick Ratio (Acid Test)</td>
            <td>(Cash 1010 + Receivables 1200) / Current Liabilities</td>
            <td>&gt; 1.00 (Excludes slower-moving inventory assets).</td>
          </tr>
          <tr>
            <td class="col-field">Operating Profit Margin</td>
            <td>Operating Profit (4000 - 5000 - 6000) / Total Revenue</td>
            <td>&gt; 15.0% (Measures operational efficiency).</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">CONSOLIDATION WITH INTER-COMPANY ELIMINATIONS</div>
        When selecting <em>All Entities (Consolidated)</em>, Acconeer ERP dynamically eliminates balances between Account 1950 (Due from Affiliates) and Account 2950 (Due to Affiliates) to present a true consolidated picture to corporate directors.
      </div>
    </div>
    """

def get_page_20():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/VAT_Returns/01_VAT_Filing_Dashboard.png",
        "UAE VAT Return (Form 201) Preparation Workspace with 7 Emirates Breakdown",
        "/tax/vat201",
        [
            ("Form 201 Header", "Tax Registration Number (TRN), Tax Period (e.g. 2026-Q3), and Return Due Date."),
            ("Box 1: Standard Rated Sales", "Mandatory breakdown of 5% commercial sales and VAT amount across all 7 Emirates."),
            ("Box 9: Standard Rated Expenses", "Summary of input VAT incurred on local purchases and operational expenses."),
            ("Generate EmaraTax XML", "Export official structured data file for direct submission to the UAE FTA portal.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">STATUTORY COMPLIANCE · TAXATION</div>
          <div class="chapter-title">UAE VAT Return (Form 201) Preparation</div>
        </div>
        <div class="chapter-right-meta">MODULE 16<br>/tax/vat201</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Statutory Tax ➔ VAT Return (Form 201)
      </div>

      <p>
        The VAT Return Preparation module automatically aggregates sales invoices, credit notes, supplier bills, and expense receipts into the official 14-box layout mandated by the UAE Federal Tax Authority (FTA) for quarterly Form 201 filings.
      </p>

      {wf}

      <h2>UAE VAT Form 201 Box Classification Architecture</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 14%;">Box #</th>
            <th style="width: 26%;">Statutory Box Description</th>
            <th style="width: 32%;">ERP Sub-Ledger Transaction Source</th>
            <th style="width: 28%;">Tax Rate & Calculation Basis</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Box 1</td>
            <td>Standard Rated Supplies</td>
            <td>Customer Sales Invoices categorized by branch Emirate.</td>
            <td>5% VAT calculated across each of the 7 Emirates.</td>
          </tr>
          <tr>
            <td class="col-field">Box 2</td>
            <td>Tax Refunds for Tourists</td>
            <td>Retail tax-free sales registered through Planet scheme.</td>
            <td>Amounts refunded to tourists under statutory scheme.</td>
          </tr>
          <tr>
            <td class="col-field">Box 3</td>
            <td>Supplies Subject to Reverse Charge</td>
            <td>Imported services from foreign overseas suppliers.</td>
            <td>Reverse charge accounting (Self-accounted 5%).</td>
          </tr>
          <tr>
            <td class="col-field">Box 4</td>
            <td>Zero-Rated Supplies</td>
            <td>Direct exports of goods and international logistics.</td>
            <td>0% VAT; requires export proof of exit attached.</td>
          </tr>
          <tr>
            <td class="col-field">Box 9</td>
            <td>Standard Rated Expenses</td>
            <td>Supplier bills and OpEx vouchers with verified TRNs.</td>
            <td>5% Recoverable Input VAT credited against liability.</td>
          </tr>
          <tr>
            <td class="col-field">Box 12</td>
            <td>Total Value of Due Tax</td>
            <td>Net liability: <code>Total Output VAT - Recoverable Input VAT</code>.</td>
            <td>Determines net tax payable to the FTA or refund claim.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Generating Quarterly VAT Return (Form 201)</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Statutory Tax ➔ VAT Return (Form 201)</strong>.</li>
        <li>Select the operating <strong>Legal Entity</strong> and choose the target tax quarter (e.g. <em>Q3 2026: Jul 01 – Sep 30</em>).</li>
        <li>Click <strong>Generate Return</strong>. The engine scans all posted sales and expense transactions within the date window.</li>
        <li>Inspect <strong>Box 1</strong>: verify that sales are accurately distributed across Dubai, Abu Dhabi, Sharjah, and other Emirates.</li>
        <li>Inspect <strong>Box 9</strong>: verify that all claimed input VAT is supported by valid vendor tax invoices with registered TRNs.</li>
        <li>Click <strong>Export Audit File (FAF)</strong> to generate the FTA Audit File for internal compliance review.</li>
        <li>Click the blue <strong>Download EmaraTax File</strong> button to export the finalized return for direct upload to the FTA portal.</li>
      </ol>

      <h2>Pre-Filing Tax Reconciliation & Exception Audit</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Audit Verification Step</th>
            <th style="width: 35%;">System Reconciliation Comparison</th>
            <th style="width: 40%;">Expected Balance & Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Revenue Alignment</td>
            <td>Box 1 Net Supplies vs P&L Operating Revenue (4000).</td>
            <td>Variance must equal zero or reconcile to exempt/foreign sales.</td>
          </tr>
          <tr>
            <td class="col-field">Missing Supplier TRNs</td>
            <td>System identifies bills claiming 5% VAT without verified TRN.</td>
            <td>Input tax is automatically blocked until supplier TRN is provided.</td>
          </tr>
          <tr>
            <td class="col-field">Customs Import VAT</td>
            <td>Reconcile FTA auto-populated Box 6 against Customs declarations.</td>
            <td>Match Port/Airway bill numbers against customs import documents.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">DRILL-DOWN TRANSACTION AUDIT</div>
        Clicking on any figure inside Box 1 through Box 12 opens the underlying transaction list showing invoice numbers, customer names, TRNs, net taxable values, and VAT amounts for rapid pre-filing auditing.
      </div>
    </div>
    """

def get_page_21():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/focused/mod11_vat_returns.png",
        "VAT Period Settlement Workspace with Clearing Journal and Payment Confirmation",
        "/tax/settlement",
        [
            ("Settlement Period Selector", "Select target tax quarter to close, view total output liability, and input deductions."),
            ("Net Tax Settlement Summary", "Calculates net tax payable to the FTA or net refundable tax credit in AED."),
            ("Post Settlement Journal", "Generates balanced journal entry clearing Input and Output VAT into Net VAT Payable (2250)."),
            ("Record Tax Payment", "Logs electronic tax payment reference (GIBAN / e-Dirham) and clears VAT Payable.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">STATUTORY COMPLIANCE · TAXATION</div>
          <div class="chapter-title">VAT Settlement Posting & Period Closure</div>
        </div>
        <div class="chapter-right-meta">MODULE 17<br>/tax/settlement</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Statutory Tax ➔ VAT Settlement
      </div>

      <p>
        The VAT Settlement module closes the statutory tax period in the general ledger. It automates the transfer of cumulative balances from Output VAT (Account 2200) and Input VAT (Account 1250) into Net VAT Payable (Account 2250), locking the quarter against retroactive edits.
      </p>

      {wf}

      <h2>VAT Settlement Journal Voucher Architecture</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Accounting Step</th>
            <th style="width: 35%;">General Ledger Account & Action</th>
            <th style="width: 40%;">Accounting Purpose & Balancing Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">1. Clear Output VAT</td>
            <td><strong>Debit Account 2200 (Output VAT)</strong></td>
            <td>Removes cumulative 5% sales tax liability collected from clients during the quarter.</td>
          </tr>
          <tr>
            <td class="col-field">2. Clear Input VAT</td>
            <td><strong>Credit Account 1250 (Input VAT)</strong></td>
            <td>Clears recoverable 5% purchase tax incurred on verified supplier bills.</td>
          </tr>
          <tr>
            <td class="col-field">3. Establish Net Liability</td>
            <td><strong>Credit Account 2250 (Net VAT Payable)</strong></td>
            <td>Records the net tax payable to the Federal Tax Authority (or Debit if in refund position).</td>
          </tr>
          <tr>
            <td class="col-field">4. Record FTA Payment</td>
            <td><strong>Debit 2250 / Credit 1010 (Bank Account)</strong></td>
            <td>Clears Net VAT Payable upon electronic transfer through corporate bank GIBAN payment.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Closing Tax Quarter & Posting Settlement</h2>
      <ol class="step-list">
        <li>Following successful submission of Form 201 on the FTA EmaraTax portal, open <strong>Statutory Tax ➔ VAT Settlement</strong>.</li>
        <li>Select the closed <strong>Tax Period</strong> (e.g. <em>Q3 2026</em>). Verify that the Net Tax Payable matches the EmaraTax receipt exactly.</li>
        <li>Click the blue <strong>Post Settlement Journal</strong> button. The system generates and posts the clearing voucher.</li>
        <li>Once payment is remitted to the FTA via your corporate bank GIBAN, click <strong>Record Tax Payment</strong>.</li>
        <li>Select the paying corporate <strong>Bank Account</strong>, enter the payment date, and type the official <strong>FTA Payment Reference Number</strong>.</li>
        <li>Click <strong>Save Payment & Lock Tax Period</strong>. The system locks all transactions in Q3 against retroactive modifications.</li>
      </ol>

      <h2>Handling Tax Credits, Refunds & Voluntary Disclosures</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Tax Event Scenario</th>
            <th style="width: 35%;">System Accounting Behavior</th>
            <th style="width: 40%;">Corporate Operator Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Net Tax Refund Position</td>
            <td>Input VAT exceeds Output VAT; Account 2250 carries Debit.</td>
            <td>Select <em>Carry Forward to Next Period</em> or submit FTA cash refund claim.</td>
          </tr>
          <tr>
            <td class="col-field">Voluntary Disclosure (Form 211)</td>
            <td>Error discovered in historical closed tax period (&gt; 10,000 AED).</td>
            <td>Generate Form 211 adjustment voucher; system posts penalty accrual (6450).</td>
          </tr>
          <tr>
            <td class="col-field">GIBAN Payment Allocation</td>
            <td>FTA GIBAN unique virtual account number credited via wire.</td>
            <td>Attach bank debit confirmation advice to tax payment settlement record.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">PERIOD LOCKING SAFEGUARD</div>
        Once a VAT settlement is posted and locked, Acconeer ERP strictly prohibits creating, editing, or deleting invoices, bills, or journals with posting dates inside that closed quarter. Any subsequent adjustments must be processed as prior-period corrections in the active open quarter.
      </div>
    </div>
    """

def get_page_22():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Document_Vault/01_Vault_Registry.png",
        "Document Vault Digital Repository with Category Tagging and Expiry Alerts",
        "/documents/vault",
        [
            ("Document Repository Table", "Directory of archived corporate files with Document Name, Entity, Category, and Size."),
            ("+ Upload Document", "Primary action trigger to upload digital files with metadata and access permissions."),
            ("Category Navigation", "Filter files by Trade Licenses, Contracts, Tax Certificates, Bank Letters, and Tenancy."),
            ("Expiry Date Tracking", "Monitors official expiration dates and flags items requiring renewal within 30 days.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GOVERNANCE & ASSETS · DOCUMENT MANAGEMENT</div>
          <div class="chapter-title">Document Vault & Digital File Management</div>
        </div>
        <div class="chapter-right-meta">MODULE 18<br>/documents/vault</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Document Vault (or via transaction attachments)
      </div>

      <p>
        The Document Vault provides an encrypted, centralized digital repository for all commercial, corporate, and statutory documentation in Acconeer ERP. It links digital assets directly to financial vouchers, vendor profiles, and audit packages.
      </p>

      {wf}

      <h2>Document Categories & Access Classification Framework</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Document Category</th>
            <th style="width: 36%;">Representative Corporate Assets</th>
            <th style="width: 40%;">Authorized Access Roles & Privacy Level</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Corporate Licenses</td>
            <td>Department of Economy & Tourism (DET) Commercial Licenses, MOA.</td>
            <td>Executive, CFO, Legal Counsel (Confidential).</td>
          </tr>
          <tr>
            <td class="col-field">Tax & Statutory</td>
            <td>FTA Tax Registration Certificates, VAT Return Receipts, FAF bundles.</td>
            <td>Finance Directors, Tax Accountants, External Auditors.</td>
          </tr>
          <tr>
            <td class="col-field">Commercial Contracts</td>
            <td>Customer Master Agreements, Vendor Supply Contracts, NDAs.</td>
            <td>Commercial Managers, Sales Directors, Procurement Staff.</td>
          </tr>
          <tr>
            <td class="col-field">Banking & Treasury</td>
            <td>Bank Mandates, Account Confirmation Letters, Board Resolutions.</td>
            <td>Chief Financial Officer, Treasury Managers (Strict Privacy).</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Uploading and Tagging Documents</h2>
      <ol class="step-list">
        <li>Navigate to the <strong>Document Vault</strong> workspace from the sidebar menu.</li>
        <li>Click the blue <strong>+ Upload Document</strong> button located at the top-right.</li>
        <li>Drag and drop the digital file (PDF, PNG, JPG, or XLSX) into the upload target area.</li>
        <li>Enter a clear descriptive <strong>Document Title</strong> (e.g. <em>2026 Dubai Commercial Trade License</em>).</li>
        <li>Select the operating <strong>Legal Entity</strong> and assign the appropriate <strong>Category</strong>.</li>
        <li>If the document carries an official expiration date, check <strong>Set Expiry Date</strong> and select the date.</li>
        <li>Select the <strong>Access Permission Tier</strong> to govern which user roles are permitted to view or download the file.</li>
        <li>Click <strong>Upload & Encrypt</strong>. The file is saved with SHA-256 integrity verification.</li>
      </ol>

      <h2>Document Retention Policies & Automated Expiry Alerts</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Document Classification</th>
            <th style="width: 35%;">Statutory Retention Standard</th>
            <th style="width: 40%;">System Notification Cadence</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Commercial Trade License</td>
            <td>Renewed annually; previous versions archived permanently.</td>
            <td>Amber alert at 60 days, 30 days, and 7 days prior to expiry.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Invoices & Vouchers</td>
            <td>Mandatory 5-year retention under UAE Federal Tax Law.</td>
            <td>System locks deletion; files protected against accidental purge.</td>
          </tr>
          <tr>
            <td class="col-field">Employee Passports & Visas</td>
            <td>Duration of employment + 2 years post-cancellation.</td>
            <td>Automatic notification dispatched to HR Manager and employee email.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">UNIVERSAL TRANSACTION ATTACHMENTS</div>
        Documents can also be uploaded directly inside any sales invoice, supplier bill, or manual journal entry. Files uploaded to vouchers automatically populate in the Document Vault under the respective financial category.
      </div>
    </div>
    """

def get_page_23():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Audit_Trail/01_Security_Audit_Logs.png",
        "System Audit Trail Register with Field-Level Change Logs and User Tracking",
        "/audit/logs",
        [
            ("Audit Log Table", "Complete chronological log of system events: Timestamp, User, Module, Action, and IP Address."),
            ("Action Type Filters", "Filter events by CREATE, UPDATE, POST, REVERSE, DELETE, or LOGIN_ATTEMPT."),
            ("Field-Level Diff Viewer", "Inspect exact pre-change and post-change values for modified master records or vouchers."),
            ("Export Audit Bundle", "Download cryptographically signed audit log extract for internal or external auditors.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GOVERNANCE & CONTROLS · SYSTEM INTEGRITY</div>
          <div class="chapter-title">Audit Trail Logging & Compliance Inspections</div>
        </div>
        <div class="chapter-right-meta">MODULE 19<br>/audit/logs</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Governance & Audit ➔ Audit Trail
      </div>

      <p>
        The Audit Trail module provides immutable, tamper-evident logging of every user transaction, master data modification, security event, and authentication attempt in Acconeer ERP. It satisfies external auditor and statutory governance mandates.
      </p>

      {wf}

      <h2>Audit Event Classifications & Monitored Operations</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Action Event</th>
            <th style="width: 40%;">Monitored System Operations</th>
            <th style="width: 40%;">Captured Metadata & Forensic Information</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">CREATE</td>
            <td>New invoice creation, bill origination, employee onboarding, SKU setup.</td>
            <td>User ID, timestamp, entity ID, assigned record number, initial values.</td>
          </tr>
          <tr>
            <td class="col-field">UPDATE</td>
            <td>Editing draft invoices, updating customer credit limits, modifying COA names.</td>
            <td>Field-level diff: exact previous value versus new updated value.</td>
          </tr>
          <tr>
            <td class="col-field">POST</td>
            <td>Committing draft vouchers to the general ledger; period settlements.</td>
            <td>Voucher ID, balanced debit/credit totals, posting timestamp.</td>
          </tr>
          <tr>
            <td class="col-field">REVERSE</td>
            <td>Executing offsetting reversal of a posted journal voucher.</td>
            <td>Original voucher ID, reason code, authorized manager ID.</td>
          </tr>
          <tr>
            <td class="col-field">AUTH_EVENT</td>
            <td>User logins, failed password attempts, multi-factor authentication (MFA).</td>
            <td>Source IP address, browser user-agent, session ID, pass/fail result.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Inspecting User Actions and Exporting Audit Logs</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Governance & Audit ➔ Audit Trail</strong> (restricted to Chief Auditor & CFO).</li>
        <li>To investigate a specific document, enter the document number (e.g. <code>INV-2026-0042</code>) in the Search Filter.</li>
        <li>To review changes by an operator, select the <strong>User Name</strong> from the user dropdown.</li>
        <li>Click on any log entry row to open the <strong>Detailed Change Inspector</strong> modal.</li>
        <li>Review the side-by-side diff comparison displaying the previous value in red and the updated value in green.</li>
        <li>To prepare records for external compliance review, click the blue <strong>Export Audit Bundle</strong> button to generate an encrypted, tamper-evident log extract.</li>
      </ol>

      <h2>Security Incident Forensics & Automated Alerts</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Forensic Alert Trigger</th>
            <th style="width: 35%;">Threshold Condition</th>
            <th style="width: 40%;">Automated Escalation Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Repeated Failed Logins</td>
            <td>&gt; 5 failed password attempts within 10 minutes.</td>
            <td>Locks user account temporarily; dispatches security alert to IT Admin.</td>
          </tr>
          <tr>
            <td class="col-field">High-Value Journal Posting</td>
            <td>Manual JV exceeding AED 250,000 threshold.</td>
            <td>Dispatches immediate notification to Chief Financial Officer email.</td>
          </tr>
          <tr>
            <td class="col-field">Vendor Bank IBAN Alteration</td>
            <td>Any change to supplier bank coordinates.</td>
            <td>Freezes payment run capabilities for vendor pending dual authorization.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">IMMUTABLE DATABASE LOGGING</div>
        Audit trail tables in Acconeer ERP are write-only. System administrators and database engineers cannot alter, truncate, or delete historical audit entries, ensuring absolute legal integrity for court or regulatory proceedings.
      </div>
    </div>
    """

def get_page_24():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Budgeting/01_Budgeting_Matrix.png",
        "Departmental Budget Management Workspace with Real-Time Variance Tracking",
        "/budgeting/master",
        [
            ("Budget Overview Matrix", "Annual and quarterly budgets categorized by Cost Center, Account, and Allocated Amount."),
            ("+ Configure Budget", "Primary action trigger to establish new fiscal year departmental expenditure budgets."),
            ("Real-Time Consumption Bar", "Visual progress bars displaying Actual Spend versus Approved Budget in AED."),
            ("Variance Warning Indicators", "Automatic alert status: Normal (&lt;80%), Caution (80–100%), and Over-Budget (&gt;100%).")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GOVERNANCE & CONTROLS · FINANCIAL PLANNING</div>
          <div class="chapter-title">Budgeting & Variance Alert Controls</div>
        </div>
        <div class="chapter-right-meta">MODULE 20<br>/budgeting/master</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Budgeting & Controls ➔ Budget Master
      </div>

      <p>
        The Budgeting module enables finance executives to configure departmental expenditure limits, track real-time consumption against allocated funds, and prevent unbudgeted purchase orders through automated approval locks.
      </p>

      {wf}

      <h2>Budget Threshold Escalation Tiers & Control Behavior</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Consumption Tier</th>
            <th style="width: 18%;">Threshold Range</th>
            <th style="width: 38%;">System Operational Behavior</th>
            <th style="width: 22%;">Required Authorization</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Normal Operation</td>
            <td><code>0.0% – 79.9%</code></td>
            <td>Purchase orders and supplier bills process without restriction.</td>
            <td>Standard Department Head</td>
          </tr>
          <tr>
            <td class="col-field">Caution Alert</td>
            <td><code>80.0% – 99.9%</code></td>
            <td>System displays amber warning banner on PO creation; notifies buyer.</td>
            <td>Finance Manager Review</td>
          </tr>
          <tr>
            <td class="col-field">Hard Budget Lock</td>
            <td><code>100.0% +</code></td>
            <td>System blocks PO submission; displays <em>"Budget Exceeded"</em> error.</td>
            <td>Chief Financial Officer (CFO)</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Configuring Departmental Budgets</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Budgeting & Controls ➔ Budget Master</strong> and click <strong>+ Configure Budget</strong>.</li>
        <li>Select the fiscal year (e.g. <em>FY 2026</em>) and the target <strong>Legal Entity</strong>.</li>
        <li>Select the <strong>Branch Cost Center</strong> (e.g. <em>Logistics Department - Dubai</em>).</li>
        <li>Choose the expense accounts to govern (e.g. <code>6100 Rent</code>, <code>6200 Office Supplies</code>, <code>6300 Travel</code>).</li>
        <li>Enter the approved total annual budget and select the distribution method: <em>Equal Monthly (1/12)</em> or <em>Custom Seasonal</em>.</li>
        <li>Set the <strong>Enforcement Rule</strong> to <em>Hard Block at 100%</em> to prevent unauthorized purchases.</li>
        <li>Click <strong>Save & Activate Budget</strong>. Real-time spend tracking begins immediately across all linked accounts.</li>
      </ol>

      <h2>Mid-Year Budget Re-Allocations & CapEx Approval Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Budget Revision Action</th>
            <th style="width: 35%;">Operational Procedure in ERP</th>
            <th style="width: 40%;">System Governance & Audit Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Inter-Account Transfer</td>
            <td>Click <em>Transfer Budget</em>: move surplus travel funds to IT software.</td>
            <td>Preserves total departmental spend; updates individual line limits.</td>
          </tr>
          <tr>
            <td class="col-field">Emergency Budget Supplement</td>
            <td>Submit <em>Budget Amendment Request</em> with business justification.</td>
            <td>Requires Board/CFO approval; logs permanent amendment history.</td>
          </tr>
          <tr>
            <td class="col-field">Capital Expenditure (CapEx)</td>
            <td>Link PO to approved Fixed Asset budget line item.</td>
            <td>Ensures capital acquisitions do not consume operational expense funds.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">REAL-TIME PURCHASE ORDER VERIFICATION</div>
        When a procurement clerk creates a purchase order, Acconeer ERP instantly checks the uncommitted budget balance. If the new order causes spend to exceed 100%, the system halts the workflow and routes the request to the CFO for special budget re-allocation.
      </div>
    </div>
    """

def get_page_25():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/AI_Assistant/01_Spectrum_Zestwings_AI.png",
        "AI Financial Assistant Workspace with Natural Language Querying and Draft Vouchers",
        "/ai/assistant",
        [
            ("Conversational Input Bar", "Type natural language accounting questions, variance queries, or voucher instructions."),
            ("Prompt Suggestions Drawer", "Pre-configured financial prompts for AR Aging, P&L Analysis, and Journal Drafting."),
            ("Interactive Response Cards", "Formatted responses with KPI callouts, comparative tables, and drill-down links."),
            ("Review & Post Action", "One-click review and posting of AI-drafted journal vouchers with accountant verification.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INTELLIGENCE & AUTOMATION · COPILOT</div>
          <div class="chapter-title">AI Financial Assistant & Conversational Queries</div>
        </div>
        <div class="chapter-right-meta">MODULE 21<br>/ai/assistant</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ AI Assistant (or click Sparkle icon in header)
      </div>

      <p>
        The AI Financial Assistant provides governed, natural language financial intelligence inside Acconeer ERP. Operators can query complex ledger balances, analyze gross margin variances, and draft journal vouchers using everyday conversational instructions.
      </p>

      {wf}

      <h2>High-Value Operational Prompt Templates</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Operational Intent</th>
            <th style="width: 44%;">Sample Natural Language Prompt</th>
            <th style="width: 32%;">Generated System Output</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Receivables Analysis</td>
            <td><code>"Show me all customer invoices overdue by more than 30 days in Dubai."</code></td>
            <td>Filtered AR aging table with customer names, contact info, and total overdue in AED.</td>
          </tr>
          <tr>
            <td class="col-field">Margin Performance</td>
            <td><code>"What was our gross margin variance between Q2 and Q3 for Electronics?"</code></td>
            <td>Comparative revenue, COGS, and margin breakdown with key variance drivers.</td>
          </tr>
          <tr>
            <td class="col-field">Voucher Drafting</td>
            <td><code>"Draft a monthly prepayment amortization voucher for office rent of 15,000 AED."</code></td>
            <td>Balanced draft journal entry: Dr. Rent Expense 6100 / Cr. Prepaid Rent 1300.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Inquiries</td>
            <td><code>"Summarize our current Q3 VAT liability and list any bills missing TRNs."</code></td>
            <td>Box 1–12 tax estimation and list of potential input VAT exception bills.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Using the AI Copilot to Draft a Journal Entry</h2>
      <ol class="step-list">
        <li>Click the <strong>AI Assistant</strong> icon in the universal top toolbar.</li>
        <li>Type your natural language request in the prompt input field (e.g. <em>"Draft an accrual of 12,500 AED for warehouse utilities for September"</em>).</li>
        <li>The AI Assistant analyzes your Chart of Accounts, determines the appropriate accounts (e.g. <code>6150 Utilities</code> and <code>2350 Accrued Utilities</code>), and constructs the voucher.</li>
        <li>Review the drafted entry in the verification card: inspect accounts, debit/credit balancing, and description narrative.</li>
        <li>Click <strong>Open in Journal Entry Modal</strong>. The accountant reviews the lines and makes any required adjustments.</li>
        <li>Attach supporting vendor utility bill and click <strong>Post Voucher</strong> to commit the entry to the general ledger.</li>
      </ol>

      <h2>Accountant Verification Checklist & Privacy Safeguards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Verification Check</th>
            <th style="width: 35%;">Human-in-the-Loop Audit Requirement</th>
            <th style="width: 40%;">Privacy & Security Standard</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Account Number Accuracy</td>
            <td>Confirm generated accounts exist and belong to active posting tree.</td>
            <td>Zero Model Training: financial prompts never train global public models.</td>
          </tr>
          <tr>
            <td class="col-field">Debit / Credit Equality</td>
            <td>Verify total debits exactly match total credits (AED 0.00 difference).</td>
            <td>Inference Enclave: data processed inside isolated VPC in UAE region.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Rate Conformity</td>
            <td>Confirm 5% Standard Rate is applied to applicable commercial items.</td>
            <td>Ephemeral Execution: conversation queries discarded immediately after delivery.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">HUMAN-IN-THE-LOOP GOVERNANCE</div>
        The AI Financial Assistant cannot directly post transactions to the general ledger. All AI-generated vouchers remain in draft state until an authorized accountant performs human review and executes the final posting.
      </div>
    </div>
    """

def get_page_26():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">SYSTEM APPENDIX · SUPPORT & GOVERNANCE</div>
          <div class="chapter-title">System Administration & Technical Support SLAs</div>
        </div>
        <div class="chapter-right-meta">APPENDIX<br>SUPPORT DIRECTORY</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Universal Header ➔ Help Center ➔ Enterprise Support Directory
      </div>

      <p>
        Acconeer ERP is maintained under enterprise service level agreements (SLAs) guaranteed by Spectrum Zestwings Technologies LLC. This chapter details user access management, system technical requirements, and incident escalation procedures.
      </p>

      <h2>Document Revision History & Quality Approvals</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 14%;">Revision #</th>
            <th style="width: 18%;">Release Date</th>
            <th style="width: 32%;">Scope of Documentation Updates</th>
            <th style="width: 20%;">Approved By</th>
            <th style="width: 16%;">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>v1.0.0</code></td>
            <td>15 Jan 2026</td>
            <td>Initial production baseline release for UAE commercial enterprise market.</td>
            <td>Technology Director</td>
            <td>Archived</td>
          </tr>
          <tr>
            <td><code>v2.0.0</code></td>
            <td>01 Jul 2026</td>
            <td>Multi-Entity Architecture, WPS SIF export, and AI Assistant operations.</td>
            <td>Lead Systems Architect</td>
            <td>Archived</td>
          </tr>
          <tr>
            <td><code>v3.0.0</code></td>
            <td>18 Nov 2026</td>
            <td>Volume I: Universal Enterprise Standard Operations Manual.</td>
            <td>Documentation Board</td>
            <td><strong>Production</strong></td>
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
            <td>Minimum: 1366 &times; 768. Multi-column financial tables optimized for 1080p+.</td>
          </tr>
          <tr>
            <td class="col-field">Network Bandwidth</td>
            <td>Minimum 2.0 Mbps dedicated per concurrent operator</td>
            <td>HTTPS TLS 1.3 encrypted connection; latency &lt; 50ms to UAE cloud region.</td>
          </tr>
        </tbody>
      </table>

      <h2>Enterprise Technical Support Escalation Tiers</h2>
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
            <td>User login issues, password resets, role assignment, navigation assistance.</td>
            <td><code>support@sztech.ae</code></td>
            <td>&lt; 2 Business Hours</td>
          </tr>
          <tr>
            <td class="col-field">Tier 2: Financial Systems</td>
            <td>GL balancing inquiries, VAT Form 201 mapping, WPS SIF export file validation.</td>
            <td><code>finance-support@sztech.ae</code></td>
            <td>&lt; 1 Hour (Priority)</td>
          </tr>
          <tr>
            <td class="col-field">Tier 3: Cloud Operations</td>
            <td>System availability, database failover, security events, disaster recovery.</td>
            <td><code>ops@sztech.ae</code></td>
            <td>&lt; 15 Minutes (24/7/365)</td>
          </tr>
        </tbody>
      </table>

      <h2>Incident Severity Classification & Response Cadence</h2>
      <div class="grid-2col">
        <div>
          <h3>Severity 1: Critical (System Outage)</h3>
          <p>
            Core application inaccessible or unable to process transactions. Response within <strong>15 minutes</strong> with 24/7 executive bridge and continuous engineering engagement.
          </p>
        </div>
        <div>
          <h3>Severity 2: High (Feature Degraded)</h3>
          <p>
            Key operational capability impacted (e.g. VAT export or WPS payroll) without immediate workaround. Response within <strong>1 hour</strong> during standard business hours.
          </p>
        </div>
      </div>

      <h2>Disaster Recovery, Automated Backups & System Continuity</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Continuity Element</th>
            <th style="width: 35%;">Architecture Specification</th>
            <th style="width: 40%;">Operational Guarantee</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Automated Database Backups</td>
            <td>Continuous write-ahead log (WAL) archiving + daily snapshots.</td>
            <td>Point-in-time recovery (PITR) with maximum 15-minute RPO.</td>
          </tr>
          <tr>
            <td class="col-field">Multi-Region Redundancy</td>
            <td>Active-passive replication across UAE cloud data centers.</td>
            <td>Automated failover execution with target RTO &lt; 30 minutes.</td>
          </tr>
          <tr>
            <td class="col-field">Data Encryption at Rest</td>
            <td>AES-256 encrypted database volumes and digital vault storage.</td>
            <td>In-country UAE residency; compliant with Federal Law No. 47.</td>
          </tr>
        </tbody>
      </table>

      <h2>Scheduled Maintenance Windows & Infrastructure Monitoring</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Service Dimension</th>
            <th style="width: 35%;">Standard Operating Schedule</th>
            <th style="width: 40%;">Customer Communication Channel</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Routine Maintenance</td>
            <td>Saturdays 02:00 – 04:00 GST (bi-weekly patch window).</td>
            <td>Advanced notification banner posted in ERP header 48 hours prior.</td>
          </tr>
          <tr>
            <td class="col-field">Real-Time Status Portal</td>
            <td>Continuous telemetry at <code>status.sztech.ae</code>.</td>
            <td>Live incident dashboard tracking API, database, and background jobs.</td>
          </tr>
          <tr>
            <td class="col-field">Backup Verification</td>
            <td>Automated daily test restoration in isolated sandbox.</td>
            <td>Quarterly disaster recovery audit report provided to enterprise clients.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">SPECTRUM ZESTWINGS TECHNOLOGIES LLC — ENTERPRISE ASSURANCE</div>
        For corporate inquiries, custom addenda, or on-site operational training, contact the Enterprise Support Desk at <code>support@sztech.ae</code> or visit the developer portal at <code>www.sztech.ae</code>.
      </div>
    </div>
    """

if __name__ == "__main__":
    print("Pages 17-26 module updated successfully.")

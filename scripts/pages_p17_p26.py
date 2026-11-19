# scripts/pages_p17_p26.py
from generate_complete_manual import window_frame

def get_page_17():
    wf = window_frame(
        "images/02_Employee_Directory.png",
        "Employee Master Directory with Workforce Profiles and Department Taxonomy",
        "/hr/employees",
        [
            ("Top Actions", "Export Employee Master and + Onboard Employee action buttons."),
            ("Department Filters", "Filter workforce by Executive, Finance, Operations, Logistics, or Warehouse."),
            ("Search Input", "Real-time search by employee ID, legal name, designation, or national identity."),
            ("Workforce Grid", "Columns for Employee ID, Name, Job Title, Department, Visa/EID Expiry, Salary, Status, Actions.")
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
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ HR ➔ Employee Directory
      </div>

      <p>
        The Employee Master Directory provides centralized workforce governance in Acconeer ERP. It maintains statutory employee profiles, employment contract terms, personal UAE banking coordinates, and document expiration dates in compliance with UAE Labour regulations.
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
            <td class="col-field">+ Onboard Employee</td>
            <td>Solid Purple Button</td>
            <td>Opens employee registration modal to record personal data, contract dates, salary, and UAE IBAN.</td>
          </tr>
          <tr>
            <td class="col-field">Export Master</td>
            <td>Export Button</td>
            <td>Exports complete workforce roster and compliance status to Excel spreadsheet or formatted PDF.</td>
          </tr>
          <tr>
            <td class="col-field">Department Filter</td>
            <td>Dropdown Filter</td>
            <td>Filters directory by organizational department: Management, Finance, Sales, Logistics, Engineering.</td>
          </tr>
          <tr>
            <td class="col-field">Search Input Bar</td>
            <td>Text Field</td>
            <td>Real-time search across employee legal names, internal staff codes, and Emirates ID numbers.</td>
          </tr>
        </tbody>
      </table>

      <h2>Employee Directory Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 60%;">On-Screen Information & Operational Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Employee ID</td>
            <td>Sequential Code</td>
            <td>Unique employee personnel code (e.g. <code>EMP-2026-0012</code>); links to complete personnel profile.</td>
          </tr>
          <tr>
            <td class="col-field">Full Legal Name</td>
            <td>Text (Passport Match)</td>
            <td>Full legal name matching Emirates ID and MOHRE statutory employment contract.</td>
          </tr>
          <tr>
            <td class="col-field">Designation & Dept</td>
            <td>Role & Department</td>
            <td>Corporate job title and organizational department cost-center mapping.</td>
          </tr>
          <tr>
            <td class="col-field">Visa & EID Expiry</td>
            <td>Date & Expiry Alert</td>
            <td>Statutory expiration dates with visual alerts when renewals are required within 30 days.</td>
          </tr>
          <tr>
            <td class="col-field">Basic Salary & IBAN</td>
            <td>Currency & Account</td>
            <td>Contractual basic salary in AED and verified 23-character UAE IBAN for payroll routing.</td>
          </tr>
          <tr>
            <td class="col-field">Status & Actions</td>
            <td>Badge & Actions</td>
            <td>Employment status (<code>Active</code>, <code>On Leave</code>) and menu triggers to Edit Profile or View Payroll.</td>
          </tr>
        </tbody>
      </table>

      <h2>Document Expiry Alert Windows & Compliance Status</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Expiry Window</th>
            <th style="width: 28%;">Visual Status Indicator</th>
            <th style="width: 50%;">Statutory Obligation & HR Action Required</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">&gt; 60 Days Remaining</td>
            <td><code>Valid / Current</code> (Green)</td>
            <td>Compliance in good standing; no immediate action needed.</td>
          </tr>
          <tr>
            <td class="col-field">30 – 60 Days</td>
            <td><code>Expiring Soon</code> (Amber)</td>
            <td>Early reminder; initiate medical test and immigration renewal papers.</td>
          </tr>
          <tr>
            <td class="col-field">&lt; 30 Days</td>
            <td><code>Urgent Expiry</code> (Red)</td>
            <td>Mandatory renewal trigger; dashboard alert dispatched to HR Manager.</td>
          </tr>
          <tr>
            <td class="col-field">Expired / Overdue</td>
            <td><code>Statutory Violation</code> (Black)</td>
            <td>Late fines apply; system blocks employee from standard WPS payroll batch.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">WPS SIF COMPLIANCE VALIDATION</div>
        All onboarded employees must have a verified 14-digit MOHRE Labour Card number and a valid 23-character UAE IBAN registered to enable automated inclusion in monthly Wages Protection System (WPS) payment batches.
      </div>
    </div>
    """

def get_page_18():
    wf = window_frame(
        "images/07_Payroll.png",
        "Monthly Payroll Processing Engine with Timesheet Locking and WPS SIF Export",
        "/hr/payroll",
        [
            ("Payroll Batch Header", "Current payroll month (e.g. September 2026), head count, and gross payroll total."),
            ("Run Payroll Batch", "Primary action trigger to execute automated salary, allowance, and deduction calculations."),
            ("WPS SIF Export Trigger", "Generates encrypted CBUAE-compliant Salary Information File for bank upload."),
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
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ HR ➔ Payroll
      </div>

      <p>
        The Payroll Processing Engine automates monthly compensation runs, attendance and overtime calculations, statutory UAE Wages Protection System (WPS) SIF file generation, and synchronous General Ledger wage expense postings.
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
            <td class="col-field">Run Payroll Batch</td>
            <td>Solid Purple Button</td>
            <td>Calculates monthly basic pay, contractual allowances, unpaid leave deductions, and net wage totals.</td>
          </tr>
          <tr>
            <td class="col-field">Export WPS SIF</td>
            <td>Solid Green Button</td>
            <td>Generates official Central Bank of UAE compliant Salary Information File (<code>.SIF</code>) for corporate bank upload.</td>
          </tr>
          <tr>
            <td class="col-field">Post Salary Journal</td>
            <td>Solid Blue Button</td>
            <td>Writes balanced wage accrual voucher to General Ledger: debits salary expense and credits payroll clearing.</td>
          </tr>
          <tr>
            <td class="col-field">Lock Pay Period</td>
            <td>Outline Button</td>
            <td>Locks attendance timesheets and wage calculations, preventing further payroll modifications for that month.</td>
          </tr>
        </tbody>
      </table>

      <h2>Payroll Batch Summary Telemetry Cards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Telemetry Card</th>
            <th style="width: 18%;">Display Value</th>
            <th style="width: 58%;">Calculation Source & Operational Meaning on Screen</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">GROSS PAYROLL</td>
            <td><code>AED 0.00</code></td>
            <td>Cumulative contractual basic salaries plus fixed housing and transport allowances across all active staff.</td>
          </tr>
          <tr>
            <td class="col-field">TOTAL DEDUCTIONS</td>
            <td><code>AED 0.00</code></td>
            <td>Unpaid leave deductions, salary advances, and disciplinary withholdings calculated by the engine.</td>
          </tr>
          <tr>
            <td class="col-field">NET PAYABLE (WPS)</td>
            <td><code>AED 0.00</code></td>
            <td>Net monetary amount disbursed to employees via corporate bank WPS routing file.</td>
          </tr>
          <tr>
            <td class="col-field">WPS VALIDATION</td>
            <td><code>100% Passed</code></td>
            <td>Automated pre-flight check confirming all employee records hold valid MOHRE IDs and UAE IBANs.</td>
          </tr>
        </tbody>
      </table>

      <h2>Payroll Register Grid Columns & Actions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 60%;">On-Screen Information & Operational Function</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Emp ID & Name</td>
            <td>Code & Legal Name</td>
            <td>Personnel code and employee full name linked to HR master profile.</td>
          </tr>
          <tr>
            <td class="col-field">Basic Salary</td>
            <td>Contract Currency</td>
            <td>MOHRE registered contractual monthly basic wage in AED.</td>
          </tr>
          <tr>
            <td class="col-field">Fixed Allowances</td>
            <td>Itemized Breakdown</td>
            <td>Contractual housing, utility, and transport allowances.</td>
          </tr>
          <tr>
            <td class="col-field">Net Salary (AED)</td>
            <td>Disbursement Total</td>
            <td>Final net monthly pay after adding overtime and subtracting authorized deductions.</td>
          </tr>
          <tr>
            <td class="col-field">WPS Status & Actions</td>
            <td>Badge & Menu</td>
            <td>WPS routing compliance badge and options to <em>Download Payslip (PDF)</em> or <em>Adjust Deductions</em>.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_19():
    wf = window_frame(
        "images/01_Financial_Reports.png",
        "Financial Statements & Executive Reporting Suite with Analytical Ratios",
        "/reports/financials",
        [
            ("Top Actions", "Print, Export Excel, and Export PDF action buttons."),
            ("Reporting Period Filters", "Entity scope, quick period pills (All time, YTD, This month, Q1-Q4), and Hide zero lines toggle."),
            ("4 Executive KPI Cards", "Top-Line Operating Revenue, EBITDA, Total Balance Sheet Assets, Accounting Equation Equilibrium."),
            ("Report Navigation Tabs", "D3 Visual Analytics, Profit & Loss (P&L), Balance Sheet, Trial Balance, General Ledger.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">FINANCIAL INTELLIGENCE · STATUTORY REPORTS</div>
          <div class="chapter-title">Financial Statements & Reporting Suite</div>
        </div>
        <div class="chapter-right-meta">MODULE 15<br>/reports/financials</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Reports ➔ Financial Statements
      </div>

      <p>
        The Financial Statements & Reporting Suite generates real-time statutory financial statements directly from posted General Ledger vouchers, providing interactive drilldown into account balances, period-over-period variance analysis, and multi-format exports.
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
            <td class="col-field">Print</td>
            <td>White Border Button</td>
            <td>Formats active financial statement for professional physical printing or PDF printer spooling.</td>
          </tr>
          <tr>
            <td class="col-field">Export Excel</td>
            <td>Solid Green Button</td>
            <td>Exports active financial statement to multi-tab spreadsheet with intact formula calculations.</td>
          </tr>
          <tr>
            <td class="col-field">Export PDF</td>
            <td>Solid Purple Button</td>
            <td>Generates official publication-grade audited financial statement PDF document.</td>
          </tr>
          <tr>
            <td class="col-field">Period Pills</td>
            <td>Filter Buttons</td>
            <td>Instant period selection: <code>All time</code>, <code>YTD</code>, <code>This month</code>, <code>Q1</code>, <code>Q2</code>, <code>Q3</code>, <code>Q4</code>, <code>Custom</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Hide Zero Lines</td>
            <td>Checkbox (Checked)</td>
            <td>Toggles suppression of inactive accounts with zero balances for clean statement presentation.</td>
          </tr>
        </tbody>
      </table>

      <h2>On-Screen Metric & Telemetry Cards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 26%;">Metric Card</th>
            <th style="width: 18%;">Display Value</th>
            <th style="width: 56%;">Calculation Source & Operational Meaning on Screen</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Top-Line Revenue</td>
            <td><code>AED 0.00</code></td>
            <td>Gross operational turnover from commercial sales; displays real-time <em>Gross Margin: 0.0%</em>.</td>
          </tr>
          <tr>
            <td class="col-field">EBITDA</td>
            <td><code>AED 0.00</code></td>
            <td>Earnings before interest, taxes, depreciation, and amortization computed dynamically from GL.</td>
          </tr>
          <tr>
            <td class="col-field">Total Assets</td>
            <td><code>AED 0.00</code></td>
            <td>Total balance sheet carrying value across current, fixed, and liquid cash assets.</td>
          </tr>
          <tr>
            <td class="col-field">Equation Equilibrium</td>
            <td><code>Assets = Liab + Eq</code></td>
            <td>Green checkmark verification confirming double-entry accounting integrity holds across all ledgers.</td>
          </tr>
        </tbody>
      </table>

      <h2>Report Statement Tabs & Visual Analytics</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Report Tab</th>
            <th style="width: 35%;">Statement Scope</th>
            <th style="width: 40%;">On-Screen Analytical Content</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Profit & Loss (P&L)</td>
            <td>Revenues, COGS, Gross Profit, Operating Expenses, Net Income.</td>
            <td>Income statement detailing operational profitability over the selected fiscal period.</td>
          </tr>
          <tr>
            <td class="col-field">Balance Sheet</td>
            <td>Assets (1000s), Liabilities (2000s), Shareholders' Equity (3000s).</td>
            <td>Statement of financial position showing enterprise net worth at period close.</td>
          </tr>
          <tr>
            <td class="col-field">Trial Balance</td>
            <td>Complete listing of all active Chart of Accounts ledgers.</td>
            <td>Auditor trial balance verifying Total Debits equal Total Credits across all accounts.</td>
          </tr>
          <tr>
            <td class="col-field">General Ledger</td>
            <td>Transaction book grouped by account code.</td>
            <td>Detailed chronological journal postings supporting every balance sheet line item.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_20():
    wf = window_frame(
        "images/01_VAT_Filing_Dashboard.png",
        "UAE VAT Return (Form VAT 201) Preparation Workspace & FTA Compliance",
        "/tax/vat201",
        [
            ("Top Action Buttons", "CSV, Excel, PDF, and + Create VAT Return action buttons."),
            ("4 VAT Metric Cards", "Gross Output Tax (Box 8), Recoverable Input Tax (Box 11), Net VAT Payable (Box 14), FTA Filing Status."),
            ("View Tabs", "VAT Returns Register (Form 201) and FTA Compliance & Tax Rates Guide tabs."),
            ("Returns Data Grid", "8-column table tracking Return Reference, Period, Due Date, Outputs, Box 8, Box 11, Box 14, Status, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">STATUTORY COMPLIANCE · TAXATION</div>
          <div class="chapter-title">UAE VAT Return (Form VAT 201) Preparation</div>
        </div>
        <div class="chapter-right-meta">MODULE 16<br>/tax/vat201</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ VAT Returns (or <kbd>Alt + V</kbd>)
      </div>

      <p>
        The VAT Returns workspace automatically aggregates commercial sales invoices, credit notes, supplier bills, and expenses into the official 14-box layout mandated by the UAE Federal Tax Authority (FTA) for quarterly Form VAT 201 declarations.
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
            <td class="col-field">+ Create VAT Return</td>
            <td>Solid Purple Button</td>
            <td>Initializes a new quarterly tax declaration period and scans posted ledgers for taxable supplies.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & CSV</td>
            <td>Export Buttons</td>
            <td>Exports formatted Form 201 calculation schedule and transaction-level audit worksheets.</td>
          </tr>
          <tr>
            <td class="col-field">PDF</td>
            <td>Export Button</td>
            <td>Generates official summary tax return filing report for CFO sign-off and audit archiving.</td>
          </tr>
          <tr>
            <td class="col-field">Status Filter</td>
            <td>Dropdown Filter</td>
            <td>Filters VAT return records by filing status: <code>All Statuses</code>, <code>Draft</code>, <code>Ready to File</code>, <code>Settled</code>.</td>
          </tr>
        </tbody>
      </table>

      <h2>On-Screen Metric & Telemetry Cards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 26%;">Metric Card</th>
            <th style="width: 18%;">Display Value</th>
            <th style="width: 56%;">Calculation Source & Operational Meaning on Screen</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Gross Output Tax (Box 8)</td>
            <td><code>AED 0.00</code></td>
            <td>Total 5% VAT collected across standard-rated commercial sales invoices (Account 2200).</td>
          </tr>
          <tr>
            <td class="col-field">Recoverable Input (Box 11)</td>
            <td><code>AED 0.00</code></td>
            <td>Total 5% VAT paid on allowable business purchases and imported supplies (Account 1300).</td>
          </tr>
          <tr>
            <td class="col-field">Net VAT Payable (Box 14)</td>
            <td><code>AED 0.00</code></td>
            <td>Net statutory liability payable to the FTA: <code>Box 8 minus Box 11</code> (Tax Liability Balance).</td>
          </tr>
          <tr>
            <td class="col-field">FTA Filing & GL Compliance</td>
            <td><code>0 Settled / 0 Drafts</code></td>
            <td>Audit-grade status counter indicating finalized settlements versus active working draft returns.</td>
          </tr>
        </tbody>
      </table>

      <h2>VAT Returns Register Grid Columns & Actions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 62%;">On-Screen Information & Regulatory Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Return Reference</td>
            <td>Sequential Link</td>
            <td>Filing reference (e.g. <code>VAT-2026-Q1</code>); clickable to open detailed Box 1-14 breakdown.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Period & Due Date</td>
            <td>Date Range & Deadline</td>
            <td>Reporting quarter (e.g. <em>01 Jan – 31 Mar 2026</em>) and statutory submission deadline.</td>
          </tr>
          <tr>
            <td class="col-field">Outputs & Box 8</td>
            <td>Currencies in AED</td>
            <td>Gross commercial supplies and total 5% output tax collected on standard supplies.</td>
          </tr>
          <tr>
            <td class="col-field">Input Tax (Box 11)</td>
            <td>Currency in AED</td>
            <td>Total eligible input tax deducted from purchases and operational expenses.</td>
          </tr>
          <tr>
            <td class="col-field">Net Due (Box 14)</td>
            <td>Net Liability</td>
            <td>Final net amount due for payment to the Federal Tax Authority (or tax refund balance).</td>
          </tr>
          <tr>
            <td class="col-field">Actions</td>
            <td>Context Menu</td>
            <td>Menu triggers to <em>View Form 201 Matrix</em>, <em>Download FAF Audit File</em>, or <em>Post Settlement</em>.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no returns exist in the selected view, the workspace displays: <em>"No VAT returns found matching your filter criteria. Click 'Create VAT Return' to start a new filing."</em>
      </div>
    </div>
    """

def get_page_21():
    wf = window_frame(
        "images/mod11_vat_returns.png",
        "VAT Return Form 201 Detailed Box Inspection & Settlement Workflow",
        "/tax/vat201/detail",
        [
            ("Telemetry Cards [1]", "Gross Output Tax (Box 8), Recoverable Input (Box 11), Net VAT Payable (Box 14)."),
            ("Regulatory Tabs [2]", "Toggle between VAT Returns Register (Form 201) and FTA Compliance Guide."),
            ("Search & Filter [3]", "Search by reference, period, or TRN with live lifecycle status filter."),
            ("Box-by-Box Matrix", "Detailed drilldown into standard supplies across the 7 Emirates and reverse charges.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">STATUTORY COMPLIANCE · TAX SETTLEMENT</div>
          <div class="chapter-title">VAT Return Box Breakdown & Period Settlement</div>
        </div>
        <div class="chapter-right-meta">MODULE 17<br>/tax/settlement</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ VAT Returns ➔ Return Reference Drilldown
      </div>

      <p>
        Clicking any return reference opens the Form VAT 201 Box Inspection interface. Acconeer ERP categorizes all underlying transactions into statutory FTA boxes and enables one-click generation of the balancing tax settlement journal voucher.
      </p>

      {wf}

      <h2>Form VAT 201 Box Matrix & Sub-Ledger Classification</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 14%;">Box Number</th>
            <th style="width: 26%;">Statutory Declaration Name</th>
            <th style="width: 32%;">Underlying ERP Sub-Ledger Source</th>
            <th style="width: 28%;">Calculation & Tax Treatment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Box 1 (a-g)</td>
            <td>Standard Rated Supplies</td>
            <td>Sales Invoices grouped by customer delivery Emirate.</td>
            <td>5% VAT calculated across Abu Dhabi, Dubai, Sharjah, etc.</td>
          </tr>
          <tr>
            <td class="col-field">Box 2</td>
            <td>Tourist Tax Refunds</td>
            <td>Retail tax-free sales registered under Planet scheme.</td>
            <td>Statutory tourist refund adjustments.</td>
          </tr>
          <tr>
            <td class="col-field">Box 3</td>
            <td>Supplies Under Reverse Charge</td>
            <td>Imported vendor services from international suppliers.</td>
            <td>Self-accounted 5% RCM output and input tax.</td>
          </tr>
          <tr>
            <td class="col-field">Box 4</td>
            <td>Zero-Rated Supplies</td>
            <td>Commercial exports of goods outside the GCC.</td>
            <td>0% tax; requires official customs export exit paper.</td>
          </tr>
          <tr>
            <td class="col-field">Box 9</td>
            <td>Standard Rated Expenses</td>
            <td>Supplier bills and expense vouchers with verified TRNs.</td>
            <td>5% Recoverable input tax credited against liability.</td>
          </tr>
          <tr>
            <td class="col-field">Box 14</td>
            <td>Net VAT Payable to FTA</td>
            <td>Total Output Tax (Box 8) minus Total Input Tax (Box 11).</td>
            <td>Final net settlement liability or refund claim.</td>
          </tr>
        </tbody>
      </table>

      <h2>VAT Period Settlement Journal Voucher Impact</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Accounting Entry</th>
            <th style="width: 28%;">General Ledger Account</th>
            <th style="width: 20%;">Debit / Credit</th>
            <th style="width: 30%;">Operational Ledger Result</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Clear Output VAT</td>
            <td>Account 2200 (Output VAT Payable)</td>
            <td>DEBIT</td>
            <td>Zeroes out cumulative output tax collected for the quarter.</td>
          </tr>
          <tr>
            <td class="col-field">Clear Input VAT</td>
            <td>Account 1300 (Input VAT Recoverable)</td>
            <td>CREDIT</td>
            <td>Zeroes out cumulative input tax paid on purchases.</td>
          </tr>
          <tr>
            <td class="col-field">Net Settlement</td>
            <td>Account 2210 (FTA VAT Settlement)</td>
            <td>CREDIT</td>
            <td>Records net statutory liability awaiting bank remittance.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMARATAX PORTAL SUBMISSION</div>
        Click <strong>Export EmaraTax XML</strong> from the action menu to download the official structured filing file for direct upload to the UAE Federal Tax Authority portal, ensuring 100% digital alignment with your general ledger.
      </div>
    </div>
    """

def get_page_22():
    wf = window_frame(
        "images/01_Vault_Registry.png",
        "Company Document Repository & Enterprise Governance Vault",
        "/vault",
        [
            ("Primary Action", "+ Upload Document button to store legal, corporate, or financial files."),
            ("Governance Tag", "ENTERPRISE KNOWLEDGE & GOVERNANCE classification banner."),
            ("Multi-Filter Row", "Company Legal Entity, Document Category, Status, and Search Documents input bar."),
            ("Main Repository", "Documents Repository counter and filtered display for the active legal entity.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">ENTERPRISE GOVERNANCE · DOCUMENT VAULT</div>
          <div class="chapter-title">Company Document Repository & Digital Vault</div>
        </div>
        <div class="chapter-right-meta">MODULE 18<br>/vault</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Document Vault (or press <kbd>Alt + V</kbd>)
      </div>

      <p>
        The Company Document Repository provides secure, audit-grade digital archiving for essential corporate records, including commercial trade licenses, tax certificates, corporate contracts, and statutory compliance documents.
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
            <td class="col-field">+ Upload Document</td>
            <td>Solid Purple Button</td>
            <td>Opens upload modal to drag-and-drop PDF/images, tag document category, and set expiration alerts.</td>
          </tr>
          <tr>
            <td class="col-field">Company Legal Entity</td>
            <td>Dropdown Filter</td>
            <td>Restricts document repository view to records owned by that specific corporate operating company.</td>
          </tr>
          <tr>
            <td class="col-field">Document Category</td>
            <td>Dropdown Filter</td>
            <td>Filters files by class: <em>All Categories</em>, <em>Trade Licenses</em>, <em>Tax Certificates</em>, <em>Contracts</em>, <em>Leases</em>.</td>
          </tr>
          <tr>
            <td class="col-field">Search Documents</td>
            <td>Text Field</td>
            <td>Instant real-time search across document titles, identification numbers, issuing authority, and tags.</td>
          </tr>
        </tbody>
      </table>

      <h2>Document Categories & Governance Taxonomy</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Document Category</th>
            <th style="width: 36%;">Typical Uploaded Records</th>
            <th style="width: 40%;">System Monitoring & Automated Alerts</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Corporate Licenses</td>
            <td>DED Commercial License, Chamber of Commerce, MOA.</td>
            <td>Monitors annual renewal deadline; sends 30-day expiry notifications.</td>
          </tr>
          <tr>
            <td class="col-field">Tax & VAT Certs</td>
            <td>FTA Tax Registration Certificate, Corporate Tax Filing.</td>
            <td>Linked to VAT Returns workspace for statutory audit compliance inspections.</td>
          </tr>
          <tr>
            <td class="col-field">Legal Agreements</td>
            <td>Customer master contracts, supplier agreements, NDAs.</td>
            <td>Version-controlled archive with digital audit trail of user access.</td>
          </tr>
          <tr>
            <td class="col-field">Financial Audits</td>
            <td>External auditor signed financial statements, bank mandates.</td>
            <td>Permanent read-only archive accessible to authorized directors and auditors.</td>
          </tr>
        </tbody>
      </table>

      <h2>Retention Schedules & Cryptographic Storage Policies</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Record Classification</th>
            <th style="width: 35%;">Statutory Retention Mandate</th>
            <th style="width: 40%;">Cryptographic Security & Storage Tier</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Corporate Charters & MOA</td>
            <td>Permanent Enterprise Life</td>
            <td>Immutable WORM (Write Once, Read Many) cloud object storage.</td>
          </tr>
          <tr>
            <td class="col-field">VAT & Tax Documentation</td>
            <td>7 Years (UAE FTA Law)</td>
            <td>Encrypted AES-256 with timestamped SHA-256 access integrity hash.</td>
          </tr>
          <tr>
            <td class="col-field">Commercial Customer Contracts</td>
            <td>Contract Term + 5 Years</td>
            <td>Restricted RBAC access limited to Legal and Authorized Executive roles.</td>
          </tr>
          <tr>
            <td class="col-field">Bank Mandates & Signatures</td>
            <td>Active Banking Lifetime</td>
            <td>Dual-authorization access tier requiring Finance Manager credentials.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no documents match the active filters, the repository displays: <em>"No documents found — No internal documents match the active filters. Upload legal licenses, corporate certificates, and contracts for internal team reference."</em>
      </div>
    </div>
    """

def get_page_23():
    wf = window_frame(
        "images/01_Security_Audit_Logs.png",
        "Security Audit Trail & Real-Time User Activity Log with Live Inspector",
        "/audit-trail",
        [
            ("Navigation Tabs", "Access & actions (active blue button) and System events view tabs."),
            ("Action & Filters", "Refresh button, Search user/action/path input, All categories, and All severities dropdowns."),
            ("Left Activity Grid", "Chronological table tracking WHEN (UTC timestamp), WHO, WHERE, and ACTION."),
            ("Right Inspector", "Real-time NAVIGATION inspector card detailing Path, User email, Role, Entity, and IP address.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">SECURITY & COMPLIANCE · IMMUTABLE AUDIT LOG</div>
          <div class="chapter-title">Security Audit Trail & User Activity Log</div>
        </div>
        <div class="chapter-right-meta">MODULE 19<br>/audit-trail</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Audit Trail (or press <kbd>Alt + L</kbd>)
      </div>

      <p>
        The Security Audit Trail provides an immutable, real-time activity ledger recording every authenticated user action, record modification, page navigation, and system event with cryptographic precision and originating IP telemetry.
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
            <td class="col-field">Access & actions</td>
            <td>Solid Blue Button</td>
            <td>Displays user operational interactions, page navigations, and record modifications.</td>
          </tr>
          <tr>
            <td class="col-field">System events</td>
            <td>Outline Tab Button</td>
            <td>Displays backend infrastructure events, background automated sync jobs, and security alerts.</td>
          </tr>
          <tr>
            <td class="col-field">Refresh</td>
            <td>Solid Blue Button</td>
            <td>Polls the immutable audit log and appends newly recorded transactions to the live view.</td>
          </tr>
          <tr>
            <td class="col-field">Search Input Bar</td>
            <td>Text Field</td>
            <td>Instant search across authenticated user emails, action codes, module tabs, and route paths.</td>
          </tr>
          <tr>
            <td class="col-field">Category & Severity</td>
            <td>2 Dropdown Filters</td>
            <td>Filters log entries by category (Navigation, Transaction, Security) and severity (INFO, WARN, CRITICAL).</td>
          </tr>
        </tbody>
      </table>

      <h2>Activity Log Grid & Live Inspector Fields</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Interface Field</th>
            <th style="width: 26%;">On-Screen Display Example</th>
            <th style="width: 54%;">Recorded Telemetry & Governance Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">WHEN</td>
            <td><code>2026-11-17 17:41:00 UTC</code></td>
            <td>High-precision coordinated universal time timestamp of the recorded action.</td>
          </tr>
          <tr>
            <td class="col-field">WHO</td>
            <td><code>Rondla Anvith Reddy / ORG_ADMIN</code></td>
            <td>Full user name and assigned role authorization tier.</td>
          </tr>
          <tr>
            <td class="col-field">WHERE</td>
            <td><code>Banking / Audit Trail</code></td>
            <td>ERP module workspace and sub-view where the event transpired.</td>
          </tr>
          <tr>
            <td class="col-field">ACTION</td>
            <td><code>INFO / PAGE_VIEW</code></td>
            <td>Standardized event classification code and severity tier.</td>
          </tr>
          <tr>
            <td class="col-field">Path (Inspector)</td>
            <td><code>/banking/audit-trail</code></td>
            <td>Exact URL route path accessed within the web application.</td>
          </tr>
          <tr>
            <td class="col-field">User & Email</td>
            <td><code>ops1@sztech.ae</code></td>
            <td>Verified authenticated single-sign-on corporate email address.</td>
          </tr>
          <tr>
            <td class="col-field">IP Address</td>
            <td><code>2.51.126.109</code></td>
            <td>Originating client public network IP address for cyber forensic traceability.</td>
          </tr>
        </tbody>
      </table>

      <h2>Audit Event Classification & Severity Thresholds</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Severity Code</th>
            <th style="width: 38%;">Captured Event Type</th>
            <th style="width: 42%;">Security & Compliance Escalation Protocol</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">INFO</td>
            <td>Routine navigation, page views, and read-only searches.</td>
            <td>Logged permanently for compliance; zero operational alerting.</td>
          </tr>
          <tr>
            <td class="col-field">WARN</td>
            <td>Failed login attempt, permission escalation retry, draft discard.</td>
            <td>Recorded in security telemetry; triggers review after 3 threshold events.</td>
          </tr>
          <tr>
            <td class="col-field">CRITICAL</td>
            <td>User role modification, integration API reset, period lock toggle.</td>
            <td>Instant email alert dispatched to Organization Administrator.</td>
          </tr>
        </tbody>
      </table>
    </div>
    """

def get_page_24():
    wf = window_frame(
        "images/01_Budgeting_Matrix.png",
        "Fiscal Budgeting & Variance Matrix with Real-Time GL Tracking",
        "/budgeting",
        [
            ("Top Actions", "+ New Plan button and Refresh button to pull live General Ledger actuals."),
            ("Navigation Tabs", "Budget vs. Actual Variance (active), Budget Registry (0), and Forecasts & Trends."),
            ("Plan Setup Panel", "No Budget Plan Selected working area with prompt and + Create New Plan trigger."),
            ("Variance Engine", "Compares budgeted allocations against posted operational expenses in real-time.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">FINANCIAL PLANNING · FISCAL CONTROL</div>
          <div class="chapter-title">Fiscal Budgeting & Variance Controls</div>
        </div>
        <div class="chapter-right-meta">MODULE 20<br>/budgeting</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Budgeting & Forecasts
      </div>

      <p>
        The Fiscal Budgeting & Variance workspace provides financial planning governance, enabling corporate controllers to allocate departmental expenditure budgets and monitor real-time consumption against live General Ledger postings.
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
            <td class="col-field">+ New Plan</td>
            <td>Solid Purple Button</td>
            <td>Top-right action trigger to initialize a new annual or quarterly corporate budget matrix.</td>
          </tr>
          <tr>
            <td class="col-field">+ Create New Plan</td>
            <td>Solid Purple Button</td>
            <td>Central working area trigger opening the budget planning wizard to allocate account caps.</td>
          </tr>
          <tr>
            <td class="col-field">Refresh Button</td>
            <td>Circular Arrow Icon</td>
            <td>Re-calculates actual posted expenditures from live General Ledger ledgers against budget caps.</td>
          </tr>
          <tr>
            <td class="col-field">Navigation Tabs</td>
            <td>3 Top Tabs</td>
            <td>Switch between <em>Budget vs. Actual Variance</em>, <em>Budget Registry</em>, and <em>Forecasts & Trends</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Budgeting Workspace Tabs & Analytical Views</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 28%;">Workspace Tab</th>
            <th style="width: 22%;">Active Indicator</th>
            <th style="width: 50%;">Operational Purpose & Information Displayed</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Budget vs. Actual</td>
            <td>Active Lavender Tab</td>
            <td>Side-by-side comparison of budgeted amounts versus posted actuals, displaying variance % in AED.</td>
          </tr>
          <tr>
            <td class="col-field">Budget Registry</td>
            <td>Badge Count (<code>0</code>)</td>
            <td>Complete directory of approved, active, and historical corporate budget plans.</td>
          </tr>
          <tr>
            <td class="col-field">Forecasts & Trends</td>
            <td>Trending Line Icon</td>
            <td>Visual projection modeling future cash expenditures based on historical burn rate.</td>
          </tr>
        </tbody>
      </table>

      <h2>Budget Allocation Types & Spend Lock Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Allocation Method</th>
            <th style="width: 36%;">System Enforcement Rule</th>
            <th style="width: 40%;">Operational Alerting & Purchase Order Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Hard Budget Cap</td>
            <td>Purchase orders blocked if budget is exceeded.</td>
            <td>System displays red error; requires CFO authorization to override.</td>
          </tr>
          <tr>
            <td class="col-field">Soft Advisory Cap</td>
            <td>Warns user at 80% and 100% threshold utilization.</td>
            <td>Dispatches automated warning email to department head; allows posting.</td>
          </tr>
          <tr>
            <td class="col-field">Quarterly Rolling</td>
            <td>Unused budget balances automatically roll over.</td>
            <td>Re-balances Q2/Q3/Q4 caps dynamically based on quarterly performance.</td>
          </tr>
          <tr>
            <td class="col-field">Capex Project Pool</td>
            <td>Dedicated budget allocation tied to specific Asset Tag.</td>
            <td>Enforces capital expenditure caps for machinery and fleet acquisition.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">PLAN SELECTION NOTICE</div>
        When no budget is actively loaded, the center panel displays: <em>"No Budget Plan Selected — Please create or select an active budget plan to review real-time spend variance against general ledger actuals."</em> Click <strong>+ Create New Plan</strong> to begin.
      </div>
    </div>
    """

def get_page_25():
    wf = window_frame(
        "images/01_Spectrum_Zestwings_AI.png",
        "Spectrum Zestwings AI Financial Assistant & Conversational Copilot",
        "/copilot",
        [
            ("Copilot Header", "Spectrum Zestwings AI branding, Assistant badge, active legal entity scope, and window controls."),
            ("Integration Warning", "Advisory callout noting AI credentials must be configured in Organization settings."),
            ("Chat Greeting", "Welcome message explaining assistant capabilities: ledger analysis, tax, and planning."),
            ("Quick Prompts", "One-click suggestion pills for tax obligations, Zoho Books sync, and comparisons.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INTELLIGENT AUTOMATION · COPILOT</div>
          <div class="chapter-title">AI Financial Assistant & Conversational Queries</div>
        </div>
        <div class="chapter-right-meta">MODULE 21<br>/copilot</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Click Floating Purple AI Pill at bottom-right of any workspace
      </div>

      <p>
        The Spectrum Zestwings Financial AI Assistant is an integrated conversational copilot that queries live ledger data, explains chart of accounts mappings, suggests tax optimizations, and accelerates daily operational accounting.
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
            <td class="col-field">Floating AI Pill</td>
            <td>Purple Circle (AI)</td>
            <td>Persistent floating button at viewport bottom-right; toggles the conversational assistant drawer.</td>
          </tr>
          <tr>
            <td class="col-field">Window Controls</td>
            <td>Top-Right Icons</td>
            <td>Trash can (clears conversation history), Maximize/Expand icon, and Close (X) button.</td>
          </tr>
          <tr>
            <td class="col-field">Ask Assistant...</td>
            <td>Text Input Bar</td>
            <td>Natural language input bar to submit accounting questions, queries, or command instructions.</td>
          </tr>
          <tr>
            <td class="col-field">Send Button</td>
            <td>Purple Paper Plane</td>
            <td>Dispatches user query to the AI engine for real-time ledger analysis and natural language response.</td>
          </tr>
        </tbody>
      </table>

      <h2>Quick Suggestion Pills & Conversational Shortcuts</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 32%;">Quick Prompt Pill</th>
            <th style="width: 28%;">Pre-Configured Intent</th>
            <th style="width: 40%;">Information Returned by Assistant</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Analyze current tax obligations</td>
            <td>VAT & Tax Audit</td>
            <td>Calculates Box 8 output tax vs Box 11 input tax and projects current net payable balance.</td>
          </tr>
          <tr>
            <td class="col-field">Summarize recent Zoho Books sync</td>
            <td>External Integration Audit</td>
            <td>Summarizes recently imported journal entries, customer invoices, and sync exceptions.</td>
          </tr>
          <tr>
            <td class="col-field">Compare multi-period P&L</td>
            <td>Variance Analysis</td>
            <td>Analyzes revenue and expense changes between current quarter and prior quarter.</td>
          </tr>
        </tbody>
      </table>

      <h2>AI Integration Credentials & Architecture Parameters</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 24%;">Configuration Field</th>
            <th style="width: 36%;">Setup Parameter Location</th>
            <th style="width: 40%;">Operational Functionality & Security Boundary</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">AI Model Provider</td>
            <td>Organization ➔ Integrations ➔ AI Model</td>
            <td>Select enterprise model provider (e.g. Gemini 1.5 Pro, Claude 3.5 Sonnet).</td>
          </tr>
          <tr>
            <td class="col-field">API Key Secret</td>
            <td>Encrypted Vault Storage</td>
            <td>Client-side KMS encrypted key; never exposed in client browser network calls.</td>
          </tr>
          <tr>
            <td class="col-field">Context Memory Window</td>
            <td>Active Session Cache</td>
            <td>Maintains conversational memory across active queries within that login session.</td>
          </tr>
          <tr>
            <td class="col-field">Ledger Access Scope</td>
            <td>RBAC Role Authorization</td>
            <td>AI responses strictly adhere to user role; cannot reveal unauthorized data.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">CONFIGURATION ADVISORY BANNER</div>
        If AI credentials have not been configured for the active company, the drawer displays: <em>"AI is currently disabled for Anson Enterprises Legal Entity LLC. Please configure custom keys in Organization > Company Integrations > AI Model & Credentials."</em>
      </div>
    </div>
    """

def get_page_26():
    return """
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">ENTERPRISE GOVERNANCE · SYSTEM SECURITY</div>
          <div class="chapter-title">System Administration & Technical Support SLAs</div>
        </div>
        <div class="chapter-right-meta">SECTION 22<br>ADMIN & SUPPORT</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Manage Organization ➔ System Settings
      </div>

      <p>
        Acconeer ERP enforces enterprise governance standards covering role-based access control (RBAC), multi-factor authentication (MFA), automated database backup policies, and guaranteed commercial support response levels.
      </p>

      <h2>Role-Based Access Control (RBAC) Security Matrix</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">System Role</th>
            <th style="width: 38%;">Authorized Operational Scope</th>
            <th style="width: 40%;">Enforced Interface Restrictions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">ORG_ADMIN</td>
            <td>Full system governance, user provisioning, integration setup.</td>
            <td>Unrestricted access across all legal entities and modules.</td>
          </tr>
          <tr>
            <td class="col-field">FINANCE_MANAGER</td>
            <td>General Ledger posting, VAT filing, bank reconciliation, budgets.</td>
            <td>Restricted from user account creation and integration API keys.</td>
          </tr>
          <tr>
            <td class="col-field">BILLING_OPERATOR</td>
            <td>Customer invoicing, delivery notes, customer receipts.</td>
            <td>Cannot access General Ledger journal entries or tax settings.</td>
          </tr>
          <tr>
            <td class="col-field">AUDITOR</td>
            <td>Read-only access across all financial registers, reports, audit logs.</td>
            <td>Zero edit or posting permissions; export capabilities enabled.</td>
          </tr>
        </tbody>
      </table>

      <h2>Enterprise Technical Support Channels & SLA Response Times</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Severity Level</th>
            <th style="width: 38%;">Operational Incident Definition</th>
            <th style="width: 20%;">Target Response</th>
            <th style="width: 20%;">Target Resolution</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Critical (Sev-1)</td>
            <td>System outage, core database unreachable, ledger posting blocked.</td>
            <td>&lt; 30 Minutes</td>
            <td>&lt; 4 Hours</td>
          </tr>
          <tr>
            <td class="col-field">High (Sev-2)</td>
            <td>VAT return calculation error, bank file export failure.</td>
            <td>&lt; 2 Hours</td>
            <td>&lt; 12 Hours</td>
          </tr>
          <tr>
            <td class="col-field">Medium (Sev-3)</td>
            <td>Individual user login issues, report formatting inquiry.</td>
            <td>&lt; 4 Hours</td>
            <td>&lt; 24 Hours</td>
          </tr>
          <tr>
            <td class="col-field">Low (Sev-4)</td>
            <td>Feature requests, general UI configuration guidance.</td>
            <td>&lt; 8 Hours</td>
            <td>&lt; 48 Hours</td>
          </tr>
        </tbody>
      </table>

      <h2>User Security Policies & Session Governance Standards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Security Standard</th>
            <th style="width: 35%;">System Architectural Rule</th>
            <th style="width: 40%;">Operational Compliance Result</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Password Complexity</td>
            <td>Minimum 12 characters; alphanumeric + special symbols.</td>
            <td>Enforced during onboarding; mandatory 90-day password rotation.</td>
          </tr>
          <tr>
            <td class="col-field">Session Inactivity Lock</td>
            <td>Auto-locks screen after 15 minutes of inactivity.</td>
            <td>Protects unattended terminals; re-prompt for master credentials.</td>
          </tr>
          <tr>
            <td class="col-field">Multi-Factor Auth (MFA)</td>
            <td>Mandatory TOTP authenticator app verification.</td>
            <td>Required for all Admin and Finance Manager operational logins.</td>
          </tr>
          <tr>
            <td class="col-field">Audit Trail Immutability</td>
            <td>WORM storage; cryptographic hash on every record.</td>
            <td>Prevents retroactive alteration of user logs or system actions.</td>
          </tr>
        </tbody>
      </table>

      <h2>Automated Backup Policies & Disaster Recovery Objectives</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Recovery Dimension</th>
            <th style="width: 35%;">Backup Schedule & Architecture</th>
            <th style="width: 40%;">Enterprise Target Commitment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Snapshot Frequency</td>
            <td>Continuous write-ahead logging (WAL) + hourly snapshots.</td>
            <td>Recovery Point Objective (RPO) &lt; 5 Minutes.</td>
          </tr>
          <tr>
            <td class="col-field">Disaster Recovery (DR)</td>
            <td>Multi-region geo-redundant database replication.</td>
            <td>Recovery Time Objective (RTO) &lt; 1 Hour.</td>
          </tr>
          <tr>
            <td class="col-field">Support Email Desk</td>
            <td><code>support@sztech.ae</code></td>
            <td>24/7/365 Continuous Enterprise Monitoring.</td>
          </tr>
        </tbody>
      </table>

      <h2>Statutory Audit Readiness & Financial Compliance Standards</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Regulatory Framework</th>
            <th style="width: 35%;">Compliance Mandate & Law</th>
            <th style="width: 40%;">System Governance Verification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">UAE FTA Tax Compliance</td>
            <td>Federal Decree-Law No. 8 on Value Added Tax</td>
            <td>Generates official FTA Audit Files (FAF) with full transaction line tracing.</td>
          </tr>
          <tr>
            <td class="col-field">IFRS Accounting Standard</td>
            <td>International Financial Reporting Standards</td>
            <td>Enforces double-entry balance constraints and strict sub-ledger reconciliation.</td>
          </tr>
          <tr>
            <td class="col-field">MOHRE Wage Protection</td>
            <td>Wages Protection System (WPS) Ministerial Decree</td>
            <td>Validates automated CBUAE SIF routing and employee bank coordinates.</td>
          </tr>
          <tr>
            <td class="col-field">Sovereign Cloud Data</td>
            <td>UAE Cloud Data Residency Standards</td>
            <td>Encrypted AES-256 cloud storage hosted within compliant regional facilities.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">ENTERPRISE SLA GUARANTEE</div>
        All Acconeer ERP database instances are continuously backed up with point-in-time recovery (PITR) and replicated across multi-region secure cloud infrastructure with 99.95% guaranteed uptime SLA.
      </div>
    </div>
    """

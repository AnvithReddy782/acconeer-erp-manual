# scripts/pages_p09_p16.py
from generate_complete_manual import window_frame

def get_page_09():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Customer_Activity/03_Sales_Order.png",
        "Sales Order Management Pipeline with Fulfillment and Payment Status",
        "/customers/orders",
        [
            ("Order Pipeline View", "Tracks order lifecycle from confirmed quotation to ready-for-delivery."),
            ("Convert Action Trigger", "One-click conversion to physical Delivery Note or commercial Tax Invoice."),
            ("Credit Limit Monitor", "Real-time verification of customer outstanding receivables against approved limits."),
            ("Fulfillment Status", "Visual status badge showing Pending, In-Transit, Delivered, or Invoiced.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · ORDER-TO-CASH</div>
          <div class="chapter-title">Sales Orders & Customer Payment Receipts</div>
        </div>
        <div class="chapter-right-meta">MODULE 05<br>/customers/orders</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Customer Activity ➔ Sales Orders (or press <kbd>Alt + S</kbd>)
      </div>

      <p>
        The Order-to-Cash (O2C) module manages customer quotations, sales orders, warehouse delivery fulfillment, and customer payment receipts. Acconeer ERP connects each stage to maintain strict credit limits and synchronized stock allocations.
      </p>

      {wf}

      <h2>Order-to-Cash Workflow Stages & Ledger Impact</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Workflow Stage</th>
            <th style="width: 38%;">Operational Action in Acconeer ERP</th>
            <th style="width: 40%;">Accounting & Inventory Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Sales Quotation</td>
            <td>Draft commercial price quotation sent to client.</td>
            <td>No GL impact; holds agreed line pricing and expiry date.</td>
          </tr>
          <tr>
            <td class="col-field">Sales Order</td>
            <td>Confirmed client order; locks inventory stock.</td>
            <td>Reserves warehouse inventory quantity; checks credit limit.</td>
          </tr>
          <tr>
            <td class="col-field">Delivery Note (DN)</td>
            <td>Warehouse dispatch and customer delivery handover.</td>
            <td>Relieves inventory: <code>Dr. COGS 5000 / Cr. Inventory 1400</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Invoice</td>
            <td>Commercial billing; generates invoice PDF and TRN record.</td>
            <td>Records receivable: <code>Dr. AR 1200 / Cr. Sales 4000 / Cr. VAT 2200</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Customer Receipt</td>
            <td>Bank payment receipt or check clearing allocated to invoice.</td>
            <td>Clears receivable: <code>Dr. Bank 1010 / Cr. AR 1200</code>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Creating a Sales Order & Converting to Invoice</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Customer Activity ➔ Sales Orders</strong> (<kbd>Alt + S</kbd>) and click <strong>+ New Order</strong>.</li>
        <li>Select the <strong>Customer Name</strong>. Verify that credit limit status indicates <code>APPROVED</code>.</li>
        <li>Add the requested catalog items, quantities, and agreed unit selling prices.</li>
        <li>Click <strong>Confirm Order</strong>. The system reserves physical warehouse stock and updates order status to <code>CONFIRMED</code>.</li>
        <li>When goods are ready for delivery, click <strong>Create Delivery Note</strong> to print the warehouse dispatch slip.</li>
        <li>Once delivery is acknowledged by the customer, click <strong>Convert to Invoice</strong>. The system populates all line items into a draft tax invoice for immediate posting.</li>
      </ol>

      <h2>Customer Credit Limits & Partial Fulfillment Protocols</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Operational Scenario</th>
            <th style="width: 35%;">System Control Behavior</th>
            <th style="width: 40%;">Authorized Operator Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Credit Limit Exceeded</td>
            <td>System halts confirmation if order total exceeds approved credit.</td>
            <td>Request Finance Manager temporary override or record advance receipt.</td>
          </tr>
          <tr>
            <td class="col-field">Partial Stock Delivery</td>
            <td>Warehouse issues partial Delivery Note for available inventory.</td>
            <td>System maintains remaining balance as backorder for subsequent delivery.</td>
          </tr>
          <tr>
            <td class="col-field">Direct Receipt Allocation</td>
            <td>Customer payment allocated across multiple open invoices.</td>
            <td>Navigate to <em>Receipts</em>; select FIFO or manual line item clearing.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">RECORDING CUSTOMER PAYMENT RECEIPTS</div>
        To record incoming customer payments, navigate to <strong>Customer Activity ➔ Receipts</strong>, select the client, enter the bank reference, and allocate the funds across open invoices using FIFO or manual item selection.
      </div>
    </div>
    """

def get_page_10():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Supplier_Activity/03_Bills.png",
        "Supplier Bills Register with 3-Way Matching and Accounts Payable Aging",
        "/suppliers/bills",
        [
            ("Bills Register Table", "Overview of vendor invoices with Bill #, Supplier, Date, Due Date, and Total."),
            ("+ Enter Bill Button", "Primary action trigger to log a new vendor invoice against open purchase orders."),
            ("3-Way Match Verification", "Automated tolerance check comparing PO quantity/price against GRN and Bill."),
            ("Approval Status Pills", "Status indicators displaying Draft, Pending Approval, Approved, or Paid.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · PROCURE-TO-PAY</div>
          <div class="chapter-title">Supplier Bills & 3-Way Procure-to-Pay Matching</div>
        </div>
        <div class="chapter-right-meta">MODULE 06<br>/suppliers/bills</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Supplier Activity ➔ Bills (or press <kbd>Alt + P</kbd>)
      </div>

      <p>
        The Supplier Bills module manages vendor liability recording, automated 3-way matching, invoice approval workflows, and accounts payable (AP) aging. It safeguards corporate disbursements by verifying invoice details against verified purchase orders and receiving notes.
      </p>

      {wf}

      <h2>The Automated 3-Way Match Verification Protocol</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Comparison Pillar</th>
            <th style="width: 35%;">Source Document Reference</th>
            <th style="width: 40%;">System Verification & Tolerance Rule</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Purchase Order (PO)</td>
            <td>Authorized procurement order and agreed unit prices.</td>
            <td>Billed unit price must match approved PO line price exactly (0.00% variance).</td>
          </tr>
          <tr>
            <td class="col-field">Goods Received Note</td>
            <td>Physical warehouse inspection count and accepted quantity.</td>
            <td>Billed quantity cannot exceed total accepted items on linked GRN.</td>
          </tr>
          <tr>
            <td class="col-field">Supplier Bill Invoice</td>
            <td>Official tax invoice delivered by the vendor.</td>
            <td>Supplier TRN and tax calculation must match FTA 5% VAT rules.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Logging and Approving a Vendor Bill</h2>
      <ol class="step-list">
        <li>From the Bills workspace (<kbd>Alt + P</kbd>), click the blue <strong>+ Enter Bill</strong> button.</li>
        <li>Select the <strong>Vendor Name</strong> and choose the corresponding <strong>Purchase Order Number</strong> from the lookup list.</li>
        <li>Enter the vendor's official invoice number in the <strong>Supplier Bill Reference</strong> field and verify the invoice date.</li>
        <li>Link the warehouse <strong>GRN Intake Number</strong> to pull the verified received quantities automatically.</li>
        <li>Inspect the system <strong>3-Way Match Indicator</strong>. A green match checkmark confirms quantity and price agreement.</li>
        <li>Verify the calculated 5% Input VAT amount against the physical invoice.</li>
        <li>Click <strong>Submit for Approval</strong>. Once approved by the Finance Manager, the bill posts to Accounts Payable (Account 2100).</li>
      </ol>

      <h2>Discrepancy Tiers & Commercial Dispute Resolution</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Exception Type</th>
            <th style="width: 35%;">System Match Status</th>
            <th style="width: 40%;">Resolution Procedure</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Quantity Shortage</td>
            <td><code>GRN_QTY &lt; BILLED_QTY</code></td>
            <td>Reduce billed line quantity to match GRN; vendor must bill remainder later.</td>
          </tr>
          <tr>
            <td class="col-field">Price Inflation</td>
            <td><code>UNIT_PRICE &gt; PO_PRICE</code></td>
            <td>System places bill on <em>Commercial Hold</em> pending buyer authorization or credit note.</td>
          </tr>
          <tr>
            <td class="col-field">Invalid Vendor TRN</td>
            <td><code>TRN_CHECK_FAIL</code></td>
            <td>System blocks input VAT deduction; tax treated as non-recoverable expense.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">VARIANCE EXCEPTION HANDLING</div>
        If a price or quantity discrepancy exceeds corporate tolerance, the system flags the bill with <code>MATCH EXCEPTION</code>. The bill cannot be posted for payment until the vendor issues an adjusting credit note or the buyer re-authorizes the price increase.
      </div>
    </div>
    """

def get_page_11():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Supplier_Activity/01_Vendor_Directory.png",
        "Vendor Master Directory with Supplier Profiles and Bank Disbursement Controls",
        "/suppliers/directory",
        [
            ("Vendor Directory Table", "Listing of approved suppliers with Trade License #, TRN, and payment terms."),
            ("+ Add Vendor Button", "Modal trigger to register and onboard a new commercial supplier."),
            ("Verified Banking Status", "Indicator showing whether vendor IBAN has completed dual-verification."),
            ("Payment Run Trigger", "Filter approved due bills and initiate scheduled batch disbursement runs.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · PROCURE-TO-PAY</div>
          <div class="chapter-title">Vendor Master Directory & Disbursement Controls</div>
        </div>
        <div class="chapter-right-meta">MODULE 07<br>/suppliers/directory</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Supplier Activity ➔ Vendor Directory
      </div>

      <p>
        The Vendor Master Directory stores supplier credentials, contact information, approved commercial payment terms, and verified bank disbursement accounts. It enforces dual-authorization controls on vendor banking details to prevent fraudulent payouts.
      </p>

      {wf}

      <h2>Vendor Profile Data Dictionary & Required Inputs</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Name</th>
            <th style="width: 14%;">Field Type</th>
            <th style="width: 38%;">Operational Purpose & Format</th>
            <th style="width: 26%;">Validation & Control Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Vendor Name *</td>
            <td>Text</td>
            <td>Legal corporate registered name (e.g. <code>Al-Naboodah Logistics LLC</code>).</td>
            <td>Mandatory; checked for duplicate trade names.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Registration (TRN)</td>
            <td>Text (15 digits)</td>
            <td>Official UAE FTA Tax Registration Number.</td>
            <td>Validated: 15 numeric digits starting with 100.</td>
          </tr>
          <tr>
            <td class="col-field">Payment Terms *</td>
            <td>Dropdown</td>
            <td>Standard commercial credit terms (e.g. <em>Net 30</em>, <em>Net 60</em>, <em>Immediate</em>).</td>
            <td>Mandatory; dictates due dates on vendor bills.</td>
          </tr>
          <tr>
            <td class="col-field">Bank Name & IBAN *</td>
            <td>Text</td>
            <td>Supplier corporate bank name and 23-character UAE IBAN.</td>
            <td>Requires dual-authorization before payment release.</td>
          </tr>
          <tr>
            <td class="col-field">AP Control Account *</td>
            <td>Lookup</td>
            <td>General Ledger liability mapping (defaults to <code>2100 Accounts Payable</code>).</td>
            <td>Mandatory; links all vendor bills to sub-ledger.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Onboarding a New Vendor</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Supplier Activity ➔ Vendor Directory</strong> and click <strong>+ Add Vendor</strong>.</li>
        <li>Enter the official <strong>Vendor Legal Name</strong>, trade license number, and corporate phone/email.</li>
        <li>Enter the 15-digit UAE <strong>Tax Registration Number (TRN)</strong> if the vendor is VAT-registered.</li>
        <li>Input the supplier's corporate bank name, branch, and 23-character <strong>IBAN</strong>.</li>
        <li>Attach a scanned copy of the supplier's official Bank Account Confirmation Letter in the Attachments tab.</li>
        <li>Click <strong>Submit for Verification</strong>. An independent authorized treasury manager must review and verify the IBAN before the vendor can receive electronic payouts.</li>
      </ol>

      <h2>Weekly Vendor Disbursement Run Protocol</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Disbursement Step</th>
            <th style="width: 35%;">Operational Action in Acconeer ERP</th>
            <th style="width: 40%;">System Control & Output Artifact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">1. Bill Due Date Filter</td>
            <td>Filter AP bills by <em>Due on or before Friday</em>.</td>
            <td>Aggregates verified, approved bills ready for electronic payment.</td>
          </tr>
          <tr>
            <td class="col-field">2. Select Paying Account</td>
            <td>Choose corporate bank account with sufficient AED liquidity.</td>
            <td>Verifies available funds in Account Class 1010.</td>
          </tr>
          <tr>
            <td class="col-field">3. Generate Payment File</td>
            <td>Click <em>Generate Payment File</em> for online banking.</td>
            <td>Exports formatted bank batch transfer file (e.g. ENBD/ADCB format).</td>
          </tr>
          <tr>
            <td class="col-field">4. Post Payment Vouchers</td>
            <td>Confirm batch release; posts GL debit to AP (2100).</td>
            <td>Dr. AP 2100 / Cr. Bank 1010; generates vendor remittance advice PDF.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">DISBURSEMENT RUN WORKFLOW</div>
        To process weekly supplier payouts, click <strong>Payment Runs</strong>, select approved bills due within the current week, choose the corporate paying bank account, and click <strong>Generate Batch Payment File</strong> for online corporate banking upload.
      </div>
    </div>
    """

def get_page_12():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/General_Ledger/01_Journal_Entries.png",
        "Manual Journal Voucher Entry Screen with Real-Time Debit and Credit Balancing",
        "/gl/journals",
        [
            ("Voucher Header Information", "Voucher Number, Posting Date, Currency (AED), and Reference Description."),
            ("Journal Line Items Grid", "Dynamic table to add GL Accounts, Cost Centers, Debit amounts, and Credit amounts."),
            ("Real-Time Balancing Bar", "Calculates Total Debits, Total Credits, and displays Current Balance Difference."),
            ("Save & Post Controls", "Save Draft or Post Voucher; disabled when debits do not equal credits.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GENERAL LEDGER · CORE ACCOUNTING</div>
          <div class="chapter-title">General Ledger & Manual Journal Voucher Entry</div>
        </div>
        <div class="chapter-right-meta">MODULE 08<br>/gl/journals</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ General Ledger ➔ Journal Entry (or press <kbd>Alt + J</kbd>)
      </div>

      <p>
        The General Ledger module is the core double-entry accounting engine of Acconeer ERP. Manual journal entries are utilized for adjustments, accruals, prepayments, and reclassifications with strict mathematical debit/credit equality enforcement.
      </p>

      {wf}

      <h2>Journal Voucher Header & Line Item Data Dictionary</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Element</th>
            <th style="width: 14%;">Field Type</th>
            <th style="width: 38%;">Description & Required Format</th>
            <th style="width: 26%;">System Validation Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Voucher Date *</td>
            <td>Date Picker</td>
            <td>Accounting effective date for the double-entry transaction.</td>
            <td>Must belong to an open fiscal reporting period.</td>
          </tr>
          <tr>
            <td class="col-field">Journal Reference *</td>
            <td>Text</td>
            <td>Descriptive narrative explaining purpose (e.g. <code>Monthly Rent Accrual</code>).</td>
            <td>Mandatory; minimum 5 characters.</td>
          </tr>
          <tr>
            <td class="col-field">GL Account *</td>
            <td>Account Lookup</td>
            <td>Select 5-digit account from Chart of Accounts (e.g. <code>6100 Rent Expense</code>).</td>
            <td>Requires at least two valid account lines.</td>
          </tr>
          <tr>
            <td class="col-field">Debit / Credit *</td>
            <td>Numeric (AED)</td>
            <td>Monetary transaction amount formatted to two decimal places.</td>
            <td>Either Debit or Credit per row; cannot be both.</td>
          </tr>
          <tr>
            <td class="col-field">Branch / Cost Center</td>
            <td>Dropdown</td>
            <td>Assigns transaction to specific operating branch or department.</td>
            <td>Mandatory for Expense (6000) accounts.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Creating and Posting a Journal Voucher</h2>
      <ol class="step-list">
        <li>Click <strong>+ New Journal</strong> in the top toolbar or press <kbd>Alt + J</kbd> on your keyboard.</li>
        <li>Confirm the active <strong>Voucher Date</strong> and enter a clear commercial narrative in the <strong>Reference</strong> box.</li>
        <li>On line 1, select the target account to debit, select the cost center, and enter the <strong>Debit Amount</strong>.</li>
        <li>Click <strong>+ Add Line</strong>. On line 2, select the account to credit and enter the matching <strong>Credit Amount</strong>.</li>
        <li>Inspect the bottom balancing counter: verify that <strong>Total Debits</strong> equals <strong>Total Credits</strong> with <code>Difference: 0.00 AED</code>.</li>
        <li>Optionally upload supporting PDF documentation (e.g. calculation spreadsheet) in the attachments drawer.</li>
        <li>Click <strong>Post Voucher</strong>. The system assigns an immutable sequence number (e.g. <code>JV-2026-0184</code>) and updates GL balances.</li>
      </ol>

      <h2>Standard Recurring Journal Templates & Reversals</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Journal Entry Type</th>
            <th style="width: 35%;">Typical Debit / Credit Accounts</th>
            <th style="width: 40%;">Operational Usage & Timing</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Prepaid Rent Amortization</td>
            <td>Dr. Rent Expense 6100 / Cr. Prepaid Rent 1300</td>
            <td>Monthly recurring schedule amortizing quarterly lease payments.</td>
          </tr>
          <tr>
            <td class="col-field">Accrued Utilities / Audit</td>
            <td>Dr. Utilities 6150 / Cr. Accrued Expenses 2350</td>
            <td>Month-end accrual for unbilled operational utility expenses.</td>
          </tr>
          <tr>
            <td class="col-field">Voucher Reversal</td>
            <td>Dr./Cr. exact inversion of original voucher lines</td>
            <td>Click <em>Reverse Voucher</em> on posted record to correct errors cleanly.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout callout-warn">
        <div class="callout-title">IMMUTABILITY & REVERSAL PROTOCOL</div>
        Posted journal vouchers are permanently locked in the database and cannot be edited or deleted. To correct an erroneous voucher, open the record and click <strong>Reverse Voucher</strong> to generate an exact offsetting journal entry.
      </div>
    </div>
    """

def get_page_13():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Chart_of_Accounts/01_Accounts_Tree.png",
        "Chart of Accounts Master Tree with 5-Digit Structure and Sub-Account Mapping",
        "/gl/coa",
        [
            ("Account Classification Tree", "Hierarchical tree view of Assets (1000), Liabilities (2000), Equity (3000), Revenue (4000), and Expenses (5000/6000)."),
            ("+ Add Account Button", "Primary action trigger to configure a new general ledger posting account."),
            ("Control Account Locks", "Visual padlock icons identifying system control accounts linked to sub-ledgers."),
            ("Real-Time Account Balances", "Current opening balance, net period movement, and closing balance in AED.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GENERAL LEDGER · MASTER DATA</div>
          <div class="chapter-title">Chart of Accounts (COA) Structure & Creation</div>
        </div>
        <div class="chapter-right-meta">MODULE 09<br>/gl/coa</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ General Ledger ➔ Chart of Accounts (or press <kbd>Alt + A</kbd>)
      </div>

      <p>
        The Chart of Accounts (COA) establishes the foundational financial taxonomy of Acconeer ERP. It organizes accounts using a standardized 5-digit numbering system compliant with IFRS standards and UAE corporate reporting structures.
      </p>

      {wf}

      <h2>Standard 5-Digit Account Classification Framework</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 14%;">Code Range</th>
            <th style="width: 22%;">Major Account Class</th>
            <th style="width: 20%;">Normal Balance</th>
            <th style="width: 44%;">Operational Representative Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>1000–1999</code></td>
            <td><strong>Current & Fixed Assets</strong></td>
            <td>Debit</td>
            <td><code>1010 Bank Current Accounts</code> • <code>1200 Accounts Receivable</code> • <code>1400 Inventory</code></td>
          </tr>
          <tr>
            <td><code>2000–2999</code></td>
            <td><strong>Liabilities & Accruals</strong></td>
            <td>Credit</td>
            <td><code>2100 Accounts Payable</code> • <code>2200 Output VAT Payable</code> • <code>2300 Accrued Salaries</code></td>
          </tr>
          <tr>
            <td><code>3000–3999</code></td>
            <td><strong>Shareholders' Equity</strong></td>
            <td>Credit</td>
            <td><code>3010 Paid-Up Share Capital</code> • <code>3100 Retained Earnings</code> • <code>3200 Statutory Reserve</code></td>
          </tr>
          <tr>
            <td><code>4000–4999</code></td>
            <td><strong>Operating Revenue</strong></td>
            <td>Credit</td>
            <td><code>4000 Commercial Sales Revenue</code> • <code>4100 Service Income</code> • <code>4200 Logistics Fees</code></td>
          </tr>
          <tr>
            <td><code>5000–5999</code></td>
            <td><strong>Cost of Goods Sold (COGS)</strong></td>
            <td>Debit</td>
            <td><code>5000 Direct Material Costs</code> • <code>5100 Freight Inbound</code> • <code>5200 Packaging</code></td>
          </tr>
          <tr>
            <td><code>6000–6999</code></td>
            <td><strong>Operating Expenses (OpEx)</strong></td>
            <td>Debit</td>
            <td><code>6010 Staff Salaries</code> • <code>6100 Office Rent</code> • <code>6200 Depreciation Expense</code></td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Adding a New Account to the COA</h2>
      <ol class="step-list">
        <li>Navigate to the Chart of Accounts (<kbd>Alt + A</kbd>) and click the blue <strong>+ Add Account</strong> button.</li>
        <li>Select the <strong>Parent Account Category</strong> (e.g. <em>6000 Operating Expenses</em>).</li>
        <li>Enter the unique 5-digit <strong>Account Code</strong> (e.g. <code>6250</code> for <em>Software Subscriptions</em>).</li>
        <li>Enter the official <strong>Account Name</strong> and select the currency (defaults to <code>AED</code>).</li>
        <li>Choose whether the account is an operational posting account or a non-posting summary header.</li>
        <li>Click <strong>Save & Add to Tree</strong>. The account is immediately available for journal and voucher postings.</li>
      </ol>

      <h2>Sub-Account Nesting & Inactivation Policies</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">COA Policy Dimension</th>
            <th style="width: 35%;">System Architectural Rule</th>
            <th style="width: 40%;">Accounting Governance Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Sub-Account Mapping</td>
            <td>Click <em>+ Map Sub</em> on parent to create child branch accounts.</td>
            <td>Child balances automatically roll up to parent header on Trial Balance.</td>
          </tr>
          <tr>
            <td class="col-field">Account Inactivation</td>
            <td>Accounts with zero balance can be set to <em>Inactive</em>.</td>
            <td>Hides account from active lookup dropdowns while preserving history.</td>
          </tr>
          <tr>
            <td class="col-field">Control Account Lock</td>
            <td>Accounts 1200, 2100, 1400 locked against manual journals.</td>
            <td>Ensures sub-ledger integrity; postings allowed only via Invoices/Bills.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">PROTECTION OF SUB-LEDGER CONTROL ACCOUNTS</div>
        Accounts flagged with a lock symbol (e.g. <code>1200 AR Control</code>, <code>2100 AP Control</code>, <code>1400 Inventory Control</code>) are system control accounts. Manual journal entries to these accounts are restricted to prevent variances between sub-ledgers and the general ledger.
      </div>
    </div>
    """

def get_page_14():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Inventory/01_Inventory_Master.png",
        "Inventory Product Master Catalog with Stock Levels and Valuation Parameters",
        "/inventory/products",
        [
            ("Inventory Catalog Grid", "Comprehensive directory of active SKUs, categories, quantities on hand, and cost values."),
            ("+ Add Item Button", "Primary action trigger to configure a new stock or non-stock inventory item."),
            ("Stock Health Indicators", "Real-time stock indicators showing Healthy, Low Stock, or Out of Stock."),
            ("Valuation Engine Trigger", "Access FIFO and Weighted Average Cost (WAC) ledger valuation reports.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INVENTORY & ASSETS · SUPPLY CHAIN</div>
          <div class="chapter-title">Inventory Master Catalog & Valuation Rules</div>
        </div>
        <div class="chapter-right-meta">MODULE 10<br>/inventory/products</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Inventory ➔ Product Master
      </div>

      <p>
        The Inventory Master module maintains the centralized product catalog, tracks real-time warehouse stock balances, manages stock reorder thresholds, and calculates accurate inventory valuation under First-In, First-Out (FIFO) or Weighted Average Costing (WAC).
      </p>

      {wf}

      <h2>Inventory Item Profile Data Dictionary</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Field Name</th>
            <th style="width: 14%;">Field Type</th>
            <th style="width: 38%;">Operational Purpose & Format</th>
            <th style="width: 26%;">Validation & Control Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Item SKU Code *</td>
            <td>Text</td>
            <td>Unique product identifier (e.g. <code>SKU-ELEC-0042</code>).</td>
            <td>Mandatory; alphanumeric unique constraint.</td>
          </tr>
          <tr>
            <td class="col-field">Item Name *</td>
            <td>Text</td>
            <td>Commercial product description used on customer invoices.</td>
            <td>Mandatory; minimum 3 characters.</td>
          </tr>
          <tr>
            <td class="col-field">Item Category *</td>
            <td>Dropdown</td>
            <td>Classification (e.g. <em>Electronics</em>, <em>Raw Materials</em>, <em>Finished Goods</em>).</td>
            <td>Determines default GL inventory and COGS accounts.</td>
          </tr>
          <tr>
            <td class="col-field">Unit of Measure (UOM) *</td>
            <td>Dropdown</td>
            <td>Physical stocking unit (e.g. <code>PCS</code>, <code>BOX</code>, <code>KG</code>, <code>MTR</code>).</td>
            <td>Mandatory; governs warehouse piece counts.</td>
          </tr>
          <tr>
            <td class="col-field">Costing Method *</td>
            <td>Dropdown</td>
            <td>Valuation rule: <code>FIFO (First-In, First-Out)</code> or <code>Weighted Average (WAC)</code>.</td>
            <td>Fixed per item category; dictates balance sheet valuation.</td>
          </tr>
          <tr>
            <td class="col-field">Reorder Level</td>
            <td>Numeric</td>
            <td>Minimum warehouse stock threshold before reorder alert fires.</td>
            <td>Triggers automated replenishment notification.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Creating a New Inventory SKU</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Inventory ➔ Product Master</strong> and click the blue <strong>+ Add Item</strong> button.</li>
        <li>Enter the unique <strong>SKU Code</strong> and complete descriptive <strong>Item Name</strong>.</li>
        <li>Select the <strong>Item Category</strong> and assign the physical <strong>Unit of Measure (UOM)</strong>.</li>
        <li>Enter the standard purchase cost and default commercial selling price in AED.</li>
        <li>Set the <strong>Reorder Level</strong> (e.g. <code>50 PCS</code>) to ensure automated low-stock warnings appear on the dashboard.</li>
        <li>Verify that the linked GL accounts populate: <strong>Inventory Asset (Account 1400)</strong> and <strong>COGS (Account 5000)</strong>.</li>
        <li>Click <strong>Save & Register SKU</strong> to activate the item across purchasing and sales modules.</li>
      </ol>

      <h2>Physical Stock Counts & Inventory Adjustments</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Inventory Procedure</th>
            <th style="width: 35%;">Action Trigger & Inputs</th>
            <th style="width: 40%;">System Accounting & Stock Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Stock Take Reconciliation</td>
            <td>Navigate to <em>Physical Count</em>; input counted physical units.</td>
            <td>System highlights variance between book stock and counted stock.</td>
          </tr>
          <tr>
            <td class="col-field">Inventory Shrinkage Write-Off</td>
            <td>Post <em>Stock Adjustment Voucher</em> for damaged/lost inventory.</td>
            <td>Dr. Inventory Shrinkage Expense (5150) / Cr. Inventory Asset (1400).</td>
          </tr>
          <tr>
            <td class="col-field">Inter-Warehouse Transfer</td>
            <td>Create <em>Transfer Order</em>: Dubai Main Depot to Abu Dhabi.</td>
            <td>Updates physical warehouse bin tags; balance sheet remains unchanged.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">REAL-TIME INVENTORY GL INTEGRATION</div>
        Acconeer ERP uses a perpetual inventory system. Receiving goods via a GRN immediately debits Inventory Asset 1400. Fulfilling a sales order immediately credits Inventory 1400 and debits Cost of Goods Sold 5000 with zero manual journals required.
      </div>
    </div>
    """

def get_page_15():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Inventory/11_Goods_Received_Note.png",
        "Goods Received Notes (GRN) Inbound Intake Register and Warehouse Quality Inspection",
        "/inventory/grn",
        [
            ("GRN Intake Register", "Log of inbound warehouse deliveries with GRN #, Vendor, PO Ref, and Intake Date."),
            ("+ New GRN Intake", "Primary action trigger to initiate a warehouse receipt against an open purchase order."),
            ("Inspection Counter", "Tracks Received Quantity, Accepted Quality Count, and Rejected Discrepancy Count."),
            ("Post to Warehouse", "Finalize physical intake, assign warehouse bin location, and post GL inventory accrual.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INVENTORY & ASSETS · SUPPLY CHAIN</div>
          <div class="chapter-title">Goods Received Notes (GRN) & Warehouse Intake</div>
        </div>
        <div class="chapter-right-meta">MODULE 11<br>/inventory/grn</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Inventory ➔ Goods Received Notes
      </div>

      <p>
        The Goods Received Notes (GRN) module governs physical warehouse receiving, inbound inspection, quality control verification, and automated inventory accrual. Completing a GRN updates on-hand stock balances and forms the basis for 3-way matching.
      </p>

      {wf}

      <h2>GRN Receiving Fields & Quality Inspection Tracking</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Interface Field</th>
            <th style="width: 38%;">Description & Operating Role</th>
            <th style="width: 40%;">System Validation & Inventory Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Purchase Order Ref *</td>
            <td>Open procurement order authorizing supplier delivery.</td>
            <td>Auto-loads ordered SKU line items and expected quantities.</td>
          </tr>
          <tr>
            <td class="col-field">Delivered Quantity *</td>
            <td>Physical quantity counted upon truck unloading at dock.</td>
            <td>Cannot exceed PO ordered quantity without buyer variance override.</td>
          </tr>
          <tr>
            <td class="col-field">Accepted Quantity *</td>
            <td>Items passing physical inspection and quality verification.</td>
            <td>This exact quantity increments physical stock on hand.</td>
          </tr>
          <tr>
            <td class="col-field">Rejected Quantity</td>
            <td>Items damaged in transit or failing specifications.</td>
            <td>Routed to quarantine; generates automated vendor return notice.</td>
          </tr>
          <tr>
            <td class="col-field">Warehouse Bin Location *</td>
            <td>Physical rack and shelf storage tag (e.g. <code>BIN-DXB-A-12</code>).</td>
            <td>Directs warehouse pickers during order fulfillment.</td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Processing Warehouse Inbound Intake</h2>
      <ol class="step-list">
        <li>From the GRN workspace, click the blue <strong>+ New GRN Intake</strong> button.</li>
        <li>Select the delivering <strong>Supplier Name</strong> and choose the active <strong>Purchase Order Number</strong>.</li>
        <li>Enter the supplier delivery note number and the physical arrival date.</li>
        <li>For each line item, enter the physical <strong>Delivered Quantity</strong> and verify against the packing list.</li>
        <li>Enter the <strong>Accepted Quantity</strong> following physical inspection. If damaged goods are found, log the count in <strong>Rejected Quantity</strong>.</li>
        <li>Assign the target <strong>Warehouse Bin Location</strong> for stock shelving.</li>
        <li>Click <strong>Post GRN Intake</strong>. The system prints warehouse stock labels and generates the inventory accrual voucher.</li>
      </ol>

      <h2>Inbound Quality Discrepancy & Quarantine Protocol</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Discrepancy Category</th>
            <th style="width: 35%;">Warehouse Action Required</th>
            <th style="width: 40%;">Accounting & Supplier Resolution</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Physical Transit Damage</td>
            <td>Log units in <em>Rejected Qty</em>; take photos via attachment drawer.</td>
            <td>Generates Return-to-Vendor (RTV) slip; unit excluded from AP bill.</td>
          </tr>
          <tr>
            <td class="col-field">Incorrect SKU Delivered</td>
            <td>Reject item; do not assign warehouse bin location.</td>
            <td>System notifies purchasing officer for immediate supplier replacement.</td>
          </tr>
          <tr>
            <td class="col-field">Over-Shipment (+Q)</td>
            <td>Count units; buyer must approve addition before intake.</td>
            <td>If accepted, auto-updates PO line item quantity and purchase total.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">ACCOUNTING IMPACT: POSTING A GRN</div>
        Posting a GRN synchronously records: <strong>Debit Account 1400 (Inventory Control)</strong> for the accepted stock value and <strong>Credit Account 2150 (Accrued Purchases / GRN Clearing)</strong>. When the supplier bill arrives, Account 2150 clears against Accounts Payable.
      </div>
    </div>
    """

def get_page_16():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Assets/06_Asset_Register.png",
        "Fixed Assets Master Registry with Capitalization Values and Depreciation Schedules",
        "/assets/registry",
        [
            ("Asset Registry Table", "Inventory of capitalized company assets with Asset Tag #, Category, Cost, and NBV."),
            ("+ Register Asset", "Primary action trigger to capitalize a new fixed asset from a supplier bill or PO."),
            ("Depreciation Status", "Tracks monthly depreciation progress, accumulated depreciation, and useful life."),
            ("Run Depreciation Batch", "Execute automated monthly straight-line depreciation journal postings.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INVENTORY & ASSETS · CAPITAL ASSETS</div>
          <div class="chapter-title">Fixed Assets Registry & Monthly Depreciation</div>
        </div>
        <div class="chapter-right-meta">MODULE 12<br>/assets/registry</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Fixed Assets ➔ Asset Registry
      </div>

      <p>
        The Fixed Assets module maintains the capital equipment register, records asset acquisition costs, manages physical asset tag assignments, and automates monthly depreciation schedules in compliance with International Accounting Standard 16 (IAS 16).
      </p>

      {wf}

      <h2>Standard Asset Categories & Depreciation Parameters</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Asset Category</th>
            <th style="width: 18%;">Standard Useful Life</th>
            <th style="width: 18%;">Depreciation Method</th>
            <th style="width: 42%;">Linked General Ledger Accounts</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">IT & Computer Equipment</td>
            <td>3 Years (36 Months)</td>
            <td>Straight-Line (33.33%)</td>
            <td>Asset: <code>1510</code> • Acc. Dep: <code>1515</code> • Dep Exp: <code>6210</code></td>
          </tr>
          <tr>
            <td class="col-field">Office Furniture & Fixtures</td>
            <td>5 Years (60 Months)</td>
            <td>Straight-Line (20.00%)</td>
            <td>Asset: <code>1520</code> • Acc. Dep: <code>1525</code> • Dep Exp: <code>6220</code></td>
          </tr>
          <tr>
            <td class="col-field">Motor Vehicles & Trucks</td>
            <td>4 Years (48 Months)</td>
            <td>Straight-Line (25.00%)</td>
            <td>Asset: <code>1530</code> • Acc. Dep: <code>1535</code> • Dep Exp: <code>6230</code></td>
          </tr>
          <tr>
            <td class="col-field">Warehouse Machinery</td>
            <td>7 Years (84 Months)</td>
            <td>Straight-Line (14.28%)</td>
            <td>Asset: <code>1540</code> • Acc. Dep: <code>1545</code> • Dep Exp: <code>6240</code></td>
          </tr>
        </tbody>
      </table>

      <h2>Standard Operating Procedure: Running Monthly Asset Depreciation</h2>
      <ol class="step-list">
        <li>Navigate to <strong>Fixed Assets ➔ Asset Registry</strong> and confirm all new monthly asset acquisitions are registered.</li>
        <li>Click the blue <strong>Run Depreciation Batch</strong> button located above the asset table.</li>
        <li>Select the closing <strong>Depreciation Period</strong> (e.g. <em>September 2026</em>).</li>
        <li>Review the pre-calculated depreciation summary displaying monthly expense per asset class and total batch debit.</li>
        <li>Click <strong>Execute Batch Posting</strong>.</li>
        <li>The system automatically generates a balanced journal voucher: <strong>Debit Account 6200 (Depreciation Expense)</strong> and <strong>Credit Account 1500 (Accumulated Depreciation)</strong>.</li>
        <li>The Net Book Value (NBV) on each asset card automatically updates to reflect current period amortization.</li>
      </ol>

      <h2>Asset Relocation, Disposal & Impairment Workflow</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Lifecycle Event</th>
            <th style="width: 35%;">Action Trigger & Documentation</th>
            <th style="width: 40%;">System Accounting & Balance Sheet Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Branch Asset Transfer</td>
            <td>Click <em>Transfer Asset</em>; select new branch cost center.</td>
            <td>Transfers future depreciation expense to new branch P&L.</td>
          </tr>
          <tr>
            <td class="col-field">Asset Sale / Disposal</td>
            <td>Click <em>Retire Asset</em>; enter commercial proceeds and buyer.</td>
            <td>Dr. Bank / Dr. Acc. Dep / Cr. Asset Cost / Dr./Cr. Gain/Loss on Sale.</td>
          </tr>
          <tr>
            <td class="col-field">Total Asset Scrap</td>
            <td>Mark asset as <em>Scrapped / Obsolete</em> with board approval.</td>
            <td>Dr. Impairment Loss (6290) / Dr. Acc. Dep / Cr. Asset Historical Cost.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">ASSET RETIREMENT & DISPOSAL</div>
        When an asset is sold or scrapped, open the asset profile and click <strong>Retire Asset</strong>. The system prompts for sale proceeds, calculates the Gain or Loss on Disposal, and automatically offsets the historical cost and accumulated depreciation accounts.
      </div>
    </div>
    """

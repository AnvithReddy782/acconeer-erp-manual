# scripts/pages_p09_p16.py
from generate_complete_manual import window_frame

def get_page_09():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Customer_Activity/03_Sales_Order.png",
        "Sales Order Management Pipeline with Delivery Tracking and Credit Status",
        "/customers/orders",
        [
            ("Order Pipeline View", "Tracks order lifecycle from confirmed commercial quotation to ready-for-delivery."),
            ("Convert Action Trigger", "One-click conversion to physical Delivery Note or commercial Tax Invoice."),
            ("Credit Limit Monitor", "Real-time verification of customer outstanding receivables against approved limits."),
            ("Fulfillment Status", "Visual status badge showing Pending, In-Transit, Delivered, or Invoiced.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 03 · MODULE 03 (PART 2)</div>
          <div class="chapter-title">Order-to-Cash Lifecycle: Orders & Receipts</div>
        </div>
        <div class="chapter-cat">ORDER-TO-CASH LIFECYCLE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Customer Activity ➔ Sales Order
      </div>

      <p>
        The Order-to-Cash (O2C) pipeline governs commercial quotes, confirmed customer purchase orders, warehouse delivery documentation, commercial tax invoicing, and customer cash receipt allocations within a unified state machine.
      </p>

      {wf}

      <h2>End-to-End Order-to-Cash (O2C) State Machine</h2>
      <div class="process-strip">
        <span class="process-strip-title">State Flow:</span>
        <span class="process-node">1. Sales Quote (Non-posting)</span>
        <span class="process-arrow">➔</span>
        <span class="process-node process-node-active">2. Sales Order (Reserved)</span>
        <span class="process-arrow">➔</span>
        <span class="process-node">3. Delivery Note (Stock Relief)</span>
        <span class="process-arrow">➔</span>
        <span class="process-node">4. Tax Invoice (AR Posting)</span>
        <span class="process-arrow">➔</span>
        <span class="process-node process-node-active">5. Cash Receipt (Settlement)</span>
      </div>

      <h2>Accounting State Transitions & Ledger Postings</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Workflow Stage</th>
            <th style="width: 35%;">System Operational Trigger</th>
            <th style="width: 40%;">General Ledger Double-Entry Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Sales Quotation</td>
            <td>Non-posting commercial offer</td>
            <td>No GL impact. Holds negotiated pricing and validity period.</td>
          </tr>
          <tr>
            <td class="col-field">Sales Order Confirmation</td>
            <td>Locks customer credit limit and reserves stock</td>
            <td>No GL impact. Allocates physical inventory quantity in warehouse.</td>
          </tr>
          <tr>
            <td class="col-field">Delivery Note (Goods Issue)</td>
            <td>Warehouse dispatch confirmation</td>
            <td><strong>Dr. 5000 Cost of Goods Sold / Cr. 1400 Inventory Control</strong></td>
          </tr>
          <tr>
            <td class="col-field">Commercial Tax Invoice</td>
            <td>Billing event and statutory tax point</td>
            <td><strong>Dr. 1200 AR Control / Cr. 4000 Sales / Cr. 2210 Output VAT (5%)</strong></td>
          </tr>
          <tr>
            <td class="col-field">Customer Receipt Voucher</td>
            <td>Bank settlement or cheque clearing</td>
            <td><strong>Dr. 1010 Corporate Bank Account / Cr. 1200 AR Control</strong></td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Processing Customer Receipts & Allocation</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Customer Activity ➔ Receipts</strong> and click <strong>+ New Receipt Voucher</strong>.</li>
          <li>Select the Customer; the system populates all open unpaid invoices with invoice numbers, dates, and balances in AED.</li>
          <li>Select the receiving corporate Bank Account (e.g. <code>1010-01 Operating Account</code>) and enter the payment reference.</li>
          <li>Allocate the received amount across specific open invoices (FIFO or manual allocation) to clear AR aging buckets.</li>
          <li>Click <strong>Post Receipt</strong>. System generates receipt PDF and posts cash journal: <em>Dr. 1010 Bank / Cr. 1200 AR Control</em>.</li>
        </ol>
      </div>

      <div class="note-card" style="margin-top: 4pt; margin-bottom: 0;">
        <div class="note-card-title">Statutory Tax Point & Revenue Recognition Policy</div>
        <strong>UAE VAT Law (Article 25) Compliance:</strong> The tax point for supply of goods occurs on the date of physical delivery (Delivery Note), the date of issuance of the commercial tax invoice, or the date of receipt of payment, whichever occurs earliest. Issuing an invoice synchronously posts output tax to <code>2210 Output VAT</code> and updates FTA Form 201 Box 1 in real time.
      </div>
    </div>
    """

def get_page_10():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Supplier_Activity/01_Supplier_Bills.png",
        "Supplier Bill Directory with 3-Way Matching Status and Payment Approvals",
        "/suppliers/bills",
        [
            ("Bill Directory Table", "Lists vendor bills, bill numbers, PO links, taxable amounts, 5% input VAT, and matching status."),
            ("New Bill Entry Action", "Opens the vendor bill logging workflow with PO auto-matching and GRN linkage."),
            ("Matching Indicator", "Visual badge showing 3-Way Matched, Price Discrepancy Review, or Quantity Hold."),
            ("Payment Batch Selector", "Multi-select bills for batched electronic bank payment execution.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 04 · MODULE 04 (PART 1)</div>
          <div class="chapter-title">Supplier Activity: Bills & 3-Way Matching</div>
        </div>
        <div class="chapter-cat">PROCURE-TO-PAY & EXPENDITURE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Supplier Activity ➔ Supplier Bills
      </div>

      <p>
        The Supplier Bills engine enforces automated 3-way matching between Purchase Orders (PO), Goods Received Notes (GRN), and vendor tax invoices. It ensures that expenditures are authorized, quantities are verified, and input VAT is recoverable.
      </p>

      {wf}

      <div class="sop-meta-grid">
        <div class="sop-meta-item">
          <span class="sop-meta-title">Prerequisites & Document Dependencies</span>
          <span class="sop-meta-desc">Approved Purchase Order • Certified GRN from Warehouse • Valid Vendor Tax Invoice with Vendor TRN</span>
        </div>
        <div class="sop-meta-item">
          <span class="sop-meta-title">Authorized Roles & Tolerance Policy</span>
          <span class="sop-meta-desc">Data Entry: AP Clerk • Approval (&gt; 0.5% Variance or &gt; AED 50,000): Procurement Manager / Chief Accountant</span>
        </div>
      </div>

      <h2>Automated 3-Way Matching & Discrepancy Tolerance Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Matching Dimension</th>
            <th style="width: 35%;">System Tolerance Policy</th>
            <th style="width: 40%;">Operational Exception Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Unit Price Discrepancy</td>
            <td>Configurable tolerance: &le; 0.5% (or max AED 50)</td>
            <td>Auto-approved; difference posted to <strong>5200 Purchase Price Variance (PPV)</strong>. Discrepancies &gt; 0.5% route to Manager.</td>
          </tr>
          <tr>
            <td class="col-field">Quantity Verification</td>
            <td>Billed Qty must &le; GRN Received Qty</td>
            <td>Excess billing placed on immediate <em>Quantity Hold</em>. Requires revised vendor bill or supplemental GRN intake.</td>
          </tr>
          <tr>
            <td class="col-field">Tax Code & TRN Check</td>
            <td>Vendor TRN verified against FTA format</td>
            <td>If vendor is not VAT registered, 5% input tax is blocked; expense posts as gross to expense account.</td>
          </tr>
        </tbody>
      </table>

      <h2>General Ledger Posting Impact: Approved Vendor Bill</h2>
      <div class="journal-demo-card">
        <div class="journal-demo-header">
          <span>POSTING: Vendor Bill #BILL-2026-0094 (Linked to PO-2026-0051 & GRN-0038)</span>
          <span class="badge-mono badge-blue">POSTED TO GL</span>
        </div>
        <div class="journal-demo-row">
          <span>Dr. 1410-01 GRN Clearing / Accrued Accounts Payable (Reversing GRN accrual)</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 20,000.00</span>
          <span>AED 0.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Dr. 2220-01 Input VAT Recoverable (UAE Standard 5% Rate — Form 201 Box 9)</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 1,000.00</span>
          <span>AED 0.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Cr. 2100-01 Accounts Payable Control (Trade Vendor Sub-Ledger)</span>
          <span>AED 0.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 21,000.00</span>
        </div>
        <div class="journal-demo-total">
          <span>Balanced Journal Total</span>
          <span>Debit: AED 21,000.00</span>
          <span>Credit: AED 21,000.00 (Variance: AED 0.00)</span>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Logging and 3-Way Matching a Supplier Bill</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Supplier Activity ➔ Supplier Bills</strong> and click <strong>+ New Bill</strong>.</li>
          <li>Select Vendor and link the corresponding approved Purchase Order and certified Goods Received Note (GRN).</li>
          <li>Enter Vendor's external Invoice Number, date, and line item billing details. System runs 3-way matching.</li>
          <li>If variance is within 0.5%, bill is cleared. If variance exceeds threshold, route to Procurement Manager for sign-off.</li>
          <li>Click <strong>Post Bill</strong>. System clears GRN accrual, debits recoverable VAT, and credits Accounts Payable.</li>
        </ol>
      </div>

      <h2>AP Discrepancy & Price Variance Resolution Workflow</h2>
      <div class="sop-meta-grid" style="margin-top: 3.5pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Tolerance Exceeded (&gt; 0.5% or &gt; AED 500)</div>
          <div class="sop-meta-desc">Automated hold placed on vendor disbursement. Requisitioner and Procurement Buyer must review vendor invoice against initial contract quote.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Vendor Credit Note Adjustment</div>
          <div class="sop-meta-desc">When vendor bills in excess of PO agreed terms, AP requests an official Credit Note prior to releasing payment. Credit Note links directly to bill #BILL.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Under-Delivery Settlement</div>
          <div class="sop-meta-desc">If received quantity is less than PO quantity, bill is certified only for the received quantity. Balance PO remains open for backorder fulfillment.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Emergency Override Authorization</div>
          <div class="sop-meta-desc">CFO dual-approval required to override price holds without revised PO. All override transactions are permanently flagged in the executive audit log.</div>
        </div>
      </div>

      <div class="note-card" style="margin-top: 3.5pt; margin-bottom: 0;">
        <div class="note-card-title">Commercial Dispute Management & Credit Note Linkage</div>
        <strong>Disputed Invoicing Protocol:</strong> When vendor line items carry unresolvable price or quantity discrepancies exceeding authorized tolerances, the bill status is transitioned to <em>Disputed Hold</em>. System notifications prompt the vendor to submit a formal Credit Note or revised invoice before AP payment scheduling.
      </div>
    </div>
    """

def get_page_11():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Supplier_Activity/02_Vendors.png",
        "Vendor Directory with Trade License Verification and Payment Details",
        "/suppliers/vendors",
        [
            ("Vendor Directory Table", "Vendor business names, trade license numbers, TRNs, payment terms, and open AP balances in AED."),
            ("Vendor Onboarding Action", "Opens vendor registration modal with mandatory compliance document attachments."),
            ("Bank Details Management", "Encrypted storage of vendor beneficiary bank name, branch, and UAE IBAN."),
            ("Payment Run Generator", "Batch disbursement trigger to generate bank payment files.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 04 · MODULE 04 (PART 2)</div>
          <div class="chapter-title">Vendor Directory & Disbursement Governance</div>
        </div>
        <div class="chapter-cat">PROCUREMENT & FRAUD CONTROLS</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Supplier Activity ➔ Vendors
      </div>

      <p>
        The Vendor Directory manages supplier profiles, statutory compliance records, payment terms, and disbursement execution. It implements internal controls to prevent fraudulent vendor updates and duplicate invoice processing.
      </p>

      {wf}

      <h2>Vendor Master Governance & Statutory Compliance Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Compliance Gate</th>
            <th style="width: 35%;">System Verification Standard</th>
            <th style="width: 40%;">Statutory Fraud & Tax Governance</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Trade License Verification</td>
            <td>Valid UAE Department of Economy license</td>
            <td>Mandatory PDF license upload; expiration date monitored by automated alerts.</td>
          </tr>
          <tr>
            <td class="col-field">FTA TRN Validation</td>
            <td>15-Digit verified Tax Registration Number</td>
            <td>Validates supplier tax registration; unverified vendors cannot be assigned 5% VAT codes.</td>
          </tr>
          <tr>
            <td class="col-field">Duplicate Invoice Protection</td>
            <td>System uniqueness constraint</td>
            <td>Blocks saving any bill where <code>Vendor ID + Vendor Invoice Number</code> already exists in the system.</td>
          </tr>
        </tbody>
      </table>

      <h2>Dual-Control Authorization: Vendor Bank Details (IBAN)</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>1. Bank Modification Lock</h4>
          <p>Editing a vendor's bank name or IBAN immediately locks the vendor profile from inclusion in payment runs.</p>
        </div>
        <div class="matching-card">
          <h4>2. Out-of-Band Callback</h4>
          <p>Finance team must perform an independent phone callback to the vendor's registered contact to verify account changes.</p>
        </div>
        <div class="matching-card">
          <h4>3. Secondary Dual Approval</h4>
          <p>Chief Accountant or Finance Director must review callback logs and provide secondary cryptographic authorization.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Executing a Vendor Payment Run</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Supplier Activity ➔ Payments</strong> and click <strong>+ New Payment Run</strong>.</li>
          <li>Filter approved vendor bills by due date and payment terms. Select bills for disbursement.</li>
          <li>Choose corporate disbursement bank account (Class 1010) and payment method (WPS, Corporate Wire, or Cheque).</li>
          <li>Verify payment batch total in AED. Payments exceeding AED 100,000 route for dual executive sign-off (CFO + CEO).</li>
          <li>Click <strong>Release Payment Batch</strong>. Generates bank payment file and posts GL entry: <em>Dr. 2100 AP / Cr. 1010 Bank</em>.</li>
        </ol>
      </div>

      <h2>Vendor Onboarding Compliance & AML Verification Checklist</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Compliance Document</th>
            <th style="width: 35%;">Verification & Validation Standard</th>
            <th style="width: 40%;">System Enforcement & Controls</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">UAE Trade License</td>
            <td>Certified copy from DED or Free Zone Authority</td>
            <td>Mandatory PDF upload; system tracks expiry date and auto-locks expired vendors.</td>
          </tr>
          <tr>
            <td class="col-field">FTA VAT Certificate</td>
            <td>15-Digit verified Tax Registration Number</td>
            <td>System validates TRN syntax; non-registered vendors are locked from input VAT.</td>
          </tr>
          <tr>
            <td class="col-field">Bank Account Letter</td>
            <td>Original stamped bank verification letter</td>
            <td>IBAN, SWIFT BIC, and account title must match trade license name exactly.</td>
          </tr>
        </tbody>
      </table>

      <h2>Disbursement Approval Thresholds & Execution Rails</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Tier 1: Up to AED 25,000</div>
          <div class="sop-meta-desc">Senior Accountant single authorization. Payment released via automated corporate online banking rail.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Tier 2: AED 25,001 to AED 100,000</div>
          <div class="sop-meta-desc">Dual approval required: Chief Accountant + Finance Director. Executed via CBUAE Local Transfer.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Tier 3: Above AED 100,000</div>
          <div class="sop-meta-desc">Executive sign-off: CFO + CEO dual key authorization required prior to bank file generation.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Bank File Security (ISO 20022)</div>
          <div class="sop-meta-desc">Generated XML/pain.001 payment files are cryptographically hashed (SHA-256) to prevent tampering.</div>
        </div>
      </div>

      <div class="note-card" style="margin-top: 3.5pt; margin-bottom: 0;">
        <div class="note-card-title">Vendor Blacklist & Sanction Screening (UAE Central Bank)</div>
        <strong>Statutory AML/CFT Compliance:</strong> Prior to releasing payment batches, the disbursement engine cross-checks vendor names and beneficiary IBANs against the UAE Executive Office for Control & Non-Proliferation (EOCN) national sanctions list. Matched profiles are immediately quarantined from payment execution.
      </div>
    </div>
    """

def get_page_12():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/General_Ledger/01_Journal_Entries.png",
        "General Ledger Journal Entries Directory with Debit/Credit Audit Trails",
        "/gl/journals",
        [
            ("Journal Entries Table", "Voucher IDs, transaction dates, source modules, total debits/credits in AED, and posting status."),
            ("New Journal Action", "Direct trigger opening the double-entry voucher entry modal with live balance validation."),
            ("Source Module Filter", "Filter by Manual Adjustments, Payroll, Depreciation, Invoicing, and Period Close."),
            ("Audit Trail Viewer", "Inspect cryptographic timestamp, creator ID, approver ID, and supporting document attachments.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 05 · MODULE 05</div>
          <div class="chapter-title">General Ledger & Manual Journal Entries</div>
        </div>
        <div class="chapter-cat">CORE GENERAL LEDGER</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Journal Entries (General Ledger)
      </div>

      <p>
        The General Ledger Journal Entries module is the foundational double-entry record for Acconeer ERP. It records statutory adjustments, payroll allocations, depreciation runs, and inter-entity balance transfers with complete audit traceability.
      </p>

      {wf}

      <h2>Balanced Double-Entry Journal Voucher Simulation</h2>
      <div class="journal-demo-card">
        <div class="journal-demo-header">
          <span>JOURNAL VOUCHER: JV-2026-0042 (Monthly Office Rent & VAT Allocation)</span>
          <span class="badge-mono badge-green">AUDITED & BALANCED</span>
        </div>
        <div class="journal-demo-row">
          <span>Dr. 6100-01 Office Rent & Facilities Expense (Dubai HQ)</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 42,857.14</span>
          <span>AED 0.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Dr. 2220-01 Input VAT Recoverable (5% UAE Standard Rate — Form 201 Box 9)</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 2,142.86</span>
          <span>AED 0.00</span>
        </div>
        <div class="journal-demo-row">
          <span>Cr. 1010-01 Corporate Operating Account (AED)</span>
          <span>AED 0.00</span>
          <span style="font-weight: 600; color: var(--color-navy);">AED 45,000.00</span>
        </div>
        <div class="journal-demo-total">
          <span>Balanced Journal Total</span>
          <span>Debit: AED 45,000.00</span>
          <span>Credit: AED 45,000.00 (Variance: AED 0.00)</span>
        </div>
      </div>

      <h2>Journal Voucher Approval Hierarchy & Correction Controls</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Voucher Class / Value</th>
            <th style="width: 35%;">Required Approval Hierarchy</th>
            <th style="width: 40%;">Mandatory Supporting Evidence & Rules</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Standard (&le; AED 25,000)</td>
            <td>Senior Accountant sign-off</td>
            <td>Vendor tax invoice, receipt voucher, or petty cash expense summary.</td>
          </tr>
          <tr>
            <td class="col-field">Material (&gt; AED 25,000)</td>
            <td>Dual sign-off: Chief Accountant + Finance Director</td>
            <td>Commercial contract, board-authorized capital approval, or bank advice.</td>
          </tr>
          <tr>
            <td class="col-field">Auto-Reversing Accruals</td>
            <td>Chief Accountant approval</td>
            <td>Check <em>[x] Auto-Reverse on Next Period Day 1</em> for month-end accruals.</td>
          </tr>
          <tr>
            <td class="col-field">Voucher Correction</td>
            <td>Chief Accountant approval</td>
            <td>Posted JVs cannot be edited; must post a linked <strong>Reversal Journal</strong>.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Creating and Posting a Double-Entry Journal Voucher</div>
        <ol class="proc-steps">
          <li>Click <strong>+ New Journal</strong> in the universal toolbar or navigate to the Journal Entries directory.</li>
          <li>Enter Voucher Date, select active Fiscal Period, and input a detailed commercial description in the Memo field.</li>
          <li>Add debit and credit lines, selecting accounts from the Chart of Accounts. Total Debits must equal Total Credits.</li>
          <li>Attach mandatory supporting PDF documentation (contracts, calculations, invoices).</li>
          <li>Click <strong>Submit for Approval</strong>. Once authorized by the appropriate role, click <strong>Post Journal</strong>.</li>
        </ol>
      </div>

      <div class="note-card" style="margin-top: 4pt; margin-bottom: 0;">
        <div class="note-card-title">General Ledger Immutability & Reversal Protocol</div>
        <strong>Statutory Audit Trail Mandate:</strong> In accordance with UAE Federal Decree-Law No. 47 of 2022 on Corporate Tax, posted journal vouchers cannot be edited or erased under any circumstances. Corrections are executed by clicking <strong>Reverse Journal</strong>, which generates an offsetting mirrored voucher with mandatory documented rationale and secondary approval sign-off.
      </div>
    </div>
    """

def get_page_13():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Chart_of_Accounts/01_Accounts_Tree.png",
        "Hierarchical Chart of Accounts Tree with Classification and Normal Balances",
        "/gl/coa",
        [
            ("Account Tree Directory", "Hierarchical tree showing account codes, titles, classifications, and active balances in AED."),
            ("Search Filter", "Search accounts instantly by 5-digit code, account title, or financial statement classification."),
            ("Classification Indicator", "Shows normal accounting balance (Debit vs. Credit) and statement mapping."),
            ("Map Sub-Account Trigger", "Direct row action to nest subsidiary child accounts under parent master codes.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 06 · MODULE 06</div>
          <div class="chapter-title">Chart of Accounts (COA Master)</div>
        </div>
        <div class="chapter-cat">GENERAL LEDGER ARCHITECTURE</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Chart of Accounts
      </div>

      <p>
        The Chart of Accounts (COA) establishes the unified financial accounting taxonomy for all legal entities within the organization. It enforces standardized 5-digit account numbering aligned with International Financial Reporting Standards (IFRS) and UAE GAAP.
      </p>

      {wf}

      <h2>Standard 5-Digit General Ledger Numbering Structure</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 18%;">Code Block</th>
            <th style="width: 25%;">Account Classification</th>
            <th style="width: 15%;">Normal Balance</th>
            <th style="width: 42%;">Representative Financial Accounts & Sub-Ledger Mappings</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>10000 - 19999</code></td>
            <td><strong>Assets (Current & Non-Current)</strong></td>
            <td><span class="badge-mono badge-blue">Debit</span></td>
            <td>10100 Bank Operating, 12000 AR Control (Locked), 14000 Inventory, 15000 Fixed Assets.</td>
          </tr>
          <tr>
            <td><code>20000 - 29999</code></td>
            <td><strong>Liabilities (Current & Long-Term)</strong></td>
            <td><span class="badge-mono badge-amber">Credit</span></td>
            <td>21000 AP Control (Locked), 22100 Output VAT, 22200 Input VAT, 22300 FTA Settlement, 22500 Gratuity.</td>
          </tr>
          <tr>
            <td><code>30000 - 39999</code></td>
            <td><strong>Equity & Reserves</strong></td>
            <td><span class="badge-mono badge-amber">Credit</span></td>
            <td>30100 Share Capital, 30500 Retained Earnings, 31000 Current Year Profit/Loss Clearing.</td>
          </tr>
          <tr>
            <td><code>40000 - 49999</code></td>
            <td><strong>Operating Revenue</strong></td>
            <td><span class="badge-mono badge-amber">Credit</span></td>
            <td>40000 Commercial Sales Revenue, 41000 Service Consulting Fees, 49000 Other Income.</td>
          </tr>
          <tr>
            <td><code>50000 - 59999</code></td>
            <td><strong>Cost of Goods Sold (COGS)</strong></td>
            <td><span class="badge-mono badge-blue">Debit</span></td>
            <td>50100 Direct Materials Intake, 50200 Inbound Freight & Customs, 52000 Purchase Price Variance.</td>
          </tr>
          <tr>
            <td><code>60000 - 69999</code></td>
            <td><strong>Operating Expenses (OpEx)</strong></td>
            <td><span class="badge-mono badge-blue">Debit</span></td>
            <td>61000 Facilities & Rent, 62000 Marketing, 63000 Salaries, 63500 Gratuity Expense, 65000 Depreciation.</td>
          </tr>
        </tbody>
      </table>

      <h2>Account Governance & Control Account Lock Rules</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Header Accounts</h4>
          <p>Level-1 parent accounts (e.g. 10000 Current Assets) are non-posting summary nodes used strictly for report rollups.</p>
        </div>
        <div class="matching-card">
          <h4>Sub-Ledger Locks</h4>
          <p>Accounts 12000 (AR Control) and 21000 (AP Control) reject manual journal vouchers to prevent GL/sub-ledger divergence.</p>
        </div>
        <div class="matching-card">
          <h4>Post-Closing Lock</h4>
          <p>Creating or archiving accounts requires Chief Accountant sign-off and is locked while a monthly financial close is in progress.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Adding a Subsidiary Child Account (+ Map Sub)</div>
        <ol class="proc-steps">
          <li>Locate target parent account in the tree (e.g. <em>10100 Corporate Bank Accounts</em>) and click <strong>+ Map Sub</strong>.</li>
          <li>Enter the 5-digit child code (e.g. <code>10102</code>) and descriptive title (e.g. <em>Commercial Bank Dubai Operating AED</em>).</li>
          <li>Specify currency (AED/USD) and verify that the normal balance (Debit) inherits from the parent class.</li>
          <li>Link to appropriate financial statement line (Balance Sheet ➔ Cash and Cash Equivalents).</li>
          <li>Click <strong>Save & Map</strong> to commit child account to the live chart of accounts.</li>
        </ol>
      </div>
    </div>
    """

def get_page_14():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Inventory/01_Inventory_Master.png",
        "Inventory Master Catalog with Multi-Tier Category Hierarchy and SKU Attributes",
        "/inventory/master",
        [
            ("Inventory Catalog View", "Master directory of all registered stock keeping units (SKUs) and valuation balances."),
            ("Category Setup Toolbar", "Actions to Add Category, Sub Category, Attribute Criterion, and Attribute Values."),
            ("SKU Creation Trigger", "Button to register new stock items and link supplier catalog codes."),
            ("Reorder Point Monitor", "Flags inventory lots falling below safety stock minimum thresholds.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 07 · MODULE 07 (PART 1)</div>
          <div class="chapter-title">Inventory Master Catalog & Valuation</div>
        </div>
        <div class="chapter-cat">SUPPLY CHAIN & LOGISTICS</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Inventory & Warehousing ➔ Master Catalog
      </div>

      <p>
        The Inventory & Warehousing module maintains perpetual inventory balances, multi-warehouse bin locations, and SKU master data. It governs stock intake, valuation accounting, and direct integration with commercial sales.
      </p>

      {wf}

      <h2>Supported Inventory Valuation Methodologies</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Valuation Methodology</th>
            <th style="width: 35%;">System Accounting Engine Behavior</th>
            <th style="width: 40%;">Operational & Financial Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Moving Weighted Average (Standard Default)</td>
            <td>Unit cost automatically recalculates upon each GRN intake: <code>(Current Value + Inbound Value) / Total Qty</code>.</td>
            <td>Smooths price fluctuations; standard across high-volume distribution. Balance sheet reflects current weighted average.</td>
          </tr>
          <tr>
            <td class="col-field">Perpetual FIFO (Configurable by Category)</td>
            <td>Maintains discrete cost layers by GRN batch date. Sales orders relieve cost from the oldest available batch first.</td>
            <td>Accurately matches physical flow of perishable or date-sensitive goods. Preserves original lot acquisition costs.</td>
          </tr>
          <tr>
            <td class="col-field">Configuration Scope</td>
            <td>Configurable at Product Category level in Master Catalog</td>
            <td>Selected at category setup; locked once transactions are posted to ensure accounting consistency under IFRS.</td>
          </tr>
        </tbody>
      </table>

      <h2>Relational SKU Master Data Hierarchy</h2>
      <div class="process-strip">
        <span class="process-strip-title">SKU Hierarchy:</span>
        <span class="process-node">Category</span>
        <span class="process-arrow">➔</span>
        <span class="process-node">Sub Category</span>
        <span class="process-arrow">➔</span>
        <span class="process-node">Attribute Criterion</span>
        <span class="process-arrow">➔</span>
        <span class="process-node">Attribute Value</span>
        <span class="process-arrow">➔</span>
        <span class="process-node">Unit of Measure (UOM)</span>
        <span class="process-arrow">➔</span>
        <span class="process-node process-node-active">SKU Master</span>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Creating an Inventory SKU and Assigning Costing Policy</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Inventory ➔ Master Catalog</strong> and click <strong>+ Add SKU</strong>.</li>
          <li>Assign Category and Sub Category; confirm the inherited valuation policy (Moving Average or FIFO).</li>
          <li>Input SKU Code, Description, barcode, Unit of Measure (e.g. PCS, BOX), and reorder threshold quantity.</li>
          <li>Map linked GL accounts: Inventory Asset (14000), COGS (50100), and Sales Revenue (40000).</li>
          <li>Click <strong>Save SKU</strong>. Item is activated across sales orders, purchase orders, and warehouse intake.</li>
        </ol>
      </div>

      <h2>Unit of Measure (UOM) Multipliers & Reorder Thresholds</h2>
      <div class="sop-meta-grid" style="margin-top: 3.5pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Stocking vs. Purchasing UOM</div>
          <div class="sop-meta-desc">Base inventory is held in discrete Units (PCS). Supplier purchasing orders in Cartons (CTN) or Pallets (PLT) apply fixed conversion multipliers upon GRN intake.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Automated Safety Stock Alarms</div>
          <div class="sop-meta-desc">When available stock (On-Hand minus Reserved) breaches the reorder threshold, the system flags the SKU in the procurement replenishment queue.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Valuation Consistency Check</div>
          <div class="sop-meta-desc">Under IFRS, changing valuation method (FIFO to Weighted Average) requires retrospective disclosure and CFO sign-off; in-system switches are locked during active periods.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Physical Barcode Integration</div>
          <div class="sop-meta-desc">EAN-13 and Code-128 barcodes printed on physical bin tags enable instant handheld barcode scanner intake during GRN receiving.</div>
        </div>
      </div>
    </div>
    """

def get_page_15():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Inventory/02_Goods_Received_Notes.png",
        "Goods Received Notes (GRN) Intake Register with Inspection Status",
        "/inventory/grn",
        [
            ("GRN Intake Directory", "GRN reference numbers, linked PO numbers, supplier names, received quantities, and QA status."),
            ("Certify GRN Action", "Official warehouse receipt confirmation updating perpetual inventory asset balances in Class 1400."),
            ("Quarantine Hold Indicator", "Flags shipments pending quality control inspection or damaged in transit."),
            ("Discrepancy Certificate", "Generates damaged goods certificates for automated debit note claims.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 07 · MODULE 07 (PART 2)</div>
          <div class="chapter-title">Goods Received Notes (GRN) & Intake</div>
        </div>
        <div class="chapter-cat">WAREHOUSING & INTAKE CONTROL</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Inventory & Warehousing ➔ GRN
      </div>

      <p>
        The Goods Received Notes (GRN) module governs physical stock intake into corporate warehouse facilities. It enforces technical quality inspections, records lot discrepancies, and automates perpetual inventory general ledger postings.
      </p>

      {wf}

      <h2>Landed Cost Allocation & Inventory Valuation Capitalization</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Landed Cost Component</th>
            <th style="width: 35%;">Allocation Methodology</th>
            <th style="width: 40%;">General Ledger Accounting Treatment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Inbound Freight & Shipping</td>
            <td>Apportioned by weight or line-item value</td>
            <td>Capitalized into inventory: <strong>Dr. 14000 Inventory / Cr. 21000 Freight Vendor AP</strong>.</td>
          </tr>
          <tr>
            <td class="col-field">UAE Customs Duties (5%)</td>
            <td>Calculated on CIF value declared to Dubai Customs</td>
            <td>Capitalized into item cost: <strong>Dr. 14000 Inventory / Cr. 21000 Customs Clearing</strong>.</td>
          </tr>
          <tr>
            <td class="col-field">Local Handling & Port Fees</td>
            <td>Direct fee allocation to received lot</td>
            <td>Increases unit cost basis prior to commercial sale, ensuring accurate gross margin reporting.</td>
          </tr>
        </tbody>
      </table>

      <h2>Damaged Stock Quarantine & Debit Note Protocol</h2>
      <div class="matching-grid">
        <div class="matching-card">
          <h4>Physical Quarantine Holding</h4>
          <p>Damaged or non-compliant goods are routed to Quarantine Holding (Bay 09), locked from inclusion in sales orders.</p>
        </div>
        <div class="matching-card">
          <h4>Discrepancy Certification</h4>
          <p>Warehouse inspector records photos and issues an electronic Discrepancy Certificate transmitted to vendor within 24 hours.</p>
        </div>
        <div class="matching-card">
          <h4>Debit Note Generation</h4>
          <p>Rejection sign-off automatically drafts a Debit Note in Supplier Activity, decrementing billable amounts before payment release.</p>
        </div>
      </div>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Receiving Stock and Certifying a GRN</div>
        <ol class="proc-steps">
          <li>Upon shipment delivery, navigate to <strong>Inventory ➔ GRN</strong> and locate the approved Purchase Order.</li>
          <li>Perform physical piece count and QA inspection. Enter accepted quantity and rejected quantity with reason codes.</li>
          <li>Assign accepted goods to designated warehouse bins (e.g. <em>Main Dubai Warehouse — Bay 04</em>).</li>
          <li>If freight or customs invoices exist, click <strong>Allocate Landed Costs</strong> to capitalize them into unit costs.</li>
          <li>Click <strong>Certify GRN</strong>. Updates Class 14000 inventory balance and clears shipment for supplier 3-way matching.</li>
        </ol>
      </div>

      <h2>Inbound Quality Inspection & Return-to-Vendor (RTV) Matrix</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Inspection Dimension</th>
            <th style="width: 35%;">Acceptance & Verification Criteria</th>
            <th style="width: 40%;">Non-Compliance & Quarantine Protocol</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Physical Seal & Packaging</td>
            <td>Container seal matches ocean bill of lading / airway bill</td>
            <td>Broken seals require joint survey with customs broker and maritime insurer.</td>
          </tr>
          <tr>
            <td class="col-field">Lot & Expiry Tracking</td>
            <td>Batch numbers and expiry dates recorded on intake</td>
            <td>Goods with &lt; 80% remaining shelf life require Commercial Director waiver.</td>
          </tr>
          <tr>
            <td class="col-field">Surplus Delivery Protocol</td>
            <td>Inbound quantity exceeds PO by &gt; 0.0%</td>
            <td>Surplus held in staging area; buyer must issue PO amendment or return excess.</td>
          </tr>
        </tbody>
      </table>

      <h2>Warehouse Bin Storage & High-Value Serial Logging</h2>
      <div class="sop-meta-grid" style="margin-top: 3pt;">
        <div class="sop-meta-item">
          <div class="sop-meta-title">Physical Bin Locators</div>
          <div class="sop-meta-desc">Intake items are assigned to discrete bin addresses (e.g. <code>DXB-W1-A04-B02</code>) to optimize warehouse pick-path routing.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Serialized Equipment Capture</div>
          <div class="sop-meta-desc">High-value IT hardware and machinery require unique serial number scanning during GRN certification before GL posting.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Real-Time Stock Relief</div>
          <div class="sop-meta-desc">Certified GRN balances immediately populate available-to-promise (ATP) inventory for customer order allocation.</div>
        </div>
        <div class="sop-meta-item">
          <div class="sop-meta-title">Automated Debit Notes</div>
          <div class="sop-meta-desc">Rejected lots generate automated vendor debit notes that deduct from outstanding payable vouchers in Module 04.</div>
        </div>
      </div>

      <div class="note-card" style="margin-top: 3.5pt; margin-bottom: 0;">
        <div class="note-card-title">Warehouse Physical Cycle Counting & Perpetual Audit</div>
        <strong>Blind Count Verification:</strong> Periodic cycle counts require warehouse inventory clerks to perform blind item counts without visibility into current GL system ledger balances. Variances exceeding 1.0% trigger an automatic physical recounting protocol and require Chief Accountant adjustment authorization.
      </div>
    </div>
    """

def get_page_16():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Assets/06_Asset_Register.png",
        "Fixed Asset Register with Capitalization Values and Depreciation Schedules",
        "/assets/register",
        [
            ("Asset Register Table", "Asset serial tags, descriptions, purchase costs, accumulated depreciation, and net book value in AED."),
            ("Category Filter", "Filter by Land, Buildings, Plant & Machinery, Vehicles, and IT Equipment."),
            ("Depreciation Run Action", "Automated trigger calculating monthly straight-line depreciation across all active assets."),
            ("Asset Tagging Modal", "Register asset identifiers, physical barcodes, and cost center assignments.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-pill">CHAPTER 08 · MODULE 08</div>
          <div class="chapter-title">Fixed Assets & Depreciation Accounting</div>
        </div>
        <div class="chapter-cat">CAPITAL ASSETS & DEPRECIATION</div>
      </div>

      <div class="nav-breadcrumb">
        <span>📍</span> <strong>Navigation Path:</strong> Sidebar Menu ➔ Assets ➔ Asset Register
      </div>

      <p>
        The Fixed Assets module maintains the statutory fixed asset register, capital asset identification tags, and automated monthly depreciation schedules. It ensures full compliance with IFRS IAS 16 property, plant, and equipment reporting standards.
      </p>

      {wf}

      <h2>Illustrative Corporate Depreciation Policies (Configurable under IAS 16)</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Asset Class Category</th>
            <th style="width: 20%;">Useful Lifespan (Policy)</th>
            <th style="width: 20%;">Depreciation Method</th>
            <th style="width: 35%;">General Ledger Account Mapping</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Buildings & Facilities</td>
            <td>20 Years (240 Mos)</td>
            <td>5.0% Straight-Line</td>
            <td>Asset: 15100 / Acc. Dep: 15190 / Dep. Expense: 65100</td>
          </tr>
          <tr>
            <td class="col-field">Plant & Machinery</td>
            <td>10 Years (120 Mos)</td>
            <td>10.0% Straight-Line</td>
            <td>Asset: 15200 / Acc. Dep: 15290 / Dep. Expense: 65200</td>
          </tr>
          <tr>
            <td class="col-field">Motor Vehicles</td>
            <td>5 Years (60 Mos)</td>
            <td>20.0% Straight-Line</td>
            <td>Asset: 15300 / Acc. Dep: 15390 / Dep. Expense: 65300</td>
          </tr>
          <tr>
            <td class="col-field">IT Hardware & Servers</td>
            <td>3 Years (36 Mos)</td>
            <td>33.3% Straight-Line</td>
            <td>Asset: 15400 / Acc. Dep: 15490 / Dep. Expense: 65400</td>
          </tr>
          <tr>
            <td class="col-field">Office Furniture & Fixtures</td>
            <td>7 Years (84 Mos)</td>
            <td>14.3% Straight-Line</td>
            <td>Asset: 15500 / Acc. Dep: 15590 / Dep. Expense: 65500</td>
          </tr>
        </tbody>
      </table>

      <h2>Asset Capitalization, Impairment & Disposal Accounting</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 25%;">Asset Lifecycle Event</th>
            <th style="width: 35%;">Double-Entry Accounting Treatment</th>
            <th style="width: 40%;">Statutory & UAE Corporate Tax Treatment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Capitalization from CIP</td>
            <td>Dr. 15200 Fixed Asset / Cr. 15900 Construction in Progress</td>
            <td>Capitalizes asset upon commissioning; initiates monthly straight-line depreciation.</td>
          </tr>
          <tr>
            <td class="col-field">Commercial Sale of Asset</td>
            <td>Dr. 10100 Bank / Dr. 15290 Acc. Dep / Cr. 15200 Asset Cost</td>
            <td>Net proceeds recognized in Account 49200 (Gain) or 69200 (Loss on Asset Disposal).</td>
          </tr>
          <tr>
            <td class="col-field">Scrap / Retirement</td>
            <td>Dr. 15290 Acc. Dep / Dr. 69300 Impairment / Cr. 15200 Cost</td>
            <td>Asset retired permanently from register; tax pooling adjustments applied.</td>
          </tr>
        </tbody>
      </table>

      <div class="proc-box">
        <div class="proc-title"><span>⚡</span> Standard Operating Procedure: Capitalizing an Asset and Executing Depreciation</div>
        <ol class="proc-steps">
          <li>Navigate to <strong>Assets ➔ Asset Register</strong> and click <strong>+ Add Asset</strong>.</li>
          <li>Enter asset title, serial number, physical barcode identifier, and assign branch cost center location.</li>
          <li>Select Asset Category; confirm useful lifespan and straight-line depreciation percentage per company policy.</li>
          <li>Link purchase bill to establish verified historical acquisition cost in AED. Click <strong>Save & Capitalize</strong>.</li>
          <li>At month-end, click <strong>Run Depreciation Batch</strong>. System generates automated GL entry: <em>Dr. 65000 / Cr. Accumulated Dep</em>.</li>
        </ol>
      </div>
    </div>
    """

print("Pages 09-16 module finalized.")

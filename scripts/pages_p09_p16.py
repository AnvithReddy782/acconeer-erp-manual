# scripts/pages_p09_p16.py
from generate_complete_manual import window_frame

def get_page_09():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Customer_Activity/03_Sales_Order.png",
        "Commercial Sales Order Register with Customer Fulfillment Tracking",
        "/customers/orders",
        [
            ("Action Trigger", "+ New sales order button to initiate a verified customer order."),
            ("Search & Filter", "Search bar for order #, customer, or PO, plus ALL status dropdown filter."),
            ("6-Column Grid", "Order, Customer, Date, Status, Total, and Actions columns."),
            ("Order Lifecycle", "Real-time tracking of order fulfillment prior to delivery and invoice posting.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · ORDER-TO-CASH</div>
          <div class="chapter-title">Sales Orders & Customer Order Management</div>
        </div>
        <div class="chapter-right-meta">MODULE 05<br>/customers/orders</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Customer Activity ➔ Sales Order (or <kbd>Alt + S</kbd>)
      </div>

      <p>
        The Sales Order interface manages confirmed commercial sales orders placed by customers. Booking an order reserves inventory quantities, checks customer credit availability, and establishes the source record for delivery fulfillment and billing.
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
            <td class="col-field">+ New sales order</td>
            <td>Solid Purple Button</td>
            <td>Opens order creation form to select customer, delivery date, currency, line items, and pricing.</td>
          </tr>
          <tr>
            <td class="col-field">Search Input Bar</td>
            <td>Text Field</td>
            <td>Instant real-time search across sales order numbers, customer names, and customer purchase orders.</td>
          </tr>
          <tr>
            <td class="col-field">Status Filter Dropdown</td>
            <td>Selection Menu</td>
            <td>Filters order table by status: <code>ALL</code>, <code>Draft</code>, <code>Confirmed</code>, <code>Shipped</code>, <code>Billed</code>, or <code>Cancelled</code>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Data Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 18%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 64%;">On-Screen Information & Operational Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Order</td>
            <td>Sequential Link</td>
            <td>Unique sales order identifier (e.g. <code>SO-2026-0001</code>); clickable to view ordered items and terms.</td>
          </tr>
          <tr>
            <td class="col-field">Customer</td>
            <td>Account Name</td>
            <td>Registered commercial counterparty name linked to Customer Directory.</td>
          </tr>
          <tr>
            <td class="col-field">Date</td>
            <td>Date Stamp</td>
            <td>Order confirmation date defining contract commitment point.</td>
          </tr>
          <tr>
            <td class="col-field">Status</td>
            <td>Badge</td>
            <td>Fulfillment stage indicator (e.g. <code>Open</code>, <code>In Production</code>, <code>Fulfilled</code>).</td>
          </tr>
          <tr>
            <td class="col-field">Total</td>
            <td>Currency Amount</td>
            <td>Committed commercial value in AED inclusive of calculated taxes.</td>
          </tr>
          <tr>
            <td class="col-field">Actions</td>
            <td>Context Menu</td>
            <td>Menu triggers to <em>Convert to Delivery Note</em>, <em>Generate Sales Invoice</em>, or <em>Print Order</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Order Fulfillment Lifecycle Badges & System Transitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Status Badge</th>
            <th style="width: 38%;">Operational Fulfillment State</th>
            <th style="width: 40%;">Inventory & Commercial System Effect</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Draft</td>
            <td>Sales quote or preliminary booking in progress.</td>
            <td>Prices editable; inventory is not yet allocated or reserved.</td>
          </tr>
          <tr>
            <td class="col-field">Confirmed</td>
            <td>Customer purchase authorization verified.</td>
            <td>Locks required SKU stock quantities in warehouse inventory.</td>
          </tr>
          <tr>
            <td class="col-field">In Production</td>
            <td>Warehouse picking and staging underway.</td>
            <td>Generates dispatch manifest; triggers warehouse staff packing list.</td>
          </tr>
          <tr>
            <td class="col-field">Shipped</td>
            <td>Goods physically dispatched from dock.</td>
            <td>Generates Delivery Note; relieves stock from Inventory Asset (1400).</td>
          </tr>
          <tr>
            <td class="col-field">Billed</td>
            <td>Final commercial tax invoice generated.</td>
            <td>Posts revenue to Account 4000 and customer debt to Account 1200.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no orders exist for the active legal entity, the grid displays: <em>"No sales orders yet."</em> Click the purple <strong>+ New sales order</strong> button to book your first commercial customer order.
      </div>
    </div>
    """

def get_page_10():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Supplier_Activity/03_Bills.png",
        "Supplier Purchase Bills Register with AI OCR Scan and AP Status",
        "/bills",
        [
            ("Action Bar", "Upload & OCR Scan and + New Purchase Bill action buttons."),
            ("4 Metric Cards", "Total Receivables (AR), Total Payables (AP), Sales Invoiced, and OCR & GL Automated."),
            ("Search & Export", "Multi-attribute text search bar, All Statuses dropdown, and Excel/PDF export buttons."),
            ("Payables Data Grid", "8-column table tracking Bill #, Type, Supplier, Dates, Total Amount, GL Status, Status, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · PROCURE-TO-PAY</div>
          <div class="chapter-title">Supplier Bills & Accounts Payable (AP)</div>
        </div>
        <div class="chapter-right-meta">MODULE 06<br>/bills</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Supplier Activity ➔ Bills (or <kbd>Alt + P</kbd>)
      </div>

      <p>
        The Supplier Bills workspace manages accounts payable liabilities, vendor tax invoice processing, automated AI OCR document ingestion, and synchronous double-entry General Ledger voucher posting.
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
            <td class="col-field">+ New Purchase Bill</td>
            <td>White Border Button</td>
            <td>Opens manual bill entry form to select vendor, enter vendor invoice number, line items, and tax.</td>
          </tr>
          <tr>
            <td class="col-field">Upload & OCR Scan</td>
            <td>Solid Purple Button</td>
            <td>Triggers AI optical character recognition to upload scanned PDFs/receipts and auto-extract billing data.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Downloads current filtered payables register directly to spreadsheet or formatted PDF document.</td>
          </tr>
          <tr>
            <td class="col-field">All Statuses</td>
            <td>Dropdown Filter</td>
            <td>Filters bill register by lifecycle state: All Statuses, Draft, Approved, Paid, or Overdue.</td>
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
            <td>Displays outstanding customer receivables for cross-module cash context.</td>
          </tr>
          <tr>
            <td class="col-field">Total Payables (AP)</td>
            <td><code>AED 0.00</code></td>
            <td>Cumulative outstanding vendor obligations awaiting payment authorization (synced from Account 2010).</td>
          </tr>
          <tr>
            <td class="col-field">Sales Invoiced (Period)</td>
            <td><code>AED 0.00</code></td>
            <td>Enterprise billed revenue context for commercial cash flow comparison.</td>
          </tr>
          <tr>
            <td class="col-field">OCR & GL Automated</td>
            <td><code>0 Docs / 0 Posted</code></td>
            <td>Automation counter showing OCR-parsed supplier bills versus auto-posted General Ledger vouchers.</td>
          </tr>
        </tbody>
      </table>

      <h2>Payables Data Grid Columns & Actions</h2>
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
            <td>Vendor invoice reference number; clickable to inspect line items, tax, and OCR attachments.</td>
          </tr>
          <tr>
            <td class="col-field">Customer / Vendor</td>
            <td>Trade Name</td>
            <td>Supplier legal business name and tax registration number (TRN) from Vendor Directory.</td>
          </tr>
          <tr>
            <td class="col-field">Dates & Total Amount</td>
            <td>Date & Currency</td>
            <td>Bill issuance date, payment due date, and gross payable amount in AED inclusive of 5% VAT.</td>
          </tr>
          <tr>
            <td class="col-field">GL Ledger Status</td>
            <td>Sync Indicator</td>
            <td>Real-time General Ledger posting status (<code>Posted</code>, <code>Pending Sync</code>, <code>Error</code>).</td>
          </tr>
          <tr>
            <td class="col-field">Status & Actions</td>
            <td>Badge & Action Menu</td>
            <td>Payment badge (Draft, Approved, Paid, Overdue) and action menu to Schedule Payment or Issue Debit Note.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no vendor bills exist in the active scope, the screen displays: <em>"No invoices found — Upload an invoice via AI OCR or create a new invoice to start auto-posting to the General Ledger."</em>
      </div>
    </div>
    """

def get_page_11():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Supplier_Activity/01_Vendor_Directory.png",
        "Vendor and Supplier Master Directory with AP Creditor Telemetry",
        "/vendors",
        [
            ("Top Action Buttons", "Excel, PDF, and + Add New Supplier action buttons."),
            ("4 Metric Cards", "Active Customers, Total AR Outstanding, Active Suppliers/Vendors, and Total AP Payables."),
            ("Filter Controls", "Text search bar, Legal Entity dropdown, Currencies, Jurisdictions, and Statuses filters."),
            ("Creditors Data Grid", "7-column table tracking Entity Code & Name, Contact, Auto-Linked GL, Terms, Balance, Status, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">COMMERCIAL & CASH · VENDOR MASTER</div>
          <div class="chapter-title">Vendor Master Directory & Disbursement Controls</div>
        </div>
        <div class="chapter-right-meta">MODULE 07<br>/vendors</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Supplier Activity ➔ Vendors/ Suppliers
      </div>

      <p>
        The Vendors / Suppliers directory provides centralized governance for procurement counterparties, managing trade creditor onboarding, bank disbursement details, payment terms, and automated sub-ledger mapping.
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
            <td class="col-field">+ Add New Supplier</td>
            <td>Solid Purple Button</td>
            <td>Opens vendor registration modal to record trade name, TRN, bank IBAN, and payment terms.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Exports complete filtered vendor master database to spreadsheet or formal directory document.</td>
          </tr>
          <tr>
            <td class="col-field">Filter Dropdowns</td>
            <td>4 Top Dropdowns</td>
            <td>Filters directory by Legal Entity LLC, Currency (AED/USD), Country Jurisdiction, and Status.</td>
          </tr>
          <tr>
            <td class="col-field">Search Input Bar</td>
            <td>Text Field</td>
            <td>Instant multi-field search across supplier trade name, vendor code, and auto-linked GL account.</td>
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
            <td class="col-field">ACTIVE CUSTOMERS</td>
            <td><code>0</code></td>
            <td>Debtor count context; indicates customers auto-linked to Account 1020 (Accounts Receivable).</td>
          </tr>
          <tr>
            <td class="col-field">TOTAL AR OUTSTANDING</td>
            <td><code>AED 0.00</code></td>
            <td>Total outstanding receivables across all customer sub-ledgers.</td>
          </tr>
          <tr>
            <td class="col-field">ACTIVE SUPPLIERS</td>
            <td><code>0</code></td>
            <td>Active onboarded trade creditors auto-linked to Account 2010 (Accounts Payable).</td>
          </tr>
          <tr>
            <td class="col-field">TOTAL AP PAYABLES</td>
            <td><code>AED 0.00</code></td>
            <td>Cumulative balance owed across all supplier sub-ledgers awaiting disbursement.</td>
          </tr>
        </tbody>
      </table>

      <h2>Vendor Directory Grid Columns & System Actions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 60%;">On-Screen Information & Accounting Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Entity Code & Name</td>
            <td>Code & Legal Name</td>
            <td>Internal vendor code (e.g. <code>VND-00101</code>) and registered corporate business name.</td>
          </tr>
          <tr>
            <td class="col-field">Contact Info</td>
            <td>Email & Phone</td>
            <td>Official procurement email address, telephone contact, and billing physical address.</td>
          </tr>
          <tr>
            <td class="col-field">Auto-Linked GL</td>
            <td>Account Number</td>
            <td>Designated Accounts Payable sub-account mapped under Account 2010.</td>
          </tr>
          <tr>
            <td class="col-field">Payment Terms</td>
            <td>Credit Window</td>
            <td>Agreed payment terms (e.g. <em>Net 30 Days</em>, <em>Due on Receipt</em>, <em>Advance</em>).</td>
          </tr>
          <tr>
            <td class="col-field">GL Ledger Balance</td>
            <td>Live Currency</td>
            <td>Real-time balance owed to the vendor calculated from posted bills minus payments.</td>
          </tr>
          <tr>
            <td class="col-field">Status & Actions</td>
            <td>Badge & Actions</td>
            <td>Creditor status (Active/Hold) and menu triggers to Edit Profile, View Statement, or Make Payment.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no suppliers match the active search or scope filters, the table displays: <em>"No suppliers found matching your filter criteria."</em> Click <strong>+ Add New Supplier</strong> to onboard a vendor.
      </div>
    </div>
    """

def get_page_12():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/General_Ledger/01_Journal_Entries.png",
        "General Ledger Journal Entries Register with Double-Entry Verification",
        "/general-ledger",
        [
            ("Top Actions", "Export to Excel (.xlsx) and + New Journal Entry primary action buttons."),
            ("Filter Tabs", "All Entries (0) and Posted (0) quick-filter tabs."),
            ("Search Input", "Search entry #, reference, memo... real-time multi-field search bar."),
            ("Journal Grid", "6-column table tracking Voucher # & Date, Reference/Memo, Source/User, Attachments, Amount, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GENERAL LEDGER · DOUBLE-ENTRY ACCOUNTING</div>
          <div class="chapter-title">General Ledger & Journal Entries</div>
        </div>
        <div class="chapter-right-meta">MODULE 08<br>/general-ledger</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Journal Entries (or <kbd>Alt + J</kbd>)
      </div>

      <p>
        The General Ledger workspace serves as the authoritative double-entry accounting register in Acconeer ERP. All financial events—whether entered manually or auto-posted from billing, payroll, or banking—are permanently recorded here as balanced vouchers.
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
            <td class="col-field">+ New Journal Entry</td>
            <td>Solid Purple Button</td>
            <td>Opens the double-entry voucher creation modal with debit/credit balancing validation.</td>
          </tr>
          <tr>
            <td class="col-field">Export to Excel (.xlsx)</td>
            <td>Solid Green Button</td>
            <td>Exports complete general ledger journal book to formatted Excel workbook.</td>
          </tr>
          <tr>
            <td class="col-field">All Entries (0)</td>
            <td>Active Black Pill</td>
            <td>Filter tab displaying all journal vouchers within the selected fiscal scope regardless of status.</td>
          </tr>
          <tr>
            <td class="col-field">Posted (0)</td>
            <td>Filter Tab</td>
            <td>Filter tab displaying only finalized, immutable journal entries that have posted to trial balances.</td>
          </tr>
        </tbody>
      </table>

      <h2>Journal Register Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 60%;">On-Screen Information & Accounting Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">VOUCHER # & DATE</td>
            <td>Code & Timestamp</td>
            <td>Sequential voucher code (e.g. <code>JV-2026-0042</code>) and effective accounting value date.</td>
          </tr>
          <tr>
            <td class="col-field">REFERENCE / MEMO</td>
            <td>Text Narration</td>
            <td>Operational description, external transaction memo, or adjustment justification narrative.</td>
          </tr>
          <tr>
            <td class="col-field">SOURCE / USER</td>
            <td>Origin Tag & User</td>
            <td>Sub-system source (Manual Entry, Invoicing, Payroll Run) and creator username.</td>
          </tr>
          <tr>
            <td class="col-field">ATTACHMENTS</td>
            <td>Document Counter</td>
            <td>Count of uploaded supporting audit documents (signed slips, receipts, agreements).</td>
          </tr>
          <tr>
            <td class="col-field">TOTAL AMOUNT</td>
            <td>Balanced Currency</td>
            <td>Total voucher value in AED; system enforces Total Debits must equal Total Credits before save.</td>
          </tr>
          <tr>
            <td class="col-field">ACTIONS</td>
            <td>Context Menu</td>
            <td>Menu triggers to <em>View Voucher Lines</em>, <em>Print Journal Slip</em>, or <em>Post Reversal Voucher</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Voucher Source System Classifications & Prefix Conventions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Voucher Prefix</th>
            <th style="width: 38%;">Originating Sub-System</th>
            <th style="width: 40%;">Default General Ledger Account Posting</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">JV-2026-XXXX</td>
            <td>Manual General Ledger Adjusting Voucher</td>
            <td>Discretionary accounts; requires dual-sign approval for high values.</td>
          </tr>
          <tr>
            <td class="col-field">INV-2026-XXXX</td>
            <td>Sales Invoicing Module Auto-Post</td>
            <td>Dr. Accounts Receivable (1020) / Cr. Sales (4000) / Cr. VAT (2200).</td>
          </tr>
          <tr>
            <td class="col-field">BIL-2026-XXXX</td>
            <td>Supplier Bills Payables Auto-Post</td>
            <td>Dr. Expense (5000/6000) / Dr. VAT (1300) / Cr. Accounts Payable (2010).</td>
          </tr>
          <tr>
            <td class="col-field">PAY-2026-XXXX</td>
            <td>Payroll Processing Engine Auto-Post</td>
            <td>Dr. Salaries (6010) / Cr. Payroll Clearing / Bank Account (1010).</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">EMPTY STATE NOTIFICATION</div>
        When no journal vouchers exist matching the selected filter or date window, the register displays: <em>"No journal entries match this filter."</em> Click <strong>+ New Journal Entry</strong> to create a manual voucher.
      </div>
    </div>
    """

def get_page_13():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Chart_of_Accounts/01_Accounts_Tree.png",
        "Chart of Accounts (COA) Hierarchical Tree Structure & Account Mapping",
        "/chart-of-accounts",
        [
            ("Top Actions", "Excel, PDF, Opening Balances, and + Map New Sub-Account action buttons."),
            ("Class Filters", "Category pills for All Accounts (1000-7999), Assets, Liabilities, Equity, Revenue, COGS, Expense."),
            ("Search Bar", "Search account code, name... real-time multi-field search input."),
            ("Hierarchical Tree", "Columns for Account Code, Title & Description, Classification, Type, Normal, Currency, Balance, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">GENERAL LEDGER · FINANCIAL FOUNDATION</div>
          <div class="chapter-title">Chart of Accounts Hierarchy & Account Mapping</div>
        </div>
        <div class="chapter-right-meta">MODULE 09<br>/chart-of-accounts</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Chart of Accounts (or <kbd>Alt + A</kbd>)
      </div>

      <p>
        The Chart of Accounts (COA) defines the foundational accounting architecture of Acconeer ERP. It establishes the multi-tier numerical hierarchy for balance sheet assets, liabilities, equity, revenues, and operating expenses.
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
            <td>Opens modal to map and create a subsidiary account under an existing parent code.</td>
          </tr>
          <tr>
            <td class="col-field">Opening Balances</td>
            <td>Teal Outline Button</td>
            <td>Opens interface to record starting debit/credit balances for newly migrated accounting ledgers.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Exports entire hierarchical chart of accounts to spreadsheet or formal audit document.</td>
          </tr>
          <tr>
            <td class="col-field">Account Class Pills</td>
            <td>Filter Buttons</td>
            <td>Pills to filter by class: Assets (1000s), Liabilities (2000s), Equity (3000s), Revenue (4000s), COGS (5000s), Expenses (6000s).</td>
          </tr>
        </tbody>
      </table>

      <h2>Tree Table Columns & Account Node Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 60%;">On-Screen Information & Accounting Purpose</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">ACCOUNT CODE</td>
            <td>Numeric Code</td>
            <td>4-digit primary code with lock icon indicating protected GAAP control account.</td>
          </tr>
          <tr>
            <td class="col-field">ACCOUNT TITLE</td>
            <td>Text & Subtext</td>
            <td>Official title (e.g. <em>Cash and Cash Equivalents</em>) and descriptive operational definition.</td>
          </tr>
          <tr>
            <td class="col-field">CLASSIFICATION</td>
            <td>Standard Tag</td>
            <td>Statutory accounting framework classification tag (e.g. <code>GAAP Primary</code>).</td>
          </tr>
          <tr>
            <td class="col-field">TYPE & NORMAL</td>
            <td>Badges</td>
            <td>Statement category badge (<code>ASSET</code>, <code>LIABILITY</code>) and natural balance (<code>DEBIT</code> or <code>CREDIT</code>).</td>
          </tr>
          <tr>
            <td class="col-field">CURRENT BALANCE</td>
            <td>Live Currency</td>
            <td>Cumulative balance in base currency (AED) calculated across all posted general ledger journals.</td>
          </tr>
          <tr>
            <td class="col-field">ACTIONS</td>
            <td>Context Trigger</td>
            <td>Clickable <code>+ Map Sub</code> trigger to instantly add a child ledger under that parent node.</td>
          </tr>
        </tbody>
      </table>

      <h2>Chart of Accounts Numerical Architecture & Range Hierarchy</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Code Range</th>
            <th style="width: 30%;">Account Class</th>
            <th style="width: 25%;">Normal Balance</th>
            <th style="width: 25%;">Financial Statement</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">1000 – 1999</td>
            <td>Current & Fixed Assets</td>
            <td>DEBIT</td>
            <td>Balance Sheet (Assets)</td>
          </tr>
          <tr>
            <td class="col-field">2000 – 2999</td>
            <td>Liabilities (AP, Accruals, VAT)</td>
            <td>CREDIT</td>
            <td>Balance Sheet (Liabilities)</td>
          </tr>
          <tr>
            <td class="col-field">3000 – 3999</td>
            <td>Equity & Retained Earnings</td>
            <td>CREDIT</td>
            <td>Balance Sheet (Equity)</td>
          </tr>
          <tr>
            <td class="col-field">4000 – 4999</td>
            <td>Operating Commercial Revenue</td>
            <td>CREDIT</td>
            <td>Profit & Loss (P&L)</td>
          </tr>
          <tr>
            <td class="col-field">5000 – 5999</td>
            <td>Cost of Goods Sold (COGS)</td>
            <td>DEBIT</td>
            <td>Profit & Loss (P&L)</td>
          </tr>
          <tr>
            <td class="col-field">6000 – 6999</td>
            <td>Operating & Administrative Expenses</td>
            <td>DEBIT</td>
            <td>Profit & Loss (P&L)</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">SUB-ACCOUNT NESTING GUIDANCE</div>
        Expanding a parent node displays subsidiary accounts. If no child accounts exist, the system indicates: <em>"No custom sub-accounts mapped under 1010. Click '+ Map Sub' to create one."</em> Use sub-accounts for individual bank accounts and credit cards.
      </div>
    </div>
    """

def get_page_14():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Inventory/01_Inventory_Master.png",
        "Inventory Master Catalog & Stock Valuation Management",
        "/inventory",
        [
            ("Top Actions", "Excel, PDF, Opening Balances, and + Add SKU action buttons."),
            ("Category Pills", "Filter items by category, raw materials, finished goods, and consumables."),
            ("Search Input", "Search SKU, item code, barcode, or product name in real-time."),
            ("Inventory Grid", "Tracks SKU Code, Description, Category, UOM, Valuation, Cost, Price, Stock on Hand, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INVENTORY & WAREHOUSE · STOCK CONTROLS</div>
          <div class="chapter-title">Inventory Master Catalog & Valuation Rules</div>
        </div>
        <div class="chapter-right-meta">MODULE 10<br>/inventory</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Inventory ➔ Inventory Master
      </div>

      <p>
        The Inventory Master workspace governs the corporate product catalog, warehouse stock balances, unit-of-measure definitions, reorder thresholds, and inventory valuation accounting methods (FIFO and Weighted Average Cost).
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
            <td class="col-field">+ Add SKU</td>
            <td>Solid Purple Button</td>
            <td>Opens product registration modal to define SKU code, name, UOM, cost price, and sales price.</td>
          </tr>
          <tr>
            <td class="col-field">+ Add Category</td>
            <td>Outline Button</td>
            <td>Creates a new product family taxonomy to group items for reporting and GL revenue mapping.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Downloads complete inventory catalog and stock-on-hand valuation report to spreadsheet or PDF.</td>
          </tr>
          <tr>
            <td class="col-field">Search Input Bar</td>
            <td>Text Field</td>
            <td>Real-time filter searching across SKU codes, item descriptions, and barcode identifiers.</td>
          </tr>
        </tbody>
      </table>

      <h2>Inventory Register Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 62%;">On-Screen Information & Operational Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">SKU Code</td>
            <td>Code & Barcode</td>
            <td>Unique product stock keeping unit (e.g. <code>SKU-ELC-0091</code>); links to item card.</td>
          </tr>
          <tr>
            <td class="col-field">Item Name & UOM</td>
            <td>Text & Unit Badge</td>
            <td>Commercial description and stock unit of measure (e.g. <code>PCS</code>, <code>BOX</code>, <code>KG</code>, <code>SET</code>).</td>
          </tr>
          <tr>
            <td class="col-field">Valuation Method</td>
            <td>Costing Badge</td>
            <td>Assigned inventory valuation rule: <code>FIFO</code> (First-In, First-Out) or <code>WAC</code> (Weighted Average Cost).</td>
          </tr>
          <tr>
            <td class="col-field">Cost Price & Selling Price</td>
            <td>Currency Amounts</td>
            <td>Standard unit acquisition cost and default commercial sales price in AED.</td>
          </tr>
          <tr>
            <td class="col-field">Stock on Hand</td>
            <td>Numeric Counter</td>
            <td>Physical quantity currently located across active warehouse facilities.</td>
          </tr>
          <tr>
            <td class="col-field">Actions</td>
            <td>Context Menu</td>
            <td>Options to <em>Adjust Stock Quantity</em>, <em>View Stock Movement Ledger</em>, or <em>Edit SKU Specs</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Stock Level Indicators & Automated Reorder Alert Thresholds</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Stock Indicator</th>
            <th style="width: 38%;">Warehouse Inventory Condition</th>
            <th style="width: 40%;">System Alert & Procurement Action Trigger</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">In Stock</td>
            <td>Stock on hand exceeds minimum safety buffer.</td>
            <td>Available for sales order allocation and delivery notes.</td>
          </tr>
          <tr>
            <td class="col-field">Low Stock Alert</td>
            <td>Quantity falls below designated Reorder Point.</td>
            <td>Amber badge displayed; triggers automated purchase requisition.</td>
          </tr>
          <tr>
            <td class="col-field">Out of Stock</td>
            <td>Zero physical units remaining in active bins.</td>
            <td>Red alert; delivery notes blocked unless backorder is approved.</td>
          </tr>
          <tr>
            <td class="col-field">Quarantined</td>
            <td>Damaged or uninspected GRN shipments.</td>
            <td>Held in Account 1410 (Quarantine Stock) pending quality sign-off.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">GENERAL LEDGER INTEGRATION</div>
        Every inventory receipt or dispatch automatically posts balancing vouchers: Inventory Receipts credit Account 2010 (AP) and debit Account 1400 (Inventory Asset); Sales Dispatches debit Account 5000 (COGS) and credit Account 1400.
      </div>
    </div>
    """

def get_page_15():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Inventory/11_Goods_Received_Note.png",
        "Goods Received Notes (GRN) & Warehouse Inbound Intake Register",
        "/inventory/grn",
        [
            ("Top Actions", "Export and + New Goods Received Note primary action buttons."),
            ("Search & Filter", "Search by GRN #, PO #, supplier name, and status filter dropdown."),
            ("Receiving Grid", "Columns for GRN #, PO Reference, Supplier, Receipt Date, Location, Qty, Status, Actions."),
            ("3-Way Match Link", "Direct verification of physically received goods against purchase orders.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">INVENTORY & WAREHOUSE · INBOUND RECEIVING</div>
          <div class="chapter-title">Goods Received Notes (GRN) & Warehouse Intake</div>
        </div>
        <div class="chapter-right-meta">MODULE 11<br>/inventory/grn</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Inventory ➔ Goods Received Note (GRN)
      </div>

      <p>
        The Goods Received Note (GRN) workspace logs physical warehouse deliveries from suppliers. Creating a GRN validates delivered goods against purchase order quantities, performs quality inspection, and updates perpetual inventory asset ledgers.
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
            <td class="col-field">+ New Goods Received Note</td>
            <td>Solid Purple Button</td>
            <td>Opens inbound intake form to link an approved Purchase Order and record delivered item counts.</td>
          </tr>
          <tr>
            <td class="col-field">Export Register</td>
            <td>Export Button</td>
            <td>Exports complete warehouse receiving history and inspection status to Excel or PDF.</td>
          </tr>
          <tr>
            <td class="col-field">Status Filter</td>
            <td>Dropdown Filter</td>
            <td>Filters receiving records by status: <code>All Statuses</code>, <code>Accepted</code>, <code>Quarantined</code>, <code>Rejected</code>.</td>
          </tr>
          <tr>
            <td class="col-field">Search Input Bar</td>
            <td>Text Field</td>
            <td>Real-time search across GRN numbers, purchase order references, and supplier business names.</td>
          </tr>
        </tbody>
      </table>

      <h2>GRN Register Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 62%;">On-Screen Information & Operational Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">GRN Number</td>
            <td>Sequential Link</td>
            <td>System sequential tracking code (e.g. <code>GRN-2026-0018</code>); clickable to inspect delivery details.</td>
          </tr>
          <tr>
            <td class="col-field">PO Reference</td>
            <td>Linked Order #</td>
            <td>Hyperlinked purchase order reference establishing the 3-way procure-to-pay match.</td>
          </tr>
          <tr>
            <td class="col-field">Supplier / Vendor</td>
            <td>Trade Name</td>
            <td>Delivering vendor legal entity name and delivery driver consignment reference.</td>
          </tr>
          <tr>
            <td class="col-field">Receipt Date & Location</td>
            <td>Date & Facility</td>
            <td>Physical delivery date and receiving warehouse facility/bin location.</td>
          </tr>
          <tr>
            <td class="col-field">Received Qty & Status</td>
            <td>Counts & Badges</td>
            <td>Delivered quantity versus ordered count, and quality status badge (<code>Accepted</code> or <code>Quarantine</code>).</td>
          </tr>
          <tr>
            <td class="col-field">Actions</td>
            <td>Context Menu</td>
            <td>Menu triggers to <em>Print GRN Slip</em>, <em>View Inspection Log</em>, or <em>Generate Supplier Bill</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Warehouse Quality Inspection Classifications & Dispositions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Inspection Code</th>
            <th style="width: 38%;">Physical Goods Evaluation Condition</th>
            <th style="width: 40%;">Inventory Ledger & Bill Settlement Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Accepted to Stock</td>
            <td>Item counts match packing slip; zero packaging damage.</td>
            <td>Posts full quantity to Active Inventory (1400); clears for billing.</td>
          </tr>
          <tr>
            <td class="col-field">Short Shipment</td>
            <td>Received count is less than ordered PO quantity.</td>
            <td>GRN updates to partial intake; invoice matched only to received units.</td>
          </tr>
          <tr>
            <td class="col-field">Quarantined (QC)</td>
            <td>Technical goods requiring lab testing or serial logging.</td>
            <td>Held in Account 1410; excluded from sales dispatch availability.</td>
          </tr>
          <tr>
            <td class="col-field">Rejected / Return</td>
            <td>Damaged in transit or incorrect product SKU.</td>
            <td>Intake rejected; generates vendor Debit Note / Return Slip.</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">3-WAY MATCHING ENFORCEMENT</div>
        When a supplier bill is entered, Acconeer ERP automatically compares the billed quantity against the accepted quantity on the linked GRN. Variances exceeding allowable tolerance require management authorization before payment release.
      </div>
    </div>
    """

def get_page_16():
    wf = window_frame(
        "Acconeer_ERP_UserFlows/Assets/06_Asset_Register.png",
        "Fixed Asset Register with Capitalization and Depreciation Schedules",
        "/assets",
        [
            ("Top Actions", "Excel, PDF, Run Depreciation, and + Register New Asset action buttons."),
            ("Category Filters", "Filter assets by Machinery, IT Equipment, Vehicles, Buildings, and Furniture."),
            ("Search Input", "Search asset tag, serial number, location, or custodian in real-time."),
            ("Asset Grid", "Columns for Asset Tag, Description, Category, Cost, Depreciation, Net Book Value, Actions.")
        ]
    )
    return f"""
    <div class="page">
      <div class="chapter-header">
        <div>
          <div class="chapter-category">FIXED ASSETS · CAPITALIZATION & AMORTIZATION</div>
          <div class="chapter-title">Fixed Assets Registry & Monthly Depreciation</div>
        </div>
        <div class="chapter-right-meta">MODULE 12<br>/assets</div>
      </div>

      <div class="nav-path">
        <strong>NAVIGATION:</strong> Sidebar Navigation ➔ Assets ➔ Asset Register
      </div>

      <p>
        The Fixed Assets Register tracks company capital assets from acquisition through monthly depreciation to final disposal. It maintains immutable asset identification, useful life schedules, and automated General Ledger depreciation postings.
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
            <td class="col-field">+ Register New Asset</td>
            <td>Solid Purple Button</td>
            <td>Opens asset registration form to record asset tag, purchase date, cost, salvage value, and useful life.</td>
          </tr>
          <tr>
            <td class="col-field">Run Depreciation</td>
            <td>Solid Blue Button</td>
            <td>Executes the monthly depreciation calculation run, posting straight-line amortization vouchers to GL.</td>
          </tr>
          <tr>
            <td class="col-field">Excel & PDF</td>
            <td>Export Buttons</td>
            <td>Downloads complete fixed asset register with accumulated depreciation and NBV to spreadsheet or PDF.</td>
          </tr>
          <tr>
            <td class="col-field">Category Pills</td>
            <td>Filter Buttons</td>
            <td>Filters assets by class: Plant & Machinery (1510), IT Equipment (1520), Motor Vehicles (1530), etc.</td>
          </tr>
        </tbody>
      </table>

      <h2>Asset Register Grid Columns & Field Definitions</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 20%;">Column Header</th>
            <th style="width: 18%;">Data Type</th>
            <th style="width: 62%;">On-Screen Information & Accounting Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Asset Tag #</td>
            <td>Tag & Serial</td>
            <td>Physical barcode tag identifier (e.g. <code>AST-2026-0042</code>); clickable to open asset master profile.</td>
          </tr>
          <tr>
            <td class="col-field">Asset Description</td>
            <td>Text & Model</td>
            <td>Equipment specification, brand, model number, and assigned employee custodian.</td>
          </tr>
          <tr>
            <td class="col-field">Acquisition Cost</td>
            <td>Historical Cost</td>
            <td>Capitalized purchase price in AED debited to Fixed Asset Account 1500.</td>
          </tr>
          <tr>
            <td class="col-field">Useful Life & Method</td>
            <td>Years & Method</td>
            <td>Depreciation formula (Straight-Line) and statutory economic lifetime (e.g. <em>3 Years</em>, <em>5 Years</em>).</td>
          </tr>
          <tr>
            <td class="col-field">Net Book Value (NBV)</td>
            <td>Calculated Balance</td>
            <td>Current balance sheet carrying value (Gross Historical Cost minus Accumulated Depreciation).</td>
          </tr>
          <tr>
            <td class="col-field">Actions</td>
            <td>Context Menu</td>
            <td>Menu triggers to <em>View Depreciation History</em>, <em>Record Maintenance</em>, or <em>Post Asset Disposal</em>.</td>
          </tr>
        </tbody>
      </table>

      <h2>Asset Lifecycle States & Retirement Accounting Rules</h2>
      <table class="doc-table">
        <thead>
          <tr>
            <th style="width: 22%;">Asset State</th>
            <th style="width: 38%;">Operational Status in Company</th>
            <th style="width: 40%;">Balance Sheet & General Ledger Treatment</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="col-field">Active in Service</td>
            <td>Asset deployed in production or office use.</td>
            <td>Depreciated monthly; carrying NBV reflected on Balance Sheet.</td>
          </tr>
          <tr>
            <td class="col-field">Fully Depreciated</td>
            <td>Useful life ended; remaining salvage value.</td>
            <td>Monthly amortization ceases; remains on registry at residual value.</td>
          </tr>
          <tr>
            <td class="col-field">Disposed / Sold</td>
            <td>Asset sold to external buyer.</td>
            <td>Derecognized from Account 1500; recognizes gain/loss on disposal.</td>
          </tr>
          <tr>
            <td class="col-field">Scrapped / Written Off</td>
            <td>Damaged beyond repair or decommissioned.</td>
            <td>Writes off remaining NBV directly to Impairment Loss (6700).</td>
          </tr>
        </tbody>
      </table>

      <div class="callout">
        <div class="callout-title">AUTOMATED MONTHLY DEPRECIATION POSTING</div>
        Clicking <strong>Run Depreciation</strong> posts balancing double-entry vouchers: <strong>Debit Account 6100 (Depreciation Expense)</strong> and <strong>Credit Account 1700 (Accumulated Depreciation)</strong>, updating the Balance Sheet NBV automatically.
      </div>
    </div>
    """

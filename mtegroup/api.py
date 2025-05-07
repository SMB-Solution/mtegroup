# File: mtegroup/api.py

import frappe

@frappe.whitelist()
def cancel_linked_journal_entry(expense_claim_name):
    # 1. load the Expense Claim
    doc = frappe.get_doc("MTE Expense Claims", expense_claim_name)

    # 2. if there's a linked JE
    if doc.journal_entry:
        je_name = doc.journal_entry

        # 3. clear the link field in the Expense Claim
        frappe.db.set_value(doc.doctype, doc.name, "journal_entry", "")

        # 4. now load & cancel the JE
        try:
            je = frappe.get_doc("Journal Entry", je_name)
            if je.docstatus == 1:
                je.cancel()
                return f"Journal Entry {je.name} cancelled."
        except frappe.DoesNotExistError:
            return "Journal Entry not found."
    return "No linked Journal Entry."

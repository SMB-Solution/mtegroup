# File: mtegroup/api.py

import frappe

@frappe.whitelist()
def cancel_linked_journal_entry(expense_claim_name):
    doc = frappe.get_doc("MTE Expense Claims", expense_claim_name)
    if doc.journal_entry:
        try:
            je = frappe.get_doc("Journal Entry", doc.journal_entry)
            if je.docstatus == 1:
                je.cancel()
                return f"Journal Entry {je.name} cancelled."
        except frappe.DoesNotExistError:
            return "Journal Entry not found."
    return "No linked Journal Entry."
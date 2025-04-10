# File: mtegroup/api.py

import frappe
from erpnext.subcontracting.doctype.subcontracting_receipt.subcontracting_receipt import make_purchase_receipt as erpnext_make_pr

def custom_make_purchase_receipt(source_name):
    pr = erpnext_make_pr(source_name)

    subcontracting_receipt = frappe.get_doc("Subcontracting Receipt", source_name)

    pr.supplier_delivery_note = subcontracting_receipt.supplier_delivery_note

    pr.insert(ignore_permissions=True)
    pr.submit()

    frappe.msgprint(f"Purchase Receipt <b>{pr.name}</b> created with Supplier Delivery Note.")

    return pr


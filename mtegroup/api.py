# File: mtegroup/api.py

# import frappe
# from erpnext.erpnext.subcontracting.doctype.subcontracting_receipt.subcontracting_receipt import make_purchase_receipt as erpnext_make_pr

# def custom_make_purchase_receipt(source_name):
#     try:
#         subcontracting_receipt = frappe.get_doc("Subcontracting Receipt", source_name)
#         pr = erpnext_make_pr(source_name)
#         if subcontracting_receipt.supplier_delivery_note:
#             pr.supplier_delivery_note = subcontracting_receipt.supplier_delivery_note
#         else:
#             frappe.throw("Supplier Delivery Note is missing in Subcontracting Receipt")
#         pr.insert(ignore_permissions=True)
#         pr.submit()
#         frappe.msgprint(f"Purchase Receipt <b>{pr.name}</b> created successfully.")
#         return pr
#     except Exception as e:
#         frappe.log_error(f"Error creating Purchase Receipt from {source_name}: {str(e)}")
#         frappe.throw(f"Failed to create Purchase Receipt: {str(e)}")
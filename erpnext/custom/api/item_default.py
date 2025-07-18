# fetch default warehouse from Item Default for a given item and company
import frappe

@frappe.whitelist()
def get_default_warehouse(item_code, company):
    value = frappe.db.get_value(
        "Item Default",
        {"parent": item_code, "company": company},
        "default_warehouse"
    )
    return value

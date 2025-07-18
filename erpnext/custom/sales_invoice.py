import frappe
from frappe import _

def calculate_exchange_grand_total(doc, method):
    # only apply logic for USD to KHR conversion
    if doc.currency != "USD":
        return

    # get today's date in the format YYYY-MM-DD
    today = frappe.utils.today()

    # try fetching currency exchange for USD to KHR for selling
    ccy_rate = frappe.get_all("Currency Exchange",
        filters={
            "date": today,
            "from_currency": "USD",
            "to_currency": "KHR",
            "for_selling": 1
        },
        fields=["exchange_rate"],
        limit=1
    )

    if not ccy_rate:
        frappe.throw(_("Please setup currency exchange rate for USD to KHR (Selling) on {0}").format(today))

    exchange_rate = ccy_rate[0]["exchange_rate"]
    doc.custom_grand_total_khr_currency = doc.base_grand_total * exchange_rate

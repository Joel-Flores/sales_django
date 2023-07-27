from receipts.helper import HelperReceipts
from sales.helper import HelperSale

class HelperHome():
    def get_receipt(form):
        id = form.cleaned_data['sale_total']
        receipt = HelperReceipts.search_receipt(id)
        sales = HelperSale.search_sales(receipt)
        return sales
    
    def sales_today():
        return HelperSale.sales_today()
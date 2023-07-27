from datetime import datetime
from datetime import date

from django.db.models import Sum

from src.helper import HelperApp
from product.helper import HelperProduct
from .models import Sales

class HelperSale():
    def search_in_list(product_name : str, all_data : list):
        """
        Busca un elemento en una lista de objetos por el nombre del producto.

        Parameters:
            product_name (str): El nombre del producto que se desea buscar en la lista.
            all_data (list): Una lista de objetos que contienen información de productos.

        Returns:
            object or None: El objeto de la lista que tiene el nombre de producto coincidente, o None si no se encuentra.

        Description:
            Esta función realiza una búsqueda en la lista 'all_data' para encontrar el objeto cuyo nombre de producto coincida con 'product_name'. Utiliza una expresión generadora para iterar a través de los elementos de 'all_data', y retorna el primer objeto que tenga el nombre de producto igual a 'product_name'. Si no se encuentra ningún objeto con el nombre de producto especificado, retorna None.

            Esta función es útil para buscar y obtener un objeto específico en una lista de objetos en base a un criterio de búsqueda. Puede ser utilizada para encontrar un producto en una lista de productos u otros objetos que contengan información similar.

            Ejemplo de uso:
            ```
            products_list = [...]  # Una lista de objetos ProductName
            product_name = 'Producto 1'
            result = search_in_list(product_name, products_list)
            if result is not None:
                # Se encontró el producto con el nombre especificado
                print(f"Producto encontrado: {result}")
            else:
                # No se encontró el producto con el nombre especificado
                print("Producto no encontrado.")
            ```

        """
        if len(all_data) > 0:
            if type(all_data[0]) == dict:
                return next(
                    (data for data in all_data if data['name'] == product_name)
                    , None
                )
        return next(
            (data for data in all_data if data.name == product_name)
            , None
        )
        
    def save_sales_receipts(request, receipt):
        orders = HelperApp.get_order(request)
        for order in orders:
            product = HelperProduct.get_product(order['id'])
            new_sale = Sales(
                receipt = receipt,
                product = product,
                count = int(order['count']),
                price = order['price'],
                price_total = order['total']
            )
            new_sale.save()
        return orders
    
    def search_sales(receipt):
        return Sales.objects.filter(receipt = receipt)
    
    def sales_today():
        today = date.today()
        sales_today = Sales.objects.filter(create__date=today)
        total_count_today = sales_today.aggregate(Sum('count'))['count__sum']
        total_price_today = sales_today.aggregate(Sum('price_total'))['price_total__sum']
        return sales_today, total_count_today, total_price_today
from django.shortcuts import get_object_or_404
from .models import ProductName
from .models import ProductType

class HelperTypeProduct():
    def get_type_products():
        return ProductType.objects.all()

class HelperProduct():
    def get_products_filter_type(type_id : int) -> list[ProductName]:
        """
        Filtra y devuelve los objetos ProductName relacionados con un objeto ProductType específico.

        Args:
            type_id (int): El ID del objeto ProductType con el que se desea filtrar los productos.

        Returns:
            QuerySet[ProductName]: Un conjunto de consultas que contiene los objetos ProductName
                                relacionados con el ProductType especificado por type_id.
        """
        return ProductName.objects.filter(type__id= type_id)
    
    def get_product(id : int) -> type[ProductName]:
        '''  '''
        return ProductName.objects.get(id=id)
    
    def get_product_name(name : str) -> type[ProductName]:
        '''  '''
        return ProductName.objects.get(name=name)
 
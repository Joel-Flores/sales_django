from django import forms

from product.models import ProductName

def form_add_cart_to_products(products : list[ProductName], form = None) -> type[forms.Form]:
    """
    Crea un formulario dinámico para agregar productos al carrito.

    Args:
        products (list[ProductName]): Una lista de objetos ProductName que se agregarán al carrito.

    Returns:
        Type[forms.Form]: Una clase de formulario personalizada con campos dinámicos para cada producto
                         de la lista products, que permiten ingresar la cantidad del producto a agregar.

    Example:
        products = [product1, product2, product3]
        form = form_add_cart_to_products(products)

        # El formulario generado tendrá campos dinámicos para product1, product2 y product3,
        # donde se puede ingresar la cantidad de cada producto a agregar al carrito.

    """
    class FormOption(forms.Form):
        # Define los campos en el ciclo for
        pass
    
    for product in products:
        
        FormOption.base_fields[product.name] = forms.IntegerField(
            label='Cantidad del producto',
            initial=0,
            min_value = 0,
            widget=forms.NumberInput(
                attrs={
                'class': 'block w-full mt-1 text-sm dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none focus:shadow-outline-purple dark:text-gray-300 dark:focus:shadow-outline-gray form-input'
                }
            )
        )

    # Devuelve la clase FormOption personalizada
    return FormOption(form)
class HelperApp():
    def get_order(request) -> list:
        """
        Obtiene los datos de las órdenes almacenados en la sesión del usuario.

        Parameters:
            request (HttpRequest): La solicitud HTTP enviada por el cliente.

        Returns:
            list: Una lista con los datos de las órdenes almacenados en la sesión del usuario. Si no hay datos de órdenes, retorna una lista vacía.

        Description:
            Esta función recupera los datos de las órdenes previamente guardados en la sesión del usuario. Utiliza el objeto 'request' para acceder a la sesión y obtener la clave 'orders'. Si la clave 'orders' existe en la sesión, retorna su valor (que es una lista de datos de órdenes); de lo contrario, retorna una lista vacía.

            El objeto 'request' debe ser pasado como argumento a esta función para que pueda acceder a la sesión del usuario. La función es útil para obtener los datos de órdenes previamente guardados en la sesión y utilizarlos en las vistas o en otras funciones de Django.

            Ejemplo de uso en una vista:
            ```
            def mi_vista(request):
                orders = get_order(request)
                # Resto de la lógica de la vista
                # ...
            ```

        """
        return request.session.get('orders', [])
    
    def new_order(product : object, count : int) -> dict:
        """
        Crea un nuevo objeto que representa un pedido con información específica del producto.

        Parameters:
            product (object): Un objeto que contiene información del producto.
            count (int): La cantidad del producto que se incluirá en el pedido.

        Returns:
            dict: Un diccionario que representa el pedido con la siguiente información:
                - 'id': El ID del producto.
                - 'name': El nombre del producto.
                - 'price': El precio del producto.
                - 'count': La cantidad del producto en el pedido (convertida a un número flotante).
                - 'total': El total del pedido, calculado como el precio del producto multiplicado por la cantidad (redondeado a un decimal).

        Description:
            Esta función crea un nuevo objeto que representa un pedido con información específica del producto. El objeto de pedido es representado como un diccionario con las siguientes claves:
            - 'id': El ID del producto.
            - 'name': El nombre del producto.
            - 'price': El precio del producto.
            - 'count': La cantidad del producto en el pedido, convertida a un número flotante para permitir fracciones de producto en el pedido.
            - 'total': El total del pedido, calculado como el precio del producto multiplicado por la cantidad, redondeado a un decimal.

            Esta función puede ser útil para generar objetos que representen pedidos individuales con información específica del producto, y luego agregarlos a una lista para formar un carrito de compras.

            Ejemplo de uso:
            ```
            product = ProductName.objects.get(id=1)  # Obtener el objeto del producto desde la base de datos
            count = 3  # Cantidad del producto en el pedido
            order = new_order(product, count)  # Crear el objeto de pedido
            print(order)  # Imprimir el objeto de pedido
            ```
        """
        return {
            'id' : product.id,
            'name': product.name,
            'price': product.price,
            'count': float(count),
            'total': round(float(count) * product.price,1)
        }
        
    def update_order(order : dict, product_data : object, count : int) -> None:
        """
        Actualiza los datos de un pedido existente con la nueva cantidad y el total.

        Parameters:
            order (dict): Un diccionario que representa el pedido existente con información del producto.
            product_data (object): Un objeto que contiene información del producto.
            count (int): La cantidad adicional del producto que se agregará al pedido.

        Returns:
            None

        Description:
            Esta función actualiza los datos de un pedido existente con la nueva cantidad y el total. El pedido es representado como un diccionario que debe contener las siguientes claves:
            - 'id': El ID del producto.
            - 'name': El nombre del producto.
            - 'price': El precio del producto.
            - 'count': La cantidad actual del producto en el pedido.
            - 'total': El total del pedido, calculado como el precio del producto multiplicado por la cantidad actual.

            La función toma como parámetros el diccionario 'order', el objeto 'product_data' con la información actualizada del producto y la cantidad 'count' adicional del producto que se agregará al pedido. Luego, actualiza la cantidad y el total del pedido en el diccionario 'order' con los nuevos valores.

            Esta función puede ser utilizada para actualizar la cantidad de un producto en un pedido existente y recalcular el total del pedido después de agregar más unidades del producto.

            Ejemplo de uso:
            ```
            order_data = {'id': 1, 'name': 'Producto 1', 'price': 10.0, 'count': 3, 'total': 30.0}
            product = ProductName.objects.get(id=1)  # Obtener el objeto del producto desde la base de datos
            count_additional = 2  # Cantidad adicional del producto que se agregará al pedido
            update_order(order_data, product, count_additional)  # Actualizar el pedido existente
            print(order_data)  # Imprimir el pedido actualizado
            ```
        """
        order['count'] += float(count)
        order['total'] = round(order['count'] * product_data.price, 1)
    
    def update_order_in_session(request, orders : list) -> None:
        """
        Actualiza los datos de la sesión del usuario con la lista de pedidos y el total.

        Parameters:
            request (HttpRequest): La solicitud HTTP enviada por el cliente.
            orders (list): Una lista de diccionarios que representan los pedidos con información del producto.

        Returns:
            None

        Description:
            Esta función actualiza los datos de la sesión del usuario con la lista de pedidos 'orders' y el total acumulado. Los datos de la sesión se almacenan en el objeto 'request.session'.

            La función toma como parámetros 'request', que es la solicitud HTTP enviada por el cliente, y la lista 'orders' que contiene los diccionarios de pedidos. Cada diccionario de pedido debe contener las siguientes claves:
            - 'id': El ID del producto.
            - 'name': El nombre del producto.
            - 'price': El precio del producto.
            - 'count': La cantidad del producto en el pedido.
            - 'total': El total del pedido, calculado como el precio del producto multiplicado por la cantidad.

            Luego, la función actualiza los datos de la sesión con la lista de pedidos 'orders' y calcula el total acumulado de todos los pedidos en la lista. El total se almacena en la clave 'total' en la sesión.

            Esta función es útil para mantener los datos de los pedidos en la sesión del usuario mientras navega por la aplicación, permitiendo que los datos del carrito de compras u otros pedidos persistan en diferentes vistas.

            Ejemplo de uso:
            ```
            orders_list = [...]  # Lista de diccionarios que representan los pedidos
            update_session(request, orders_list)  # Actualizar la sesión con los datos de los pedidos
            ```
        """
        request.session['orders'] = orders
        request.session['total'] = float(sum([order['total'] for order in orders]))
        
    def delete_order(id : int) -> list:
        """
        Elimina una orden específica de la lista de órdenes almacenadas en la sesión del usuario.

        Parameters:
            id (int): El ID de la orden que se desea eliminar.

        Returns:
            list: Una nueva lista de órdenes que excluye la orden con el ID especificado. Si no se encuentra una orden con el ID dado, se retorna la lista de órdenes original.

        Description:
            Esta función elimina una orden específica de la lista de órdenes almacenadas en la sesión del usuario. Para realizar la eliminación, primero obtiene la lista actual de órdenes llamando al método estático 'get_order()' de la clase 'HelperApp'. Luego, utiliza una comprensión de lista para crear una nueva lista que excluya la orden con el ID especificado.

            La función toma como parámetro 'id', que es el ID de la orden que se desea eliminar. Luego, busca la orden con el ID dado en la lista de órdenes y crea una nueva lista que excluye la orden encontrada.

            Si no se encuentra una orden con el ID dado, la función retornará la lista original de órdenes sin realizar ninguna modificación.

            Ejemplo de uso:
            ```
            orders_list = HelperApp.get_order()  # Obtener la lista de órdenes desde la sesión
            order_id_to_delete = 123  # ID de la orden que se desea eliminar
            new_orders_list = delete_order(order_id_to_delete)  # Eliminar la orden de la lista de órdenes
            print(new_orders_list)  # Imprimir la nueva lista de órdenes
            ```
        """
        orders = HelperApp.get_order()
        return [order for order in orders if order["id"] != id]
    
    def get_total(request) -> int:
        return request.session.get('total')
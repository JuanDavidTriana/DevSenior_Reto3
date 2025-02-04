# productos.py

# Diccionario con los productos precargados
productos = {
    1: {"nombre": "Manzana", "precio": 1.5, "stock": 100},
    2: {"nombre": "Plátano", "precio": 1.0, "stock": 150},
    3: {"nombre": "Pera", "precio": 2.0, "stock": 80},
    4: {"nombre": "Uva", "precio": 2.5, "stock": 120},
    5: {"nombre": "Sandía", "precio": 3.0, "stock": 50},
    6: {"nombre": "Melón", "precio": 2.8, "stock": 60},
    7: {"nombre": "Naranja", "precio": 1.2, "stock": 200},
    8: {"nombre": "Mandarina", "precio": 1.3, "stock": 180},
    9: {"nombre": "Kiwi", "precio": 3.5, "stock": 70},
    10: {"nombre": "Fresa", "precio": 2.8, "stock": 90},
    11: {"nombre": "Aguacate", "precio": 2.2, "stock": 110},
    12: {"nombre": "Papaya", "precio": 2.6, "stock": 40},
    13: {"nombre": "Granada", "precio": 3.2, "stock": 75},
    14: {"nombre": "Cereza", "precio": 4.0, "stock": 85},
    15: {"nombre": "Frambuesa", "precio": 3.7, "stock": 65},
    16: {"nombre": "Plátano macho", "precio": 1.8, "stock": 95},
    17: {"nombre": "Piña", "precio": 3.5, "stock": 55},
    18: {"nombre": "Mango", "precio": 2.5, "stock": 105},
    19: {"nombre": "Lima", "precio": 1.0, "stock": 130},
    20: {"nombre": "Limón", "precio": 1.0, "stock": 140},
}

# Historial de ventas
historial_ventas = []

def obtener_producto(id_producto):
    """Retorna los datos del producto según su ID."""
    return productos.get(id_producto, None)

def calcular_total(lista_productos):
    """Calcula el total de la compra."""
    total = 0
    for producto in lista_productos:
        total += producto['precio']
    return total

def agregar_producto(id_producto, cantidad, lista_productos):
    """Agrega un producto a la lista de compra y registra la venta."""
    producto = obtener_producto(id_producto)
    if producto:
        lista_productos.append({"nombre": producto["nombre"], "precio": producto["precio"] * cantidad})
        
        # Registrar la venta en el historial
        historial_ventas.append({
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio_total": producto["precio"] * cantidad
        })
    else:
        raise ValueError(f"Producto con ID {id_producto} no encontrado.")

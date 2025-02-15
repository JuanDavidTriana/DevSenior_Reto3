from tkinter import messagebox

class ControladorTienda:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.carrito = []

    def obtener_productos(self):
        return self.modelo.productos

    def agregar_al_carrito(self, id_producto, cantidad):
        producto = self.modelo.obtener_producto(id_producto)
        if producto:
            if cantidad > producto.stock:
                raise ValueError("Stock insuficiente")
            self.carrito.append({"producto": producto.nombre, "cantidad": cantidad, "precio_total": producto.precio * cantidad})
        else:
            raise ValueError("Producto no encontrado")

    def finalizar_compra(self):
        total = sum(item["precio_total"] for item in self.carrito)
        messagebox.showinfo("Compra Finalizada", f"Total: ${total:.2f}")
        for item in self.carrito:
            
            producto_id = next((p_id for p_id, p in self.modelo.productos.items() if p.nombre == item["producto"]), None)
            if producto_id is not None:
                self.modelo.registrar_venta(producto_id, item["cantidad"])
            else:
                messagebox.showerror("Error", "Producto no encontrado en la tienda")
                
        
        self.vista.actualizar_vista_productos()
            
                    
        self.carrito.clear()
        

import tkinter as tk
from tkinter import messagebox, ttk

class VistaTienda:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Caja Registradora - Tienda Fruber")
        self._configurar_interfaz()
        self._cargar_productos()
        self.ventana.mainloop()

    def _configurar_interfaz(self):
        self.treeview_productos = ttk.Treeview(self.ventana, columns=("Producto", "Precio", "Stock"), show="headings")
        self.treeview_productos.heading("Producto", text="Producto")
        self.treeview_productos.heading("Precio", text="Precio")
        self.treeview_productos.heading("Stock", text="Stock")
        self.treeview_productos.pack()

        self.entry_cantidad = tk.Entry(self.ventana)
        self.entry_cantidad.pack()

        self.boton_agregar = tk.Button(self.ventana, text="Agregar", command=self.agregar_producto)
        self.boton_agregar.pack()

        self.boton_finalizar = tk.Button(self.ventana, text="Finalizar Compra", command=self.controlador.finalizar_compra)
        self.boton_finalizar.pack()

    def _cargar_productos(self):
        for id_producto, producto in self.controlador.obtener_productos().items():
            self.treeview_productos.insert("", "end", iid=str(id_producto), values=(producto.nombre, producto.precio, producto.stock))

    def agregar_producto(self):
        try:
            selected_item = self.treeview_productos.selection()[0]
            id_producto = int(selected_item)
            cantidad = int(self.entry_cantidad.get())
            self.controlador.agregar_al_carrito(id_producto, cantidad)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def actualizar_vista_productos(self):
        for item in self.treeview_productos.get_children():
            self.treeview_productos.delete(item)  # Limpiar la tabla

        for id_producto, producto in self.controlador.obtener_productos().items():
            self.treeview_productos.insert("", "end", iid=str(id_producto), values=(producto.nombre, producto.precio, producto.stock))

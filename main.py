import tkinter as tk
from tkinter import messagebox, ttk
from operaciones import agregar_producto, calcular_total
from excepciones import manejar_error
from productos import productos, historial_ventas

# Lista de productos seleccionados
productos_seleccionados = []

# Función para agregar productos desde el Treeview
def agregar_desde_lista():
    try:
        # Obtener el item seleccionado en el Treeview
        selected_item = treeview_productos.selection()
        if not selected_item:
            raise ValueError("Debe seleccionar un producto de la lista.")
        
        # El ID del producto generalmente se obtiene del iid del Treeview
        id_producto = selected_item[0]  # 'iid' del Treeview, que debe ser el ID del producto en el diccionario
        
        # Aquí asumimos que el id_producto es la clave que corresponde al producto en el diccionario 'productos'
        if not id_producto.isdigit() or int(id_producto) not in productos:
            raise ValueError("ID de producto no válido.")
        
        # Obtener la cantidad del campo de entrada
        cantidad = int(entry_cantidad.get())
        
        # Validar que haya suficiente cantidad disponible
        producto = productos[int(id_producto)]
        cantidad_disponible = 100  # Asumimos que este valor se obtiene correctamente
        if cantidad > cantidad_disponible:
            raise ValueError("No hay suficiente cantidad disponible.")

        # Agregar el producto
        agregar_producto(int(id_producto), cantidad, productos_seleccionados)
        
        # Actualizar cantidad disponible en el Treeview
        cantidad_disponible -= cantidad
        treeview_productos.item(selected_item, values=(producto['nombre'], f"${producto['precio']:.2f}", cantidad_disponible))
        
        actualizar_lista()

    except ValueError as e:
        manejar_error(e)
        messagebox.showerror("Error", str(e))


# Función para mostrar los productos en la interfaz
def actualizar_lista():
    for row in treeview_seleccionados.get_children():
        treeview_seleccionados.delete(row)
    for producto in productos_seleccionados:
        treeview_seleccionados.insert("", "end", values=(producto['nombre'], f"${producto['precio']:.2f}"))
    total = calcular_total(productos_seleccionados)
    etiqueta_total.config(text=f"Total: ${total:.2f}")

# Función para finalizar la compra y mostrar el recibo
def finalizar_compra():
    total = calcular_total(productos_seleccionados)
    recibo_texto = "RECIBO DE COMPRA\n\n"
    recibo_texto += "-"*30 + "\n"
    for producto in productos_seleccionados:
        recibo_texto += f"{producto['nombre']} - ${producto['precio']:.2f}\n"
    
    # Agregar al historial de ventas
    for producto in productos_seleccionados:
        historial_ventas.append({
            "producto": producto['nombre'],
            "cantidad": 1,  # Aquí puedes manejar la cantidad que realmente se vendió
            "precio_total": producto['precio']
        })

    recibo_texto += "-"*30 + "\n"
    recibo_texto += f"Total: ${total:.2f}\n"
    recibo_texto += "-"*30
    messagebox.showinfo("Recibo de Compra", recibo_texto)
    
    # Limpiar lista de productos seleccionados
    productos_seleccionados.clear()
    actualizar_lista()

# Función para mostrar el historial de ventas
def mostrar_historial():
    historial_ventana = tk.Toplevel(ventana)
    historial_ventana.title("Historial de Ventas")

    # Crear Treeview para el historial de ventas
    treeview_historial = ttk.Treeview(historial_ventana, columns=("Producto", "Cantidad", "Precio Total"), show="headings", height=10)
    treeview_historial.heading("Producto", text="Producto")
    treeview_historial.heading("Cantidad", text="Cantidad")
    treeview_historial.heading("Precio Total", text="Precio Total")
    treeview_historial.column("Producto", width=200)
    treeview_historial.column("Cantidad", width=100)
    treeview_historial.column("Precio Total", width=150)

    # Insertar las ventas al Treeview
    for venta in historial_ventas:
        treeview_historial.insert("", "end", values=(venta["producto"], venta["cantidad"], f"${venta['precio_total']:.2f}"))

    treeview_historial.pack(padx=20, pady=20)

    # Mostrar las ganancias totales
    ganancias_totales = sum(venta["precio_total"] for venta in historial_ventas)
    etiqueta_ganancias = tk.Label(historial_ventana, text=f"Ganancias Totales: ${ganancias_totales:.2f}", font=("Arial", 14, "bold"))
    etiqueta_ganancias.pack(pady=10)

# Configuración de la interfaz
ventana = tk.Tk()
ventana.title("Caja Registradora - Tienda Fruber")

# Marco principal
marco_principal = tk.Frame(ventana, padx=30, pady=30, bg="#f4f4f9")
marco_principal.pack(fill="both", expand=True)

# Título
titulo = tk.Label(marco_principal, text="Bienvenido a la Tienda Fruber", font=("Arial", 20, "bold"), fg="green", bg="#f4f4f9")
titulo.grid(row=0, column=0, columnspan=3, pady=20)

# Frame para la lista de productos
frame_productos = tk.Frame(marco_principal, bg="#f4f4f9")
frame_productos.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Treeview para seleccionar productos
etiqueta_lista_productos = tk.Label(frame_productos, text="Selecciona un Producto:", font=("Arial", 14), bg="#f4f4f9")
etiqueta_lista_productos.pack(pady=10)

treeview_productos = ttk.Treeview(frame_productos, columns=("Producto", "Precio", "Cantidad Disponible"), show="headings", height=10)
treeview_productos.heading("Producto", text="Producto")
treeview_productos.heading("Precio", text="Precio")
treeview_productos.heading("Cantidad Disponible", text="Cantidad Disponible")
treeview_productos.column("Producto", width=220)
treeview_productos.column("Precio", width=100)
treeview_productos.column("Cantidad Disponible", width=150)

# Insertar productos en el Treeview
for key, producto in productos.items():
    cantidad_disponible = 100  # Aquí puedes cambiar la cantidad disponible según lo necesites
    treeview_productos.insert("", "end", iid=str(key), values=(producto['nombre'], f"${producto['precio']}", cantidad_disponible))

treeview_productos.pack(pady=10)

# Frame para la cantidad y el botón de agregar
frame_cantidad = tk.Frame(marco_principal, bg="#f4f4f9")
frame_cantidad.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Campo para cantidad
etiqueta_cantidad = tk.Label(frame_cantidad, text="Cantidad:", font=("Arial", 14), bg="#f4f4f9")
etiqueta_cantidad.pack(pady=10)

entry_cantidad = tk.Entry(frame_cantidad, font=("Arial", 14), width=10)
entry_cantidad.pack(pady=10)

# Botón para agregar producto desde el Treeview
boton_agregar = tk.Button(frame_cantidad, text="Agregar Producto", command=agregar_desde_lista, bg="#81c784", font=("Arial", 14))
boton_agregar.pack(pady=10)

# Frame para la lista de productos seleccionados
frame_seleccionados = tk.Frame(marco_principal, bg="#f4f4f9")
frame_seleccionados.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Treeview para productos agregados
treeview_seleccionados = ttk.Treeview(frame_seleccionados, columns=("Producto", "Precio"), show="headings", height=10)
treeview_seleccionados.heading("Producto", text="Producto")
treeview_seleccionados.heading("Precio", text="Precio")
treeview_seleccionados.column("Producto", width=250)
treeview_seleccionados.column("Precio", width=100)

treeview_seleccionados.pack(pady=10)

# Etiqueta de total
etiqueta_total = tk.Label(frame_seleccionados, text="Total: $0.00", font=("Arial", 16, "bold"), bg="#f4f4f9")
etiqueta_total.pack(pady=20)

# Frame para los botones de finalizar compra y ver historial
frame_botones = tk.Frame(marco_principal, bg="#f4f4f9")
frame_botones.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

# Botón para finalizar compra
boton_finalizar = tk.Button(frame_botones, text="Finalizar Compra", command=finalizar_compra, bg="#4caf50", font=("Arial", 14, "bold"))
boton_finalizar.pack(pady=20)

# Botón para ver el historial
boton_historial = tk.Button(frame_botones, text="Ver Historial de Ventas", command=mostrar_historial, bg="#ff9800", font=("Arial", 14))
boton_historial.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
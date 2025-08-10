import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class VentanaVentas:
    def __init__(self, sistema, notebook):
        self.sistema = sistema
        self.notebook = notebook
        self.tree_ventas = None
        
    def crear_pestana(self):
        """Crear la pestaña de ventas"""
        self.ventas_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.ventas_frame, text="💰 Ventas")
        
        btn_frame = tk.Frame(self.ventas_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(btn_frame, text="🛒 Nueva Venta", command=self.nueva_venta, 
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_ventas, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        columns = ("ID", "Cliente", "Producto", "Cantidad", "Total", "Fecha", "Vendedor")
        self.tree_ventas = ttk.Treeview(self.ventas_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_ventas.heading(col, text=col)
            self.tree_ventas.column(col, width=100)
        
        scrollbar_ventas = ttk.Scrollbar(self.ventas_frame, orient='vertical', command=self.tree_ventas.yview)
        self.tree_ventas.configure(yscrollcommand=scrollbar_ventas.set)
        
        self.tree_ventas.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_ventas.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_ventas()
    
    def nueva_venta(self):
        """Abrir ventana para nueva venta"""
        inventario = self.sistema.db.get_inventario()
        clientes = self.sistema.db.get_clientes()

        if not inventario:
            messagebox.showwarning("Advertencia", "No hay productos en inventario")
            return
        
        if not clientes:
            messagebox.showwarning("Advertencia", "No hay clientes registrados")
            return
        
        ventana = VentanaNuevaVenta(self.sistema, self)
        ventana.crear_ventana()
    
    def actualizar_ventas(self):
        """Actualizar la tabla de ventas"""
        if not self.tree_ventas:
            return
            
        for item in self.tree_ventas.get_children():
            self.tree_ventas.delete(item)
        
        ventas = self.sistema.db.get_ventas()
        for venta in ventas:
            self.tree_ventas.insert('', 'end', values=(
                venta["id"], venta["cliente"], venta["producto"], 
                venta["cantidad"], f"${venta['total']}", venta["fecha"], venta["vendedor"]
            ))

class VentanaNuevaVenta:
    def __init__(self, sistema, ventana_ventas):
        self.sistema = sistema
        self.ventana_ventas = ventana_ventas
        self.llantas = self.sistema.db.get_inventario()
        self.clientes = self.sistema.db.get_clientes()
        self.llanta_seleccionada = None
    
    def crear_ventana(self):
        """Crear ventana para nueva venta"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Nueva Venta")
        self.ventana.geometry("500x400")
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text="Cliente:", bg='#ecf0f1').pack(pady=5)
        self.combo_cliente = ttk.Combobox(self.ventana, width=40)
        self.combo_cliente['values'] = [f"{c['id']} - {c['nombre']}" for c in self.clientes]
        self.combo_cliente.pack(pady=5)
        
        tk.Label(self.ventana, text="Producto:", bg='#ecf0f1').pack(pady=5)
        self.combo_producto = ttk.Combobox(self.ventana, width=40)
        self.combo_producto['values'] = [f"{l['id']} - {l['marca']} {l['modelo']} ({l['medida']})" for l in self.llantas]
        self.combo_producto.bind("<<ComboboxSelected>>", self.seleccionar_llanta)
        self.combo_producto.pack(pady=5)
        
        self.label_stock = tk.Label(self.ventana, text="Stock disponible: 0", bg='#ecf0f1')
        self.label_stock.pack(pady=5)
        
        tk.Label(self.ventana, text="Cantidad:", bg='#ecf0f1').pack(pady=5)
        self.entry_cantidad = tk.Entry(self.ventana, width=10)
        self.entry_cantidad.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar Venta", command=self.guardar_venta, 
                  bg='#27ae60', fg='white').pack(pady=20)
    
    def seleccionar_llanta(self, event):
        seleccion_str = self.combo_producto.get()
        llanta_id = int(seleccion_str.split(' - ')[0])
        self.llanta_seleccionada = self.sistema.db.get_llanta_by_id(llanta_id)
        if self.llanta_seleccionada:
            self.label_stock.config(text=f"Stock disponible: {self.llanta_seleccionada['stock']}")
        else:
            self.label_stock.config(text="Stock disponible: 0")

    def guardar_venta(self):
        cliente_str = self.combo_cliente.get()
        producto_str = self.combo_producto.get()
        cantidad_str = self.entry_cantidad.get().strip()
        
        if not all([cliente_str, producto_str, cantidad_str]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios", parent=self.ventana)
            return
        
        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Advertencia", "La cantidad debe ser un número entero positivo", parent=self.ventana)
            return

        cliente_id = int(cliente_str.split(' - ')[0])
        cliente = self.sistema.db.get_cliente_by_id(cliente_id)

        if not self.llanta_seleccionada:
            messagebox.showwarning("Advertencia", "Seleccione un producto válido", parent=self.ventana)
            return

        if cantidad > self.llanta_seleccionada['stock']:
            messagebox.showwarning("Advertencia", f"No hay suficiente stock. Stock disponible: {self.llanta_seleccionada['stock']}", parent=self.ventana)
            return
            
        total = cantidad * self.llanta_seleccionada['precio']
        
        # Registrar la venta
        self.sistema.db.registrar_venta(
            cliente['nombre'],
            f"{self.llanta_seleccionada['marca']} {self.llanta_seleccionada['modelo']} ({self.llanta_seleccionada['medida']})",
            cantidad,
            total,
            self.sistema.usuario_actual
        )
        
        # Actualizar el stock
        nuevo_stock = self.llanta_seleccionada['stock'] - cantidad
        self.sistema.db.modificar_llanta(
            self.llanta_seleccionada['id'],
            self.llanta_seleccionada['marca'],
            self.llanta_seleccionada['modelo'],
            self.llanta_seleccionada['medida'],
            self.llanta_seleccionada['precio'],
            nuevo_stock
        )
        
        messagebox.showinfo("Éxito", "Venta registrada y stock actualizado", parent=self.ventana)
        self.ventana_ventas.actualizar_ventas()
        self.ventana.destroy()
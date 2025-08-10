import tkinter as tk
from tkinter import ttk, messagebox

class VentanaInventario:
    def __init__(self, sistema, notebook, completa=True):
        self.sistema = sistema
        self.notebook = notebook
        self.completa = completa
        self.tree_inventario = None

    def crear_pestana(self):
        """Crear la pestaña de inventario"""
        self.inv_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inv_frame, text="📦 Inventario")
        
        btn_frame = tk.Frame(self.inv_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        if self.completa:
            tk.Button(btn_frame, text="➕ Agregar Llanta", command=self.agregar_llanta, 
                     bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="✏ Modificar", command=self.modificar_llanta, 
                     bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="🗑 Eliminar", command=self.eliminar_llanta, 
                     bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_inventario, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        columns = ("ID", "Marca", "Modelo", "Medida", "Precio", "Stock")
        self.tree_inventario = ttk.Treeview(self.inv_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_inventario.heading(col, text=col)
            self.tree_inventario.column(col, width=120)
        
        scrollbar_inv = ttk.Scrollbar(self.inv_frame, orient='vertical', command=self.tree_inventario.yview)
        self.tree_inventario.configure(yscrollcommand=scrollbar_inv.set)
        
        self.tree_inventario.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_inv.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_inventario()
    
    def agregar_llanta(self):
        """Abrir ventana para agregar nueva llanta"""
        ventana = VentanaAgregarLlanta(self.sistema, self)
        ventana.crear_ventana()
    
    def modificar_llanta(self):
        """Abrir ventana para modificar llanta seleccionada"""
        seleccion = self.tree_inventario.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una llanta para modificar")
            return
        
        item = self.tree_inventario.item(seleccion[0])
        llanta_id = int(item['values'][0])
        
        llanta = self.sistema.db.get_llanta_by_id(llanta_id)
        if not llanta:
            messagebox.showerror("Error", "Llanta no encontrada.")
            return
        
        ventana = VentanaModificarLlanta(self.sistema, self, llanta)
        ventana.crear_ventana()
    
    def eliminar_llanta(self):
        """Eliminar llanta seleccionada"""
        seleccion = self.tree_inventario.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una llanta para eliminar")
            return
        
        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar esta llanta?"):
            item = self.tree_inventario.item(seleccion[0])
            llanta_id = int(item['values'][0])
            self.sistema.db.eliminar_llanta(llanta_id)
            self.actualizar_inventario()
            messagebox.showinfo("Éxito", "Llanta eliminada correctamente")

    def actualizar_inventario(self):
        """Actualizar la tabla de inventario"""
        if not self.tree_inventario:
            return
            
        for item in self.tree_inventario.get_children():
            self.tree_inventario.delete(item)
        
        inventario = self.sistema.db.get_inventario()
        for llanta in inventario:
            self.tree_inventario.insert('', 'end', values=(
                llanta["id"], llanta["marca"], llanta["modelo"], llanta["medida"], f"${llanta['precio']}", llanta["stock"]
            ))

class VentanaAgregarLlanta:
    def __init__(self, sistema, ventana_inventario):
        self.sistema = sistema
        self.ventana_inventario = ventana_inventario
    
    def crear_ventana(self):
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Agregar Llanta")
        self.ventana.geometry("400x300")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text="Marca:", bg='#ecf0f1').pack(pady=5)
        self.entry_marca = tk.Entry(self.ventana, width=40)
        self.entry_marca.pack(pady=5)
        
        tk.Label(self.ventana, text="Modelo:", bg='#ecf0f1').pack(pady=5)
        self.entry_modelo = tk.Entry(self.ventana, width=40)
        self.entry_modelo.pack(pady=5)
        
        tk.Label(self.ventana, text="Medida:", bg='#ecf0f1').pack(pady=5)
        self.entry_medida = tk.Entry(self.ventana, width=40)
        self.entry_medida.pack(pady=5)
        
        tk.Label(self.ventana, text="Precio:", bg='#ecf0f1').pack(pady=5)
        self.entry_precio = tk.Entry(self.ventana, width=40)
        self.entry_precio.pack(pady=5)
        
        tk.Label(self.ventana, text="Stock:", bg='#ecf0f1').pack(pady=5)
        self.entry_stock = tk.Entry(self.ventana, width=40)
        self.entry_stock.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar", command=self.guardar_llanta, 
                  bg='#27ae60', fg='white').pack(pady=20)
    
    def guardar_llanta(self):
        marca = self.entry_marca.get().strip()
        modelo = self.entry_modelo.get().strip()
        medida = self.entry_medida.get().strip()
        precio_str = self.entry_precio.get().strip()
        stock_str = self.entry_stock.get().strip()
        
        if not all([marca, modelo, medida, precio_str, stock_str]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios", parent=self.ventana)
            return
        
        try:
            precio = float(precio_str)
            stock = int(stock_str)
        except ValueError:
            messagebox.showwarning("Advertencia", "Precio y Stock deben ser números válidos", parent=self.ventana)
            return

        self.sistema.db.agregar_llanta(marca, modelo, medida, precio, stock)
        messagebox.showinfo("Éxito", "Llanta agregada correctamente", parent=self.ventana)
        self.ventana_inventario.actualizar_inventario()
        self.ventana.destroy()

class VentanaModificarLlanta:
    def __init__(self, sistema, ventana_inventario, llanta):
        self.sistema = sistema
        self.ventana_inventario = ventana_inventario
        self.llanta = llanta
    
    def crear_ventana(self):
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Modificar Llanta")
        self.ventana.geometry("400x300")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text=f"ID: {self.llanta['id']}", bg='#ecf0f1').pack(pady=5)
        
        tk.Label(self.ventana, text="Marca:", bg='#ecf0f1').pack(pady=5)
        self.entry_marca = tk.Entry(self.ventana, width=40)
        self.entry_marca.insert(0, self.llanta['marca'])
        self.entry_marca.pack(pady=5)
        
        tk.Label(self.ventana, text="Modelo:", bg='#ecf0f1').pack(pady=5)
        self.entry_modelo = tk.Entry(self.ventana, width=40)
        self.entry_modelo.insert(0, self.llanta['modelo'])
        self.entry_modelo.pack(pady=5)
        
        tk.Label(self.ventana, text="Medida:", bg='#ecf0f1').pack(pady=5)
        self.entry_medida = tk.Entry(self.ventana, width=40)
        self.entry_medida.insert(0, self.llanta['medida'])
        self.entry_medida.pack(pady=5)
        
        tk.Label(self.ventana, text="Precio:", bg='#ecf0f1').pack(pady=5)
        self.entry_precio = tk.Entry(self.ventana, width=40)
        self.entry_precio.insert(0, self.llanta['precio'])
        self.entry_precio.pack(pady=5)
        
        tk.Label(self.ventana, text="Stock:", bg='#ecf0f1').pack(pady=5)
        self.entry_stock = tk.Entry(self.ventana, width=40)
        self.entry_stock.insert(0, self.llanta['stock'])
        self.entry_stock.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar_cambios,
                  bg='#f39c12', fg='white').pack(pady=20)
    
    def guardar_cambios(self):
        marca = self.entry_marca.get().strip()
        modelo = self.entry_modelo.get().strip()
        medida = self.entry_medida.get().strip()
        precio_str = self.entry_precio.get().strip()
        stock_str = self.entry_stock.get().strip()
        
        if not all([marca, modelo, medida, precio_str, stock_str]):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios", parent=self.ventana)
            return

        try:
            precio = float(precio_str)
            stock = int(stock_str)
        except ValueError:
            messagebox.showwarning("Advertencia", "Precio y Stock deben ser números válidos", parent=self.ventana)
            return
        
        self.sistema.db.modificar_llanta(self.llanta['id'], marca, modelo, medida, precio, stock)
        messagebox.showinfo("Éxito", "Llanta modificada correctamente", parent=self.ventana)
        self.ventana_inventario.actualizar_inventario()
        self.ventana.destroy()
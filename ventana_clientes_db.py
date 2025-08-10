import tkinter as tk
from tkinter import ttk, messagebox

class VentanaClientes:
    def __init__(self, sistema, notebook):
        self.sistema = sistema
        self.notebook = notebook
        self.tree_clientes = None
        
    def crear_pestana(self):
        """Crear la pestaña de clientes"""
        self.clientes_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.clientes_frame, text="👥 Clientes")
        
        btn_frame = tk.Frame(self.clientes_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(btn_frame, text="➕ Agregar Cliente", command=self.agregar_cliente, 
                 bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="✏ Modificar", command=self.modificar_cliente, 
                 bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_clientes, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        columns = ("ID", "Nombre", "Teléfono", "Email")
        self.tree_clientes = ttk.Treeview(self.clientes_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_clientes.heading(col, text=col)
            self.tree_clientes.column(col, width=150)
        
        scrollbar_clientes = ttk.Scrollbar(self.clientes_frame, orient='vertical', command=self.tree_clientes.yview)
        self.tree_clientes.configure(yscrollcommand=scrollbar_clientes.set)
        
        self.tree_clientes.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_clientes.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_clientes()
    
    def agregar_cliente(self):
        """Abrir ventana para agregar cliente"""
        ventana = VentanaAgregarCliente(self.sistema, self)
        ventana.crear_ventana()
    
    def modificar_cliente(self):
        """Abrir ventana para modificar cliente"""
        seleccion = self.tree_clientes.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un cliente para modificar")
            return
        
        item = self.tree_clientes.item(seleccion[0])
        cliente_id = int(item['values'][0])
        
        cliente = self.sistema.db.get_cliente_by_id(cliente_id)
        if not cliente:
            messagebox.showerror("Error", "Cliente no encontrado.")
            return
        
        ventana = VentanaModificarCliente(self.sistema, self, cliente)
        ventana.crear_ventana()
    
    def actualizar_clientes(self):
        """Actualizar la tabla de clientes"""
        if not self.tree_clientes:
            return
        
        for item in self.tree_clientes.get_children():
            self.tree_clientes.delete(item)
        
        clientes = self.sistema.db.get_clientes()
        for cliente in clientes:
            self.tree_clientes.insert('', 'end', values=(
                cliente["id"], cliente["nombre"], cliente["telefono"], cliente["email"]
            ))

class VentanaAgregarCliente:
    def __init__(self, sistema, ventana_clientes):
        self.sistema = sistema
        self.ventana_clientes = ventana_clientes
    
    def crear_ventana(self):
        """Crear ventana para agregar cliente"""
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Agregar Cliente")
        self.ventana.geometry("400x300")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text="Nombre:", bg='#ecf0f1').pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana, width=40)
        self.entry_nombre.pack(pady=5)
        
        tk.Label(self.ventana, text="Teléfono:", bg='#ecf0f1').pack(pady=5)
        self.entry_telefono = tk.Entry(self.ventana, width=40)
        self.entry_telefono.pack(pady=5)
        
        tk.Label(self.ventana, text="Email:", bg='#ecf0f1').pack(pady=5)
        self.entry_email = tk.Entry(self.ventana, width=40)
        self.entry_email.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar", command=self.guardar_cliente, 
                  bg='#27ae60', fg='white').pack(pady=20)
    
    def guardar_cliente(self):
        nombre = self.entry_nombre.get().strip()
        telefono = self.entry_telefono.get().strip()
        email = self.entry_email.get().strip()
        
        if not nombre:
            messagebox.showwarning("Advertencia", "El nombre es obligatorio", parent=self.ventana)
            return
        
        self.sistema.db.agregar_cliente(nombre, telefono, email)
        messagebox.showinfo("Éxito", "Cliente agregado correctamente", parent=self.ventana)
        self.ventana_clientes.actualizar_clientes()
        self.ventana.destroy()

class VentanaModificarCliente:
    def __init__(self, sistema, ventana_clientes, cliente):
        self.sistema = sistema
        self.ventana_clientes = ventana_clientes
        self.cliente = cliente
    
    def crear_ventana(self):
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Modificar Cliente")
        self.ventana.geometry("400x300")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text=f"ID: {self.cliente['id']}", bg='#ecf0f1').pack(pady=5)
        
        tk.Label(self.ventana, text="Nombre:", bg='#ecf0f1').pack(pady=5)
        self.entry_nombre = tk.Entry(self.ventana, width=40)
        self.entry_nombre.insert(0, self.cliente['nombre'])
        self.entry_nombre.pack(pady=5)
        
        tk.Label(self.ventana, text="Teléfono:", bg='#ecf0f1').pack(pady=5)
        self.entry_telefono = tk.Entry(self.ventana, width=40)
        self.entry_telefono.insert(0, self.cliente['telefono'])
        self.entry_telefono.pack(pady=5)
        
        tk.Label(self.ventana, text="Email:", bg='#ecf0f1').pack(pady=5)
        self.entry_email = tk.Entry(self.ventana, width=40)
        self.entry_email.insert(0, self.cliente['email'])
        self.entry_email.pack(pady=5)
        
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar_cambios,
                  bg='#f39c12', fg='white').pack(pady=20)
    
    def guardar_cambios(self):
        nombre = self.entry_nombre.get().strip()
        telefono = self.entry_telefono.get().strip()
        email = self.entry_email.get().strip()
        
        if not nombre:
            messagebox.showwarning("Advertencia", "El nombre es obligatorio", parent=self.ventana)
            return
        
        self.sistema.db.modificar_cliente(self.cliente['id'], nombre, telefono, email)
        messagebox.showinfo("Éxito", "Cliente modificado correctamente", parent=self.ventana)
        self.ventana_clientes.actualizar_clientes()
        self.ventana.destroy()
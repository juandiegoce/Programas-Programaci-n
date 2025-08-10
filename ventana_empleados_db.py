import tkinter as tk
from tkinter import ttk, messagebox

class VentanaEmpleados:
    def __init__(self, sistema, notebook):
        self.sistema = sistema
        self.notebook = notebook
        self.tree_empleados = None
        
    def crear_pestana(self):
        """Crear la pestaña de empleados"""
        self.emp_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.emp_frame, text="👨‍💼 Empleados")
        
        btn_frame = tk.Frame(self.emp_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        if self.sistema.role_actual == "admin":
            tk.Button(btn_frame, text="➕ Agregar Usuario", command=self.agregar_usuario, 
                     bg='#27ae60', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="✏ Modificar", command=self.modificar_usuario, 
                     bg='#f39c12', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
            tk.Button(btn_frame, text="🗑 Eliminar", command=self.eliminar_usuario, 
                     bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        
        tk.Button(btn_frame, text="🔄 Actualizar", command=self.actualizar_empleados, 
                 bg='#3498db', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        columns = ("Usuario", "Rol")
        self.tree_empleados = ttk.Treeview(self.emp_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.tree_empleados.heading(col, text=col)
            self.tree_empleados.column(col, width=150)
        
        scrollbar_empleados = ttk.Scrollbar(self.emp_frame, orient='vertical', command=self.tree_empleados.yview)
        self.tree_empleados.configure(yscrollcommand=scrollbar_empleados.set)
        
        self.tree_empleados.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_empleados.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        self.actualizar_empleados()
    
    def agregar_usuario(self):
        """Abrir ventana para agregar usuario"""
        ventana = VentanaAgregarUsuario(self.sistema, self)
        ventana.crear_ventana()
    
    def modificar_usuario(self):
        """Abrir ventana para modificar usuario"""
        seleccion = self.tree_empleados.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para modificar")
            return
        
        item = self.tree_empleados.item(seleccion[0])
        usuario = item['values'][0]
        
        user_data = self.sistema.db.get_usuario_by_username(usuario)
        if not user_data:
            messagebox.showerror("Error", "Usuario no encontrado.")
            return

        ventana = VentanaModificarUsuario(self.sistema, self, user_data)
        ventana.crear_ventana()
    
    def eliminar_usuario(self):
        """Eliminar usuario seleccionado"""
        seleccion = self.tree_empleados.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar")
            return
        
        item = self.tree_empleados.item(seleccion[0])
        usuario = item['values'][0]
        
        if usuario == self.sistema.usuario_actual:
            messagebox.showwarning("Advertencia", "No puedes eliminar tu propio usuario")
            return

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar al usuario '{usuario}'?"):
            self.sistema.db.eliminar_usuario(usuario)
            self.actualizar_empleados()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente")

    def actualizar_empleados(self):
        """Actualizar la tabla de empleados"""
        if not self.tree_empleados:
            return
            
        for item in self.tree_empleados.get_children():
            self.tree_empleados.delete(item)
        
        usuarios = self.sistema.db.get_usuarios()
        for usuario, datos in usuarios.items():
            self.tree_empleados.insert('', 'end', values=(usuario, datos['role']))

class VentanaAgregarUsuario:
    def __init__(self, sistema, ventana_empleados):
        self.sistema = sistema
        self.ventana_empleados = ventana_empleados
    
    def crear_ventana(self):
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Agregar Usuario")
        self.ventana.geometry("400x300")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#ecf0f1')
        
        tk.Label(self.ventana, text="Nombre de usuario:", bg='#ecf0f1').pack(pady=5)
        self.entry_usuario = tk.Entry(self.ventana, width=30)
        self.entry_usuario.pack(pady=5)
        
        tk.Label(self.ventana, text="Contraseña:", bg='#ecf0f1').pack(pady=5)
        self.entry_password = tk.Entry(self.ventana, width=30, show='*')
        self.entry_password.pack(pady=5)
        
        tk.Label(self.ventana, text="Tipo de usuario:", bg='#ecf0f1').pack(pady=5)
        
        self.tipo_usuario = tk.StringVar(value="vendedor")
        frame_tipo = tk.Frame(self.ventana, bg='#ecf0f1')
        frame_tipo.pack()
        tk.Radiobutton(frame_tipo, text="Vendedor", variable=self.tipo_usuario, value="vendedor", bg='#ecf0f1').pack(side='left', padx=10)
        tk.Radiobutton(frame_tipo, text="Almacenista", variable=self.tipo_usuario, value="almacenista", bg='#ecf0f1').pack(side='left', padx=10)
        
        tk.Button(self.ventana, text="Guardar", command=self.guardar_usuario, bg='#27ae60', fg='white').pack(pady=20)
    
    def guardar_usuario(self):
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()
        role = self.tipo_usuario.get()
        
        if not usuario or not password:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios", parent=self.ventana)
            return

        exito = self.sistema.db.agregar_usuario(usuario, password, role)
        if exito:
            messagebox.showinfo("Éxito", "Usuario agregado correctamente", parent=self.ventana)
            self.ventana_empleados.actualizar_empleados()
            self.ventana.destroy()
        else:
            messagebox.showerror("Error", "El usuario ya existe", parent=self.ventana)

class VentanaModificarUsuario:
    def __init__(self, sistema, ventana_empleados, usuario_data):
        self.sistema = sistema
        self.ventana_empleados = ventana_empleados
        self.usuario_data = usuario_data
    
    def crear_ventana(self):
        self.ventana = tk.Toplevel(self.sistema.root)
        self.ventana.title("Modificar Usuario")
        self.ventana.geometry("400x300")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#ecf0f1')

        tk.Label(self.ventana, text=f"Usuario: {self.usuario_data['username']}", bg='#ecf0f1').pack(pady=5)
        
        tk.Label(self.ventana, text="Nueva Contraseña:", bg='#ecf0f1').pack(pady=5)
        self.entry_password = tk.Entry(self.ventana, width=30, show='*')
        self.entry_password.pack(pady=5)
        
        tk.Label(self.ventana, text="Nuevo Rol:", bg='#ecf0f1').pack(pady=5)
        
        self.tipo_usuario = tk.StringVar(value=self.usuario_data['role'])
        frame_tipo = tk.Frame(self.ventana, bg='#ecf0f1')
        frame_tipo.pack()
        tk.Radiobutton(frame_tipo, text="Admin", variable=self.tipo_usuario, value="admin", bg='#ecf0f1').pack(side='left', padx=10)
        tk.Radiobutton(frame_tipo, text="Vendedor", variable=self.tipo_usuario, value="vendedor", bg='#ecf0f1').pack(side='left', padx=10)
        tk.Radiobutton(frame_tipo, text="Almacenista", variable=self.tipo_usuario, value="almacenista", bg='#ecf0f1').pack(side='left', padx=10)
        
        tk.Button(self.ventana, text="Guardar Cambios", command=self.guardar_cambios, bg='#f39c12', fg='white').pack(pady=20)
    
    def guardar_cambios(self):
        password = self.entry_password.get().strip()
        role = self.tipo_usuario.get()
        
        if not password:
            messagebox.showwarning("Advertencia", "La contraseña es obligatoria", parent=self.ventana)
            return

        self.sistema.db.modificar_usuario(self.usuario_data['username'], password, role)
        messagebox.showinfo("Éxito", "Usuario modificado correctamente", parent=self.ventana)
        self.ventana_empleados.actualizar_empleados()
        self.ventana.destroy()
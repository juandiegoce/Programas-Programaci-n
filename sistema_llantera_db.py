import tkinter as tk
from tkinter import ttk
from database import DatabaseManager

from ventana_login_db import VentanaLogin
from ventana_inventario_db import VentanaInventario
from ventana_ventas_db import VentanaVentas
from ventana_clientes_db import VentanaClientes
from ventana_reportes_db import VentanaReportes
from ventana_empleados_db import VentanaEmpleados

class SistemaLlantera:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clamatin")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Inicializar base de datos
        self.db = DatabaseManager()
        
        self.usuario_actual = None
        self.role_actual = None
        
        # Instanciar ventanas
        self.ventana_login = VentanaLogin(self)
        self.ventana_inventario = None
        self.ventana_ventas = None
        self.ventana_clientes = None
        self.ventana_reportes = None
        self.ventana_empleados = None
        
        self.ventana_login.crear_ventana()
    
    def iniciar_sesion(self, usuario, role):
        """Método para iniciar sesión y crear el menú principal"""
        self.usuario_actual = usuario
        self.role_actual = role
        self.crear_menu_principal()
    
    def crear_menu_principal(self):
        """Crear el menú principal con pestañas según el rol"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text=f"🔧 CLAMATIN", 
                 font=('Arial', 20, 'bold'), 
                 fg='white', bg='#2c3e50').pack(side='left', padx=10)
        
        tk.Label(header_frame, text=f"Usuario: {self.usuario_actual} ({self.role_actual})", 
                 font=('Arial', 12), 
                 fg='white', bg='#2c3e50').pack(side='left', padx=20)
        
        tk.Button(header_frame, text="🚪 Cerrar Sesión", command=self.cerrar_sesion, 
                  bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=10)
        
        # Notebook (pestañas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Pestaña de Inventario
        self.ventana_inventario = VentanaInventario(self, self.notebook, self.role_actual in ["admin", "almacenista"])
        self.ventana_inventario.crear_pestana()
        
        # Pestaña de Ventas (si es vendedor o admin)
        if self.role_actual in ["admin", "vendedor"]:
            self.ventana_ventas = VentanaVentas(self, self.notebook)
            self.ventana_ventas.crear_pestana()
            
            # Pestaña de Clientes
            self.ventana_clientes = VentanaClientes(self, self.notebook)
            self.ventana_clientes.crear_pestana()
            
            # Pestaña de Reportes
            self.ventana_reportes = VentanaReportes(self, self.notebook)
            self.ventana_reportes.crear_pestana()
        
        # Pestaña de Empleados (si es admin)
        if self.role_actual == "admin":
            self.ventana_empleados = VentanaEmpleados(self, self.notebook)
            self.ventana_empleados.crear_pestana()

    def cerrar_sesion(self):
        """Cerrar sesión y volver a la ventana de login"""
        self.usuario_actual = None
        self.role_actual = None
        self.ventana_login = VentanaLogin(self)
        self.ventana_login.crear_ventana()
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    sistema = SistemaLlantera()
    sistema.run()
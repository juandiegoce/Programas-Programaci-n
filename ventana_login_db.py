import tkinter as tk
from tkinter import messagebox

class VentanaLogin:
    def __init__(self, sistema):
        self.sistema = sistema
        self.root = sistema.root
        self.entry_usuario = None
        self.entry_password = None
        
    def crear_ventana(self):
        """Crear la ventana de login"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        login_frame = tk.Frame(self.root, bg='#2c3e50', relief='raised', bd=2)
        login_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=300)
        
        title_label = tk.Label(login_frame, text="🔧 CLAMATIN", 
                              font=('Arial', 20, 'bold'), 
                              fg='white', bg='#2c3e50')
        title_label.pack(pady=20)
        
        tk.Label(login_frame, text="Usuario:", font=('Arial', 12), 
                fg='white', bg='#2c3e50').pack(pady=5)
        self.entry_usuario = tk.Entry(login_frame, font=('Arial', 12), width=20)
        self.entry_usuario.pack(pady=5)
        
        tk.Label(login_frame, text="Contraseña:", font=('Arial', 12), 
                fg='white', bg='#2c3e50').pack(pady=5)
        self.entry_password = tk.Entry(login_frame, font=('Arial', 12), width=20, show="*")
        self.entry_password.pack(pady=5)
        
        login_btn = tk.Button(login_frame, text="Iniciar Sesión", command=self.iniciar_sesion,
                             font=('Arial', 12, 'bold'), bg='#27ae60', fg='white', 
                             activebackground='#2ecc71', activeforeground='white')
        login_btn.pack(pady=20)
    
    def iniciar_sesion(self):
        """Verificar credenciales y cambiar a la ventana principal"""
        usuario = self.entry_usuario.get().strip()
        password = self.entry_password.get().strip()

        user_data = self.sistema.db.get_usuario_by_username(usuario)

        if user_data and user_data['password'] == password:
            self.sistema.iniciar_sesion(usuario, user_data['role'])
        else:
            messagebox.showerror("Error de Autenticación", "Usuario o contraseña incorrectos")
import tkinter as tk
from tkinter import ttk
from collections import defaultdict
from datetime import datetime

class VentanaReportes:
    def __init__(self, sistema, notebook):
        self.sistema = sistema
        self.notebook = notebook
        self.text_reportes = None
        
    def crear_pestana(self):
        """Crear la pestaña de reportes"""
        self.reportes_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.reportes_frame, text="📊 Reportes")
        
        btn_frame = tk.Frame(self.reportes_frame)
        btn_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Button(btn_frame, text="📈 Reporte de Ventas", command=self.generar_reporte_ventas, 
                 bg='#8e44ad', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="📦 Reporte de Inventario", command=self.generar_reporte_inventario, 
                 bg='#2980b9', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="💰 Reporte Financiero", command=self.generar_reporte_financiero, 
                 bg='#16a085', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=5)
        tk.Button(btn_frame, text="🗑 Limpiar", command=self.limpiar_reportes, 
                 bg='#e74c3c', fg='white', font=('Arial', 10, 'bold')).pack(side='right', padx=5)
        
        self.text_reportes = tk.Text(self.reportes_frame, font=('Courier', 10), wrap='word')
        scrollbar_reportes = ttk.Scrollbar(self.reportes_frame, orient='vertical', command=self.text_reportes.yview)
        self.text_reportes.configure(yscrollcommand=scrollbar_reportes.set)
        
        self.text_reportes.pack(side='left', fill='both', expand=True, padx=(10,0), pady=10)
        scrollbar_reportes.pack(side='right', fill='y', padx=(0,10), pady=10)
        
        mensaje_inicial = """
        🔧 SISTEMA DE REPORTES - LLANTERA
        =====================================
        
        Seleccione un tipo de reporte para generar:
        
        📈 Reporte de Ventas: Muestra todas las ventas realizadas
        📦 Reporte de Inventario: Estado actual del inventario
        💰 Reporte Financiero: Resumen de ingresos y estadísticas
        
        Los reportes aparecerán en esta área.
        """
        self.text_reportes.insert('1.0', mensaje_inicial)
    
    def limpiar_reportes(self):
        """Limpiar el área de reportes"""
        self.text_reportes.delete('1.0', tk.END)
    
    def generar_reporte_ventas(self):
        """Generar reporte detallado de ventas"""
        ventas = self.sistema.db.get_ventas()
        
        if not ventas:
            reporte = """
            📈 REPORTE DE VENTAS
            ==================
            
            ⚠  NO HAY VENTAS REGISTRADAS
            
            """
        else:
            reporte = "=" * 80 + "\n"
            reporte += "                           📈 REPORTE DE VENTAS\n"
            reporte += "=" * 80 + "\n\n"
            
            total_ventas = 0
            ventas_por_vendedor = defaultdict(lambda: {'total': 0, 'cantidad': 0})
            productos_vendidos = defaultdict(int)
            
            for i, venta in enumerate(ventas, 1):
                reporte += f"🛒 VENTA #{venta['id']}:\n"
                reporte += f"   Cliente: {venta['cliente']}\n"
                reporte += f"   Producto: {venta['producto']}\n"
                reporte += f"   Cantidad: {venta['cantidad']} unidades\n"
                reporte += f"   Total: ${venta['total']:.2f}\n"
                reporte += f"   Fecha: {venta['fecha']}\n"
                reporte += f"   Vendedor: {venta['vendedor']}\n"
                reporte += "-" * 60 + "\n\n"
                
                total_ventas += venta['total']
                
                # Estadísticas por vendedor
                ventas_por_vendedor[venta['vendedor']]['total'] += venta['total']
                ventas_por_vendedor[venta['vendedor']]['cantidad'] += 1
                
                # Productos más vendidos
                productos_vendidos[venta['producto']] += venta['cantidad']
            
            # Resumen
            reporte += "=" * 80 + "\n"
            reporte += "                              📊 RESUMEN GENERAL\n"
            reporte += "=" * 80 + "\n"
            reporte += f"💰 Total de ventas realizadas: {len(ventas)}\n"
            reporte += f"💵 Ingresos totales: ${total_ventas:.2f}\n"
            reporte += f"💸 Promedio por venta: ${total_ventas/len(ventas):.2f}\n\n"
            
            reporte += "👨‍💼 VENTAS POR VENDEDOR:\n"
            reporte += "-" * 40 + "\n"
            for vendedor, datos in ventas_por_vendedor.items():
                reporte += f" {vendedor.upper()}:\n"
                reporte += f" • Ventas: {datos['cantidad']}\n"
                reporte += f" • Total: ${datos['total']:.2f}\n"
                reporte += f" • Promedio: ${datos['total']/datos['cantidad']:.2f}\n\n"
            
            if productos_vendidos:
                reporte += "🏆 PRODUCTOS MÁS VENDIDOS:\n"
                reporte += "-" * 40 + "\n"
                productos_ordenados = sorted(productos_vendidos.items(), key=lambda x: x[1], reverse=True)
                for i, (producto, cantidad) in enumerate(productos_ordenados[:5], 1):
                    reporte += f" {i}. {producto}: {cantidad} unidades\n"
            
            reporte += "\n" + "=" * 80 + "\n"
        
        self.text_reportes.delete('1.0', tk.END)
        self.text_reportes.insert('1.0', reporte)
    
    def generar_reporte_inventario(self):
        """Generar reporte detallado del inventario"""
        inventario = self.sistema.db.get_inventario()
        
        reporte = "=" * 80 + "\n"
        reporte += "                           📦 REPORTE DE INVENTARIO\n"
        reporte += "=" * 80 + "\n\n"
        
        valor_total = 0
        productos_bajo_stock = []
        productos_sin_stock = []
        productos_por_marca = defaultdict(int)
        
        for producto in inventario:
            reporte += f"🔧 PRODUCTO ID #{producto['id']}:\n"
            reporte += f"   Marca: {producto['marca']}\n"
            reporte += f"   Modelo: {producto['modelo']}\n"
            reporte += f"   Medida: {producto['medida']}\n"
            reporte += f"   Precio: ${producto['precio']:.2f}\n"
            reporte += f"   Stock: {producto['stock']} unidades\n"
            reporte += "-" * 60 + "\n\n"
            
            valor_total += producto['precio'] * producto['stock']
            productos_por_marca[producto['marca']] += producto['stock']
            
            if producto['stock'] == 0:
                productos_sin_stock.append(producto)
            elif producto['stock'] < 5:
                productos_bajo_stock.append(producto)
                
        # Resumen
        reporte += "=" * 80 + "\n"
        reporte += "                              📊 RESUMEN GENERAL\n"
        reporte += "=" * 80 + "\n"
        reporte += f"🔢 Total de productos distintos: {len(inventario)}\n"
        reporte += f"💲 Valor total del inventario: ${valor_total:.2f}\n\n"
        
        if productos_sin_stock:
            reporte += "⚠️ PRODUCTOS SIN STOCK:\n"
            reporte += "-" * 40 + "\n"
            for p in productos_sin_stock:
                reporte += f" - {p['marca']} {p['modelo']} ({p['medida']})\n"
            reporte += "\n"
        
        if productos_bajo_stock:
            reporte += "⚠️ PRODUCTOS CON BAJO STOCK (menos de 5):\n"
            reporte += "-" * 40 + "\n"
            for p in productos_bajo_stock:
                reporte += f" - {p['marca']} {p['modelo']} ({p['medida']}): {p['stock']} unidades\n"
            reporte += "\n"
            
        reporte += "🏭 STOCK POR MARCA:\n"
        reporte += "-" * 40 + "\n"
        for marca, stock in productos_por_marca.items():
            reporte += f" - {marca}: {stock} unidades\n"
        
        reporte += "\n" + "=" * 80 + "\n"
        
        self.text_reportes.delete('1.0', tk.END)
        self.text_reportes.insert('1.0', reporte)
    
    def generar_reporte_financiero(self):
        """Generar un reporte financiero a partir de las ventas"""
        ventas = self.sistema.db.get_ventas()
        
        reporte = "=" * 80 + "\n"
        reporte += "                           💰 REPORTE FINANCIERO\n"
        reporte += "=" * 80 + "\n\n"
        
        if not ventas:
            reporte += "⚠ NO HAY VENTAS REGISTRADAS PARA GENERAR EL REPORTE.\n"
        else:
            ingresos_totales = sum(v['total'] for v in ventas)
            numero_ventas = len(ventas)
            
            reporte += f"💸 Ingresos Totales por Ventas: ${ingresos_totales:.2f}\n"
            reporte += f"📊 Número Total de Ventas: {numero_ventas}\n"
            if numero_ventas > 0:
                reporte += f"💰 Promedio de Ingreso por Venta: ${ingresos_totales / numero_ventas:.2f}\n"
            else:
                reporte += "💰 Promedio de Ingreso por Venta: $0.00\n"
        
        reporte += "\n" + "=" * 80 + "\n"
        
        self.text_reportes.delete('1.0', tk.END)
        self.text_reportes.insert('1.0', reporte)
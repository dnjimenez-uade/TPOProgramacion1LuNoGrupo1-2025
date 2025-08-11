# Trabajo Práctico Final - Programación 1 con Python
# CRUD - Sistema de gestión de inventarios
#
# *--------------------------------------*
# |                Grupo 1               |
# |--------------------------------------|
# | Integrantes              | Legajo    |
# |--------------------------------------|
# | Cichello, Octavio        | 1215173   |
# | Ianuzzi, Thiago          | 1216765   |
# | Jiménez, Dario Nicolas   | 1225360   |
# | Mora, Santiago           | 1218773   |
# | Zenobio, Lucas           | 1217600   |
# *--------------------------------------*

import random

# Funciones ---------------------------------------------------------------------------------------------------------

def cargar_titulos(t_productos, t_categorias, t_proveedores): # Carga los títulos de las tablas para mostrar en el layout
    t_productos.append('ID Producto','Nombre','Descripción','Cantidad','Precio','Cantidad','ID Categoria', 'ID Proveedor','Anulado')
    t_categorias.append('ID Categoria','Nombre','Descripción')
    t_proveedores.append('ID Proveedor','Nombre','País','Ciudad','Dirección','Código Postal','Teléfono','Email')

# Programa Principal -------------------------------------------------------------------------------------------------

def main():

    # Declarar listas de títulos
    t_productos = []
    t_categorias = []
    t_proveedores = []

    # Declarar matrices de datos
    m_productos = []
    m_categorias = []
    m_proveedores = []

    # Cargar títulos
    cargar_titulos(t_productos, t_categorias, t_proveedores)

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
    t_productos.append('ID Producto','Nombre','Descripción','Cantidad','Precio','ID Categoria', 'ID Proveedor','Anulado')
    t_categorias.append('ID Categoria','Nombre','Descripción')
    t_proveedores.append('ID Proveedor','Nombre','País','Ciudad','Dirección','Código Postal','Teléfono','Email','Tax ID')
'''
def cargar_matriz_producto_manual(m_productos):

    flag = True

    while flag == True:

        id_producto = input("Ingrese el ID del producto (o -1 para terminar): ")
        if id_producto == "-1":
            flag = False
        else:
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            precio = input("Ingrese el precio del producto: ")
            id_categoria = input("Ingrese el ID de la categoría: ")
            id_proveedor = input("Ingrese el ID del proveedor: ")
            anulado = input("¿El producto está anulado? (S/N): ")

        m_productos.append([id_producto, nombre, descripcion, cantidad, precio, id_categoria, id_proveedor, anulado])
'''
def cargar_matriz_categoria_manual(m_categorias):

    flag = True
    while flag == True:
        nombre = input('Ingrese el nombre de la categoría (o -1 para avanzar a la carga de proveedores): ') # Nombre
        if nombre == '-1' and (m_categorias) == 0:
            nombre = input('Ingrese al menos un registro de categoría para avanzar (o -1 para avanzar a la carga de proveedores): ')
        elif id_categoria == "-1":
            flag = False
        else:
            descripcion = input('Ingrese la descripción de la categoría: ') # Descripción
            if len(m_categorias) == 0: # ID Categoria
                id_categoria = 0
            else:
                id_categoria = m_categorias[-1][0] + 1
        m_categorias.append([id_categoria, nombre, descripcion])


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

    # Cargar matrices de forma manual
    cargar_matriz_categoria_manual(m_categorias)
'''
    cargar_matriz_proveedor_manual(m_proveedores)
    cargar_matriz_producto_manual(m_productos)
'''
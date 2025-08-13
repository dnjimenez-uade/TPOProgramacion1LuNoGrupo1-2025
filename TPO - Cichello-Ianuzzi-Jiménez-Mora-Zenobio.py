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

# Lista de cosas pendientes
# FALTA VALIDAR CADA UNO DE LOS CAMPOS ---> 52
# FALTA RELACIONAR LOS IDS DE LAS CATEGORÍAS Y PROVEEDORES CON LAS OTRAS MATRICES ---> 77

#region Librerias
# Librerias ---------------------------------------------------------------------------------------------------------

import random

#region Funciones
# Funciones ---------------------------------------------------------------------------------------------------------

def cargar_titulos(t_productos, t_categorias, t_proveedores): # Carga los títulos de las tablas para mostrar en el layout
    t_productos.append(['ID Producto','Nombre','Descripción','Cantidad','Precio','ID Categoria', 'ID Proveedor','Anulado'])
    t_categorias.append(['ID Categoria','Nombre','Descripción'])
    t_proveedores.append(['ID Proveedor','Nombre','País','Ciudad','Dirección','Código Postal','Teléfono','Email','Tax ID'])


def cargar_matriz_categoria_manual(m_categorias):

    flag = True
    while flag == True:
        nombre = input('Ingrese el nombre de la categoría (o -1 para avanzar a la carga de proveedores): ') # Nombre
        if nombre == '-1' and len(m_categorias) == 0:
            nombre = input('Ingrese al menos un registro de categoría para avanzar, ingrese el nombre de la categoría (o -1 para avanzar a la carga de proveedores): ')
        elif nombre == '-1':
            flag = False
        else:
            descripcion = input('Ingrese la descripción de la categoría: ') # Descripción
            if len(m_categorias) == 0: # ID Categoria
                id_categoria = 1
            else:
                id_categoria = m_categorias[-1][0] + 1
        if nombre != '-1': # Guardo campos en matriz
            m_categorias.append([id_categoria, nombre, descripcion])

# FALTA VALIDAR CADA UNO DE LOS CAMPOS
def cargar_matriz_proveedores_manual(m_proveedores):

    flag = True
    while flag == True:
        nombre = input('Ingrese el nombre del proveedor (o -1 para avanzar a la carga de productos): ') # Nombre
        if nombre == '-1' and len(m_proveedores) == 0:
            nombre = input('Ingrese al menos un registro de proveedor para avanzar, ingrese el nombre del proveedor (o -1 para avanzar a la carga de productos): ')
        elif nombre == '-1':
            flag = False
        else:
            pais = input('Ingrese el país del proveedor: ') # País
            ciudad = input('Ingrese la ciudad del proveedor: ') # Ciudad
            direccion = input('Ingrese la dirección del proveedor: ') # Dirección
            codigo_postal = input('Ingrese el código postal del proveedor: ') # Código Postal
            telefono = input('Ingrese el teléfono del proveedor: ') # Teléfono
            email = input('Ingrese el email del proveedor: ') # Email
            tax_id = input('Ingrese el Tax ID del proveedor: ') # Tax ID
            if len(m_proveedores) == 0: # ID Proveedor
                id_proveedor = 1
            else:
                id_proveedor = m_proveedores[-1][0] + 1
        if nombre != '-1': # Guardo campos en matriz
            m_proveedores.append([id_proveedor, nombre, pais, ciudad, direccion, codigo_postal, telefono, email, tax_id])

# FALTA RELACIONAR LOS IDS DE LAS CATEGORÍAS Y PROVEEDORES CON LAS OTRAS MATRICES
def cargar_matriz_productos_manual(m_productos):

    flag = True
    while flag == True:
        nombre = input('Ingrese el nombre del producto (o -1 para terminar la ejecución): ') # Nombre
        if nombre == '-1':
            flag = False
        else:
            descripcion = input("Ingrese la descripción del producto: ") # Descripción
            cantidad = input("Ingrese la cantidad del producto: ") # Cantidad
            precio = input("Ingrese el precio del producto: ") # Precio
            id_categoria = input("Ingrese el ID de la categoría: ") # ID Categoría
            id_proveedor = input("Ingrese el ID del proveedor: ") # ID Proveedor
            anulado = input("Ingrese si el producto esta anulado ('X' para Sí): ") # Anulado
            if len(m_productos) == 0: # ID Producto
                id_producto = 1
            else:
                id_producto = m_productos[-1][0] + 1
        if nombre != '-1': # Guardo campos en matriz
            m_productos.append([id_producto, nombre, descripcion, cantidad, precio, id_categoria, id_proveedor, anulado])

def imprimir_tabla_datos(encabezado, matriz_datos):
    columnas = len(encabezado)
    anchos = [len(str(encabezado[i])) for i in range(columnas)]
    for fila in matriz_datos:
        for i in range(columnas):
            anchos[i] = max(anchos[i], len(str(fila[i])))

    # Construir separador
    separador = '+'
    for ancho in anchos:
        separador += '-' * (ancho + 2) + '+'

    # Imprimir encabezado
    print(separador)
    fila_encabezado = '| '
    for i in range(columnas):
        valor = str(encabezado[i])
        espacios = anchos[i] - len(valor)
        fila_encabezado += valor + ' ' * espacios + ' | '
    print(fila_encabezado)
    print(separador)

    # Imprimir filas de datos
    for fila in matriz_datos:
        fila_formateada = '| '
        for i in range(columnas):
            valor = str(fila[i])
            espacios = anchos[i] - len(valor)
            fila_formateada += valor + ' ' * espacios + ' | '
        print(fila_formateada)
    print(separador)

#region Programa Principal
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
    cargar_matriz_proveedores_manual(m_proveedores)
    cargar_matriz_productos_manual(m_productos)

    print()
    imprimir_tabla_datos(t_categorias[0], m_categorias)
    print()
    imprimir_tabla_datos(t_proveedores[0], m_proveedores)
    print()
    imprimir_tabla_datos(t_productos[0], m_productos)


main()
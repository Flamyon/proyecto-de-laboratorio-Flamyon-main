# este documento es solo de prueba, todavia no hay código en este proyecto
from csv import reader
from datetime import date, datetime


def extraer_datos():
    with open('dataset1.csv', encoding='utf-8') as f:
        reader = reader.csv(f)
        next(f)
        datos = []
        for columna in reader:
            fecha_pedido = date(columna[0])
            marca = columna[1]
            nombre = columna[2]
            precio_reventa = columna[3]
            precio_venta = columna[4]
            fecha_lanzamiento = date(columna[5])
            talla = int(columna[6])
            region_compra = columna[7]
            precio_reventa_menor = bool(columna[8])
            tupla = (fecha_pedido, marca, nombre, precio_reventa, precio_venta,
                     fecha_lanzamiento, talla, region_compra, precio_reventa_menor)
            datos.append(tupla)

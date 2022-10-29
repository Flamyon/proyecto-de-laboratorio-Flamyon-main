from datetime import date, datetime
import csv


def extraer_datos():
    with open('C:/Users/franr/OneDrive/Escritorio/informatica_us/FP/practicas/proyecto-de-laboratorio-Flamyon-main/proyecto-de-laboratorio-Flamyon-main/data/dataset1.csv') as f:
        lector = csv.reader(f)
        next(f)
        datos = []
        for columna in lector:
            fecha_pedido = columna[0]
            marca = columna[1]
            nombre = columna[2]
            precio_reventa = columna[3]
            precio_venta = columna[4]
            fecha_lanzamiento = columna[5]
            talla = int(columna[6])
            region_compra = columna[7]
            precio_reventa_menor = bool(columna[8])
            tupla = (fecha_pedido, marca, nombre, precio_reventa, precio_venta,
                     fecha_lanzamiento, talla, region_compra, precio_reventa_menor)
            datos.append(tupla)
    return datos

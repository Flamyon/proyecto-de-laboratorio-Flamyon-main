from datetime import date, datetime
import csv


def extraer_datos(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        datos = list()
        for columna in lector:
            fecha_pedido = datetime(columna[0], '%m/%d/%Y').date
            marca = columna[1]
            nombre = columna[2]
            precio_reventa = float(
                columna[3].replace('$', '').replace(',', '.').replace('$', ''))
            precio_venta = float(columna[4].replace(
                '$', '').replace(',', '.').replace('"', ''))
            fecha_lanzamiento = datetime(columna[5], '%m/%d/%Y').date
            talla = int(columna[6])
            region_compra = columna[7]
            if columna[8] == 'TRUE':
                columna[8] = True
            else:
                columna[8] = False
            precio_reventa_menor = columna[8]
            tupla = (fecha_pedido, marca, nombre, precio_reventa, precio_venta,
                     fecha_lanzamiento, talla, region_compra, precio_reventa_menor)
            datos.append(tupla)
    return datos

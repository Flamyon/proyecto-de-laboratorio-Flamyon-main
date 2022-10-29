from datetime import date, datetime
import csv


def extraer_datos(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        datos = list()
        for columna in lector:
            fechaPedido = datetime.strptime(columna[0], '%m/%d/%Y').date()
            marca = columna[1]
            nombre = columna[2]
            precioReventa = float(columna[3])
            precioVenta = float(columna[4])
            fechaLanzamiento = datetime.strptime(columna[5], '%m/%d/%Y').date()
            talla = int(columna[6])
            region_compra = columna[7]
            if columna[8] == 'TRUE':
                columna[8] = True
            else:
                columna[8] = False
            precioReventaMenor = columna[8]
            tupla = (fechaPedido, marca, nombre, precioReventa, precioVenta,
                     fechaLanzamiento, talla, region_compra, precioReventaMenor)
            datos.append(tupla)
    return datos

from datetime import date, datetime
import csv
from collections import namedtuple

Stock = namedtuple('Stock', ['FechaPedido', 'Marca', 'Nombre', 'PrecioReventa',
                   'PrecioVenta', 'FechaLanzamiento', 'Talla', 'Region', 'PrecioReventaMenor'])


def extraer_datos(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        datos = list()
        for columna in lector:
            FechaPedido = datetime.strptime(columna[0], '%m/%d/%Y').date()
            Marca = columna[1]
            Nombre = columna[2]
            PrecioReventa = float(columna[3])
            PrecioVenta = float(columna[4])
            FechaLanzamiento = datetime.strptime(columna[5], '%m/%d/%Y').date()
            Talla = int(columna[6])
            Region = columna[7]
            PrecioReventaMenor = columna[8] == 'TRUE'
            tupla = Stock(FechaPedido, Marca, Nombre, PrecioReventa, PrecioVenta,
                          FechaLanzamiento, Talla, Region, PrecioReventaMenor)
            datos.append(tupla)
        return datos

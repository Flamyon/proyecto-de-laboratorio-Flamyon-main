from datetime import date, datetime
import csv
from collections import namedtuple
from sqlite3 import DateFromTicks

Stock = namedtuple(
    'Stock', 'FechaPedido,Marca,Nombre,PrecioReventa,PrecioVenta,FechaLanzamiento,Talla,Region,PrecioReventaMenor')


def extraer_datos(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        next(lector)
        datos = list()
        for c in lector:
            c[0] = datetime.strptime(c[0], '%m/%d/%Y').date()
            c[3] = float(c[3])
            c[4] = float(c[4])
            c[5] = datetime.strptime(c[5], '%m/%d/%Y').date()
            c[6] = int(c[6])
            c[8] = c[8] == 'TRUE'
            tupla = Stock(c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7], c[8])
            datos.append(tupla)
        return datos


def tallas_distintas(datos):
    tallas = set()
    for i in datos:
        tallas.add(i.Talla)
    return len(tallas)


def media_PrecioReventa(datos):
    PreciosReventa = list()
    for i in datos:
        PreciosReventa.append(i.PrecioReventa)
    return (sum(PreciosReventa)/len(PreciosReventa))

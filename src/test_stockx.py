from tkinter import S
from stockx import *


def test_extraer_datos():
    print('Numero total de registros: ', len(datos), '\n')
    print('----------------------------------------------------------------------------')
    print('\nLos datos de los 3 primeros registros leídos: ', datos[:3], '\n')
    print('----------------------------------------------------------------------------')
    print('\nY los 3 últimos registros leídos de venta fueron',
          datos[-3:], '\n')
    print('----------------------------------------------------------------------------')


def test_tallas_distintas():
    print('\nEl numero total de tallas distintas: ',
          tallas_distintas(datos), '\n')
    print('----------------------------------------------------------------------------')


def test_media_PrecioReventa():
    print('\nLa media del precio de reventa es: ',
          media_PrecioReventa(datos), '\n')
    print('----------------------------------------------------------------------------')


datos = extraer_datos('data/dataset1.csv')
test_extraer_datos()
test_tallas_distintas()
test_media_PrecioReventa()

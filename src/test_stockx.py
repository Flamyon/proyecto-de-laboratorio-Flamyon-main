from stockx import *


def test_extraer_datos():
    print('Numero total de registros: ', len(datos))


datos = extraer_datos('data/dataset1.csv')
test_extraer_datos()

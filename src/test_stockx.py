from stockx import *


def test_extraer_datos():
    print('Numero total de registros: ', len(datos))
    print('Los datos de la primera venta fueron : ', datos[0])


datos = extraer_datos('data/dataset1.csv')
test_extraer_datos()

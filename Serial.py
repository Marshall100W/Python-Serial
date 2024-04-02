### Abril 2024. ###

import serial
import serial.tools.list_ports
import time


puerto = 'COM14'
valor = 0
lectura = 1


def lista_puertos():
    lista_puertos = serial.tools.list_ports.comports()
    print('Encontrados', len(lista_puertos), 'puertos.')

    for i in range(len(lista_puertos)):
        print(lista_puertos[i].name)


def conectarse_a_puerto():
    try:
        global serial_XIAO
        serial_XIAO = serial.Serial(puerto, 115200)
        time.sleep(1)
    except:
        print('*** No se pudo conectar a', puerto, '***')
        time.sleep(2)


def lee_datos(lectura):
    try:
        valor = serial_XIAO.readline().decode('ascii')
        valor = valor[slice(0,len(valor)-1)] 
        print('-', valor)
        lectura = 1
    except:
        print('Error ('+ str(lectura) + ') leyendo puerto ' + puerto, end=' ')
        conectarse_a_puerto()
        lectura += 1
    finally:
        return lectura

##################################################################


print('\n\n*** UP THE IRONS! ***\n')
lista_puertos()
conectarse_a_puerto()

while lectura < 6:
    lectura = lee_datos(lectura)
    time.sleep(1)


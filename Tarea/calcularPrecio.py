'''
Christopher Flores
10-10824

Funcion calcularPrecio para la Tarea 2 de Ing. del Software (ABR-JUL 2016). 

'''

from decimal import Decimal
from datetime import *

# Maneja una tasa para los dias de semana y otra para los fines de semana. 
class Tarifa(object):
    def __init__(self, tasaDiaSemana, tasaFinSemana):
        self.tasaDiaSemana = tasaDiaSemana
        self.tasaFinSemana = tasaFinSemana
    
# Dado un tiempo de reservacion:
#     tiempoDeReservacionr = [inicioDeReservacion, finDeReservacion]   
# Calcula el monto a pagar por la misma. 
def calcularPrecio(tarifa, tiempoDeReservacionr):
        
        if tarifa.tasaDiaSemana < 0 or tarifa.tasaFinSemana < 0:
            raise Exception("No se admiten tarifas negativas.")
        if tiempoDeReservacionr[1] - tiempoDeReservacionr[0] > timedelta(days=7):
            raise Exception("La reserva no debe ser mayor a siete (7) dias.")
        if tiempoDeReservacionr[1] - tiempoDeReservacionr[0] < timedelta(minutes=15):
            raise Exception("La reserva debe ser como minimo de quince (15) mintuos")
        
        
if __name__ == '__main__':
    tarifa_de_prueba = Tarifa(5,7)
    ini_reserva = datetime(2015, 4, 21, 6, 15)
    fin_reserva = datetime(2015, 4, 12, 6, 29)
    tiempo_reserva = [ini_reserva,fin_reserva]
    calcularPrecio(tarifa_de_prueba,tiempo_reserva)
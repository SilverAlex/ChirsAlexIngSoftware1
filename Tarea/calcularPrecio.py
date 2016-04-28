'''
Created on 27 de abr. de 2016

@author: Silver
'''
from decimal import Decimal
from datetime import *
from doctest import SKIP
from math import ceil

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
        
        if tiempoDeReservacionr[0].weekday() < 5 and tiempoDeReservacionr[1].weekday() < 5:
            horasReserva = (tiempoDeReservacionr[1]-tiempoDeReservacionr[0]).total_seconds()/3600
            return ceil(horasReserva)*tarifa.tasaDiaSemana
        elif  tiempoDeReservacionr[0].weekday() >= 5 and tiempoDeReservacionr[1].weekday() >= 5:
            horasReserva = (tiempoDeReservacionr[1]-tiempoDeReservacionr[0]).total_seconds()/3600
            return ceil(horasReserva)*tarifa.tasaFinSemana
        else:
            horasReservaSem = 0
            while tiempoDeReservacionr[0].weekday() <= 4:
                tiempoDeReservacionr[0] += timedelta(0,3600)
                horasReservaSem += 1
            horasReservaFin = 0
            while tiempoDeReservacionr[0] <= tiempoDeReservacionr[1]:
                tiempoDeReservacionr[0] += timedelta(0,3600)
                horasReservaFin += 1
            return horasReservaSem*tarifa.tasaDiaSemana + horasReservaFin*tarifa.tasaFinSemana
            
            
if __name__ == '__main__':
    tarifa_de_prueba = Tarifa(0,0)
    ini_reserva = datetime(2016, 4, 15, 0, 0)
    fin_reserva = datetime(2016, 4, 16, 15, 0)
    tiempo_reserva = [ini_reserva,fin_reserva]
    print(calcularPrecio(tarifa_de_prueba,tiempo_reserva))
        
    
    

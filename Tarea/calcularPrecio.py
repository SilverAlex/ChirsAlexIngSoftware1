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
#     tiempoDeTrabajo = [inicioDeReservacion, finDeReservacion]   
# Calcula el monto a pagar por la misma. 
def calcularPrecio(tarifa, tiempoDeTrabajo):
        
        if tarifa.tasaDiaSemana < 0 or tarifa.tasaFinSemana < 0:
            raise Exception("No se admiten tarifas negativas.")
        if tiempoDeTrabajo[1] - tiempoDeTrabajo[0] > timedelta(days=7):
            raise Exception("La reserva no debe ser mayor a siete (7) dias.")
        if tiempoDeTrabajo[1] - tiempoDeTrabajo[0] < timedelta(minutes=15):
            raise Exception("La reserva debe ser como minimo de quince (15) mintuos")
        
        if tiempoDeTrabajo[0].weekday() < 5 and tiempoDeTrabajo[1].weekday() < 5:
            if tiempoDeTrabajo[0].weekday() >= tiempoDeTrabajo[1].weekday():
                horasTrabajoSem = 0
                while (tiempoDeTrabajo[0].weekday() <= 4 and 
                       tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]
                       ):
                    tiempoDeTrabajo[0] += timedelta(0,3600)
                    horasTrabajoSem += 1
                horasTrabajoFin = 0
                while tiempoDeTrabajo[0].weekday() >= 5:
                    tiempoDeTrabajo[0] += timedelta(0,3600)
                    horasTrabajoFin += 1
                while tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]:
                    tiempoDeTrabajo[0] += timedelta(0,3600)
                    horasTrabajoSem += 1
                return horasTrabajoSem*tarifa.tasaDiaSemana + horasTrabajoFin*tarifa.tasaFinSemana
            else:
                horasReserva = (tiempoDeTrabajo[1]-tiempoDeTrabajo[0]).total_seconds()/3600
                return ceil(horasReserva)*tarifa.tasaDiaSemana
        elif  tiempoDeTrabajo[0].weekday() >= 5 and tiempoDeTrabajo[1].weekday() >= 5:
            if tiempoDeTrabajo[0].weekday() >= tiempoDeTrabajo[1].weekday():
                horasTrabajoSem = 0
                horasTrabajoFin = 0
                while (tiempoDeTrabajo[0].weekday() >= 5 and 
                       tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]):
                    tiempoDeTrabajo[0] += timedelta(0,3600)
                    horasTrabajoFin += 1
                while (tiempoDeTrabajo[0].weekday() <= 4 and 
                       tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]
                       ):
                    tiempoDeTrabajo[0] += timedelta(0,3600)
                    horasTrabajoSem += 1                
                while tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]:
                    tiempoDeTrabajo[0] += timedelta(0,3600)
                    horasTrabajoFin += 1
                return horasTrabajoSem*tarifa.tasaDiaSemana + horasTrabajoFin*tarifa.tasaFinSemana
            else:
                horasReserva = (tiempoDeTrabajo[1]-tiempoDeTrabajo[0]).total_seconds()/3600
                return ceil(horasReserva)*tarifa.tasaFinSemana
        elif  tiempoDeTrabajo[0].weekday() < 5 and tiempoDeTrabajo[1].weekday() >= 5:
            horasTrabajoSem = 0
            while tiempoDeTrabajo[0].weekday() <= 4:
                tiempoDeTrabajo[0] += timedelta(0,3600)
                horasTrabajoSem += 1
            horasTrabajoFin = 0
            if tiempoDeTrabajo[0] >= tiempoDeTrabajo[1]:
                horasTrabajoFin += 1
            while tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]:
                tiempoDeTrabajo[0] += timedelta(0,3600)
                horasTrabajoFin += 1
            return horasTrabajoSem*tarifa.tasaDiaSemana + horasTrabajoFin*tarifa.tasaFinSemana
        elif tiempoDeTrabajo[0].weekday() >= 5 and tiempoDeTrabajo[1].weekday() < 5:
            horasTrabajoSem = 0
            horasTrabajoFin = 0
            while tiempoDeTrabajo[0].weekday() != 0 :
                tiempoDeTrabajo[0] += timedelta(0,3600)
                horasTrabajoSem += 1
            if tiempoDeTrabajo[0] >= tiempoDeTrabajo[1]:
                horasTrabajoFin += 1
            while tiempoDeTrabajo[0] <= tiempoDeTrabajo[1]:
                tiempoDeTrabajo[0] += timedelta(0,3600)
                horasTrabajoFin += 1
            return horasTrabajoSem*tarifa.tasaDiaSemana + horasTrabajoFin*tarifa.tasaFinSemana
                                
            
if __name__ == '__main__':
    tarifa_de_prueba = Tarifa(2,3)
    ini_reserva = datetime(2015, 4, 20, 6, 0)
    fin_reserva = datetime(2015, 4, 27, 6, 0)
    tiempo_reserva = [ini_reserva,fin_reserva]
    precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
    print(precio)
        
    
    

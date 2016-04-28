'''
Created on 28 de abr. de 2016

@author: Silver
'''
import unittest
from calcularPrecio import * 
from datetime import datetime
from decimal import Decimal
from virtualenv import maxint

class Test_calcularPrecio(unittest.TestCase):

    def testTarifa(self):
        aTarifa = Tarifa(0,0)
        self.assertEqual(aTarifa.tasaDiaSemana, 0, "algo explota")
        self.assertEqual(aTarifa.tasaFinSemana, 0, "algo exploto, fin de semana")
        
    def test0Timer(self):
        # Caso de prueba tiempo de reservacion = (0) minutos
        pass
    
    def test0Tarifa(self):
        # Caso de prueba Tarifa(0,0)
        aTarifa = Tarifa(0,0)
        ini_reserva = datetime(2016, 4, 15, 23, 0)
        fin_reserva = datetime(2016, 4, 16, 23, 0)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempo_reserva), 0,
                          "El precio debe ser 0 para tarifa(0,0) ")
            
    def test14MinTimer(self):
        # Caso de prueba tiempo de reservacion = (14) minutos
        aTarifa = Tarifa(0,0)
        ini_reserva = datetime(2016, 4, 15, 0, 0)
        fin_reserva = datetime(2016, 4, 15, 14, 0)
        tiempo_reserva = [ini_reserva,fin_reserva]
        
    def test15MTimeT0(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        aTarifa = Tarifa(0,0)
        ini_reserva = datetime(2016, 4, 15, 0, 0)
        fin_reserva = datetime(2016, 4, 15, 0, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        
        self.assertEqual(calcularPrecio(aTarifa, tiempo_reserva), 0,
                          "El precio debe ser 0 para t=0,0 y tiempo = 15 ")
    def test15MTimeTarifa1Semana(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        aTarifa = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 15, 0, 0)
        fin_reserva = datetime(2016, 4, 15, 0, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempo_reserva), 1,
                          "El precio debe ser 1 para t=1 y tiempo = 15 ")
        
    def test15MTimeTarifa2FinSemana(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        aTarifa = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 16, 0, 0)
        fin_reserva = datetime(2016, 4, 16, 0, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempo_reserva), 2,
                          "El precio debe ser 2 para t=1 y tiempo = 15 ")
    
    def test15MTimeTarifa1_2CasoBorde(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        aTarifa = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 15, 23, 46)
        fin_reserva = datetime(2016, 4, 16, 0, 1)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempo_reserva), 3,
                              "El precio debe ser 2 para t=1 y tiempo = 15 ")


    def testMaxTarifa15MTime(self):
        aTarifa = Tarifa(maxint,maxint)
        ini_reserva = datetime(2016, 4, 15, 0, 0)
        fin_reserva = datetime(2016, 4, 15, 0, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa,tiempo_reserva), maxint, "El resultado debio ser maxint")
                                    
    def test7DaysTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias con tarifa decimal
        pass
    def test7Days1MinTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias, (1) minuto
        pass
    
    def testNegativeTimer(self):
        pass# Caso de prueba tiempo de reservacion Negativo
        
    def testNegativeTarifa(self):
        pass# Caso de prueba tarifa negativa
        
    def testImaginaryTarifa(self):
        pass# Caso de prueba tarifa imaginaria
        
    def testCharTimer(self):
        pass# Caso de prueba tiempo de reservacion con caracteres
        
    def testDiferentTimer(self):
        pass# Caso de prueba tiempo de reservacion de tipo entero
    
    def testDecimal1Tarifa(self):
        pass# Caso de prueba Tarifa decimal 1
        
    def testDecimal2Tarifa(self):
        # Caso de prueba Tarifa decimal 2
        pass
    
    def testSecondsTimer(self):
        # Caso de prueba tiempo de reservacion con segundos
        pass
    def testBigTarifa(self):
        # Caso de prueba tarifa muy grande
        pass
        
    def testTimerMax(self):
        # Caso de prueba tiempo de reservacion maximo
        pass
            
if __name__ == "__main__":
    unittest.main()

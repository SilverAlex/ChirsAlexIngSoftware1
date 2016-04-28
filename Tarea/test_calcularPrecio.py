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

    def test0Timer(self):
        # Caso de prueba tiempo de reservacion = (0) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
        
    def test0Tarifa(self):
        # Caso de prueba Tarifa(0,0)
        tarifa_de_prueba = Tarifa(0,0)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 10)
        tiempo_reserva = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(precio, 0)  
    
    def test14MinTimer(self):
        # Caso de prueba tiempo de reservacion = (14) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 29)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)       
        
    def test15MTimeSmallT(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia
        tarifa_de_prueba = Tarifa(0.01,0.01)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 30)
        tiempo_reserva = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(precio, 0.01) 

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

    def test7DaysTimerLunDom(self):
        # Caso de prueba tiempo de reservacion = (7) 
        tarifa_de_prueba = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 11, 0, 0)
        fin_reserva = datetime(2016, 4, 17, 23, 59)
        tiempo_reserva = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(precio,((1*5*24)+(2*2*24)))
    
    def test7DaysTimerLunLun(self):
        # Caso de prueba tiempo de reservacion = (7) 
        tarifa_de_prueba = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 11, 6, 0)
        fin_reserva = datetime(2016, 4, 18, 5, 59)
        tiempo_reserva = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(precio,((1*5*24)+(2*2*24)))
        
    def test7Days1MinTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias, (1) minuto
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 16)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
       
    
    def testNegativeTimer(self):
        # Caso de prueba tiempo de reservacion Negativo
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 20, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
        
    def testNegativeTarifa(self):
        # Caso de prueba tarifa negativa
        tarifa_de_prueba = Tarifa(-2,-1)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
        
    def testImaginaryTarifa(self):
        # Caso de prueba tarifa imaginaria
        tarifa_de_prueba = Tarifa(5j,7j)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(TypeError,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
        
    def testCharTimer(self):
        # Caso de prueba tiempo de reservacion con caracteres
        tarifa_de_prueba = Tarifa("a","b")
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(TypeError,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
        
    def testDiferentTimer(self):
        # Caso de prueba tiempo de reservacion de tipo entero
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = 100
        fin_reserva = 101
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(TypeError,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
    
    def testDecimal1Tarifa(self):
        # Caso de prueba Tarifa decimal 1
        tarifa_de_prueba = Tarifa(0.001,0.001)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
        
    def testDecimal2Tarifa(self):
        # Caso de prueba Tarifa decimal 2
        tarifa_de_prueba = Tarifa(5.4,7.6)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(precio,(Decimal((5.4*5*24)+ 7.6*2*24).quantize(Decimal('1.00'))))
        
    def testSecondsTimer(self):
        # Caso de prueba tiempo de reservacion con segundos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15, 2)
        fin_reserva = datetime(2015, 4, 22, 6, 15, 3)
        tiempo_reserva = [ini_reserva,fin_reserva]
        calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)

    def testBigTarifa(self):
        # Caso de prueba tarifa muy grande
        tarifa_de_prueba = Tarifa(2**31,2**64)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempo_reserva)
        self.assertEqual(precio, (((2**31)*5*24) + (2**64)*2*24))
        
    def testTimerMax(self):
        # Caso de prueba tiempo de reservacion maximo
        tarifa_de_prueba = Tarifa(2,3)
        ini_reserva = datetime.max
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempo_reserva = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempo_reserva)
            
if __name__ == "__main__":
    unittest.main()

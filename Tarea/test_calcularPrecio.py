'''
Created on 28 de abr. de 2016

@author: Alejandro
         Christopher
'''
import unittest
from calcularPrecio import * 
from datetime import datetime
from decimal import Decimal
from virtualenv import maxint

class Test_calcularPrecio(unittest.TestCase):

    def test0Timer(self):
        # Caso de prueba tiempo de trabajo = (0) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
        
    def test0Tarifa(self):
        # Caso de prueba Tarifa(0,0)
        tarifa_de_prueba = Tarifa(0,0)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 10)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempoTrabajo)
        self.assertEqual(precio, 0, "El precio debe ser 0 para t=0 y tiempo= 7 dias")  
    
    def test14MinTimer(self):
        # Caso de prueba tiempo de trabajo = (14) minutos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 29)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)       
        
    def test15MTimeSmallT(self):
        # Caso de prueba tiempo de trabajo = (15) minutos, tarifa pequenia
        tarifa_de_prueba = Tarifa(0.01,0.01)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 21, 6, 30)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempoTrabajo)
        self.assertEqual(precio, 0.01, "El precio debe ser 0.01 para t=0 y tiempo= 15") 

    def test15MTimeTarifa1Semana(self):
        # Caso de prueba tiempo de trabajo = (15) minutos, tarifa pequenia, dias de semana
        aTarifa = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 15, 0, 0)
        fin_reserva = datetime(2016, 4, 15, 0, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempoTrabajo), 1,
                          "El precio debe ser 1 para t=1 y tiempo = 15 ")
        
    def test15MTimeTarifa2FinSemana(self):
        # Caso de prueba tiempo de trabajo = (15) minutos, tarifa pequenia, fines de semana
        aTarifa = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 16, 0, 0)
        fin_reserva = datetime(2016, 4, 16, 0, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempoTrabajo), 2,
                          "El precio debe ser 2 para t=1 y tiempo = 15 ")
    
    def test15MTimeTarifa1_2CasoBorde(self):
        # Caso de prueba tiempo de trabajo = (15) minutos, tarifa pequenia, entre viernes y sabado
        aTarifa = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 15, 23, 46)
        fin_reserva = datetime(2016, 4, 16, 0, 1)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa, tiempoTrabajo), 3,
                              "El precio debe ser 3 para t=1 y tiempo = 15 ")

    def testMaxTarifa15MTime(self):
        #Caso de prueba tarifa maxima, 15 minutos
        aTarifa = Tarifa(maxint,maxint)
        ini_reserva = datetime(2016, 4, 15, 0, 0)
        fin_reserva = datetime(2016, 4, 15, 0, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(aTarifa,tiempoTrabajo), maxint, "El resultado debio ser maxint")        

    def test7DaysTimerLunDom(self):
        # Caso de prueba tiempo de trabajo = (7) 
        tarifa_de_prueba = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 11, 0, 0)
        fin_reserva = datetime(2016, 4, 17, 23, 59)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempoTrabajo)
        self.assertEqual(precio,((1*5*24)+(2*2*24)), "El precio debe ser 216 para t=1 y tiempo=7 dias")
    
    def test7DaysTimerLunLun(self):
        # Caso de prueba tiempo de trabajo = (7) 
        tarifa_de_prueba = Tarifa(1,2)
        ini_reserva = datetime(2016, 4, 11, 6, 0)
        fin_reserva = datetime(2016, 4, 18, 5, 59)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempoTrabajo)
        self.assertEqual(precio,((1*5*24)+(2*2*24)), "El precio debe ser 216 para t= 1 y tiempo= 7 dias")
        
    def test7Days1MinTimer(self):
        # Caso de prueba tiempo de trabajo = (7) dias, (1) minuto
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 16)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
       
    
    def testNegativeTimer(self):
        # Caso de prueba tiempo de trabajo Negativo
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 20, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
        
    def testNegativeTarifa(self):
        # Caso de prueba tarifa negativa
        tarifa_de_prueba = Tarifa(-2,-1)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
        
    def testImaginaryTarifa(self):
        # Caso de prueba tarifa imaginaria
        tarifa_de_prueba = Tarifa(5j,7j)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(TypeError,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
    
    def testDay(self):
        # Caso de prueba Dias erroneos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2016, 4, 24, 6, 15)
        fin_reserva = datetime(2015, 4, 20, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)

    def testCharTarifa(self):
        # Caso de prueba tiempo de trabajo con caracteres
        tarifa_de_prueba = Tarifa("a","b")
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(TypeError,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
        
    def testDiferentTimer(self):
        # Caso de prueba tiempo de trabajo de tipo entero
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = 100
        fin_reserva = 101
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(TypeError,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
    
    def testDecimal1Tarifa(self):
        # Caso de prueba Tarifa decimal 1
        tarifa_de_prueba = Tarifa(0.001,0.001)
        ini_reserva = datetime(2016, 4, 18, 6, 15)
        fin_reserva = datetime(2016, 4, 25, 6, 14)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertEqual(calcularPrecio(tarifa_de_prueba, tiempoTrabajo),
                          (0.001 * 5 * 24) + (0.001 * 2 * 24))
        
    def testDecimal2Tarifa(self):
        # Caso de prueba Tarifa decimal 2
        tarifa_de_prueba = Tarifa(5.4,7.6)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 14)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempoTrabajo)
        self.assertEqual(precio,(5.4*5*24) + (7.6*2*24))

    def testSecondsTimer(self):
        # Caso de prueba tiempo de trabajo con segundos
        tarifa_de_prueba = Tarifa(5,7)
        ini_reserva = datetime(2015, 4, 21, 6, 15, 2)
        fin_reserva = datetime(2015, 4, 21, 6, 15, 3)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)

    def testBigTarifa(self):
        # Caso de prueba tarifa muy grande
        tarifa_de_prueba = Tarifa(2**31,2**64)
        ini_reserva = datetime(2015, 4, 21, 6, 15)
        fin_reserva = datetime(2015, 4, 28, 6, 14)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        precio = calcularPrecio(tarifa_de_prueba, tiempoTrabajo)
        self.assertEqual(precio, (((2**31)*5*24) + (2**64)*2*24))
        
    def testTimerMax(self):
        # Caso de prueba tiempo de trabajo maximo
        tarifa_de_prueba = Tarifa(2,3)
        ini_reserva = datetime.max
        fin_reserva = datetime(2015, 4, 27, 6, 15)
        tiempoTrabajo = [ini_reserva,fin_reserva]
        self.assertRaises(Exception,calcularPrecio,tarifa_de_prueba, tiempoTrabajo)
            
if __name__ == "__main__":
    unittest.main()

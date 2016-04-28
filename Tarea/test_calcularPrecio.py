'''

@author: Christopher Flores
'''
import unittest
from calcularPrecio import Tarifa,calcularPrecio
from datetime import datetime
from decimal import Decimal

class Test_calcularPrecio(unittest.TestCase):

    def test0Timer(self):
        # Caso de prueba tiempo de reservacion = (0) minutos
        
    def test0Tarifa(self):
        # Caso de prueba Tarifa(0,0)
   
    def test14MinTimer(self):
        # Caso de prueba tiempo de reservacion = (14) minutos
   
    def test15MTimeSmallT(self):
        # Caso de prueba tiempo de reservacion = (15) minutos, tarifa pequenia

            
    def test7DaysTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias con tarifa decimal
    
    def test7Days1MinTimer(self):
        # Caso de prueba tiempo de reservacion = (7) dias, (1) minuto
       
    
    def testNegativeTimer(self):
        # Caso de prueba tiempo de reservacion Negativo
        
    def testNegativeTarifa(self):
        # Caso de prueba tarifa negativa
        
    def testImaginaryTarifa(self):
        # Caso de prueba tarifa imaginaria
        
    def testCharTimer(self):
        # Caso de prueba tiempo de reservacion con caracteres
        
    def testDiferentTimer(self):
        # Caso de prueba tiempo de reservacion de tipo entero
    
    def testDecimal1Tarifa(self):
        # Caso de prueba Tarifa decimal 1
        
    def testDecimal2Tarifa(self):
        # Caso de prueba Tarifa decimal 2
        
    def testSecondsTimer(self):
        # Caso de prueba tiempo de reservacion con segundos
    def testBigTarifa(self):
        # Caso de prueba tarifa muy grande
        
    def testTimerMax(self):
        # Caso de prueba tiempo de reservacion maximo
            
if __name__ == "__main__":
    unittest.main()
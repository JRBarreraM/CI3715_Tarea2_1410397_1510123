import unittest
from rules import *

class pensionTester(unittest.TestCase):

    #Mujer de 55 años con 750 horas acreditadas sin años peligrosos 
    def testCase01(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1965-01-26',0), True)
        print("Case01: Approved")

    #Hombre de 60 años con 750 horas acreditadas sin años peligrosos 
    def testCase02(self):
        self.assertEqual(aplicaPensionIVSS('M',750,'1960-01-21',0), True)
        print("Case02: Approved")
    
    #Mujer de 54 años con 750 horas acreditadas sin años peligrosos 
    def testCase03(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1966-01-26',0), False)
        print("Case03: Approved")

    #Mujer de 54 años con 749 horas acreditadas sin años peligrosos 
    def testCase04(self):
        self.assertEqual(aplicaPensionIVSS('F',749,'1966-01-26',0), False)
        print("Case04: Approved")

    #Mujer de 50 años con 750 horas acreditadas con 25 años peligrosos 
    def testCase05(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1970-01-26',25), True)
        print("Case05: Approved")

    #Hombre de 59 años con 750 horas acreditadas sin años peligrosos 
    def testCase06(self):
        self.assertEqual(aplicaPensionIVSS('M',750,'1961-01-26',0), False)
        print("Case06: Approved")

    #Hombre de 59 años con 749 horas acreditadas sin años peligrosos 
    def testCase07(self):
        self.assertEqual(aplicaPensionIVSS('M',749,'1961-01-26',0), False)
        print("Case07: Approved")

    #Hombre de 55 años con 750 horas acreditadas con 25 años peligrosos 
    def testCase08(self):
        self.assertEqual(aplicaPensionIVSS('M',750,'1965-01-26',25), True)
        print("Case08: Approved")

    #Mujer de 55 años con 749 horas acreditadas sin años peligrosos 
    def testCase09(self):
        self.assertEqual(aplicaPensionIVSS('F',749,'1965-01-26',0), False)
        print("Case09: Approved")

    #Mujer de 55 años con 0 horas acreditadas sin años peligrosos 
    def testCase10(self):
        self.assertEqual(aplicaPensionIVSS('F',0,'1965-01-26',0), False)
        print("Case10: Approved")

    #Hombre de 60 años con 749 horas acreditadas sin años peligrosos 
    def testCase11(self):
        self.assertEqual(aplicaPensionIVSS('M',749,'1960-01-21',0), False)
        print("Case11: Approved")

    #Hombre de 60 años con 0 horas acreditadas sin años peligrosos 
    def testCase12(self):
        self.assertEqual(aplicaPensionIVSS('M',0,'1960-01-21',0), False)
        print("Case12: Approved")

    #Hombre de 60 años con horas negativas acreditadas sin años peligrosos 
    def testCase13(self):
        self.assertEqual(aplicaPensionIVSS('M',-1,'1960-01-21',0), False)
        print("Case13: Approved")

    #Mujer de 55 años con horas negativas acreditadas sin años peligrosos 
    def testCase14(self):
        self.assertEqual(aplicaPensionIVSS('F',-1,'1965-01-26',0), False)
        print("Case14: Approved")

    #Mujer de 55 años con 749 horas acreditadas con 25 años de peligro 
    def testCase15(self):
        self.assertEqual(aplicaPensionIVSS('F',749,'1965-01-26',25), False)
        print("Case15: Approved")

    #Mujer de 55 años con 0 horas acreditadas con 25 años de peligro 
    def testCase16(self):
        self.assertEqual(aplicaPensionIVSS('F',0,'1965-01-26',25), False)
        print("Case16: Approved")

    #Hombre de 60 años con 749 horas acreditadas con 25 años de peligro 
    def testCase17(self):
        self.assertEqual(aplicaPensionIVSS('M',749,'1960-01-21',25), False)
        print("Case17: Approved")

    #Hombre de 60 años con 0 horas acreditadas con 25 años de peligro 
    def testCase18(self):
        self.assertEqual(aplicaPensionIVSS('M',0,'1960-01-21',25), False)
        print("Case18: Approved")

    #Hombre de 60 años con horas negativas acreditadas con 25 años de peligro 
    def testCase19(self):
        self.assertEqual(aplicaPensionIVSS('M',-1,'1960-01-21',25), False)
        print("Case19: Approved")

    #Mujer de 55 años con horas negativas acreditadas con 25 años de peligro 
    def testCase20(self):
        self.assertEqual(aplicaPensionIVSS('F',-1,'1965-01-26',25), False)
        print("Case20: Approved")
    
    #Mujer de 55 años con 749 horas acreditadas con años negativo de peligro 
    def testCase21(self):
        self.assertEqual(aplicaPensionIVSS('F',749,'1965-01-26',-1), False)
        print("Case21: Approved")

    #Mujer de 55 años con 0 horas acreditadas con años negativo de peligro 
    def testCase22(self):
        self.assertEqual(aplicaPensionIVSS('F',0,'1965-01-26',-1), False)
        print("Case22: Approved")

    #Hombre de 60 años con 749 horas acreditadas con años negativo de peligro 
    def testCase23(self):
        self.assertEqual(aplicaPensionIVSS('M',749,'1960-01-21',-1), False)
        print("Case23: Approved")

    #Hombre de 60 años con 0 horas acreditadas con años negativo de peligro 
    def testCase24(self):
        self.assertEqual(aplicaPensionIVSS('M',0,'1960-01-21',-1), False)
        print("Case24: Approved")

    #Hombre de 60 años con horas negativas acreditadas con años negativo de peligro 
    def testCase25(self):
        self.assertEqual(aplicaPensionIVSS('M',-1,'1960-01-21',-1), False)
        print("Case25: Approved")

    #Mujer de 55 años con horas negativas acreditadas con años negativo de peligro 
    def testCase26(self):
        self.assertEqual(aplicaPensionIVSS('F',-1,'1965-01-26',-1), False)
        print("Case26: Approved")

    #Hombre de 55 años con 750 horas acreditadas con 25 años peligrosos con mal formato de fecha
    def testCase27(self):
        self.assertEqual(aplicaPensionIVSS('M',750,'26-01-1965',25), False)
        print("Case27: Approved")

if __name__ == '__main__':
    unittest.main(warnings='ignore')
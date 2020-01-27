import unittest
from rules import *

class pensionTester(unittest.TestCase):

    #Mujer de 55 años con 750 horas acreditas sin años peligrosos 
    def testCase1(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1965-01-26',0), True)
        print("Case1: Approved")

    #Hombre de 60 años con 750 horas acreditas sin años peligrosos 
    def testCase2(self):
        self.assertEqual(aplicaPensionIVSS('M',750,'1960-01-21',0), True)
        print("Case2: Approved")
    
    #Mujer de 54 años con 750 horas acreditas sin años peligrosos 
    def testCase3(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1966-01-26',0), False)
        print("Case3: Approved")

    #Mujer de 54 años con 749 horas acreditas sin años peligrosos 
    def testCase4(self):
        self.assertEqual(aplicaPensionIVSS('F',749,'1966-01-26',0), False)
        print("Case4: Approved")

    #Mujer de 50 años con 750 horas acreditas con 25 años peligrosos 
    def testCase5(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1970-01-26',25), True)
        print("Case5: Approved")


if __name__ == '__main__':
    unittest.main(warnings='ignore')
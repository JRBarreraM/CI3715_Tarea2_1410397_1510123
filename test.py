import unittest
from rules import *

class pensionTester(unittest.TestCase):

    #Mujer de 55 años con 750 horas acreditas sin años peligrosos 
    def testCase1(self):
        self.assertEqual(aplicaPensionIVSS('F',750,'1975-01-26',0), True)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
from ejercicio import addit
import unittest

class TestMax(unittest.TestCase):

    def testMax_success(self):
        resultado = max(1, 2)
        self.assertEqual(resultado, 2)
    
    def testMax_assertIsInstance(self):
        resultado = max(1, 2)
        self.assertIsInstance(resultado, int)
    
    def testMax_assertNotIsInstance(self):
        resultado = max(1, 2)
        self.assertNotIsInstance(resultado, str)


if __name__ == '__main__':
    unittest.main()
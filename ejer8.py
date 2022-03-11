from ejercicio import max
import unittest

class TestMax(unittest.TestCase):

    def testMax_success(self):
        resultado = max(4, 9)
        self.assertEqual(resultado, 9)
    
    def testMax_assertIsInstance(self):
        resultado = max(4, 9)
        self.assertIsInstance(resultado, int)
    
    def testMax_assertNotIsInstance(self):
        resultado = max(4, 9)
        self.assertNotIsInstance(resultado, str)


if __name__ == '__main__':
    unittest.main()
from ejercicio import mult
import unittest

class TestMult(unittest.TestCase):

    def testMult_success(self):
        resultado = mult(1)
        self.assertEqual(resultado, 6)
        

if __name__ == '__main__':
    unittest.main()
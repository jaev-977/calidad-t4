from ejercicio import divide
import unittest

class TestDivide(unittest.TestCase):

    def testDivide_success(self):
        resultado = divide(8, 2)
        self.assertEqual(resultado, 4)

    def testDivide_assertIs(self):
        resultado = divide(8, 2)
        self.assertIs(type(resultado), float)
        
if __name__ == '__main__':
	unittest.main()
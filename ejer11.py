from ejercicio import is_even
import unittest

class TestIsEven(unittest.TestCase):

    def testIsEven_success(self):
        resultado = is_even(2)
        self.assertEqual(resultado, True)

    def testIsEven_assertTrue(self):
        resultado = is_even(2)
        self.assertTrue(resultado)

    def testIsEven_assertFalse(self):
        resultado = is_even(3)
        self.assertFalse(resultado)
    

if __name__ == '__main__':
    unittest.main()
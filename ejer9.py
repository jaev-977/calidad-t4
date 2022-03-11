from ejercicio import addit
import unittest

class TestEvenNumbers(unittest.TestCase):

    def TestEvenNumbers_success(self):
        resultado = even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(resultado, [2, 4, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()
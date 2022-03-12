from ejercicio import odd_numbers
import unittest

class TestOddNumbers(unittest.TestCase):

    def testOddNumbers_success(self):
        resultado = odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(resultado, [1, 3, 5, 7, 9])

        
if __name__ == '__main__':
    unittest.main()

from ejercicio import length
import unittest

class TestLength(unittest.TestCase):

    def testLength_success(self):
        resultado = length([2, 3, 5, 2, 6, 7, 8, 9, 10])
        self.assertEqual(resultado, "Longer than 5")
        
if __name__ == '__main__':
	unittest.main()
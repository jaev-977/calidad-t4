from ejercicio import addit
import unittest

class TestReverse(unittest.TestCase):

    def testReverse_success(self):
        resultado = reverse("casa")
        self.assertEqual(resultado, "asac")
        
if __name__ == '__main__':
    unittest.main()
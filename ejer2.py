from ejercicio import addit
import unittest

class TestAgregar(unittest.TestCase):

	def test_1(self):
		resultado = addit(5)
		self.assertEqual(resultado, 10)


if __name__ == '__main__':
	unittest.main()
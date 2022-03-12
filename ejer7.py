from ejercicio import remove_letter
import unittest

class TestRemoveLetter(unittest.TestCase):

    def testRemoveLetter_success(self):
        resultado = remove_letter("o", "john")
        self.assertEqual(resultado, "jhn")
    
    def testRemoveLetter_assertIn(self):
        resultado = remove_letter("o", "john jo")
        message = "key is not in container."
        self.assertIn("jhn", resultado, message)
    
    def testRemoveLetter_assertNotIn(self):
        resultado = remove_letter("o", "john esteban")
        message = "key is not in container."
        self.assertNotIn("john", resultado, message)

if __name__ == '__main__':
    unittest.main()
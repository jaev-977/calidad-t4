from ejercicio import addit
import unittest

class TestRemoveLetter(unittest.TestCase):

    def testRemoveLetter_success(self):
        resultado = remove_letter("a", "ana maria")
        self.assertEqual(resultado, "n mri")
    
    def testRemoveLetter_assertIn(self):
        resultado = remove_letter("a", "ana maria")
        message = "key is not in container."
        self.assertIn("mri", resultado, message)
    
    def testRemoveLetter_assertNotIn(self):
        resultado = remove_letter("a", "ana maria")
        message = "key is not in container."
        self.assertNotIn("ana", resultado, message)

if __name__ == '__main__':
    unittest.main()
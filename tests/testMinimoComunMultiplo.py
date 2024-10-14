import unittest
from src.minimoComunMultiplo import minimoComunMultiplo

class MyTestCase(unittest.TestCase):
    def setUp(self):
        return None

    def tearDown(self):
        operaciones = None
    def test_minimoComunMultiplo_retornaResultado(self):
        operaciones = minimoComunMultiplo()
        # Arrange

        factor1 = 3
        factor2 = 4
        factor3 = 5
        resultadoEsperado = 60
        # Do
        resultadoActual =operaciones.operacion(factor1, factor2, factor3)
        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)  # add assertion here

if __name__ == '__main__':
    unittest.main()

import math
class minimoComunMultiplo:
    def operacion(self, factor1, factor2, factor3):
        # Función auxiliar para calcular el MCM de dos números
        def mcm(a, b):
            return abs(a * b) // math.gcd(a, b)

        # Calculamos el MCM de los tres números
        mcm_2 = mcm(factor1, factor2)
        return mcm(mcm_2, factor3)
import cmath

class ComplexCalculator:
    """
    A stateless calculator for performing operations on complex numbers.
    """
    
    @staticmethod
    def conjugate(z):
        return z.conjugate()

    @staticmethod
    def add(z1, z2):
        return z1 + z2

    @staticmethod
    def subtract(z1, z2):
        return z1 - z2

    @staticmethod
    def multiply(z1, z2):
        return z1 * z2

    @staticmethod
    def divide(z1, z2):
        if z2 == 0:
            raise ValueError("Cannot divide by zero.")
        return z1 / z2

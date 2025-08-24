import math

class NumeroComplejo:
    """
    Clase para representar y operar con números complejos.

    Permite realizar operaciones aritméticas básicas (suma, resta, multiplicación, división), obtener el módulo,
    el argumento, el conjugado, y convertir entre forma binómica, polar y exponencial.
    """
    
    def __init__(self, real, complejo):
        """
        Inicializa un número complejo con parte real y parte imaginaria.
        
        Args:
            real (float): Parte real del número complejo.
            complejo (float): Parte imaginaria del número complejo.
        """
        self.real = real
        self.complejo = complejo

    def __str__(self):
        """
        Retorna la representación en cadena del número complejo en forma binómica.
        
        Returns:
            str: Representación del número complejo.
        """
        if self.complejo >= 0:
            return f"{self.real} + {self.complejo}i"
        else:
            return f"{self.real} - {abs(self.complejo)}i"

    def __add__(self, otro):
        """
        Suma dos números complejos.
        
        Args:
            otro (NumeroComplejo): Otro número complejo a sumar.
        Returns:
            NumeroComplejo: Resultado de la suma.
        """
        if isinstance(otro, NumeroComplejo):
            return NumeroComplejo(self.real + otro.real, self.complejo + otro.complejo)
        else:
            return NotImplemented 
        
    def __sub__(self, otro):
        """
        Resta dos números complejos.
        
        Args:
            otro (NumeroComplejo): Otro número complejo a restar.
        Returns:
            NumeroComplejo: Resultado de la resta.
        """
        if isinstance(otro, NumeroComplejo):
            return NumeroComplejo(self.real - otro.real, self.complejo - otro.complejo)
        else:
            return NotImplemented
        
    def __mul__(self, otro):
        """
        Multiplica dos números complejos.
        
        Args:
            otro (NumeroComplejo): Otro número complejo a multiplicar.
        Returns:
            NumeroComplejo: Resultado de la multiplicación.
        """
        if isinstance(otro, NumeroComplejo):
            newReal = self.real*otro.real - self.complejo*otro.complejo
            newComplejo = self.real*otro.complejo + self.complejo*otro.real
            return NumeroComplejo(newReal, newComplejo)
        else:
            return NotImplemented
        
    def __truediv__(self, otro):
        """
        Divide dos números complejos.
        
        Args:
            otro (NumeroComplejo): Otro número complejo divisor.
        Returns:
            NumeroComplejo: Resultado de la división.
        """
        if isinstance(otro, NumeroComplejo):
            denomindor = otro.real**2 + otro.complejo**2
            parteReal = (self.real*otro.real + self.complejo*otro.complejo)/denomindor
            parteCompleja = (self.complejo*otro.real - self.real*otro.complejo)/denomindor
            return NumeroComplejo(parteReal, parteCompleja)
        else:
            return NotImplemented
    @property
    def modulo(self):
        """
        Calcula el módulo del número complejo.
        
        Returns:
            float: Módulo del número complejo.
        """
        return (self.real**2 + self.complejo**2)**0.5
    
    def conjugado(self):
        """
        Retorna el conjugado del número complejo.
        
        Returns:
            NumeroComplejo: Conjugado del número complejo.
        """
        return NumeroComplejo(self.real, self.complejo*-1) 
    
    def ComplejoaPolar(self):
        """
        Convierte el número complejo a su forma polar.
        
        Returns:
            tuple: (módulo, fase en radianes)
        """
        return self.modulo, math.atan2(self.complejo, self.real)
    
    @property
    def argumento(self):
        """
        Calcula el argumento (fase) del número complejo en radianes.
        
        Returns:
            float: Argumento en radianes.
        """
        return math.atan2(self.complejo, self.real)
    
    def mostrar_polar(self, grados = False):
        """
        Muestra la forma polar del número complejo.
        
        Args:
            grados (bool): Si es True, muestra el ángulo en grados; si es False, en radianes.
        Returns:
            str: Representación en forma polar.
        """
        if grados:
            angulo = math.degrees(self.argumento)
            return f"Módulo: {self.modulo:.2f}, ∠ {angulo:.2f}°"
        return f"Módulo: {self.modulo:.2f}, ∠ {self.argumento:.2f} rad"

    @classmethod
    def desde_polar(cls, modulo, angulo):
        """
        Crea un número complejo a partir de su forma polar.
        
        Args:
            modulo (float): Módulo del número complejo.
            angulo (float): Argumento en radianes.
        Returns:
            NumeroComplejo: Número complejo correspondiente.
        """
        real = modulo * math.cos(angulo)
        complejo = modulo * math.sin(angulo)
        return cls(real, complejo)
    
    def a_exponencial(self, grados=False):
        """
        Retorna la representación exponencial del número complejo en radianes.
        
        Returns:
            str: Representación exponencial.
        """
        ang = math.degrees(self.argumento) if grados else self.argumento
        suf = "°" if grados else ""
        return f"{self.modulo:.2f}·e^(i·{ang:.2f}{suf})"

    def a_exponencial_grados(self):
        """
        Retorna la representación exponencial del número complejo en grados.
        
        Returns:
            str: Representación exponencial en grados.
        """
        return self.a_exponencial(grados=True)

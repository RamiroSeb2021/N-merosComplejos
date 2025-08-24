import unittest
import math
from Libreria.NumeroComplejo import NumeroComplejo

class TestNumeroComplejo(unittest.TestCase):

    def test_constructor(self):
        c = NumeroComplejo(5, -2)
        self.assertEqual(c.real, 5)
        self.assertEqual(c.complejo, -2)
        self.assertTrue(isinstance(c, NumeroComplejo))

    def test_suma(self):
        c1 = NumeroComplejo(2, 3)
        c2 = NumeroComplejo(1, 4)
        resultado = c1 + c2
        self.assertEqual(resultado.real, 3)
        self.assertEqual(resultado.complejo, 7)

    def test_suma_notEqual(self):
        c1 = NumeroComplejo(2, 3)
        c2 = NumeroComplejo(1, 4)
        resultado = c1 + c2
        self.assertNotEqual(resultado.real, 5)
        self.assertNotEqual(resultado.complejo, 5)

    def test_resta(self):
        c1 = NumeroComplejo(5, 6)
        c2 = NumeroComplejo(2, 1)
        resultado = c1 - c2
        self.assertEqual(resultado.real, 3)
        self.assertEqual(resultado.complejo, 5)

    def test_resta_notEqual(self):
        c1 = NumeroComplejo(5, 6)
        c2 = NumeroComplejo(2, 1)
        resultado = c1 - c2
        self.assertNotEqual(resultado.real, 0)
        self.assertNotEqual(resultado.complejo, 0)

    def test_multiplicacion(self):
        c1 = NumeroComplejo(1, 2)
        c2 = NumeroComplejo(3, 4)
        resultado = c1 * c2
        self.assertEqual(resultado.real, -5)
        self.assertEqual(resultado.complejo, 10)

    def test_multiplicacion_notEqual(self):
        c1 = NumeroComplejo(1, 2)
        c2 = NumeroComplejo(3, 4)
        resultado = c1 * c2
        self.assertNotEqual(resultado.real, 0)
        self.assertNotEqual(resultado.complejo, 0)

    def test_division(self):
        c1 = NumeroComplejo(1, 2)
        c2 = NumeroComplejo(3, 4)
        resultado = c1 / c2
        self.assertAlmostEqual(resultado.real, 0.44, places=2)
        self.assertAlmostEqual(resultado.complejo, 0.08, places=2)

    def test_division_notEqual(self):
        c1 = NumeroComplejo(1, 2)
        c2 = NumeroComplejo(3, 4)
        resultado = c1 / c2
        self.assertNotAlmostEqual(resultado.real, 1.0, places=2)
        self.assertNotAlmostEqual(resultado.complejo, 1.0, places=2)

    def test_modulo(self):
        c = NumeroComplejo(3, 4)
        self.assertAlmostEqual(c.modulo, 5.0)

    def test_modulo_notEqual(self):
        c = NumeroComplejo(3, 4)
        self.assertNotAlmostEqual(c.modulo, 6.0, places=2)

    def test_conjugado(self):
        c = NumeroComplejo(2, -3)
        conj = c.conjugado()
        self.assertEqual(conj.real, 2)
        self.assertEqual(conj.complejo, 3)

    def test_conjugado_notEqual(self):
        c = NumeroComplejo(2, -3)
        conj = c.conjugado()
        self.assertNotEqual(conj.real, 0)
        self.assertNotEqual(conj.complejo, 0)

    def test_argumento(self):
        c = NumeroComplejo(1, math.sqrt(3))
        self.assertAlmostEqual(c.argumento, math.pi/3, places=2)

    def test_argumento_notEqual(self):
        c = NumeroComplejo(1, math.sqrt(3))
        self.assertNotAlmostEqual(c.argumento, 0, places=2)

    def test_mostrarPolar(self):
        c = NumeroComplejo(1, math.sqrt(3))
        esperado = f"Módulo: {c.modulo:.2f}, ∠ {c.argumento:.2f} rad"
        self.assertEqual(c.mostrar_polar(), esperado)

    def test_mostrarPolar_grados(self):
        c = NumeroComplejo(1, math.sqrt(3))
        angulo = math.degrees(c.argumento)
        esperado = f"Módulo: {c.modulo:.2f}, ∠ {angulo:.2f}°"
        self.assertEqual(c.mostrar_polar(grados=True), esperado)

    def test_mostrarPolar_notEqual(self):
        c = NumeroComplejo(1, 1)
        self.assertNotEqual(c.mostrar_polar(), "Módulo: 0.00, ∠ 0.00 rad")

    def test_desde_polar(self):
        modulo = 2
        angulo = math.pi/4
        c = NumeroComplejo.desde_polar(modulo, angulo)
        self.assertAlmostEqual(c.real, math.sqrt(2), places=2)
        self.assertAlmostEqual(c.complejo, math.sqrt(2), places=2)

    def test_desde_polar_notEqual(self):
        modulo = 2
        angulo = math.pi/4
        c = NumeroComplejo.desde_polar(modulo, angulo)
        self.assertNotAlmostEqual(c.real, 2.0, places=2)
        self.assertNotAlmostEqual(c.complejo, 0.0, places=2)

    def test_a_exponencial(self):
        c = NumeroComplejo(1, 1)
        esperado = f"{c.modulo:.2f}·e^(i·{c.argumento:.2f})"
        self.assertEqual(c.a_exponencial(), esperado)

    def test_a_exponencial_notEqual(self):
        c = NumeroComplejo(1, 1)
        self.assertNotEqual(c.a_exponencial(), "0.00·e^(i·0.00)")

    def test_a_exponencial_grados(self):
        c = NumeroComplejo(1, 1)
        angulo_grados = math.degrees(c.argumento)
        esperado = f"{c.modulo:.2f}·e^(i·{angulo_grados:.2f}°)"
        self.assertEqual(c.a_exponencial(grados=True), esperado)

    def test_a_exponencial_grados_notEqual(self):
        c = NumeroComplejo(1, 1)
        self.assertNotEqual(c.a_exponencial(grados=True), "0.00·e^(i·0.00°)")

if __name__ == "__main__":
    unittest.main()
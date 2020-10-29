from django.test import TestCase
from .validadores_chilenos import validar_rut

class TestValidadoresChilenos(TestCase):

    def test_rut_valido(self):
        rut = "12656568-2"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)
    
    def test_rut_no_valido(self):
        rut = "12656568-7"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)

    def test_rut_formato_erroneo(self):
        rut = "1265656-8-2"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)

    def test_texto_en_vez_de_rut(self):
        rut = "Estamos al aire!"
        resultado = validar_rut(rut)
        self.assertFalse(resultado)
    
    def test_rut_conK(self):
        rut = "19912756-K"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)

    def test_rut_conk(self):
        rut = "19912756-k"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)
    
    def test_rut_varios_ceros(self):
        rut = "20002288-2"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)
    
    def test_rut_con0(self):
        rut = "9705866-0"
        resultado = validar_rut(rut)
        self.assertTrue(resultado)
        




# Para crear un Test en django debo crear una clase que herede de TestCase.
class TestTonto(TestCase) :
    # aqui puedo colocar mis casos de prueba.
    def test_sumar(self):
        """
        Este es un test tonto, solo para probar que la suma funciona...
        y mostrar como funciona una prueba.
        """
        # datos de prueba
        a = 1
        b = 2
        # ejecución de la prueba 
        c = a + b
        # verificación del resultado.
        self.assertEqual(c, 3)

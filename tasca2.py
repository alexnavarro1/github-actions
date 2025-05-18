from prova_escrita3 import trobar_min_max_rendiment,comptar_estudiants,comptar_estudiants_materia,notes_estudiants
from prova_escrita4 import sumar_fila,sumar_matriu,cercar_el,m_ex,transformar
import unittest


        
class TestProvaEscrita03(unittest.TestCase):
    
    def test1(self):
        """
        Tests per la funció trobar_min_max_rendiment.
        """

        # Comprova un cas amb valors vàlids
        resultat = trobar_min_max_rendiment(10.50, 12.00, 15.00)
        self.assertEqual(resultat, (10.50, 15.00))

        # Comprova el cas en què no hi ha valors
        resultat = trobar_min_max_rendiment()
        self.assertEqual(resultat, (0, 0))
        
    def test2(self):             
        """
        Tests per la funció comptar_estudiants.
        """
        
        # Comprova el nombre total d'estudiants
        resultat = comptar_estudiants(notes_estudiants)
        self.assertEqual(resultat, 4)
    
    def test3(self):
        """
        Tests per la funció comptar_estudiants_materia.
        """
        
        # Comprova el nombre d'estudiants en una matèria específica
        resultat = comptar_estudiants_materia(notes_estudiants, "Matemàtiques")
        self.assertEqual(resultat, 3)

        # Comprova el cas en què cap estudiant està matriculat a una matèria
        resultat = comptar_estudiants_materia(notes_estudiants, "Filosofia")
        self.assertEqual(resultat, 0)

class TestProvaEscrita04(unittest.TestCase):
    
    def test4(self):
        """
        Tests per la funció cercar_el.
        """
        
        # Comprova que troba un element existent
        resultat = cercar_el(m_ex, 5, True)
        self.assertEqual(resultat, (True, (1, 1)))

        # Comprova el cas en que l'element no es troba
        resultat = cercar_el(m_ex, 10)
        self.assertEqual(resultat, (False, None))
        
    def test5(self):
        """
        Tests per la funció sumar_fila.
        """
        
        # Comprova que retorna la suma d'una fila valida
        resultat = sumar_fila(m_ex, 2)
        self.assertEqual(resultat, 24)

        # Comprova el cas en que l'index de la fila no és valid
        resultat = sumar_fila(m_ex, 10)
        self.assertEqual(resultat, None)
    
    def test6(self):
        """
        Tests per la funció sumar_matriu.
        """
        
        # Comprova que retorna la suma total dels elements de la matriu
        resultat = sumar_matriu(m_ex)
        self.assertEqual(resultat, 45)
        
    def test7(self):
        """
        Tests per a la funció transformar.
        """
        
        # Comprova que suma correctament una constant a tots els elements
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transformar(matriu, 10, "+")
        self.assertEqual(matriu, [[11, 12, 13], [14, 15, 16], [17, 18, 19]])

        # Comprova que no modifica la matriu amb una operació no vàlida
        matriu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        transformar(matriu, 10, "%")
        self.assertEqual(matriu, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
if __name__ == "__main__":
    unittest.main()
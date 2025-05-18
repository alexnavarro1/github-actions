from Prova_escrita_05 import *
import pytest

# Test per a la funció llibres_per_categoria
@pytest.mark.parametrize(
    "dades, categoria, resultat", # Parametres de la funció a analitzar més el parametre de resultat.
    [
        (biblioteca, "fantasia", ['El Senyor dels Anells']),  # Ha de retornar una llista amb el llibre de fantasia. Sortira (.)
        (biblioteca, "ciència-ficció", ['1984']),  # Ha de retornar una llista amb el llibre de ciència-ficció. Sortira (.)
    ]
)
def test_llibres_per_categoria(dades, categoria, resultat):
    """
    Funció per comprovar que la funció llibres_per_categoria retorna correctamentels llibres disponibles en una categoria específica.
    
    - Parametres:
        dades: Biblioteca de llibres.
        categoria: Categoria a buscar.
        resultat: Resultat esperat.
        
    """
    assert llibres_per_categoria(dades, categoria) == resultat # Comprovem si el resultat es el mateix que l'esperat

# Test per a la funció esta_disponible
@pytest.mark.parametrize(
    "dades, llibre, resultat", # Parametres de la funció a analitzar més el parametre de resultat.
    [
        (biblioteca, "El Senyor dels Anells", False),  # El llibre no està disponible. Sortira (.)
        (biblioteca, "Crim i Càstig", True),  # El llibre està disponible. Sortira (.)
    ]
)
def test_esta_disponible(dades, llibre, resultat):
    """
    Funció per comprovar si un llibre està disponible per al préstec.
    
    - Parametres:
        dades: Biblioteca de llibres.
        llibre: Llibre per saber si esta disponible.
        resultat: Resultat esperat.
    """
    assert esta_disponible(dades, llibre) == resultat # Comprovem si el resultat es el mateix que l'esperat

# Test per a la funció usuari_te_prestecs
@pytest.mark.parametrize(
    "dades, usuari, resultat",
    [
        (biblioteca, "Anna", False),  # L'usuari no té préstecs.
        (biblioteca, "Marta", True),  # L'usuari té préstecs.
    ]
)
def test_usuari_te_prestecs(dades, usuari, resultat):
    """
    Funció per comprovar si un usuari té préstecs actius.
    
    - Parametres:
        dades: Biblioteca de llibres.
        usuari: Usuari a buscar si te prestecs.
        resultat: Resultat esperat.
    """
    assert usuari_te_prestecs(dades, usuari) == resultat # Comprovem si el resultat es el mateix que l'esperat

# Test per a la funció dies_prestec_total
@pytest.mark.parametrize(
    "dades, llibre, resultat", # Parametres de la funció a analitzar més el parametre de resultat.
    [
        (biblioteca, "El Quixot", 47),  # Dies totals de prestec per a El Quixot. Sortira (.)
        (biblioteca, "1984", 53),  # Dies totals de prestec per a 1984. Sortira (.)
    ]
)
def test_dies_prestec_total(dades, llibre, resultat):
    """
    Funció per comprovar els dies totals de préstec d'un llibre.
    
    - Parametres:
        dades: Biblioteca de llibres.
        llibre: Llibre per buscar el total de dies dels prestecs.
        resultat: Resultat esperat.
    """
    assert dies_prestec_total(dades, llibre) == resultat # Comprovem si el resultat es el mateix que l'esperat
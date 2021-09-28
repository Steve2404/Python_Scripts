"""###Defini une foction avec les anotations
def add(a: int, b: int) -> int:
    return a + b
add("1", 24)
## python 3.9.1 -m pip install mypy #installation de la librairie mypy
"""
"""## Importe un module se trouvant dans un notre dossier
import sys
from pprint import pprint

pprint(sys.path) # Elle affiche la liste des tous les chemins ou python stocke ces modules et librairies
                 # ce qui nous interesse ici c est celui du PYTHONPATH qui vaut:
                 # C:\\Users\\Steve\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages
                 # c est donc la qu on cree nos modules pour les les faires importe dans le scripte
"""
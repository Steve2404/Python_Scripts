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
"""## Recharg des modules
import importlib # appel le module de recharge des modules

from Module import module_test
importlib.reload(module_test) # Permet de recharger le module
"""

### La gestion des logging
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename=r"Formation_Python\fonctions_Modules_Log\log_test.log",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')# on defini le niveau de log , tout ce qui vont etre affichees

logging.debug("La fonction aa bien ete executee")
logging.info("Message d information generale")
logging.warning("Attention!")
logging.error("Une erreur est arrivee")
logging.critical("Erreur crique")
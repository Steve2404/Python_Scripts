class SerieTele:
    def diffuser(self):
        print("desole je n'ai pas de Tele")

class EpisodeDrwho(SerieTele): #creation d'une classe heritant de classe SerieT
    """
    Un episode du Docteur Who '# documentation
    """
    def __init__(self, saison, episode): #constructeur
        self.saison  = saison
        self.episode = episode
        
    def attaque_delek(self): # definition d'une methode dans la classe
     print("au secour! Attaque de Dalek dans l'episode",self.saison,self.episode)


ep = EpisodeDrwho(7,5) #creation d'un objet de type EpisodeDrwho
#ep.saison  = 7      #initialisation des attributs
#ep.episode = 5
#print(ep.saison)
ep.attaque_delek()
ep.diffuser()

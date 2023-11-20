import random
import time


class Pokemon:
    def __init__(self):
        self.nom = "Son blaze"
        self.vie = int("Vie") #entre 78 et 150
        self.dfs = int("Attaque") #entre 5 et 20
        self.type = "son type (pour savoir si il fait degat *2)" #10 type : Electrique, Feu, Glace, Eau, Terre, Gadou, Plante, Ombre, caca, radiateur
        self.atq = {} #entre 2 et 4
        
Pigrochou = Pokemon()
Pigrochou.nom = "Prigrochou"
Pigrochou.vie = "100"
Pigrochou.dfs = "5"
Pigrochou.type = "Electrique"
Pigrochou.atq = {"Coup de foudre" : int("20"), "Coup de queue" : int("10")}

Dracoco = Pokemon()
Dracoco.nom = Dracoco
Dracoco.vie = "100"
Dracoco.dfs = "10"
Dracoco.type = "Feu"
Dracoco.atq = {"Magma" : int("50"), "Rafale Feu" : int("10")}

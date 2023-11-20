import random as rd

class Pokemon:
    def __init__(self):
        self.nom = "Son blaze"
        self.vie = "Vie" #entre 78 et 150
        self.dfs = "Attaque" #entre 5 et 20
        self.type = "son type (pour savoir si il fait degat *2)" #10 type : Electrique, Feu, Glace, Eau, Terre, Gadou, Plante, Ombre, acier, radiateur
        self.atq = {} #entre 2 et 4
        
liste_tt_pokemon = []
#Pokemon num 1
Pigrochou = Pokemon()
Pigrochou.nom = "Pigrochou"
Pigrochou.vie = int(100)
Pigrochou.dfs = int(5)
Pigrochou.type = "Electrique"
Pigrochou.atq = {"Coup de foudre" : int("20"), "Coup de queue" : int("10")}
liste_tt_pokemon.append(Pigrochou)
#Pokemon num 2
dracoco = Pokemon()
dracoco.nom = "dracoco"
dracoco.vie = int(150)
dracoco.dfs = int(20)
dracoco.type = "feu"
dracoco.atq = {"Lance flamme" : int("20"), "boule de feu" : int("25")}
liste_tt_pokemon.append(dracoco)
#Pokemon num 3
ciseau = Pokemon()
ciseau.nom = "ciseau"
ciseau.vie = int(78)
ciseau.dfs = int(10)
ciseau.type = "acier"
ciseau.atq = {"tranchant" : int("15"), "ca coupe..." : int("20")}
liste_tt_pokemon.append(ciseau)

def choix_random(liste_tt_pokemon):
    equipe_1 = []
    choix = rd.randint(0,(len(liste_tt_pokemon)-1))
    equipe_1.append(liste_tt_pokemon[choix])
    print(equipe_1[0].nom, equipe_1[0].vie, equipe_1[0].dfs, equipe_1[0].type, equipe_1[0].atq)
    print(type(equipe_1))

choix_random(liste_tt_pokemon)

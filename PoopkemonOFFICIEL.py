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
    equipe_2 = []
    for i in range(2):
        choix = rd.randint(0,(len(liste_tt_pokemon)-1))
        equipe_1.append(liste_tt_pokemon[choix])
        choix = rd.randint(0,(len(liste_tt_pokemon)-1))
        equipe_2.append(liste_tt_pokemon[choix])
    return equipe_1, equipe_2
choix_random(liste_tt_pokemon)
equipe_1, equipe_2 = choix_random(liste_tt_pokemon)
#toutes les données pour l'équipe 1
equipe_1_P1_vie, equipe_1_P2_vie = equipe_1[0].vie, equipe_1[1].vie
equipe_1_P1_dfs, equipe_1_P2_dfs = equipe_1[0].dfs, equipe_1[1].dfs
equipe_1_P1_type, equipe_1_P2_type = equipe_1[0].type, equipe_1[1].type
equipe_1_P1_atq, equipe_1_P2_atq = equipe_1[0].atq, equipe_1[1].atq
#toutes les données pour l'équipe 2
equipe_2_P1_vie, equipe_2_P2_vie = equipe_2[0].vie, equipe_2[1].vie
equipe_2_P1_dfs, equipe_2_P2_dfs = equipe_2[0].dfs, equipe_2[1].dfs
equipe_2_P1_type, equipe_2_P2_type = equipe_2[0].type, equipe_2[1].type
equipe_2_P1_atq, equipe_2_P2_atq = equipe_2[0].atq, equipe_2[1].atq

def commencer_en_premier():
    commence = rd.randint(1,2)
    if commence == 1:
        print("Le joueur 1 commence")
    else:
        print("Le joueur 2 commence") 
         

#pour les prénoms de pokemon :

#sarbouboule
#arkekes
#Poussière
#Tauros de mamamia
#Sologopitch
#Bulbasaur => Redbull
#Charmander => charmandercharmant
#Squirtle => NeSquic
#Jigglypuff => Jiclepue
#Snorlax => Sorsdurelax
#Gyarados => Gytan
#Evoli => Cacali
#

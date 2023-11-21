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

Torpingpong = Pokemon()
Torpingpong.nom = Torpingpong
Torpingpong.vie = int("140")
Torpingpong.dfs = int("15")
Torpingpong.type = "Eau"
Torpingpong.atq = {"Pistolet à eau " : int("15"), "Hydrocanon" : int("12")}

Zegrouille = Pokemon()
Zegrouille.nom = Zegrouille
Zegrouille.vie = int("100")
Zegrouille.dfs = int("10")
Zegrouille.type = "Radiateur"
Zegrouille.atq = {" Rayon Chargé" : int("20"), "Éclair Fou" : int("14")}

Terramen = Pokemon()
Terramen.nom = Terramen
Terramen.vie = int("100")
Terramen.dfs = int("25")
Terramen.type = "Terre"
Terramen.atq = {" Ecra-Terre" : int("15"), " Tremblement de ramen" : int("25")}

sarbouboule = Pokemon()
sarbouboule.nom =sarbouboule
sarbouboule.vie = int("100")
sarbouboule.dfs = int("25")
sarbouboule.type = "Glace"
sarbouboule.atq = {" Attaque glaçon" : int("15"), " freezer" : int("25")}


arkekes = Pokemon()
arkekes.nom = arkekes
arkekes.vie = int("100")
arkekes.dfs = int("24")
arkekes.type = "Ombre"
arkekes.atq = {"Noir-sombre" : int("15"), " blindness" : int("25")}


Gagabou = Pokemon()
Gagabou.nom = Gagabou
Gagabou.vie = int("90")
Gagabou.dfs = int("19")
Gagabou.type = "Gadou"
Gagabou.atq = {"Lame Feuille" : int("15"), "Colère Gaga" : int("25")}


Taumamamia = Pokemon()
Taumamamia.nom = Taumamamia
Taumamamia.vie = int("100")
Taumamamia.dfs = int("20")
Taumamamia.type = "Feu"
Taumamamia.atq = {"Centrifugifle" : int("15"), "Coup de corne extrême" : int("25")}


Sologopitch = Pokemon()
Sologopitch.nom = Sologopitch
Sologopitch.vie = int("100")
Sologopitch.dfs = int("10")
Sologopitch.type = "caca"
Sologopitch.atq =  {"Vibrocaca" : int("15"), "Tacle lourd diarrhée " : int("25")}


Bulbaredbull = Pokemon ()
Bulbaredbull.nom = Bulbaredbull
Bulbaredbull.vie = int("100")
Bulbaredbull.dfs = int("8")
Bulbaredbull.type = "Eau"
Bulbaredbull.atq = {"donne des ailes" : int("15"), "plume endormissant" : int("25")}


charmandercharmant = Pokemon()
charmandercharmant.nom = charmandercharmant
charmandercharmant.vie = int("110")
charmandercharmant.dfs = int("16")
charmandercharmant.type = "caca"
charmandercharmant.atq ={"la grâce suspecte" : int("15"), "lumière 100%" : int("25")}


NeSquictle = Pokemon ()
charmandercharmant.nom = 
charmandercharmant.vie = int("99")
charmandercharmant.dfs = int("19")
charmandercharmant.type = "Terre"
charmandercharmant.atq = {"Lumière charmantisme" : int("15"), "charismatique" : int("25")}

JicleJacqueline = Pokemon ()
JicleJacqueline.nom = JicleJacqueline
JicleJacqueline.vie = int("100")
JicleJacqueline.dfs = int("19")
JicleJacqueline.type = "Plante"
JicleJacqueline.atq = {"Gifle ortie" : int("15"), "Lance-Soleil" : int("25")}

Sorsdurelax =Pokemon ()
Sorsdurelax.nom = Sorsdurelax
Sorsdurelax.vie = int("100")
Sorsdurelax.dfs = int("13")
Sorsdurelax.type = "radiateur"
Sorsdurelax.atq = {"nahass" : int("15"), "bulle piquante" : int("25")}

Gytan = Pokemon()
Gytan.nom = Gytan
Gytan.vie = int("150")
Gytan.dfs = int("20")
Gytan.type = "Feu et Electrique"
Gytan.atq = {"fusion power" : int("15"), "All power" : int("25")}


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

def start():
    commence = rd.randint(1,2)
    if commence == 1:
        print("Le joueur 1 commence")
        return 1
    else:
        print("Le joueur 2 commence") 
        return 2

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

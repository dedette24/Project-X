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
#4
Torpingpong = Pokemon()
Torpingpong.nom = "Torpingpong"
Torpingpong.vie = int("140")
Torpingpong.dfs = int("15")
Torpingpong.type = "Eau"
Torpingpong.atq = {"Pistolet à eau " : int("15"), "Hydrocanon" : int("12")}
liste_tt_pokemon.append(Torpingpong)
#5
Zegrouille = Pokemon()
Zegrouille.nom = "Zegrouille"
Zegrouille.vie = int("100")
Zegrouille.dfs = int("10")
Zegrouille.type = "Radiateur"
Zegrouille.atq = {" Rayon Chargé" : int("20"), "Éclair Fou" : int("14")}
liste_tt_pokemon.append(Zegrouille)

Terramen = Pokemon()
Terramen.nom = "Terramen"
Terramen.vie = int("100")
Terramen.dfs = int("25")
Terramen.type = "Terre"
Terramen.atq = {" Ecra-Terre" : int("15"), " Tremblement de ramen" : int("25")}
liste_tt_pokemon.append(Terramen)
#6
sarbouboule = Pokemon()
sarbouboule.nom = "sarbouboule"
sarbouboule.vie = int("100")
sarbouboule.dfs = int("25")
sarbouboule.type = "Glace"
sarbouboule.atq = {" Attaque glaçon" : int("15"), " freezer" : int("25")}
liste_tt_pokemon.append(sarbouboule)
#7
arkekes = Pokemon()
arkekes.nom = "arkekes"
arkekes.vie = int("100")
arkekes.dfs = int("24")
arkekes.type = "Ombre"
arkekes.atq = {"Noir-sombre" : int("15"), " blindness" : int("25")}
liste_tt_pokemon.append(arkekes)
#8
Gagabou = Pokemon()
Gagabou.nom = "Gagabou"
Gagabou.vie = int("90")
Gagabou.dfs = int("19")
Gagabou.type = "Gadou"
Gagabou.atq = {"Lame Feuille" : int("15"), "Colère Gaga" : int("25")}
liste_tt_pokemon.append(Gagabou)
#9
Taumamamia = Pokemon()
Taumamamia.nom = "Taumamamia"
Taumamamia.vie = int("100")
Taumamamia.dfs = int("20")
Taumamamia.type = "Feu"
Taumamamia.atq = {"Centrifugifle" : int("15"), "Coup de corne extrême" : int("25")}
liste_tt_pokemon.append(Taumamamia)
#10
Sologopitch = Pokemon()
Sologopitch.nom = "Sologopitch"
Sologopitch.vie = int("100")
Sologopitch.dfs = int("10")
Sologopitch.type = "caca"
Sologopitch.atq =  {"Vibrocaca" : int("15"), "Tacle lourd diarrhée " : int("25")}
liste_tt_pokemon.append(Sologopitch)
#11
Bulbaredbull = Pokemon ()
Bulbaredbull.nom = "Bulbaredbull"
Bulbaredbull.vie = int("100")
Bulbaredbull.dfs = int("8")
Bulbaredbull.type = "Eau"
Bulbaredbull.atq = {"donne des ailes" : int("15"), "plume endormissant" : int("25")}
liste_tt_pokemon.append(Bulbaredbull)
#12
charmandercharmant = Pokemon()
charmandercharmant.nom = "charmandercharmant"
charmandercharmant.vie = int("110")
charmandercharmant.dfs = int("16")
charmandercharmant.type = "caca"
charmandercharmant.atq ={"la grâce suspecte" : int("15"), "lumière 100%" : int("25")}
liste_tt_pokemon.append(charmandercharmant)
#13
NeSquictle = Pokemon ()
NeSquictle.nom = "NeSquictle"
NeSquictle.vie = int("99")
NeSquictle.dfs = int("19")
NeSquictle.type = "Terre"
NeSquictle.atq = {"Lumière charmantisme" : int("15"), "charismatique" : int("25")}
liste_tt_pokemon.append(NeSquictle)
#14
JicleJacqueline = Pokemon ()
JicleJacqueline.nom = "JicleJacqueline"
JicleJacqueline.vie = int("100")
JicleJacqueline.dfs = int("19")
JicleJacqueline.type = "Plante"
JicleJacqueline.atq = {"Gifle ortie" : int("15"), "Lance-Soleil" : int("25")}
liste_tt_pokemon.append(JicleJacqueline)
#15
Sorsdurelax =Pokemon ()
Sorsdurelax.nom = "Sorsdurelax"
Sorsdurelax.vie = int("100")
Sorsdurelax.dfs = int("13")
Sorsdurelax.type = "radiateur"
Sorsdurelax.atq = {"nahass" : int("15"), "bulle piquante" : int("25")}
liste_tt_pokemon.append(Sorsdurelax)
#16
Gytan = Pokemon()
Gytan.nom = "Gytan"
Gytan.vie = int("150")
Gytan.dfs = int("20")
Gytan.type = "Electrique"
Gytan.atq = {"fusion power" : int("15"), "la pelle" : int("25")}
liste_tt_pokemon.append(Gytan)
#17
Dedette = Pokemon()
Dedette.nom = "Dedette"
Dedette.vie = int("123")
Dedette.dfs = int("20")
Dedette.type = "eau"
Dedette.atq = {"Lance d'eau" : int("10"), "hydroblast" : int("25")}
liste_tt_pokemon.append(Dedette)
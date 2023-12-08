import random
class Pokemon:
    def __init__(self):
        self.nom = "Son blaze"
        self.vie = "Vie" #entre 78 et 150
        self.dfs = "Attaque" #entre 5 et 20
        self.type = "son type (pour savoir si il fait degat *2)" #10 type : Feu, Glace, Eau, Gadou, Fee, Plante, Ombre, Acier, Ombre, Caca
        self.vitesse = "sa rapiditer" #entre 1 et 20
        
class Attaque:
    def __init__(self):
        self.name = "nom de l'attaque"
        self.power = "degat"
        self.type = "le type de l'attaque"
        self.pp = "nbr d'utilisation"
        
attaques = []

Boule_de_feu = Attaque()
Boule_de_feu.name = "Boule_de_feu"
Boule_de_feu.power = int(20)
Boule_de_feu.type= "Feu"
Boule_de_feu.pp = int(5)
attaques.append(Boule_de_feu)

Coup_de_foudre = Attaque()
Coup_de_foudre.name = "Coup_de_foudre"
Coup_de_foudre.power = int(25)
Coup_de_foudre.type = "Electrique"
Coup_de_foudre.pp = int(8)
attaques.append(Coup_de_foudre)

Lance_flamme = Attaque()
Lance_flamme.name = "Lance_flamme"
Lance_flamme.power=18
Lance_flamme.type = "Feu" 
Lance_flamme.pp=10
attaques.append(Lance_flamme)

Eclair_sacré = Attaque()
Eclair_sacré.name = "Eclair_sacré"
Eclair_sacré.power=22
Eclair_sacré.type="Electrique"
Eclair_sacré.pp=7
attaques.append(Eclair_sacré)

Vague_gelée = Attaque()
Vague_gelée.name = "Vague_gelée"
Vague_gelée.power=15
Vague_gelée.type="Glace"
Vague_gelée.pp=12
attaques.append(Vague_gelée)

# Tempête_de_feu
Tempête_de_feu = Attaque()
Tempête_de_feu.name = "Tempête_de_feu"
Tempête_de_feu.power = 30
Tempête_de_feu.type = "Feu"
Tempête_de_feu.pp = 5
attaques.append(Tempête_de_feu)

# Raz_de_marée
Raz_de_marée = Attaque()
Raz_de_marée.name = "Raz_de_marée"
Raz_de_marée.power = 18
Raz_de_marée.type = "Eau"
Raz_de_marée.pp = 8
attaques.append(Raz_de_marée)

# Fouet_de_plantes
Fouet_de_plantes = Attaque()
Fouet_de_plantes.name = "Fouet_de_plantes"
Fouet_de_plantes.power = 12
Fouet_de_plantes.type = "Plante"
Fouet_de_plantes.pp = 15
attaques.append(Fouet_de_plantes)

# Tornade_de_fer
Tornade_de_fer = Attaque()
Tornade_de_fer.name = "Tornade_de_fer"
Tornade_de_fer.power = 28
Tornade_de_fer.type = "Acier"
Tornade_de_fer.pp = 6
attaques.append(Tornade_de_fer)

# Griffe_acier
Griffe_acier = Attaque()
Griffe_acier.name = "Griffe_acier"
Griffe_acier.power = 23
Griffe_acier.type = "Acier"
Griffe_acier.pp = 9
attaques.append(Griffe_acier)

# Ombre_nocturne
Ombre_nocturne = Attaque()
Ombre_nocturne.name = "Ombre_nocturne"
Ombre_nocturne.power = 17
Ombre_nocturne.type = "Ombre"
Ombre_nocturne.pp = 11
attaques.append(Ombre_nocturne)

# Rocaille
Rocaille = Attaque()
Rocaille.name = "Rocaille"
Rocaille.power = 25
Rocaille.type = "Terre"
Rocaille.pp = 7
attaques.append(Rocaille)

# Éruption_radiante
Éruption_radiante = Attaque()
Éruption_radiante.name = "Éruption_radiante"
Éruption_radiante.power = 30
Éruption_radiante.type = "Ombre"
Éruption_radiante.pp = 5
attaques.append(Éruption_radiante)

# Glace_éternelle
Glace_éternelle = Attaque()
Glace_éternelle.name = "Glace_éternelle"
Glace_éternelle.power = 25
Glace_éternelle.type = "Glace"
Glace_éternelle.pp = 8
attaques.append(Glace_éternelle)

# Torrent_d_éclairs
Torrent_d_éclairs = Attaque()
Torrent_d_éclairs.name = "Torrent_d_éclairs"
Torrent_d_éclairs.power = 28
Torrent_d_éclairs.type = "Electrique"
Torrent_d_éclairs.pp = 6
attaques.append(Torrent_d_éclairs)

# Danse_de_l_ombre
Danse_de_l_ombre = Attaque()
Danse_de_l_ombre.name = "Danse_de_l_ombre"
Danse_de_l_ombre.power = 17
Danse_de_l_ombre.type = "Ombre"
Danse_de_l_ombre.pp = 11
attaques.append(Danse_de_l_ombre)

# Séisme
Séisme = Attaque()
Séisme.name = "Séisme"
Séisme.power = 32
Séisme.type = "Terre"
Séisme.pp = 4
attaques.append(Séisme)

# Végétation_explosive
Végétation_explosive = Attaque()
Végétation_explosive.name = "Végétation_explosive"
Végétation_explosive.power = 20
Végétation_explosive.type = "Plante"
Végétation_explosive.pp = 7
attaques.append(Végétation_explosive)

# Chaleur_ardente
Chaleur_ardente = Attaque()
Chaleur_ardente.name = "Chaleur_ardente"
Chaleur_ardente.power = 26
Chaleur_ardente.type = "Feu"
Chaleur_ardente.pp = 9
attaques.append(Chaleur_ardente)

# Éclats_d_acier
Éclats_d_acier = Attaque()
Éclats_d_acier.name = "Éclats_d_acier"
Éclats_d_acier.power = 22
Éclats_d_acier.type = "Acier"
Éclats_d_acier.pp = 10
attaques.append(Éclats_d_acier)

# Rafale_aquatique
Rafale_aquatique = Attaque()
Rafale_aquatique.name = "Rafale_aquatique"
Rafale_aquatique.power = 18
Rafale_aquatique.type = "Eau"
Rafale_aquatique.pp = 12
attaques.append(Rafale_aquatique)

# Lueur_mystique
Lueur_mystique = Attaque()
Lueur_mystique.name = "Lueur_mystique"
Lueur_mystique.power = 23
Lueur_mystique.type = "Fee"
Lueur_mystique.pp = 8
attaques.append(Lueur_mystique)

# Souffle_gelé
Souffle_gelé = Attaque()
Souffle_gelé.name = "Souffle_gelé"
Souffle_gelé.power = 18
Souffle_gelé.type = "Glace"
Souffle_gelé.pp = 10
attaques.append(Souffle_gelé)

# Éclair_céleste
Éclair_céleste = Attaque()
Éclair_céleste.name = "Éclair_céleste"
Éclair_céleste.power = 30
Éclair_céleste.type = "Electrique"
Éclair_céleste.pp = 5
attaques.append(Éclair_céleste)

# Fleur_solaire
Fleur_solaire = Attaque()
Fleur_solaire.name = "Fleur_solaire"
Fleur_solaire.power = 22
Fleur_solaire.type = "Plante"
Fleur_solaire.pp = 8
attaques.append(Fleur_solaire)

# Déflagration
Déflagration = Attaque()
Déflagration.name = "Déflagration"
Déflagration.power = 25
Déflagration.type = "Feu"
Déflagration.pp = 7
attaques.append(Déflagration)

# Lame_acérée
Lame_acérée = Attaque()
Lame_acérée.name = "Lame_acérée"
Lame_acérée.power = 28
Lame_acérée.type = "Acier"
Lame_acérée.pp = 6
attaques.append(Lame_acérée)

# Cascade
Cascade = Attaque()
Cascade.name = "Cascade"
Cascade.power = 20
Cascade.type = "Eau"
Cascade.pp = 9
attaques.append(Cascade)

# Ténèbres_profondes
Ténèbres_profondes = Attaque()
Ténèbres_profondes.name = "Ténèbres_profondes"
Ténèbres_profondes.power = 16
Ténèbres_profondes.type = "Ombre"
Ténèbres_profondes.pp = 13
attaques.append(Ténèbres_profondes)

# Sacre
Sacre = Attaque()
Sacre.name = "Sacre"
Sacre.power = 26
Sacre.type = "Fee"
Sacre.pp = 7
attaques.append(Sacre)

# Étreinte_mystique
Étreinte_mystique = Attaque()
Étreinte_mystique.name = "Étreinte_mystique"
Étreinte_mystique.power = 21
Étreinte_mystique.type = "Fee"
Étreinte_mystique.pp = 9
attaques.append(Étreinte_mystique)

# Ruée_tellurique
Ruée_tellurique = Attaque()
Ruée_tellurique.name = "Ruée_tellurique"
Ruée_tellurique.power = 32
Ruée_tellurique.type = "Terre"
Ruée_tellurique.pp = 4
attaques.append(Ruée_tellurique)
    
#separer les attaques par types :
types_dict = {}
for attaque in attaques:
    type_ = attaque.type
    if type_ not in types_dict:
        types_dict[type_] = [attaque]
    else:
        types_dict[type_].append(attaque)

# on print les attaques pour chaques type :
"""for type_, attaque_list in types_dict.items():
    print(f"\nType: {type_}") #le \n ajoute juste un espace entre chaque truc (c'est plus beau)
    for attaque in attaque_list:
        print(f"Nom: {attaque.name}, Power: {attaque.power}, PP: {attaque.pp}")"""
        
        
liste_tt_pokemon = []
#Pokemon num 1
Pigrochou = Pokemon()
Pigrochou.nom = "Pigrochou"
Pigrochou.vie = int(100)
Pigrochou.dfs = int(5)
Pigrochou.type = "Electrique"
Pigrochou.vitesse = int("10")
liste_tt_pokemon.append(Pigrochou)
#Pokemon num 2
dracoco = Pokemon()
dracoco.nom = "dracoco"
dracoco.vie = int(150)
dracoco.dfs = int(20)
dracoco.type = "Feu"
dracoco.vitesse = int("5")
liste_tt_pokemon.append(dracoco)
#Pokemon num 3
ciseau = Pokemon()
ciseau.nom = "ciseau"
ciseau.vie = int(78)
ciseau.dfs = int(10)
ciseau.type = "Acier"
ciseau.vitesse = int("15")
liste_tt_pokemon.append(ciseau)
#4
Torpingpong = Pokemon()
Torpingpong.nom = "Torpingpong"
Torpingpong.vie = int("140")
Torpingpong.dfs = int("15")
Torpingpong.type = "Eau"
Torpingpong.vitesse = int("10")
liste_tt_pokemon.append(Torpingpong)
#5
Zegrouille = Pokemon()
Zegrouille.nom = "Zegrouille"
Zegrouille.vie = int("100")
Zegrouille.dfs = int("10")
Zegrouille.type = "Ombre"
Zegrouille.vitesse = int("11")
liste_tt_pokemon.append(Zegrouille)

Terramen = Pokemon()
Terramen.nom = "Terramen"
Terramen.vie = int("100")
Terramen.dfs = int("25")
Terramen.type = "Terre"
Terramen.vitesse = int("10")
liste_tt_pokemon.append(Terramen)
#6
sarbouboule = Pokemon()
sarbouboule.nom = "sarbouboule"
sarbouboule.vie = int("100")
sarbouboule.dfs = int("25")
sarbouboule.type = "Glace"
sarbouboule.vitesse = int("10")
liste_tt_pokemon.append(sarbouboule)
#7
arkekes = Pokemon()
arkekes.nom = "arkekes"
arkekes.vie = int("100")
arkekes.dfs = int("24")
arkekes.type = "Ombre"
arkekes.vitesse = int("10")
liste_tt_pokemon.append(arkekes)
#8
Gagabou = Pokemon()
Gagabou.nom = "Gagabou"
Gagabou.vie = int("90")
Gagabou.dfs = int("19")
Gagabou.type = "Fee"
Gagabou.vitesse = int("10")
liste_tt_pokemon.append(Gagabou)
#9
Taumamamia = Pokemon()
Taumamamia.nom = "Taumamamia"
Taumamamia.vie = int("100")
Taumamamia.dfs = int("20")
Taumamamia.type = "Feu"
Taumamamia.vitesse = int("10")
liste_tt_pokemon.append(Taumamamia)
#10
Sologopitch = Pokemon()
Sologopitch.nom = "Sologopitch"
Sologopitch.vie = int("100")
Sologopitch.dfs = int("10")
Sologopitch.type = "Acier"
Sologopitch.vitesse = int("10")
liste_tt_pokemon.append(Sologopitch)
#11
Bulbaredbull = Pokemon ()
Bulbaredbull.nom = "Bulbaredbull"
Bulbaredbull.vie = int("100")
Bulbaredbull.dfs = int("8")
Bulbaredbull.type = "Eau"
Bulbaredbull.vitesse = int("10")
liste_tt_pokemon.append(Bulbaredbull)
#12
charmandercharmant = Pokemon()
charmandercharmant.nom = "charmandercharmant"
charmandercharmant.vie = int("110")
charmandercharmant.dfs = int("16")
charmandercharmant.type = "Fee"
charmandercharmant.vitesse = int("10")
liste_tt_pokemon.append(charmandercharmant)
#13
NeSquictle = Pokemon ()
NeSquictle.nom = "NeSquictle"
NeSquictle.vie = int("99")
NeSquictle.dfs = int("19")
NeSquictle.type = "Terre"
NeSquictle.vitesse = int("10")
liste_tt_pokemon.append(NeSquictle)
#14
JicleJacqueline = Pokemon ()
JicleJacqueline.nom = "JicleJacqueline"
JicleJacqueline.vie = int("100")
JicleJacqueline.dfs = int("19")
JicleJacqueline.type = "Plante"
JicleJacqueline.vitesse = int("10")
liste_tt_pokemon.append(JicleJacqueline)
#15
Sorsdurelax =Pokemon ()
Sorsdurelax.nom = "Sorsdurelax"
Sorsdurelax.vie = int("100")
Sorsdurelax.dfs = int("13")
Sorsdurelax.type = "Ombre"
Sorsdurelax.vitesse = int("10")
liste_tt_pokemon.append(Sorsdurelax)
#16
Gytan = Pokemon()
Gytan.nom = "Gytan"
Gytan.vie = int("150")
Gytan.dfs = int("20")
Gytan.type = "Electrique"
Gytan.vitesse = int("10")
liste_tt_pokemon.append(Gytan)
#17
Dedette = Pokemon()
Dedette.nom = "Dedette"
Dedette.vie = int("123")
Dedette.dfs = int("20")
Dedette.type = "Eau"
Dedette.vitesse = int("10")
liste_tt_pokemon.append(Dedette)

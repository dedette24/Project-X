import random
class Pokemon:
    def __init__(self, name, vie, dfs, type, vts):
        self.name =  name #"Son blaze"
        self.vie = vie #"Vie" #entre 78 et 150
        self.dfs = dfs #"Attaque" #entre 5 et 20
        self.type = type #"son type (pour savoir si il fait degat *2)" #10 type : feu, Glace, Eau, Fee, Plante, Ombre, Acier, Caca, electrique, 
        self.vitesse = vts #"sa rapiditer" #entre 1 et 20

pokemon_names = [
    "Flarion", "Aquaphox", "Voltalon", "Terradra", "Pyrospire",
    "Zephyreon", "Dracoline", "Glacara", "Sylverix", "Magmawisp",
    "Leafblade", "Frostbite", "Thunderaegis", "Rockquake", "Psychwing",
    "Spectrosa", "Emberflare", "Aquaquill", "Galestorm", "Terrafin",
    "Flufflare", "Voltorbolt", "Earthquakeon", "Pyroclaw", "Zephyraptor",
    "Dracofire", "Glacius", "Sylvanight", "Magmaraider", "Leafshadow",
    "Frostnova", "Tidaltide", "Blitzspark", "Boulderback", "Mindflare",
    "Shadowstalker", "Flareonix", "Wavewarden", "Boltstrike", "Mossquake",
    "Infernia", "Aerowing", "Blizzardragon", "Lavalanche", "Leafwhisper",
    "Thunderclaw", "Wavecrest", "Quakestone", "Vortexblade", "Solarflare",
    "Lunarshroud", "Mysticbreeze", "Searage", "Frostfang", "Stormsurge",
    "Abyssalbite", "Ironhide", "Mysticshade", "Radiantbeam", "Dreadhowl",
    "Venomfang", "Magmaflare", "Cinderstorm", "Glacialchill", "Leafsong",
    "Zapstrike", "Aerofrost", "Aquashade", "Rockshade", "Flarefrost",
    "Voltflare", "Sylvanstrike", "Pyroscorch", "Dracothunder", "Aquamist",
    "Leafshimmer", "Frostbreeze", "Shadowsting", "Mysticblast", "Ragingroar",
    "Thunderstrike", "Blazeclaw", "Aquanox", "Gustwhisper", "Stoneshatter",
    "Flamehowl", "Waveblade", "Stormshadow", "Terraquake", "Freezefury",
    "Zephyrtide", "Dracowind", "Volcanicburst", "Lunarflare", "Solarshard",
    "Arcticstorm", "Mysticshroud", "Cinderwing", "Venomquake", "Boltstorm"
]

def generer_pokemon_aleatoire(noms):
    pokemon = []
    for _ in range(4):
        nom_aleatoire = random.choice(noms)
        vie_aléatoire = random.randint(78, 150)  
        dfs_aléatoire = random.randint(10, 25)  
        type_aleatoire = random.choice(["feu", "glace", "eau", "plante", "caca", "ombre", "fee", "electrique", "acier", "roche", "dragon", "poison", "vol", "combat", "insecte", "spectre", "lumiere", "psy"])
        vts_aleatoire = random.randint(5, 20)  

        # S'assurer qu'aucun nom n'est sélectionné deux fois
        while any(poke.name == nom_aleatoire for poke in pokemon):
            nom_aleatoire = random.choice(noms)

        choix = Pokemon(nom_aleatoire, vie_aléatoire, dfs_aléatoire, type_aleatoire, vts_aleatoire)
        pokemon.append(choix)

    return pokemon

liste_pokemon = generer_pokemon_aleatoire(pokemon_names)

class Attaque:
    def __init__(self, name, power, attack_type, pp):
        self.name = name
        self.power = power
        self.type = attack_type
        self.pp = pp

import random

noms_attaques = [
    "Lance-Flamme",
    "Hydrocanon",
    "Éclair",
    "Poing-Éclair",
    "Tranche",
    "Lame d'Air",
    "Vive-Attaque",
    "Vibraqua",
    "Laser Glace",
    "Psyko",
    "Tonnerre",
    "Fatal-Foudre",
    "Dracogriffe",
    "Séisme",
    "Boule Roc",
    "Coup d'Boule",
    "Météores",
    "Lame de Roc",
    "Bourdon",
    "Jet de Sable",
    "Morsure",
    "Ailes d'Acier",
    "Rafale Psy",
    "Ombre Nocturne",
    "Poing Météor",
    "Lance-Soleil",
    "Giga-Sangsue",
    "Piqué",
    "Bec Vrille",
    "Plaquage",
    "Lilliput",
    "Lance-Flèches",
    "Gyroballe",
    "Boue-Bombe",
    "Pouvoir Antique",
    "Bulldoboule",
    "Éclat Magique",
    "Piqûre",
    "Toxik",
    "Lutte",
    "Dard Mortel",
    "Croc de Mort",
    "Coud'Boue",
    "Balayage",
    "Sabotage",
    "Trempette",
    "Morphing",
    "Regard Médusant",
    "Force Poigne",
    "Gonflette",
    "Jet de Pierre",
    "Jet de Sable",
    "Gonflette",
    "Fléau",
    "Éclats Glace",
    "Tomberoche",
    "Casse-Brique",
    "Coup Bas",
    "Direct Toxik",
    "Séduction",
    "Attraction",
    "Tricherie",
    "Piqûre",
    "Onde de Choc",
    "Grimace",
    "Blizzard",
    "Danse-Pluie",
    "Brume",
    "Éruption",
    "Zénith",
    "Poudre Toxik",
    "Queue de Fer",
    "Faux-Chage",
    "Ombre Portée",
    "Ombre Nocturne",
    "Soin",
    "Poudre Dodo",
    "Tunnel",
    "Prescience",
    "Tir de Boue",
    "Tomberoche",
    "Blizzard",
    "Flamme Croix",
    "Pisto-Poing",
    "Tempête de Sable",
    "Piège de Roc",
    "Piqué",
    "Tunnel",
    "Croc Mortel",
    "Danse Lame",
    "Coup d'Boule",
    "Balayette",
    "Direct Toxik",
    "Piqué",
    "Ombre Nocturne",
    "Gonflette",
    "Tir de Boue",
    "Jet de Pierre",
    "Tomberoche",
    "Tranche-Nuit",
    "Mach Punch",
    "Vent Glace",
    "Plaie-Croix",
    "Force-Nature",
    "Lance-Flamme",
    "Tour Rapide",
    "Poing de Feu",
    "Saisie",
    "Berceuse",
    "Laser Glace",
    "Rugissement",
    "Picochoc",
    "Représailles",
    "Surf",
    "Onde Folie",
    "Onde de Choc",
    "Gros Yeux",
    "Attraction",
    "Poudre Toxik",
    "Météores",
    "Tricherie",
    "Coup Bas",
    "Bouclier Royal",
    "Queue de Fer",
    "Jet de Sable",
    "Exploforce",
    "Foudre",
    "Soin",
    "Morsure",
    "Direct Toxik",
    "Charge",
    "Pistolet à O",
    "Jet de Sable",
    "Coup d'Main",
    "Mégaphone",
    "Éclats Glace",
    "Balayette",
    "Coup Bas",
    "Boue-Bombe",
    "Vol Magnétik",
    "Choc Venin",
    "Champ Électrifié",
    "Séisme",
    "Coup d'Boule",
    "Vampibaiser",
    "Queue de Fer",
    "Pouvoir Antique",
    "Roulade",
    "Lance-Soleil",
    "Lance-Flamme",
    "Frappe Atlas",
    "Lame de Roc",
    "Berceuse",
    "Explosion",
    "Garde Large",
    "Soin",
    "Griffe Acier",
    "Gyroballe",
    "Laser Glace",
    "Aurore",
    "Boule Élek",
    "Vent Glace",
    "Mur Lumière",
    "Vive-Attaque",
    "Séisme",
    "Vol Magnétik",
    "Flamme Croix",
    "Chargeur",
    "Brouillard",
    "Rayon Simple",
    "Coup d'Boule",
    "Piqûre",
    "Choc Venin",
    "Vent Glace",
    "Vampibaiser",
    "Danse-Pluie",
    "Tricherie",
    "Queue de Fer",
    "Soin",
    "Jet de Pierre",
    "Poudre Dodo",
    "Saisie",
    "Poing Météor",
    "Laser Glace",
    "Séduction",
    "Pouvoir Antique",
    "Tir de Boue",
    "Coup Bas",
    "Faux-Chage",
    "Choc Psy",
    "Exploforce",
    "Ombre Nocturne",
    "Lance-Flèches",
    "Picochoc",
    "Machination",
    "Représailles",
    "Aile d'Acier",
    "Gonflette",
    "Éclat Magique",
    "Jet de Pierre",
    "Lame d'Air",
    "Soin",
    "Poing-Éclair",
    "Danse-Lames",
    "Poudre Toxik",
    "Tomberoche",
    "Dracogriffe",
    "Croc Mortel",
    "Lance-Soleil",
    "Morsure",
    "Coup d'Main",
    "Balayette",
    "Poing Météor",
    "Casse-Brique",
    "Ombre Nocturne",
    "Onde de Choc",
    "Éruption",
    "Jet de S"
]
        
def generer_attaque_aleatoire(noms):
    attaques_par_type = {}
    
    for _ in range(100):
        nom_aleatoire = random.choice(noms)
        power_aleatoire = random.randint(5, 25)  
        type_aleatoire = random.choice(["feu", "glace", "eau", "plante", "caca", "ombre", "fee", "electrique", "acier", "roche", "dragon", "poison", "vol", "combat", "insecte", "spectre", "lumiere", "psy"])
        pp_aleatoire = random.randint(4, 11)  

        attaque = Attaque(nom_aleatoire, power_aleatoire, type_aleatoire, pp_aleatoire)

        # S'assurer qu'il y a entre 6 et 8 attaques pour chaque type
        if type_aleatoire not in attaques_par_type:
            attaques_par_type[type_aleatoire] = []
        
        if len(attaques_par_type[type_aleatoire]) < 8:
            attaques_par_type[type_aleatoire].append(attaque)

    # Créer une liste finale d'attaques
    attaques_finales = []
    for attaques_liste in attaques_par_type.values():
        attaques_finales.extend(attaques_liste)

    return attaques_finales

attaques = generer_attaque_aleatoire(noms_attaques)
    
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

class Objet:
    def __init__(self, name, obj_type, pp, point):
        self.name = name
        self.type = obj_type
        self.pp = pp
        self.point = point

def generer_objets_aleatoires(noms_objets):
    objets_aleatoires = []

    for _ in range(4):
        nom_aleatoire = random.choice(noms_objets)
        type_aleatoire = random.choice(["attaque", "heal", "def"])
        pp_aleatoire = 1
        if type_aleatoire == "attaque" or type_aleatoire == "def":    
            point_aleatoire = random.randint(1, 15)  
        elif type_aleatoire == "heal":    
            point_aleatoire = random.randint(1, 20)

        # S'assurer qu'aucun objet n'est sélectionné deux fois
        while any(objet.name == nom_aleatoire for objet in objets_aleatoires):
            nom_aleatoire = random.choice(noms_objets)

        objet = Objet(nom_aleatoire, type_aleatoire, pp_aleatoire, point_aleatoire)
        objets_aleatoires.append(objet)

    return objets_aleatoires

noms_objets_pokemon = [
    "Potion",
    "Super Potion",
    "Hyper Potion",
    "Baie Oran",
    "Baie Sitrus",
    "Poudre Soin",
    "Antidote",
    "Antipara",
    "Anti-Brûle",
    "Rappel",
    "Rappel Max",
    "Méga-Gemme",
    "Pierre Dure",
    "Baie Maron",
    "Baie Pêcha",
    "Baie Ceriz",
    "Baie Fraive",
    "Baie Willia",
    "Baie Kika",
    "Baie Nanone",
    "Baie Remu",
    "Baie Qualot",
    "Baie Sédra",
    "Baie Tamato",
    "Baie Babiri",
    "Baie Jouca",
    "Baie Charti",
    "Baie Chocco",
    "Baie Babiri",
    "Baie Prine",
    "Baie Nanone",
    "Baie Kika",
    "Baie Babiri",
    "Pierre Foudre",
    "Pierre Eau",
    "Pierre feu",
    "Pierre Plante",
    "Méga-Gemme Eau",
    "Méga-Gemme feu",
    "Méga-Gemme Plante",
    "Méga-Gemme Electro",
    "Méga-Gemme Glace",
    "Méga-Gemme Psy",
    "Méga-Gemme Ténèbres",
    "Méga-Gemme Vol",
    "Méga-Gemme Acier",
    "Méga-Gemme Roche",
    "Méga-Gemme Sol",
    "Méga-Gemme Combat",
    "Méga-Gemme Poison",
    "Méga-Gemme Spectre",
    "Méga-Gemme Insecte",
    "Méga-Gemme Normal",
    "Méga-Gemme Dragon",
    "Méga-Gemme Poison",
    "Méga-Gemme Psy",
    "Méga-Gemme Vol",
    "Méga-Gemme Ténèbres",
    "Méga-Gemme Roche",
    "Méga-Gemme Sol",
    "Méga-Gemme Combat",
    "Méga-Gemme Insecte",
    "Méga-Gemme Normal",
    "Méga-Gemme Dragon",
    "Méga-Gemme Poison",
    "Méga-Gemme Psy",
    "Méga-Gemme Vol",
    "Méga-Gemme Ténèbres",
    "Méga-Gemme Roche",
    "Méga-Gemme Sol",
    "Méga-Gemme Combat",
    "Méga-Gemme Insecte",
    "Méga-Gemme Normal",
    "Méga-Gemme Dragon",
    "Méga-Gemme Poison",
    "Méga-Gemme Psy",
    "Méga-Gemme Vol",
    "Méga-Gemme Ténèbres",
    "Méga-Gemme Roche",
    "Méga-Gemme Sol",
    "Méga-Gemme Combat",
    "Méga-Gemme Insecte",
    "Méga-Gemme Normal",
    "Méga-Gemme Dragon"
]



while len(noms_objets_pokemon) < 100:
    noms_objets_pokemon.append(f"Objet_{len(noms_objets_pokemon)+1}")

# Mélanger la liste pour plus de variété
random.shuffle(noms_objets_pokemon)

"""# Afficher les 10 premiers noms d'objets
print(noms_objets_pokemon[:10])"""

# Utiliser la fonction pour générer 4 objets aléatoires
objets_aleatoires = generer_objets_aleatoires(noms_objets_pokemon)

# Afficher les détails des objets générés
for objet in objets_aleatoires:
    print(f"Nom: {objet.name}, Type: {objet.type}, PP: {objet.pp}, Point: {objet.point}")

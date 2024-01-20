import random
class Pokemon:
    def __init__(self, name, vie, dfs, atq, type, vts):
        self.name =  name #"Son blaze"
        self.vie = vie #"Vie" #entre 78 et 150
        self.def_spe = def_spe #entre 5 et 20
        self.dfs = dfs #"Défense" #entre 5 et 20
        self.atq_spe = atq_spe #entre 10 et 35
        self.atq = atq # "Attaque"  entre 10 et 35
        self.type = type #"son type (pour savoir si il fait degat *2)" #10 type : feu, Glace, Eau, Fee, Plante, Ombre, Acier, Caca, electrique, 
        self.vitesse = vts #"sa rapiditer" #entre 1 et 20
        self.pouvoir = []
        self.alive = True
        self.status = None # [brulé, paralysé, gelé, endormi, empoisonné, empoisonné+(ce qui correspond a gravement empoisonné), plein de caca, mal au crâne, brisé ]

pokemon_names = [
    "Flarion", "Aquaphox", "Voltalon", "Terradra", "Pyrospire",
    "Zephyreon", "Dracoline", "Glacara", "Sylverix", "Magmawisp",
    "Leafblade", "Frostbite", "Dracoco", "Rockquake", "Psychwing",
    "Spectrosa", "Emberflare", "Aquaquill", "Gytan", "Terrafin",
    "Flufflare", "Voltorbolt", "Earthquakeon", "Pyroclaw", "Zephyraptor",
    "Dracofire", "Glacius", "Sylvanight", "Magmaraider", "Leafshadow",
    "Frostnova", "Tidaltide", "Blitzspark", "Torpingpong", "Mindflare",
    "Shadowstalker", "Flareonix", "Wavewarden", "Boltstrike", "Mossquake",
    "Amphinlande", "Aerowing", "RedBull", "Lavalanche", "Leafwhisper",
    "Thunderclaw", "Wavecrest", "Quakestone", "Vortexblade", "Solarflare",
    "Lunarshroud", "Mysticbreeze", "Dedette", "Frostfang", "Stormsurge",
    "Abyssalbite", "Ironhide", "Mysticshade", "Radiantbeam", "Dreadhowl",
    "Venomfang", "Magmaflare", "Cinderstorm", "Glacialchill", "Dedette",
    "Zapstrike", "Aerofrost", "Aquashade", "Rockshade", "Flarefrost",
    "Voltflare", "Sylvanstrike", "Pyroscorch", "Dracothunder", "Aquamist",
    "Leafshimmer", "Frostbreeze", "Shadowsting", "Mysticblast", "Ragingroar",
    "Thunderstrike", "Pigrochou", "Aquanox", "Gustwhisper", "Stoneshatter",
    "Flamehowl", "Waveblade", "Stormshadow", "Terraquake", "Freezefury",
    "Zephyrtide", "Dracowind", "Ark", "Lunarflare", "Solarshard",
    "Arcticstorm", "Mysticshroud", "Cinderwing", "Venomquake", "Boltstorm"
]

def generer_pokemon_aleatoire(noms):
    pokemon = []
    for _ in range(4):
        nom_aleatoire = random.choice(noms)
        vie_aléatoire = random.randint(110, 150)  
        dfs_aléatoire = random.randint(5, 20)  
        def_spe_aletoire = random.randint(5, 20)
        atq_aléatoire = random.randint(10, 35)
        atq_spe_aleatoire = random.randint(10, 35)
        type_aleatoire = random.choice(["feu", "glace", "eau", "plante", "caca", "ombre", "fee", "electrique", "acier", "roche", "dragon", "poison", "vol", "combat", "insecte", "spectre", "lumiere", "psy"])
        vts_aleatoire = random.randint(10, 20)  

        # S'assurer qu'aucun nom n'est sélectionné deux fois
        while any(poke.name == nom_aleatoire for poke in pokemon):
            nom_aleatoire = random.choice(noms)

        choix = Pokemon(nom_aleatoire, vie_aléatoire, dfs_aléatoire, atq_aléatoire, type_aleatoire, vts_aleatoire)
        pokemon.append(choix)

    return pokemon

liste_pokemon = generer_pokemon_aleatoire(pokemon_names)

class Attaque:
    def __init__(self, name, power, attack_type, pp):
        self.name = name
        self.power = power
        self.type = attack_type
        self.categorie = catégorie #[Attaque, Attaque_spe, status]
        self.status = status + chance #{status : chance de l'appliquer}
        self.accuracy = précision # chance de rater entre 70 et 100 pour la plupart des attaques
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
    "Ouragan",
    "Fouet Lianes",
    "Exploflammes",
    "Coup de Grâce",
    "Lance-Pluie",
    "Flash",
    "Fracas",
    "Lance-Vapeur",
    "Rafale de Feu",
    "Éclair Fulgurant",
    "Avalanche",
    "Piqué Mortel",
    "Bourrasque",
    "Furie",
    "Geyser",
    "Canon à Ondes",
    "Écrasement",
    "Frappe Psy",
    "Étreinte Glacée",
    "Mégaphone Sonique",
    "Étincelles",
    "Écho",
    "Danse Lame",
    "Tempête Psychique",
    "Tourbillon",
    "Fulguro Charge",
    "Coup d'Éclat",
    "Souffle Gelé",
    "Acide Corrosif",
    "Bouclier Éthéré",
    "Barrage de Feu",
    "Flèche de Glace",
    "Danse du Vent",
    "Séisme Dévastateur",
    "Rafale Tornade",
    "Foudre Céleste",
    "Charge Foudroyante",
    "Vent Solaire",
    "Brume Toxique",
    "Lueur Mystique",
    "Rayon Solaire",
    "Torrent Hivernal",
    "Frappe Cosmique",
    "Sourire Éblouissant",
    "Pluie d'Étoiles",
    "Éclat de Nuit",
    "Lame Sombre",
    "Fendoir de Glace",
    "Météore Éthéré",
    "Rafale Infernale"
    "Ecrasement"
    "Triple axel"
]
        
def generer_attaque_aleatoire(noms):
    attaques_aleatoires = []
    noms_utilises = set()

    for _ in range(150):
        nom_aleatoire = random.choice(noms)

        # Assurez-vous que le nom n'a pas encore été utilisé
        while nom_aleatoire in noms_utilises:
            nom_aleatoire = random.choice(noms)

        noms_utilises.add(nom_aleatoire)

        noms.remove(nom_aleatoire)
        power_aleatoire = random.randint(19, 25)
        type_aleatoire = random.choice(["feu", "glace", "eau", "plante", "caca", "ombre", "fee", "electrique", "acier", "roche", "dragon", "poison", "vol", "combat", "insecte", "spectre", "lumiere", "psy"])
        pp_aleatoire = random.randint(2, 7)

        attaque = Attaque(nom_aleatoire, power_aleatoire, type_aleatoire, pp_aleatoire)
        attaques_aleatoires.append(attaque)

    return attaques_aleatoires

attaques = generer_attaque_aleatoire(noms_attaques)
    
"""#separer les attaques par types :
types_dict = {}
for attaque in attaques:
    type_ = attaque.type
    if type_ not in types_dict:
        types_dict[type_] = [attaque]
    else:
        types_dict[type_].append(attaque)"""

class Objet:
    def __init__(self, name, obj_type, pp, point):
        self.name = name
        self.type = obj_type
        self.pp = pp
        self.point = point
        self.owner = "1 ou 2"

def generer_objets_aleatoires(noms_objets):
    objets_aleatoires = []

    for _ in range(4):
        nom_aleatoire = random.choice(noms_objets)
        type_aleatoire = random.choice(["attaque", "heal", "def"])
        pp_aleatoire = 1
        if type_aleatoire == "attaque" or type_aleatoire == "def":    
            point_aleatoire = random.randint(5, 13)  
        elif type_aleatoire == "heal":    
            point_aleatoire = random.randint(1, 20)

        # S'assurer qu'aucun objet n'est sélectionné deux fois
        while any(objet.name == nom_aleatoire for objet in objets_aleatoires):
            nom_aleatoire = random.choice(noms_objets)

        objet = Objet(nom_aleatoire, type_aleatoire, pp_aleatoire, point_aleatoire)
        objets_aleatoires.append(objet)

    return objets_aleatoires

noms_objets_pokemon = [
    "Poopkeball Super",
    "Poopkeball Basic",
    "Poopkeball Bizarre",
    "Poopkeball 0",
    "Poopkeball EasterEgg",
    "Poopkeball Book",
    "Poopkeball Newton",
    "Poopkeball Amir",
    "Poopkeball Adam",
    "Poopkeball Elias",
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

# Utiliser la fonction pour générer 4 objets aléatoires
objets_aleatoires = generer_objets_aleatoires(noms_objets_pokemon)

liste_vrai_poopkemon = [] #Une liste de poopkemon avec des stats bien définis pour d'autres formats



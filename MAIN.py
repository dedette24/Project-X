import random as rd
import time
from classe import *
print("\n")

action = [0, 0]
liste_tt_attaques = []
Pokemon_actif = []

equipe_1 = liste_pokemon[:2]
equipe_2 = liste_pokemon[-2:]

def info(equipe_1, equipe_2):
    print("équipe 1 : ")
    print(f"le pokemon 1 de l'equipe 1 est : {equipe_1[0].name} et il a {equipe_1[0].vie} pv")
    print(f"le pokemon 2 de l'equipe 1 est : {equipe_1[1].name} et il a {equipe_1[1].vie} pv")
    print("équipe 2 : ")
    print(f"le pokemon 1 de l'equipe 2 est : {equipe_2[0].name} et il a {equipe_2[0].vie} pv")
    print(f"le pokemon 2 de l'equipe 2 est : {equipe_2[1].name} et il a {equipe_2[1].vie} pv")
    #on définit la vitesse des pokemons
    print("")
    print(f"la vitesse de {equipe_1[0].name} est de : {equipe_1[0].vitesse} et il est de type {equipe_1[0].type}")
    print(f"la vitesse de {equipe_1[1].name} est de : {equipe_1[1].vitesse} et il est de type {equipe_1[1].type}")
    print(f"la vitesse de {equipe_2[0].name} est de : {equipe_2[0].vitesse} et il est de type {equipe_2[0].type}")
    print(f"la vitesse de {equipe_2[1].name} est de : {equipe_2[1].vitesse} et il est de type {equipe_2[1].type}")
    print("")
    return equipe_1, equipe_2

#qui attaquer
def choix_attaques_DEBUT(pokemon):
    print("\n ----------------------")
    attaques_possibles = [attaque for attaque in attaques if attaque.type == pokemon.type]
    vrai_attaque_dispo = attaques_possibles[:6]
    attaques_selectionnees = []

    print(f"Choisissez 3 attaques pour {pokemon.name} parmi les attaques suivantes :")
    
    while len(attaques_selectionnees) < 3:
        for i, attaque in enumerate(vrai_attaque_dispo, 1):
            print(f"{i}. {attaque.name} (Puissance: {attaque.power}, PP: {attaque.pp})")

        while True:
            try:
                choix = int(input(f"Choisissez l'attaque {len(attaques_selectionnees) + 1}: "))
                break  # Sort de la boucle si la conversion en int réussit
            except ValueError:
                print("Veuillez entrer un nombre entier.")

        if 1 <= choix <= len(vrai_attaque_dispo):
            attaque_selectionnee = vrai_attaque_dispo.pop(choix - 1)
            
            # Vérification si l'attaque n'a pas déjà été sélectionnée
            if attaque_selectionnee not in attaques_selectionnees:
                attaques_selectionnees.append(attaque_selectionnee)
                print(f"{attaque_selectionnee.name} a été sélectionnée.")
            else:
                print("Vous avez déjà choisi cette attaque. Veuillez choisir une autre attaque.")
        else:
            print("Choix invalide. Veuillez choisir parmi les attaques disponibles.")

    print("\n")
    return attaques_selectionnees

#print(equipe_1[0].pouvoir[0].name) --> ce qui faut faire pour afficher attaque
#qui jouer
def choisir_pokemon(equipe, num):
    print("\n ----------------------")
    print(f"\nChoisissez un Pokémon a jouer parmi les suivants equipe {num}: ")
    for i, pokemon in enumerate(equipe, 1):
        print(f"{i}. {pokemon.name} (PV: {pokemon.vie})")

    while True:
        try:
            choix_pokemon = int(input("Entrez le numéro du Pokémon que vous souhaitez jouer : "))
            if equipe[choix_pokemon-1].vie < 1:
                print("Vous ne pouvez plus utiliser ce pokemon, il est KO.")
            else:
                if 1 <= choix_pokemon <= len(equipe):
                    break
                else:
                    print("Choix invalide. Veuillez choisir parmi les Pokémon disponibles.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    return equipe[choix_pokemon - 1]

"""#chaque equipe choisie les pokemons qu'ils vont jouer
poke1_actif = choisir_pokemon(equipe_1, 1)
poke2_actif = choisir_pokemon(equipe_2, 2)
Pokemon_actif.append(poke1_actif)
Pokemon_actif.append(poke2_actif)
for i, pokemon in enumerate(Pokemon_actif, 1):
            print(f"équipe {i} joue : {pokemon.name}")"""

#LES 2 MARCHES
#premier 0 : action de l'equipe 1 - deuxieme 0 action de l'equipe 2
def choix_action(num, liste):
    print("\n ----------------------")
    print(f"\nVous allez maintenant choisir l'action que vous voulez faire !")
    print(f"1. attaquer")
    print(f"2. changer de poopkemon")
    print(f"3. utiliser un objet")
    print(f"4. abandonner")
    while True:
        try:
            action = int(input(f"Choisie l'action que vous voulez faire equipe {num} en rentrant le numero de l'action : "))
            if 1 <= action <= 4:
                break
            else:
                print("Choix invalide. Veuillez choisir parmi les actions disponibles.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")
    liste[num-1] = action
    return(liste)

#CA MARCHE !

#------------------------------------------------------------------------
#a faire : attaque, objet
#fait : choix attaque

#choix_attaque : 

#print(equipe_1[0].pouvoir[0].name) --> ce qui faut faire pour afficher attaque

choix_attaque_moment = [0, 0]

def choix_attaque(pokemon, num, liste):
    print("\n ----------------------")
    # Afficher les attaques disponibles pour le Pokémon
    print(f"\n{pokemon[num-1].name} a les attaques suivantes : ")
    for i in range(3):
        print(f"attaque {i+1} : {pokemon[num-1].pouvoir[i].name} ({pokemon[num-1].pouvoir[i].pp} utilisation restantes) ({pokemon[num-1].pouvoir[i].name})")
    while True:
        try:
            action = int(input(f"Choisie l'une des attaques ci-dessous que vous voulez utiliser equipe {num} : "))
            if pokemon[num-1].pouvoir[action-1].pp < 1: 
                print("Vous n'avez plus assez d'utilisation pour cette attaque.")
            else:
                if 1 <= action <= 4:
                    break
                else:
                    print("Choix invalide. Veuillez choisir parmi les attaques disponibles.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")
    cbon = pokemon[num-1].pouvoir[action-1]
    liste[num-1] = cbon
    print(liste)
    return(liste)

def efficace_raccour(num, actif, liste, B, N, O):
    print("\n ----------------------")
    if num == 1:
        adv = 1
    else:
        adv = 0
    if actif[adv].type in B:
        degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5)) * 2  #super efficace
        actif[adv].vie -= degats_infligés
        print("c super efficace")
        return degats_infligés
    elif actif[adv].type in N:
        degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5)) / 1.5  # Pas très efficace
        actif[adv].vie -= degats_infligés
        print("c'est pas tres éfficace")
        return degats_infligés
    elif actif[adv].type in O:    #Inefficace
        print("Vous ne faites pas de degat !")
        return degats_infligés
    else:
        print("l'attaque va se derouler normalement ! ")
        degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5))    #Normal
        actif[adv].vie -= degats_infligés
        return degats_infligés

def efficace(num, actif, liste):
    degats_infligés = 0
    if num == 1:
        adv = 1
    else:
        adv = 0

    if actif[num-1].type == "feu": #feu
        liste_effi = ["glace", "plante", "acier", "insecte"] #T
        liste_nul = ["feu", "eau", "dragon", "lumiere"] #N
        liste_0 = ["roche"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        
    if actif[num-1].type == "glace": #glace
        liste_effi = ["glace", "plante", "caca", "roche", "dragon", "poison", "vol"] #T
        liste_nul = ["feu", "insecte"] #N
        liste_0 = ["eau"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "eau": #eau
        liste_effi = ["feu", "caca", "roche"] #T
        liste_nul = ["eau", "dragon"] #N
        liste_0 = [] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
            
    if actif[num-1].type == "plante": #plante
        liste_effi = ["eau", "roche"] #T
        liste_nul = ["feu", "glace","plante","acier","dragon", "poison", "insecte"] #N
        liste_0 = ["caca"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "caca": #caca
        liste_effi = ["feu", "plante", "ombre", "fee", "acier", "dragon", "combat", "lumiere", "psy"] #T
        liste_nul = ["caca", "poison", "roche"] #N
        liste_0 = ["glace", "eau"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "ombre": #ombre
        liste_effi = ["spectre", "psy"] #T
        liste_nul = ['ombre', 'dragon', 'combat'] #N
        liste_0 = ["fee"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
            
    if actif[num-1].type == "fee": #fee
        liste_effi = ["caca", "ombre", "dragon", "combat", "lumiere", "psy"] #T
        liste_nul = ['feu', 'fee', 'acier', "poison"] #N
        liste_0 = [] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "electrique": #electrique
        liste_effi = ["eau", "acier", "vol"] #T
        liste_nul = ['plante', 'electrique', 'dragon'] #N
        liste_0 = ["roche"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "acier": #acier
        liste_effi = ["glace", "caca", "fee", "roche", "dragon", "poison"] #T
        liste_nul = ["feu", "plante", "acier", "insecte"] #N
        liste_0 = [] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "roche": #roche
        liste_effi = ["feu", "glace", "electrique", "acier", "roche", "poison"] #T
        liste_nul = ['eau', 'insecte', 'dragon'] #N
        liste_0 = ["vol"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
    
    if actif[num-1].type == "dragon": #dragon
        liste_effi = ["dragon", "psy"] #T
        liste_nul = [] #N
        liste_0 = [] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "poison": #poison
        liste_effi = ["plante", "fee", "acier", "dragon", "poison", "combat"] #T
        liste_nul = ["roche", "psy"] #N
        liste_0 = [] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "vol": #vol
        liste_effi = ["plante", "combat", "insecte"] #T
        liste_nul = ["electrique", "acier", "roche", "dragon", "vol"] #N
        liste_0 = [] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
    
    if actif[num-1].type == "combat": #combat
        liste_effi = ["glace", "fee", "acier", "roche", "insecte"] #T
        liste_nul = ["eau", "caca", "dragon", "psy"] #N
        liste_0 = ["ombre", "vol", "spectre"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "insecte": #insecte
        liste_effi = ["plante", "caca", "ombre", "fee", "psy"] #T
        liste_nul = ["feu", "dragon", "insecte"] #N
        liste_0 = ["vol"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "spectre": #spectre
        liste_effi = ["dragon", "psy", "fee", "spectre"] #T
        liste_nul = [] #N
        liste_0 = ["ombre", "lumiere"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "lumiere": #lumiere
        liste_effi = ["dragon", "caca", "ombre", "vol", "combat", "spectre"] #T
        liste_nul = ["feu", "fee", "acier", "lumiere"] #N
        liste_0 = ["plante"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    if actif[num-1].type == "psy": #psy
        liste_effi = ["poison", "combat"] #T
        liste_nul = ["caca", "acier", "dragon", "insecte", "spectre", "psy"] #N
        liste_0 = ["ombre"] #X
        efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0)

    return degats_infligés

def attaque_boucle(num, actif, liste):
    print("\n ----------------------")
    if num == 1:
        adv = 1
    else: 
        adv = 0 
    print(f"Vous allez attaquer équipe {num} !")
    trans = choix_attaque(actif, num, liste)
    print(f"Vous utilisez l'attaque {trans[num-1].name}")
    degat = int(efficace(num, actif, trans))
    print(f"Vous infliger {degat} dégats à {actif[adv].name}")
    actif[adv].vie -= degat
    trans[num-1].pp -= 1
    print(f"il vous reste {trans[num-1].pp} utilisation restantes pour l'attaque {trans[num-1].name}")
    if actif[adv].vie < 1:
        actif[adv].alive = False
        print(f"Vous avez eliminé {actif[adv].name}, l'adversaire ne pourra plus l'utiliser à moins d'utiliser une potion de 'heal'.")
    else:
        print(f"il reste {actif[adv].vie} vie à {actif[adv].name}")

#attaque_boucle(1, Pokemon_actif, choix_attaque_moment)

"""attaque_boucle(1, Pokemon_actif, choix_attaque_moment)
attaque_boucle(2, Pokemon_actif, choix_attaque_moment)"""

"""def Realisation(liste, equipe, adversaire, num, num_2, poke_actif):
    if liste[num-1] == 1 and liste[num_2-1] == 1:
        if poke_actif[0].vitesse < poke_actif[1].vitesse:
            choix_cible(equipe_2, equipe_1, cible)
        else: 
            choix_cible(equipe_1, equipe_2, cible)"""
recurence = [0, 0]
#P1 = 1.0 / P2 = 2.0
#si def alors 1, si attaque alors 2

def utiliser_objet(num, actif, liste, rec):
    print("\n ----------------------")
    print("\n")
    if num == 1:
        potions_disponibles = liste[:2]
    else:
        potions_disponibles = liste[-2:]
    print(f"Voici les potions que vous avez à votre disposition, équipe {num}: ")
    for i, potion in enumerate(potions_disponibles, 1):
        print(f"{i}. {potion.name} (utilisation restantes : {potion.pp}, Points: {potion.point}, Type : {potion.type})")
    while True:
        try:
            choix_potion = int(input("Entrez le numéro de la potion que vous souhaitez utiliser : "))
            if 1 <= choix_potion <= len(potions_disponibles):
                break
            else:
                print("Choix invalide. Veuillez choisir parmi les potions disponibles.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    print(choix_potion)
    potion_choisie = potions_disponibles[choix_potion - 1]

    if potion_choisie.type == "heal":
        actif[num - 1].vie += potion_choisie.point
        print(f"Le pokemon {actif[num - 1].name} a gagné {potion_choisie.point} points de vie !")
        print(f"il passe maintenant a {actif[num - 1].vie} points de vie !")
    elif potion_choisie.type == "def":
        rec[num - 1] = potion_choisie
        print(f"La prochaine attaque de l'adversaire sera réduite de {potion_choisie.point} points !.")
    elif potion_choisie.type == "attaque":
        rec[num - 1] = potion_choisie
        print(f"Votre prochaine attaque fera {potion_choisie.point} de dégâts en plus !")
    print(rec)
    return rec, actif, liste

#utiliser_objet(1, Pokemon_actif, objets_aleatoires, recurence)

def abandon(num):
    print("\n ----------------------")
    chance = rd.randint(1, 5)
    print(f"Pour que ce soit un peu plus marrant, equipe {num}, vous avez 20% de chance de pouvoir abandonner.")
    if chance == 2:
        print(f"Le joueur {num} a perdu, victoire au joueur {num + 1 if num == 1 else num - 1}")
        return True
    else :
        print("Le combat n'est pas fini, n'abandonne pas ! \U0001f643")

#-------------------------------------------------------------------------------------------------
# Mtn faut la boucle
# A faire : L'etat KO des pokemons , Changer de poopkemon, dégats super efficace et pas très efficace,


#par exemple pour feu qui est efficace sur glace



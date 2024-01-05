import random as rd
import time
from classe import *
print("\n")

action = [0, 0]
liste_tt_attaques = []
Pokemon_actif = []


#choisie pokemon aleatoire pour chaque équipe
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

def info(equipe_1, equipe_2):
    print("équipe 1 : ")
    print(f"le pokemon 1 de l'equipe 1 est : {equipe_1[0].name} et il a {equipe_1[0].vie} pv")
    print(f"le pokemon 2 de l'equipe 1 est : {equipe_1[1].name} et il a {equipe_1[1].vie} pv")
    print("équipe 2 : ")
    print(f"le pokemon 1 de l'equipe 2 est : {equipe_2[0].name} et il a {equipe_2[0].vie} pv")
    print(f"le pokemon 2 de l'equipe 2 est : {equipe_2[1].name} et il a {equipe_2[1].vie} pv")
    #on définit la vitesse des pokemons
    print("")
    print(f"la vitesse de {equipe_1[0].name} est de : {equipe_1[0].vitesse}")
    print(f"la vitesse de {equipe_1[1].name} est de : {equipe_1[1].vitesse}")
    print(f"la vitesse de {equipe_2[0].name} est de : {equipe_2[0].vitesse}")
    print(f"la vitesse de {equipe_2[1].name} est de : {equipe_2[1].vitesse}")
    print("")
    return equipe_1, equipe_2

info(equipe_1, equipe_2)

#qui attaquer
def choix_attaques_DEBUT(pokemon):
    attaques_possibles = [attaque for attaque in attaques if attaque.type == pokemon.type]
    attaques_selectionnees = []

    print(f"Choisissez 3 attaques pour {pokemon.name} parmi les attaques suivantes :")
    
    while len(attaques_selectionnees) < 3:
        for i, attaque in enumerate(attaques_possibles, 1):
            print(f"{i}. {attaque.name} (Puissance: {attaque.power}, PP: {attaque.pp})")

        while True:
            try:
                choix = int(input(f"Choisissez l'attaque {len(attaques_selectionnees) + 1}: "))
                break  # Sort de la boucle si la conversion en int réussit
            except ValueError:
                print("Veuillez entrer un nombre entier.")

        if 1 <= choix <= len(attaques_possibles):
            attaque_selectionnee = attaques_possibles.pop(choix - 1)
            
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

"""equipe_1[0].pouvoir = choix_attaques_DEBUT(equipe_1[0])
equipe_1[1].pouvoir = choix_attaques_DEBUT(equipe_1[1])
equipe_2[0].pouvoir = choix_attaques_DEBUT(equipe_2[0])
equipe_2[1].pouvoir = choix_attaques_DEBUT(equipe_2[1])"""

#print(equipe_1[0].pouvoir[0].name) --> ce qui faut faire pour afficher attaque
#qui jouer
def choisir_pokemon(equipe, num):
    print(f"\nChoisissez un Pokémon a jouer parmi les suivants equipe {num}: ")
    for i, pokemon in enumerate(equipe, 1):
        print(f"{i}. {pokemon.name} (PV: {pokemon.vie})")

    while True:
        try:
            choix_pokemon = int(input("Entrez le numéro du Pokémon que vous souhaitez jouer : "))
            if 1 <= choix_pokemon <= len(equipe):
                break
            else:
                print("Choix invalide. Veuillez choisir parmi les Pokémon disponibles.")
        except ValueError:
            print("Veuillez entrer un namebre entier.")

    return equipe[choix_pokemon - 1]

#chaque equipe choisie les pokemons qu'ils vont jouer
poke1_actif = choisir_pokemon(equipe_1, 1)
poke2_actif = choisir_pokemon(equipe_2, 2)
Pokemon_actif.append(poke1_actif)
Pokemon_actif.append(poke2_actif)
for i, pokemon in enumerate(Pokemon_actif, 1):
            print(f"équipe {i} joue : {pokemon.name}")

#LES 2 MARCHES
#premier 0 : action de l'equipe 1 - deuxieme 0 action de l'equipe 2
def choix_action(num, liste):
    print(f"\nVous allez maintenant choisir 'action que vous voulez faire !")
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
    # Afficher les attaques disponibles pour le Pokémon
    print(f"\n{pokemon[num-1].name} a les attaques suivantes : ")
    for i in range(3):
        print(f"attaque {i+1} : {pokemon[num-1].pouvoir[i].name} ({pokemon[num-1].pouvoir[i].pp} utilisation restantes)")
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

def attaque_boucle(num, actif, liste):
    if num == 1:
        adv = 1
    else: 
        adv = 0 
    print("Il est maintenant temps d'attaquer")
    choix_attaque(actif, num, liste)
    print(f"Vous utilisez l'attaque {liste[num-1].name}")
    
    degats_infligés = (liste[num-1].power - actif[adv].def)
    print(f"Vous infliger {liste[num-1].power} à {actif[adv].name}")
    actif[adv].vie -= degats_infligés  """actif[adv].vie - (liste[num-1].power - actif[adv].def)""" # J'ai remplacé ça par degats_infligés au-dessus
    liste[num-1].pp -= 1
    print(f"il vous reste {liste[num-1].pp} utilisation restantes pour l'attaque {liste[num-1].name}")
    print(f"il reste {actif[adv].vie} vie à {actif[adv].name}")

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
    print("\n")
    if num == 1:
        potions_disponibles = liste[:2]
    else:
        potions_disponibles = liste[-2:]
    print(f"Voici les potions que vous avez à votre disposition, équipe {num}: ")
    for i, potion in enumerate(potions_disponibles, 1):
        print(f"{i}. {potion.name} (PP: {potion.pp}, Points: {potion.point}, Type : {potion.type})")

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

utiliser_objet(1, Pokemon_actif, objets_aleatoires, recurence)

def abandon(num, actif, liste, rec):
    chance = rd.randint(1, 5)
    if chance == 2:
        print(f"Le joueur {num} a perdu, victoire au joueur {num + 1 if num == 1 else num - 1}")
        break
    else :
        print("Le combat n'est pas fini, n'abandonne pas !")

#-------------------------------------------------------------------------------------------------
# Mtn faut la boucle
# A faire : L'etat KO des pokemons , Changer de poopkemon, dégats super efficace et pas très efficace,


"""par exemple pour feu qui est efficace sur glace
liste_efficace_feu = [glace, plante, etc...]
if adv.type in liste_efficace{atq.type}:
    degats_infligés = (liste[num-1].power - actif[adv].def)*1.5
    print(c super efficace)
etc pour pas très efficace et tt"""

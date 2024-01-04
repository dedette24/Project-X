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
    attaques_possibles = []
    for attaque in attaques:
        if attaque.type == pokemon.type:
            attaques_possibles.append(attaque)

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
                print("Veuillez entrer un namebre entier.")

        if 1 <= choix <= len(attaques_possibles):
            attaque_selectionnee = attaques_possibles.pop(choix - 1)
            attaques_selectionnees.append(attaque_selectionnee)
            print(f"{attaque_selectionnee.name} a été sélectionnée.")
        else:
            print("Choix invalide. Veuillez choisir parmi les attaques disponibles.")

    print("\n")
    return attaques_selectionnees


equipe_1[0].pouvoir = choix_attaques_DEBUT(equipe_1[0])
equipe_1[1].pouvoir = choix_attaques_DEBUT(equipe_1[1])
equipe_2[0].pouvoir = choix_attaques_DEBUT(equipe_2[0])
equipe_2[1].pouvoir = choix_attaques_DEBUT(equipe_2[1])
"""liste_tt_attaques.append(att1)
liste_tt_attaques.append(att2)
liste_tt_attaques.append(att3)
liste_tt_attaques.append(att4)"""

#print(equipe_1[0].pouvoir[0].name) --> ce qui faut faire pour afficher attaque


"""#choisir la cible de t'attaque
cible = 0
def choix_cible(equipe, adversaire, cible_func):
    # Sélection de la cible
    print("\nChoisissez la cible pour l'attaque:")
    for i, adversaire in enumerate(equipe, 1):
        print(f"{i}. {adversaire.name} (PV: {adversaire.vie})")

    while True:
        try:
            cible = int(input("Entrez le numéro de la cible : "))
            if 1 <= cible <= len(equipe):
                break
            else:
                print("Choix invalide. Veuillez choisir parmi les Pokémon adverses.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    cible_func = equipe[cible - 1]
    return cible_func
#IL MARCHE !""" 
#j'en ai pas besoin enfaite...

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
        print(f"attaque {i+1} : {pokemon[num-1].pouvoir[i].name}")
    while True:
        try:
            action = int(input(f"Choisie l'une des attaques ci-dessous que vous voulez utiliser equipe {num} : "))
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
        adv = 2
    else: 
        adv = 1
    print("Il est maintenant temps d'attaquer")
    choix_attaque(actif, num, liste)
    print(f"Vous utilisez l'attaque {liste[num-1].name}")

attaque_boucle(1, Pokemon_actif, choix_attaque_moment)

"""def Realisation(liste, equipe, adversaire, num, num_2, poke_actif):
    if liste[num-1] == 1 and liste[num_2-1] == 1:
        if poke_actif[0].vitesse < poke_actif[1].vitesse:
            choix_cible(equipe_2, equipe_1, cible)
        else: 
            choix_cible(equipe_1, equipe_2, cible)"""

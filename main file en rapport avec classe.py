import random as rd
import time
from classe import *


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
print(f"équipe 1 : {equipe_1[0].nom} et {equipe_1[1].nom} / equipe 2 : {equipe_2[0].nom} et {equipe_2[1].nom} ")

class action:
    def __init__(self):
        self.priorité = "1 (prioritaire) ou 2 (pas prioritaire)"
        self.type = "attaque, change, objet, fuite"

def phase_choix( pokemon_actifs """Faut les nommer""" , tour):
    action = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
    if action == 1:
        action_choisi = attaquer() # Jsp c quoi la fonction
        return action_choisi
    elif action == 2:
        change_poke = input(f"pokemon voulez-vous déployer ? 1: {equipe_1[0].nom} ou 2: {equipe_1[1]}" )
        pokemon_actif = # l'autre mon
        return action_choisi
    elif action == 3:
        utiliser_obj() #Je sais tjrs pas 
        return action_choisi
    elif action == 4:
        a = rd.randint(1,5)
        if a == 1:
            print("Bravo ! Vous avez fuit avec succès et avez perdu le combat par votre lacheté !")
            break
        else:
            print("Haha, la fuite n'est pas une option, Looser")

def phase_action(""" les poke actifs """, action_choisi):
    if 

"""def surrender(): #si le joueur veut abandonner (marche ducoup on met entre crochet)
    abandon = int(input("tu ff ? si oui ecrit 1, sinon ecrit 2 : "))
    if abandon == 1:
        print("Le joueur machin a voté pour abandonner ! bien jouer autre joueur !")
        jeux = False
        return jeux
    else: 
        print("la partie continue !")
        pass

abandon = surrender()""" 


"""def fin_de_jeu_vie(equipe_1_P1_vie, equipe_1_P2_vie, equipe_2_P1_vie, equipe_2_P2_vie):
    if equipe_1_P1_vie == 0 and equipe_1_P2_vie == 0 or equipe_2_P1_vie == 0 and equipe_2_P2_vie == 0:
        jeux = False
        print("la partie est fini !")
        return jeux
    else: 
        print("la partie continue")
        pass

to_continue = fin_de_jeu_vie(equipe_1_P1_vie, equipe_1_P2_vie, equipe_2_P1_vie, equipe_2_P2_vie)"""

def choix(equipe_1, equipe_2, tours):
    if tours / 2 == type(float):
        print("---")
        print("Choisissez un Pokémon à jouer: ")
        for i, pokemon in enumerate(equipe_1):
            print(f"{i + 1}. {pokemon.nom} ({pokemon.vie})")
        choix_pokemon = int(input("Entrez le numéro du Pokémon: ")) - 1
        print("---")
        return equipe_1[choix_pokemon]
    else:
        print("---")
        print("Choisissez un Pokémon à jouer: ")
        for i, pokemon in enumerate(equipe_2):
            print(f"{i + 1}. {pokemon.nom}")
        choix_pokemon = int(input("Entrez le numéro du Pokémon: ")) - 1
        print("---")
        return equipe_2[choix_pokemon]


def choix_attaques(pokemon):
    attaques_possibles = []
    for attaque in attaques:
        if attaque.type == pokemon.type:
            attaques_possibles.append(attaque)

    attaques_selectionnees = []
    print(f"Choisissez 3 attaques pour {pokemon.nom} parmi les attaques suivantes :")
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
            attaques_selectionnees.append(attaque_selectionnee)
            print(f"{attaque_selectionnee.name} a été sélectionnée.")
        else:
            print("Choix invalide. Veuillez choisir parmi les attaques disponibles.")

    return attaques_selectionnees

atq_pok_e1_p1 = choix_attaques(equipe_1[0])
atq_pok_e1_p2 = choix_attaques(equipe_1[1])
atq_pok_e2_p1 = choix_attaques(equipe_2[0])
atq_pok_e2_p2 = choix_attaques(equipe_2[1])
print("\n")
print(f"{equipe_1[0].nom} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e1_p1]}")
print("\n")
print(f"{equipe_1[1].nom} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e1_p2]}")
print("\n")
print(f"{equipe_2[0].nom} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e2_p1]}")
print("\n")
print(f"{equipe_2[1].nom} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e2_p2]}")
"""def tours(equipe_1[0], equipe_1[1], equipe_2[0], equipe_2[1], tour):
    action = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
    if action == 1:
        attaquer() #Jsp c quoi la fonction
    elif action == 2:
        change_poke = input(f"pokemon voulez-vous déployer ? 1: {equipe_1[0].nom} ou 2: {equipe_1[1]}" )
        le_poke_en_combat = """
        
    
    
    
    
        


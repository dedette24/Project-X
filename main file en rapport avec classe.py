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

def tours(equipe_1):
    action = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
    if action == 1:
        
        

"""def start(): #qui commence (flemme de faire un truc long ducoup y'a aussi arrangement irl mais ca marche)
    print("l'un d'entre vous choisie un chiffre entre 1 et 2 si le chiffre choisie par la perosnne est le bon, alors il commence, sinon c'est l'autre.")
    commence = rd.randint(1,2)
    print("vous avez une minute pour vous décidez")
    time.sleep(10)#1min
    print("roulement de tambourrrrr")
    if commence == 1:
        print("c'est le joueur 1 qui commence")
    else:
        print("c'est le joueur 2 qui commence")
start()"""

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


def attaque(attacker, equipe_adverse, tours):
    print(f"Nous sommes au tours {tours} !")
    print(f"Choisissez une attaque pour {attacker.nom}:")
    for i, (attaque, degat) in enumerate(attacker.atq.items()):
            print(f"{i + 1}. {attaque} ({degat} dégâts)")
    choix_attaque = int(input("Entrez le numéro de l'attaque: ")) - 1
    attaque_selectionnee = list(attacker.atq.keys())[choix_attaque]
    print("---")
    print("qui veut tu attaquer ?")
    for i, pokemon in enumerate(equipe_2):
        print(f"{i + 1}. {pokemon.nom}")
    choix_adversaire = int(input(f"entrer le numero du pokemon que vous voulez attquez : ")) - 1
    adversaire = equipe_adverse[choix_adversaire]
    degat_inflige = attacker.atq[attaque_selectionnee]
    adversaire.vie -= (degat_inflige) - adversaire.dfs
    
    print("---")
    print(f"{attacker.nom} utilise {attaque_selectionnee}et inflige {degat_inflige} dégâts à {adversaire.nom}.")
    print(f"{adversaire.nom} a maintenant {adversaire.vie} points de vie.")
    print("---")
#fonctions choix et attaque
tours = 1
pokemon_joueur = choix(equipe_1, equipe_2, tours)
for i in range(4):
    attaque(pokemon_joueur, equipe_2, tours)
    tours = tours + 1

"""def tours(equipe_1[0], equipe_1[1], equipe_2[0], equipe_2[1], tour):
    action = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
    if action == 1:
        attaquer() #Jsp c quoi la fonction
    elif action == 2:
        change_poke = input(f"pokemon voulez-vous déployer ? 1: {equipe_1[0].nom} ou 2: {equipe_1[1]}" )
        le_poke_en_combat = """
        
    
    
    
    
        


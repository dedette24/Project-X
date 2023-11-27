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
print(f"équipe 1 : {equipe_1[0].nom} et {equipe_1[1].nom} / equipe 2 : {equipe_2[0].nom} et {equipe_2[1].nom} ")

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

def choix_pokemon(equipe_1, equipe_2, tours): #celui qui joue decide quel pokemon jouer
    if tours / 2 == type(float):
        print(f"voci les pokemon que tu as : {equipe_1[0].nom} qui as {equipe_1[0].vie} et {equipe_1[1].nom} qui as {equipe_1[1].vie}")
        joueur_1_pokemon_jouer = int(input(f"tu veux jouer qui ? 1 = {equipe_1[0].nom} ou 2 = {equipe_1[0].nom}: "))
        if joueur_1_pokemon_jouer == 1:
            joueur_1_pokemon_jouer = equipe_1[0]
        else:
            joueur_1_pokemon_jouer = equipe_1[1]
        return joueur_1_pokemon_jouer
    elif tours / 2 == type(int):
        print(f"voci les pokemon que tu as : {equipe_2[0].nom} qui as {equipe_2[0].vie} et {equipe_2[1].nom} qui as {equipe_2[1].vie}")
        joueur_2_pokemon_jouer = int(input(f"tu veux jouer qui ? 1 = {equipe_2[0].nom} ou 2 = {equipe_2[0].nom}: "))
        if joueur_2_pokemon_jouer == 1:
            joueur_2_pokemon_jouer = equipe_2[0]
        else:
            joueur_2_pokemon_jouer = equipe_2[1]
        return joueur_2_pokemon_jouer

def attaque_pokemon(liste_tt_pokemon, tours, joueur_1_pokemon_jouer, joueur_2_pokemon_jouer,equipe_1_P1_atq, equipe_1_P2_atq,equipe_2_P1_atq, equipe_2_P2_atq):
    print("c'est l'heure d'attaquer !")
    if tours / 2 == type(float):    
        choix = input(f"t'attaque qui ? : 0 = {equipe_1[0].nom} ou 1 = {equipe_1[1].nom} ? : ")
        pokemon_attaquer = equipe_1[choix]
        choix2 = input(f"t'attaque qui ? : 0 = {equipe_2[0].nom} ou 1 = {equipe_2[1].nom} ? : ")
        pokemon_attaquer = equipe_2[choix]
        attaque = input(f"tu veux utiliser quel attaque joueur 1 ? 0 = {equipe_1_P1_atq}")
    else:
        choix = input(f"t'attaque qui ? : 0 = {equipe_2[0].nom} ou 1 = {equipe_2[1].nom} ? : ")
        pokemon_attaquer = equipe_2[choix]
        choix = input(f"t'attaque qui ? : 0 = {equipe_1[0].nom} ou 1 = {equipe_1[1].nom} ? : ")
        pokemon_attaquer = equipe_1[choix]
        
    
    
    
    
        


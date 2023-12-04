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
justepourlamiseenforme = []
justepourlamiseenforme.append(equipe_1)
justepourlamiseenforme.append(equipe_2)
print("équipe 1 : ")
print(f"le pokemon 1 de l'equipe 1 est : {equipe_1[0].nom}")
print(f"le pokemon 2 de l'equipe 1 est : {equipe_1[1].nom}")
print("équipe 2 : ")
print(f"le pokemon 1 de l'equipe 2 est : {equipe_2[0].nom}")
print(f"le pokemon 2 de l'equipe 2 est : {equipe_2[1].nom}")
#on définit la vitesse des pokemons
liste_vitesse_pok = []
liste_vitesse_pok.append(equipe_1[0].vitesse)
liste_vitesse_pok.append(equipe_1[1].vitesse)
liste_vitesse_pok.append(equipe_2[0].vitesse)
liste_vitesse_pok.append(equipe_2[1].vitesse)
print("")

pokemon_jouer = [
    equipe_1[0].nom,
    equipe_2[0].nom
]

print("")

for i, pokemon in enumerate(pokemon_jouer, 0):
    print(f"le pokemon de l'equipe {i+1} jouée est {pokemon}")
print("")

for pokemon in enumerate(justepourlamiseenforme):
    print(f"la vitesse du pokemon")



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

def choix(vitesse, pokemon, equipe2):
    pass

def attaques(pokemon, pokemons_adverse):
    if pokemon.vitesse > pokemons_adverse.vitesse:
        for i, pok in enumerate(1, pokemons_adverse):
            print(f"{i+1}. {pok}")
    else:
        pass
def utiliser_objet():
    alea = rd.randint(1,3)
    objet.soins = alea
    objet.anti_poison = alea
    objet.bonus_atq = alea
    objet.bonus_dfs = alea
    objet.malus_atq = alea
    objet.malus_dfs = alea

class Action:
    def __init__(self):
        self.priorité = "de 1 (pas prioritaire) a 4 (très prioritaire)"
        self.type = "attaque, change, objet, fuite"

def phase_choix( pokemon_actifs """Faut les nommer""" , tour):
    action = Action()
    action_choix = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
    if action_choix == 1:
        action.type = "attaque"
        action.priorité = 1
        return action
    elif action == 2:
        action.type = "changer"
        action.priorité = 4
        change_poke = input(f"pokemon voulez-vous déployer ? 1: {equipe_1[0].nom} ou 2: {equipe_1[1]}" )
        pokemon_actif = # l'autre mon
        return action_choisi
    elif action == 3:
        action.type = "objet"
        action.priorité = 3
        return action
    elif action == 4:
        action.type = "fuite"
        action.priorité = 2

def phase_action(""" les poke actifs """, action_choisi):
    if action.priorité == 4
        a = rd.randint(1,5)
        if a == 1:
            print("Bravo ! Vous avez fuit avec succès et avez perdu le combat par votre lacheté !")
            break
        else:
            print("Haha, la fuite n'est pas une option, Looser")
    elif action.priorité == 3
    elif action.priorité == 2
    elif action.priorité == 1

def phase_action(""" les poke actifs """, action_choisi):
    if tata==tata:
        pass
    else:
        pass


class Dodo()
  def __init__(self):
    self.fatigué = {self.dodo}

def fatiguer(self, cible):
        if self.fatigue > 0:
            print(f"{self.nom} est fatigué et ne peut pas attaquer ce tour.Il vous reste ")
            self.reposer()




        
    
    
    
    
        


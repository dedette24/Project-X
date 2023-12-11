import random as rd
import time
from classe import *
print("\n")

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
    print(f"le pokemon 1 de l'equipe 1 est : {equipe_1[0].nom} et il a {equipe_1[0].vie} pv")
    print(f"le pokemon 2 de l'equipe 1 est : {equipe_1[1].nom} et il a {equipe_1[1].vie} pv")
    print("équipe 2 : ")
    print(f"le pokemon 1 de l'equipe 2 est : {equipe_2[0].nom} et il a {equipe_2[0].vie} pv")
    print(f"le pokemon 2 de l'equipe 2 est : {equipe_2[1].nom} et il a {equipe_2[1].vie} pv")
    #on définit la vitesse des pokemons
    print("")
    print(f"la vitesse de {equipe_1[0].nom} est de : {equipe_1[0].vitesse}")
    print(f"la vitesse de {equipe_1[1].nom} est de : {equipe_1[1].vitesse}")
    print(f"la vitesse de {equipe_2[0].nom} est de : {equipe_2[0].vitesse}")
    print(f"la vitesse de {equipe_2[1].nom} est de : {equipe_2[1].vitesse}")
    print("")
    return equipe_1, equipe_2

info(equipe_1, equipe_2)

def choisir_pokemon(equipe):
    print(f"\nChoisissez un Pokémon a jouer parmi les suivants: ")
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

Pokemon_actif = []

def choix_attaques(pokemon):
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

liste_tt_attaques = []

atq_pok_e1_p1 = choix_attaques(equipe_1[0])
atq_pok_e1_p2 = choix_attaques(equipe_1[1])
atq_pok_e2_p1 = choix_attaques(equipe_2[0])
atq_pok_e2_p2 = choix_attaques(equipe_2[1])
liste_tt_attaques.append(atq_pok_e1_p1)
liste_tt_attaques.append(atq_pok_e1_p2)
liste_tt_attaques.append(atq_pok_e2_p1)
liste_tt_attaques.append(atq_pok_e2_p2)
print(f"{equipe_1[0].name} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e1_p1]}")
print(f"{equipe_1[1].name} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e1_p2]}")
print(f"{equipe_2[0].name} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e2_p1]}")
print(f"{equipe_2[1].name} a les attaques suivantes : {[attaque.name for attaque in atq_pok_e2_p2]}")

print(liste_tt_attaques)
def attaques_utilise(pokemon, attack):
        # Afficher les attaques disponibles pour le Pokémon
    print(f"\n{pokemon.name} a les attaques suivantes : {[attack.name for attaque in pokemon.attaque]}")

    # Sélection de l'attaque
    while True:
        try:
            choix_attaque = int(input(f"Choisissez l'attaque (1-{len(pokemon.attaque)}): "))
            if 1 <= choix_attaque <= len(pokemon.attaque):
                break
            else:
                print("Choix invalide. Veuillez choisir parmi les attaques disponibles.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    attaque_utilisee = pokemon.attaque[choix_attaque - 1]
    print(f"{pokemon} utilise l'attaque : {attaque_utilisee}")
    return attaque_utilisee

def attaque_cible(equipe):
    # Sélection de la cible
    print("\nChoisissez la cible pour l'attaque:")
    for i, adversaire in enumerate(equipe, 1):
        print(f"{i}. {adversaire.name} (PV: {adversaire.vie})")

    while True:
        try:
            choix_cible = int(input("Entrez le numéro de la cible : "))
            if 1 <= choix_cible <= len(equipe):
                break
            else:
                print("Choix invalide. Veuillez choisir parmi les Pokémon adverses.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

    cible_attaquee = equipe[choix_cible - 1]
    return cible_attaquee
    
def attaques(pokemon, pokemons_adverse):
    if pokemon.vitesse > pokemons_adverse.vitesse:
        for i, pok in enumerate(1, pokemons_adverse):
            print(f"{i+1}. {pok}")
    else:
        pass

poke1_actif = choisir_pokemon(equipe_1)
poke2_actif = choisir_pokemon(equipe_2)
Pokemon_actif.append(poke1_actif)
Pokemon_actif.append(poke2_actif)
for i, pokemon in enumerate(Pokemon_actif, 1):
            print(f"équipe {i} joue : {pokemon.name}")
    
class Action:
    def __init__(self):
        self.priorité = "de 1 (pas prioritaire) a 4 (très prioritaire)"
        self.type = "attaque, changer, objet, fuite"

# Phase de choix
#Joueur 1
action = Action()
action_choix = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
if action_choix == 1:
    action.priorité = 1
    action.type = "attaque"
elif action_choix == 2:
    action.priorité = 4
    action.type = "changer"
elif action_choix == 3:
    action.priorité = 3
    action.type = "objet"    
elif action_choix == 4:
    action.priorité = 2
    action.type = "fuite"

#Joueur 2
action2 = Action()
action_choix_2 = int(input("que voulez-vous faire ? 1: Attaquer, 2: Changer de poopkemon, 3: Utiliser un objet, 4:Fuire"))
if action_choix_2 == 1:
    action2.priorité = 1
    action.type = "attaque"
elif action_choix_2 == 2:
    action2.priorité = 4
    action.type = "changer"
elif action_choix_2 == 3:
    action2.priorité = 3
    action.type = "objet"
elif action_choix_2 == 4:
    action2.priorité = 2
    action.type = "fuite"

#Phase d'action
def phase_action(action_priorité):
    if action_priorité == 4:
        change_poke = int(input(f"Quel pokemon voulez-vous déployer ? 1: {equipe_1[0].name}, ou 2: {equipe_1[1].name}" ))
        pokemon_actif = equipe_1[change_poke - 1]
    elif action_priorité == 3:
        objet = input(f"Quel objet souhaitez vous utiliser ? 1:")
        """utiliser_objet(objet)"""
    elif action_priorité == 2:
        a = rd.randint(1,5)
        if a == 1:
            print("Bravo ! Vous avez fuit avec succès et avez perdu le combat par votre lacheté !")
            surrender = True
            return surrender
        else:
            print("Haha, la fuite n'est pas une option, Looser")
    elif action_priorité == 1:
        """attaquer()"""

if action.priorité > action2.priorité:
    phase_action(action.priorité)
    phase_action(action2.priorité)
elif action2.priorité > action.priorité:
    phase_action(action2.priorité)
    phase_action(action.priorité)
elif action.priorité == action2.priorité:
    if action.type == "attaque":
        """attaque()"""


class Altération_statut:
  def __init__(self):
    self.fatigué = "" 
    self.dodo = ""
    self.jet_caca = ""

#Objet soin

class Objets:
    def __init__(self):
        self.soins = alea
        self.anti_poison = alea
        self.bonus_atq = alea
        self.bonus_dfs = alea
        self.malus_atq = alea        #Malus d'atq consiste si le pokémon frappe le pokémon ,ça renvoie son coup précedent .
        self.malus_dfs = alea

ultra_soin = Objets()
ultra_soin.soins = 100

soins = Objets()
soins.soins = 50

anti_poison = Objets()
anti_poison.poison = 10                #attaque de poison sur le poopkemon , protéger le pokemon grâce à une anti_poison , qui le sauve de 10% se sa vie 

bonus_atq = Objets()
bonus_atq.attaque = 10*3

bonus_dfs = Objets() 
bonus_dfs.defense = +5

malus_atq = Objets()
malus_atq.attaque = -6

malus_dfs = Objets()
malus_dfs.defense = -8       #si le poopkemon défend l'attq de son adversaire il a des chances d'avoir un malus de dfs


def utiliser_objet(objets, pokemon):
    pokemon.vie += objets.soin
    pokemon.atq += objets.attaque          #Ou sinn les dégâts
    pokemon.dfs += objets.defense
    pokemon.statut += Objets.anti_poison
    


        
    
    
    
    
        


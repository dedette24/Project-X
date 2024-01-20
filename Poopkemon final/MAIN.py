import random as rd
import time
from classe import *
from colorama import Fore, Style
print("\n")

action = [0, 0]
liste_tt_attaques = []
Pokemon_actif = []

equipe_1 = liste_pokemon[:2]
equipe_2 = liste_pokemon[-2:]

def info(equipe_1, equipe_2):
    print("--------------")
    print("\néquipe 1 : ")
    print(f"le pokemon 1 de l'equipe 1 est : {Fore.YELLOW}{equipe_1[0].name}{Fore.RESET}, il a {Fore.RED}{equipe_1[0].vie}{Fore.RESET} pv et les dernieres states : atq : {Fore.RED}{equipe_1[0].atq}{Fore.RESET} | dfs : {Fore.RED}{equipe_1[0].dfs}{Fore.RESET}")
    print(f"le pokemon 2 de l'equipe 1 est : {Fore.YELLOW}{equipe_1[1].name}{Fore.RESET}, il a {Fore.RED}{equipe_1[1].vie}{Fore.RESET} pv et les dernieres states : atq : {Fore.RED}{equipe_1[1].atq}{Fore.RESET} | dfs : {Fore.RED}{equipe_1[1].dfs}{Fore.RESET}")
    print("\néquipe 2 : ")
    print(f"le pokemon 1 de l'equipe 2 est : {Fore.YELLOW}{equipe_2[0].name}{Fore.RESET}, il a {Fore.RED}{equipe_2[0].vie}{Fore.RESET} pv et les dernieres states : atq : {Fore.RED}{equipe_2[0].atq}{Fore.RESET} | dfs : {Fore.RED}{equipe_2[0].dfs}{Fore.RESET}")
    print(f"le pokemon 2 de l'equipe 2 est : {Fore.YELLOW}{equipe_2[1].name}{Fore.RESET}, il a {Fore.RED}{equipe_2[1].vie}{Fore.RESET} pv et les dernieres states : atq : {Fore.RED}{equipe_2[1].atq}{Fore.RESET} | dfs : {Fore.RED}{equipe_2[1].dfs}{Fore.RESET}")
    #on définit la vitesse des pokemons
    print(f"\nla vitesse de {Fore.LIGHTMAGENTA_EX}{equipe_1[0].name}{Fore.RESET} est de : {Fore.BLUE}{equipe_1[0].vitesse}{Fore.RESET} et il est de type {Fore.LIGHTGREEN_EX}{equipe_1[0].type}{Fore.RESET}")
    print(f"la vitesse de {Fore.LIGHTMAGENTA_EX}{equipe_1[1].name}{Fore.RESET} est de : {Fore.BLUE}{equipe_1[1].vitesse}{Fore.RESET} et il est de type {Fore.LIGHTGREEN_EX}{equipe_1[1].type}{Fore.RESET}")
    print(f"la vitesse de {Fore.LIGHTMAGENTA_EX}{equipe_2[0].name}{Fore.RESET} est de : {Fore.BLUE}{equipe_2[0].vitesse}{Fore.RESET} et il est de type {Fore.LIGHTGREEN_EX}{equipe_2[0].type}{Fore.RESET}")
    print(f"la vitesse de {Fore.LIGHTMAGENTA_EX}{equipe_2[1].name}{Fore.RESET} est de : {Fore.BLUE}{equipe_2[1].vitesse}{Fore.RESET} et il est de type {Fore.LIGHTGREEN_EX}{equipe_2[1].type}{Fore.RESET}")
    print("")
    return equipe_1, equipe_2

#qui attaquer
def choix_attaques_DEBUT(pokemon, attaques_disponibles):
    print("\n ----------------------")
    vrai_attaque_dispo = random.sample(attaques_disponibles, min(6, len(attaques_disponibles)))
    attaques_selectionnees = []

    print(f"Choisissez 3 attaques pour {pokemon.name} parmi les attaques suivantes : ")
    if attaque.type == pokemon.type:
        attaque.power = attaque.power * 1.5
    while len(attaques_selectionnees) < 3:
        for i, attaque in enumerate(vrai_attaque_dispo, 1):
            print(f"{i}. {attaque.name} (Puissance: {Fore.RED}{attaque.power}{Fore.RESET}, utiisations: {attaque.pp}, type : {Fore.LIGHTGREEN_EX}{attaque.type}{Fore.RESET})")

        while True:
            try:
                choix = int(input(f"Choisissez l'attaque {len(attaques_selectionnees) + 1}: "))
                break  # Sort de la boucle si la conversion en int réussit
            except ValueError:
                print(f"{Fore.RED}Veuillez entrer un nombre entier.{Fore.RESET}")

        if 1 <= choix <= len(vrai_attaque_dispo):
            attaque_selectionnee = vrai_attaque_dispo.pop(choix - 1)

            # Vérification si l'attaque n'a pas déjà été sélectionnée
            if attaque_selectionnee not in attaques_selectionnees:
                attaques_selectionnees.append(attaque_selectionnee)
                print(f"{attaque_selectionnee.name} a été sélectionnée.")
            else:
                print("Vous avez déjà choisi cette attaque. Veuillez choisir une autre attaque.")
        else:
            print(f"{Fore.RED}Choix invalide. Veuillez choisir parmi les attaques disponibles.{Fore.RESET}")

    print("\n")
    return attaques_selectionnees

#print(equipe_1[0].pouvoir[0].name) --> ce qui faut faire pour afficher attaque
#qui jouer
def choisir_pokemon(equipe, num):
    print("\n ----------------------")
    print(f"\nChoisissez un Pokémon à jouer parmi les suivants de l'équipe {num}: ")
    for i, pokemon in enumerate(equipe, 1):
        print(f"{i}. {pokemon.name} (PV: {pokemon.vie})")

    while True:
        try:
            choix_pokemon = int(input("Entrez le numéro du Pokémon que vous souhaitez jouer : "))
            
            if 1 <= choix_pokemon <= len(equipe):
                if equipe[choix_pokemon-1].vie < 1:
                    print(f"{Fore.RED}Vous ne pouvez plus utiliser ce Pokémon, il est KO.{Fore.RESET}")
                else:
                    break
            else:
                print(f"{Fore.RED}Choix invalide. Veuillez choisir parmi les Pokémon disponibles.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Veuillez entrer un nombre entier.{Fore.RESET}")
    print(f"vous avez décidez de jouer {Fore.RED}{equipe[choix_pokemon - 1].name} {Fore.RESET}!")
    #actif[num-1] = equipe[choix_pokemon - 1]
    return equipe[choix_pokemon - 1]

def choix_action(num, liste, equipe_1, equipe_2):
    print("\n ----------------------")
    print(f"\nVous allez maintenant choisir l'action que vous voulez faire !")
    print(f"1. attaquer")
    print(f"2. changer de poopkemon")
    print(f"3. utiliser un objet")
    print(f"4. abandonner")
    print(f"5. Consulter information des pokemons (ne compte pas comme une vrai action)")
    while True:
        try:
            action = int(input(f"\nChoisie l'action que vous voulez faire equipe {num} en rentrant le numero de l'action : "))
            if 1 <= action <= 5:
                if action == 5:
                    info(equipe_1, equipe_2)
                else:
                    break
            else:
                print(f"{Fore.RED}Choix invalide. Veuillez choisir parmi les actions disponibles.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Veuillez entrer un nombre entier.{Fore.RESET}")
    liste[num-1] = action
    return(liste)

#CA MARCHE !

#------------------------------------------------------------------------
#a faire : attaque, objet
#fait : choix attaque

#choix_attaque : 

#print(equipe_1[0].pouvoir[0].name) --> ce qui faut faire pour afficher attaque

choix_attaque_moment = [0, 0]

def choix_attaque(pokemon, num, liste, equipe_1, equipe_2):
    if num - 1 == 1:
        equipe = equipe_2
    elif num - 1 == 0:
        equipe = equipe_1
    print("\n ----------------------")
    # Afficher les attaques disponibles pour le Pokémon
    if pokemon[num-1].alive == False:
        print(f"{Fore.RED}Votre pokemon s'est fait tué avant de pouvoir attaquer. Il retourne dans sa Poopkeball et c'est l'autre Pokémon restant qui rentre en jeu ! {Fore.RESET}")
        if equipe[0].alive == False:
            chang = 0
        elif equipe[1].alive == False:
            chang = 1
        pokemon[num-1] = [equipe[chang]]
        print(f"{Fore.RED}Vous jouez maintenant {pokemon[num-1].name} ! {Fore.RESET}")
        cbon = 0
        pass
    else:
        print(f"\n{pokemon[num-1].name} a les attaques suivantes : ")
        for i in range(3):
            print(f"attaque {i+1} : {pokemon[num-1].pouvoir[i].name} ({pokemon[num-1].pouvoir[i].pp} utilisation restantes) {Fore.RED}(dégats de base : {pokemon[num-1].pouvoir[i].power}) {Fore.RESET} {Fore.LIGHTGREEN_EX}(type : {pokemon[num-1].pouvoir[i].type}) {Fore.RESET}")

        while True:
            try:
                action = int(input(f"Choisissez l'une des attaques ci-dessous que vous voulez utiliser avec l'équipe {num} : "))
                
                if 1 <= action <= 3:
                    if pokemon[num-1].pouvoir[action-1].pp < 1: 
                        print(f"{Fore.RED}Vous n'avez plus assez d'utilisation pour cette attaque.{Fore.RESET}")
                    else:
                        break
                else:
                    print(f"{Fore.RED}Choix invalide. Veuillez choisir parmi les attaques disponibles.{Fore.RESET}")
            except ValueError:
                print(f"{Fore.RED}Veuillez entrer un nombre entier.{Fore.RESET}")
        cbon = pokemon[num-1].pouvoir[action-1]
        liste[num-1] = cbon
    return liste

rec = [0,0]

def efficace_raccour(num, actif, liste, B, N, O, rec):
    print("\n ----------------------")
    if num == 1:
        adv = 1
    else:
        adv = 0

    potions = int(rec[num-1])
    if rec[num-1] == 0:
        pass
    else:
        print(f"{Fore.CYAN}Vous allez faire {potions} dégats en plus grâce a la potion que vous avez bu précédement!{Fore.RESET}")
    rec[num-1] = 0
    if actif[adv].type in B:
        degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5)) * 2  #super efficace
        #if liste[num-1].categorie == atq:
            #degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5)) * 2
        #elif liste[num-1].categorie == atq_spe:
            #degats_infligés = ((liste[num-1].power + actif[num - 1].atq_spe) - (actif[adv].def_spe * 1.5)) * 2
        #else:
        
        actif[adv].vie -= degats_infligés
        print(f"{Fore.GREEN}c'est super efficace{Fore.RESET} !")
        return degats_infligés
    elif actif[adv].type in N:
        degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5)) / 1.5  # Pas très efficace
        actif[adv].vie -= degats_infligés
        print(f"{Fore.YELLOW}c'est pas tres éfficace{Fore.RESET} !")
        return degats_infligés
    elif actif[adv].type in O:    #Inefficace
        degats_infligés = 0
        print(f"{Fore.RED}Vous ne faites pas de degat !{Fore.RESET}")
        return degats_infligés
    else:
        print("l'attaque va se derouler normalement ! ")
        degats_infligés = ((liste[num-1].power + actif[num - 1].atq) - (actif[adv].dfs * 1.5))    #Normal
        actif[adv].vie -= degats_infligés
        return degats_infligés + potions

def efficace(num, actif, liste, rec, attaque):
    degats_infligés = 0
    if num == 1:
        adv = 1
    else:
        adv = 0

    if attaque[num-1].type == "feu": #feu
        liste_effi = ["glace", "plante", "acier", "insecte"] #T
        liste_nul = ["feu", "eau", "dragon", "lumiere"] #N
        liste_0 = ["roche"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)
        
    if attaque[num-1].type == "glace": #glace
        liste_effi = ["glace", "plante", "caca", "roche", "dragon", "poison", "vol"] #T
        liste_nul = ["feu", "insecte"] #N
        liste_0 = ["eau"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "eau": #eau
        liste_effi = ["feu", "caca", "roche"] #T
        liste_nul = ["eau", "dragon"] #N
        liste_0 = [] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)
            
    if attaque[num-1].type == "plante": #plante
        liste_effi = ["eau", "roche"] #T
        liste_nul = ["feu", "glace","plante","acier","dragon", "poison", "insecte"] #N
        liste_0 = ["caca"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "caca": #caca
        liste_effi = ["feu", "plante", "ombre", "fee", "acier", "dragon", "combat", "lumiere", "psy"] #T
        liste_nul = ["caca", "poison", "roche"] #N
        liste_0 = ["glace", "eau"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "ombre": #ombre
        liste_effi = ["spectre", "psy"] #T
        liste_nul = ['ombre', 'dragon', 'combat'] #N
        liste_0 = ["fee"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)
            
    if attaque[num-1].type == "fee": #fee
        liste_effi = ["caca", "ombre", "dragon", "combat", "lumiere", "psy"] #T
        liste_nul = ['feu', 'fee', 'acier', "poison"] #N
        liste_0 = [] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "electrique": #electrique
        liste_effi = ["eau", "acier", "vol"] #T
        liste_nul = ['plante', 'electrique', 'dragon'] #N
        liste_0 = ["roche"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "acier": #acier
        liste_effi = ["glace", "caca", "fee", "roche", "dragon", "poison"] #T
        liste_nul = ["feu", "plante", "acier", "insecte"] #N
        liste_0 = [] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "roche": #roche
        liste_effi = ["feu", "glace", "electrique", "acier", "roche", "poison"] #T
        liste_nul = ['eau', 'insecte', 'dragon'] #N
        liste_0 = ["vol"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)
    
    if attaque[num-1].type == "dragon": #dragon
        liste_effi = ["dragon", "psy"] #T
        liste_nul = [] #N
        liste_0 = [] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "poison": #poison
        liste_effi = ["plante", "fee", "acier", "dragon", "poison", "combat"] #T
        liste_nul = ["roche", "psy"] #N
        liste_0 = [] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "vol": #vol
        liste_effi = ["plante", "combat", "insecte"] #T
        liste_nul = ["electrique", "acier", "roche", "dragon", "vol"] #N
        liste_0 = [] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)
    
    if attaque[num-1].type == "combat": #combat
        liste_effi = ["glace", "fee", "acier", "roche", "insecte"] #T
        liste_nul = ["eau", "caca", "dragon", "psy"] #N
        liste_0 = ["ombre", "vol", "spectre"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "insecte": #insecte
        liste_effi = ["plante", "caca", "ombre", "fee", "psy"] #T
        liste_nul = ["feu", "dragon", "insecte"] #N
        liste_0 = ["vol"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "spectre": #spectre
        liste_effi = ["dragon", "psy", "fee", "spectre"] #T
        liste_nul = [] #N
        liste_0 = ["ombre", "lumiere"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "lumiere": #lumiere
        liste_effi = ["dragon", "caca", "ombre", "vol", "combat", "spectre"] #T
        liste_nul = ["feu", "fee", "acier", "lumiere"] #N
        liste_0 = ["plante"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    if attaque[num-1].type == "psy": #psy
        liste_effi = ["poison", "combat"] #T
        liste_nul = ["caca", "acier", "dragon", "insecte", "spectre", "psy"] #N
        liste_0 = ["ombre"] #X
        degats_infligés = efficace_raccour(num, actif, liste, liste_effi, liste_nul, liste_0, rec)

    return degats_infligés

def attaque_boucle(num, actif, liste, rec, equipe_1, equipe_2):
    print("\n ----------------------")
    if num == 1:
        adv = 1
    else: 
        adv = 0 
    if actif[num-1].vie < 1:
        print(f"Vous n'avez pas eu le temps d'attaquer, c'est dommage")
    else:
        print(f"C'est votre tour d'attaquer, equipe {num} ! Le pokemon que vous attaquez est {Fore.RED}{actif[adv].name}{Fore.RESET} et il est de type {Fore.LIGHTGREEN_EX}{actif[adv].type}{Fore.RESET}")
        trans = choix_attaque(actif, num, liste, equipe_1, equipe_2)
        print(f"Vous utilisez l'attaque {trans[num-1].name}")
        degat = int(efficace(num, actif, trans, rec, liste))
        print(f"Vous infliger {degat} dégats à {actif[adv].name}")
        trans[num-1].pp -= 1
        print(f"il vous reste {trans[num-1].pp} utilisation restantes pour l'attaque {trans[num-1].name}")
        if actif[adv].vie < 1:
            actif[adv].alive = False
            print(f"{Fore.RED}Vous avez eliminé {actif[adv].name}, l'adversaire ne pourra plus l'utiliser à moins d'utiliser une potion de heal.{Fore.RESET}")
            print(f"{Fore.RED}{actif[adv].name} n'est maintenant plus en capacité de combattre{Fore.RESET}")
            actif[adv].vie = 0
        else:
            print(f"il reste {actif[adv].vie} vie à {actif[adv].name}")


#P1 = 1.0 / P2 = 2.0
#si def alors 1, si attaque alors 2

def utiliser_objet(num, actif, liste, rec):
    print("\n ----------------------")
    print("\n")
    if num == 1:
        potions_disponibles = liste[:2] 
        liste[0].owner = 1
        liste[1].owner = 1
    else:
        potions_disponibles = liste[-2:]
        liste[2].owner = 2
        liste[3].owner = 2
    
    print(f"Voici les potions que vous avez à votre disposition, équipe {num}: ")
    for i, potion in enumerate(potions_disponibles, 1):
        print(f"{i}. {potion.name} (utilisation restantes : {potion.pp}, Points: {potion.point}, Type : {potion.type})")
    print(f"\n{Fore.RED}Les potions de type 'Attaque' seront utiliser au prochain tour si elles sont selectionner !{Fore.RESET}")
    while True:
        try:
            choix_potion = int(input("Entrez le numéro de la potion que vous souhaitez utiliser : "))
            if 1 <= choix_potion <= len(potions_disponibles):
                if potions_disponibles[choix_potion - 1].pp > 0:  # Vérifier si la potion n'a pas déjà été utilisée
                    break
                else:
                    print(f"{Fore.RED}Vous avez déjà utilisé cette potion.{Fore.RESET}")
            else:
                print(f"{Fore.RED}Choix invalide. Veuillez choisir parmi les potions disponibles.{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED}Veuillez entrer un nombre entier.{Fore.RESET}")
    potion_choisie = potions_disponibles[choix_potion - 1]

    if potion_choisie.type == "heal":
        actif[num - 1].vie += potion_choisie.point
        print(f"Le pokemon {actif[num - 1].name} a gagné {potion_choisie.point} points de vie !")
        print(f"il passe maintenant a {actif[num - 1].vie} points de vie !")
    elif potion_choisie.type == "def":
        actif[num-1].dfs += potion_choisie.point
        print(f"{potion_choisie.point} points de défense ont été rajouter au votre defense actuel ! Elle est maintenant de {actif[num-1].dfs}")
    elif potion_choisie.type == "attaque":
        rec[num - 1] = potion_choisie.point
        print(f"Votre prochaine attaque fera {potion_choisie.point} de dégâts en plus !")
        print(f"{Fore.RED} ATTENTION !!! LA POTION SERA UTILISER AU PROCHAIN TOUR. SI VOUS LA BUVEZ MAINTENANT, ET QUE VOUS N'ATTAQUER PAS, ELLE SERA GACHER ! {Fore.RESET}")
    potion_choisie.pp = 0
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

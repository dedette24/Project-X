import random as rd
#import key as kb
from time import sleep
from classe import *
from MAIN import *
from colorama import Fore, Style

recurrence = [0, 0]

print(Fore.YELLOW + "Bienvenue dans Poopkemon, une réadaptation du jeu Pokemon version Python non graphique (donc forcément moins bien) \U0001f643 ! "+ Fore.RESET)
time.sleep(3)
print(Fore.RED + "PENDANT TOUUUUT LE DEROULER DE LA PARTIE, MERCI DE NE PAS APPUYER TROP RAPIDEMENT SUR LES TOUCHES ET D'ATTENDRE QUE LA QUESTIONS VIENNE A VOUS. merci ! "+ Fore.RESET)
time.sleep(3.5)
print("\nLa partie va maintenant commencé !")
time.sleep(1.5)
print("\nVoici les informations de chaques équipes.")
info(equipe_1, equipe_2)
#print("Dès que vous avez fini de consulté les informations de vos pokemons, vous pouvez appuyer sur 'espace'. ")
#kb.wait('space') ne marche qu'une fois sur 3, probleme avec terminal (si on veut utliser faut faire dans le vrai vs code)
print("__________________________________________________________")
round = 0
#établir les choses avant que ca commence
print("\nVous allez maintenant choisir les pouvoirs de vos pokemons parmis 6 choix possibles aléatoire : ")
time.sleep(3)
equipe_1[0].pouvoir = choix_attaques_DEBUT(equipe_1[0], attaques)
equipe_1[1].pouvoir = choix_attaques_DEBUT(equipe_1[1], attaques)
equipe_2[0].pouvoir = choix_attaques_DEBUT(equipe_2[0], attaques)
equipe_2[1].pouvoir = choix_attaques_DEBUT(equipe_2[1], attaques)
print("\nEt maintenant vous allez choisir les premiers Pokemons que vous allez jouer : ")
time.sleep(3)
poke1_actif = choisir_pokemon(equipe_1, 1)
poke2_actif = choisir_pokemon(equipe_2, 2)
Pokemon_actif.append(poke1_actif)
Pokemon_actif.append(poke2_actif)
#on établie la base de la boucle
fin = False
abandon = False
print("")
for i, pokemon in enumerate(Pokemon_actif, 1):
            print(f"équipe {i} joue : {pokemon.name}")
print("\n La partie va maintenant pouvoir commencé !")
time.sleep(2)
while not fin:
    round += 1
    print(f"\n---------------------- Round {round} ----------------------")
    time.sleep(1.5)
    choix_action(1, action, equipe_1, equipe_2)
    choix_action(2, action, equipe_1, equipe_2)
    
    print("\n")
    if action == [4, 4]:
        print("Vous avez tout les 2 abandonnées au meme moment, pas tres malin...")
    elif 4 in action:
        if round > 4:
            coordonnee = action.index(4) + 1
            print(f"LE JOUEUR {coordonnee} A DECIDER D'ABANDONNER LA PARTIE")
            abandon = True
        else:
            print("tu ne peux qu'a partir du round 4 chef... fallait lire les conditions U0001F910 :( )")  
    else:
        pass
    if equipe_1[0].alive == False and equipe_1[1].alive == False or equipe_2[0].alive == False and equipe_2[1].vie == False or abandon == True:
        fin = True
        print("GG !")
        break
    
    if action == [3, 3]:
        utiliser_objet(1, Pokemon_actif, objets_aleatoires, recurrence)
        utiliser_objet(2, Pokemon_actif, objets_aleatoires, recurrence)
    elif 3 in action:
        coordonnee = action.index(3) + 1
        utiliser_objet(coordonnee, Pokemon_actif, objets_aleatoires, recurrence)
        if coordonnee == 1:
            action[1] = 0
        else:
            action[0] = 0
    else:
        pass
    
    if action == [2, 2]:
        choisir_pokemon(equipe_1, 1)
        choisir_pokemon(equipe_2, 2)
    elif action[1] == 2:
        choisir_pokemon(equipe_2, 2)
    elif action[0] == 2:
        choisir_pokemon(equipe_1, 1)
    else: 
        pass

    if action == [1, 1]:
        if Pokemon_actif[0].vitesse < Pokemon_actif[1].vitesse:
            print(f"{Fore.RED}le pokemon de l'équipe 2 est plus rapide ! il va donc commencer a attaquer.{Fore.RESET}")
            time.sleep(1.5)
            attaque_boucle(2, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
            time.sleep(1.5)
            attaque_boucle(1, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
            time.sleep(1.5)
        elif Pokemon_actif[0].vitesse == Pokemon_actif[1].vitesse:
            print(f"{Fore.MAGENTA}Comme votre vitesse est la meme, nous allons designer aléatoirement l'ordre de passage ! {Fore.RESET}")
            x = int(random.randint(1,2))
            time.sleep(1.5)
            print(f"{Fore.LIGHTMAGENTA_EX}Le dés est tombé sur le chiffre {x}, ce sera donc l'équipe {x} qui va commecer !{Fore.RESET}")
            if x == 1:
                print(f"{Fore.RED}le pokemon de l'équipe 1 va commencer a attaquer !{Fore.RESET}")
                time.sleep(1.5)
                attaque_boucle(1, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
                time.sleep(1.5)
                attaque_boucle(2, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
                
            else:
                print(f"{Fore.RED}le pokemon de l'équipe 2 va commencer a attaquer !{Fore.RESET}")
                time.sleep(1.5)
                attaque_boucle(2, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
                time.sleep(1.5)
                attaque_boucle(1, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
        else:
            print(f"{Fore.RED}le pokemon de l'équipe 1 va commencer a attaquer !{Fore.RESET}")
            time.sleep(1.5)
            attaque_boucle(1, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
            time.sleep(1.5)
            attaque_boucle(2, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
            time.sleep(1.5)
    elif 1 in action:
        coordonnee = action.index(1) + 1
        print(f"{Fore.RED}le pokemon de l'équipe {coordonnee} attaque !{Fore.RESET}")
        time.sleep(1.5)
        attaque_boucle(coordonnee, Pokemon_actif, choix_attaque_moment, recurrence, equipe_1, equipe_2)
        time.sleep(1.5)
    else:
        pass

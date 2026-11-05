"""
Programme de combat de monstres
Nom: Liam Deehy-Rivest
Groupe: 401
"""
import random

#compteurs
pv_hero = 20
tours = 0
monstres_evites = 0
monstres_vaincus = 0
defaites = 0

def show_rules():
   print("""Voici les règles, cher héros:
  1: Vous commencez avec 20 PV
  2: Le jeu se termine si vous perdez tous vos PV, ce qui est une défaite,
  ou en survivant les 7 tours du jeu
  3: Au début de chaque tour, vous avez 3 options;
     a) combattre un monstre; soit gagner et se soigner ou perdre et subir des dégâts. Vous avez une chance de vous
     faire guérir par Samantha!
     b) éviter un combat, mais automatiquement perdre 3 PV. Cette option ne fait pas avancer les tours
     c) avoir une liste des règles, soit celle que vous lisez en ce moment! Drôle de coïncidence! cette option
     ne fait pas avancer les tours
   """)

def show_player_stats():
   print(f"Vous avez désormais {pv_hero} points de vie et {tours} tours de joué!")


def final_player_stats():
   print(f""" Vous avez survécu {tours} tours et vous avez évité {monstres_evites} monstres.
  vous avez vaincu {monstres_vaincus} monstres et vous avez perdu {defaites} fois contre des monstres.""")


pit_of_monsters = ["une abeille abbateuse", "un vampire végétarien", "un ange pleureur", "un démorgorgon débile",
                  "un squelette skibiddy", "un prof de maths", "un escargot espagnol"]

show_rules()

while tours < 7 and pv_hero > 0:
   choix_joueur = input("Tu as 3 choix, cher soldat! Tu peux combattre, éviter ou revoir règles").lower().strip()
   if choix_joueur == "combattre":
       monstre_qui_pull_up = random.choice(pit_of_monsters)
       bless = random.choices([True, False], weights=[0.2, 0.8])[0]
       if bless:
           bless_amount = random.randint(2, 5)
           pv_hero = pv_hero + bless_amount
           print(f"Quelle chance! Samantha te bénit. Vous gagnez {bless_amount} points de vie!. ")
           show_player_stats()
       victoire = random.choices([True, False], weights=[0.4, 0.6])[0]
       if victoire:
           heal = random.randint(1, 3)
           pv_hero = pv_hero + heal
           monstres_vaincus += 1
           print(
               f"Ah non! {monstre_qui_pull_up} vous attaque! Heureusement, vous l'avez tué et vous avez gagné {heal} points de vie! ")
           tours += 1
           show_player_stats()

       else:
           damage = random.randint(3, 7)
           pv_hero = pv_hero - damage
           defaites += 1
           print(f"Ah non! {monstre_qui_pull_up} vous attaque!")
           if pv_hero > 0:
               print(f"Vous perdez le combat et ainsi vous perdez {damage} points de vie.")
               tours += 1
               show_player_stats()
           else:
               show_player_stats()

   elif choix_joueur == "éviter":
       damage = 3
       pv_hero = pv_hero - damage
       monstres_evites += 1
       print(f"Vous vous êtes échappé du monstre, mais celui-ci vous fait perdre {damage} points de vie!")
       show_player_stats()

   elif choix_joueur == "revoir règles":
       show_rules()

   else:
       print("Ah, il faut sélectionner une option!!")

#les messages de fin de jeu

if tours >= 7 and pv_hero > 0:
   print(f"VOUS AVEZ GAGNÉ!!! Bravo cher soldat!")
   final_player_stats()
elif pv_hero <= 0:
   print(
       f"""Vous avez été tué! womp womp!""")
   final_player_stats()


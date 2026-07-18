"""
Projet Tour de Hanoi - Version iterative avec affichage
"""

from hanoi_iterative import HanoiIterative
from visualisation import HanoiVisualisation
import time

def main():
    """Fonction principale du programme"""
    print("="*50)
    print("   TOUR DE HANOi - VERSION ITERATIVE")
    print("=*50")

    while True:
        try:
            n = int(input("\nEntrez le nombre de disques (1-8) : "))
            if 1 <= n <= 8:
                break
            else:
                print("Veuiller entrer un nombre entre 1 et 8.")

        except ValueError:
            print("Veuillez entrer un nombre valide.")

    #Initialisation
    hanoi = HanoiIterative(n)
    visual = HanoiVisualisation(n)


    #Affichage
    visual.afficher_etat(hanoi.tours)
    print("\nAppuyez sur Entree pour commencer la resolution...")
    input()
    
    #Resolution pas a pas
    print("\n" + "="*50)
    print("RESOLUTION INTERATIVE")
    print("="*50 + "\n")


    etapes = hanoi.resoudre()

    for i, (depart, arrivee) in enumerate(etapes, 1):
        #Afficher l'etape
        print(f"\nEtape {i}: Deplacer le disque de {depart} vers {arrivee}")
        

        hanoi.mouvement(depart, arrivee)

        #Afficher l etat
        visual.afficher_etat(hanoi.tours)

        #pause pour visualisation
        time.sleep(0.5)

    print("\n" + "="*50)
    print("RESOLUTION TERMINEE !")
    print("="*50)


    #verification
    if hanoi.verifier_solution():
        print("\n La solution est correcte !")
    else:
        print("\n Erreur dans la solution !")

if __name__ == "__main__":
    main()
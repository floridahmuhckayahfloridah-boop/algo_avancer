"""
Module de visualisation pour la Tour de Hanoï
"""

import os
import platform

class HanoiVisualisation:
    """Classe pour la visualisation de la Tour de Hanoï"""
    
    def __init__(self, n):
        """
        Initialise la visualisation
        
        Args:
            n (int): Nombre de disques
        """
        self.n = n
        self.largeur = n * 2 + 1
        self.hauteur = n + 1
        
    def effacer_ecran(self):
        """Efface l'écran de la console"""
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def afficher_etat(self, tours):
        """
        Affiche l'état actuel des tours
        
        Args:
            tours (dict): Dictionnaire contenant les tours
        """
        self.effacer_ecran()
        
        print("\n" + "="*50)
        print("   TOUR DE HANOÏ - ÉTAT ACTUEL")
        print("="*50 + "\n")
        
        # Hauteur maximale des tours
        max_hauteur = max(len(tour) for tour in tours.values())
        
        # Affichage du haut vers le bas
        for i in range(max_hauteur - 1, -1, -1):
            ligne = ""
            for tour in ['A', 'B', 'C']:
                if i < len(tours[tour]):
                    disque = tours[tour][i]
                    # Créer le disque avec des caractères
                    disque_str = "█" * (2 * disque - 1)
                    # Centrer le disque
                    espaces = self.n - disque
                    ligne += " " * espaces + disque_str + " " * espaces + "  "
                else:
                    # Tour vide
                    ligne += " " * (2 * self.n - 1) + "  "
            print(ligne)
        
        # Afficher les bases des tours
        print("=" * (6 * self.n + 4))
        print("  A" + " " * (2*self.n-1) + "  B" + " " * (2*self.n-1) + "  C")
        
        # Afficher des informations supplémentaires
        print("\n" + "-"*50)
        for tour in ['A', 'B', 'C']:
            nb_disques = len(tours[tour])
            if nb_disques > 0:
                plus_grand = tours[tour][-1]
                plus_petit = tours[tour][0]
                print(f"Tour {tour}: {nb_disques} disques (min={plus_petit}, max={plus_grand})")
            else:
                print(f"Tour {tour}: Vide")
        print("-"*50 + "\n")
    
    def afficher_legende(self):
        """Affiche la légende des symboles"""
        print("Légende:")
        print("█ : Disque")
        print("  : Espace vide")
        print("= : Base des tours")  
        print("\n")
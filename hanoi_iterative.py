"""
Implémentation itérative du jeu de la Tour de Hanoï
"""

class HanoiIterative:
    """Classe implémentant la version itérative de la Tour de Hanoï"""
    
    def __init__(self, n):       
        self.n = n
        self.tours = {
            'A': list(range(n, 0, -1)),  
            'B': [],
            'C': []
        }
        self.nom_tours = ['A', 'B', 'C']
        
    def est_valide(self, depart, arrivee):
      
        if not self.tours[depart]:  
            return False
        
        if not self.tours[arrivee]: 
            return True
                    
        return self.tours[depart][-1] < self.tours[arrivee][-1]
    
    def mouvement(self, depart, arrivee):
      
        if self.est_valide(depart, arrivee):
            disque = self.tours[depart].pop()
            self.tours[arrivee].append(disque)
            return True
        return False
    
    def resoudre(self):
        
        mouvements = []
        n = self.n
        
        total_mouvements = (1 << n) - 1
        
        if n % 2 == 0:
            sens = {'A': 'B', 'B': 'C', 'C': 'A'}
        else:
            sens = {'A': 'C', 'C': 'B', 'B': 'A'}
        
        tours = ['A', 'B', 'C']
        
        for i in range(1, total_mouvements + 1):
            if i % 2 == 1:
              
                for tour in tours:
                    if self.tours[tour] and self.tours[tour][-1] == 1:
                        depart = tour
                        arrivee = sens[depart]
                        break
            else:
                # Mouvement pair : déplacer un autre disque
                # Trouver les deux tours qui ne contiennent pas le disque 1
                tours_sans_1 = []
                for tour in tours:
                    if not (self.tours[tour] and self.tours[tour][-1] == 1):
                        tours_sans_1.append(tour)
                
                # Trouver le mouvement valide entre ces deux tours
                if self.est_valide(tours_sans_1[0], tours_sans_1[1]):
                    depart, arrivee = tours_sans_1[0], tours_sans_1[1]
                else:
                    depart, arrivee = tours_sans_1[1], tours_sans_1[0]
            
            mouvements.append((depart, arrivee))
            self.mouvement(depart, arrivee)
        
        # Réinitialiser les tours pour la démonstration
        self.__init__(self.n)
        
        return mouvements
    
    def verifier_solution(self):
        
        return len(self.tours['C']) == self.n
    
    def __str__(self):
        
        resultat = ""
        max_hauteur = max(len(tour) for tour in self.tours.values())
        
        for i in range(max_hauteur - 1, -1, -1):
            ligne = ""
            for tour in ['A', 'B', 'C']:
                if i < len(self.tours[tour]):
                    disque = self.tours[tour][i]
                    # Centrer l'affichage des disques
                    espaces = self.n - disque
                    ligne += " " * espaces + "█" * (2*disque) + " " * espaces + " "
                else:
                    ligne += " " * (2*self.n) + " "
            resultat += ligne + "\n"
        
        # Afficher les noms des tours
        resultat += " " * (self.n - 1) + "A" + " " * (self.n) + " "
        resultat += " " * (self.n - 1) + "B" + " " * (self.n) + " "
        resultat += " " * (self.n - 1) + "C" + "\n"
        
        return resultat
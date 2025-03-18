import csv
import numpy as np
import random
import tkinter as tk

NB_LIEUX = 5
LARGEUR = 800
HAUTEUR = 600
RAYON = 20


class Lieu:
    def __init__(self, x=None, y=None, nom=None):
        if (x is None):
            x = np.random.rand() * LARGEUR
        if (y is None):
            y = np.random.rand() * HAUTEUR
        self.x = float(x)
        self.y = float(y)
        self.nom = nom

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def calcul_distance(self, lieu2):
        return np.sqrt((lieu2.x - self.x) ** 2 + (lieu2.y - self.y) ** 2)

    def __repr__(self):
        return "(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + "," + str(self.nom) + ")"


class Route:

    def __init__(self, ordre=None, distance=None):
        if (ordre is None):
            # créer une route aléatoire
            self.ordre = [0]
            self.ordre.extend(random.sample(range(1, NB_LIEUX), NB_LIEUX - 1))
            self.ordre.append(0)
        else:
            if len(ordre) == NB_LIEUX + 1 and ordre[0] == ordre[len(ordre) - 1]:
                self.ordre = ordre[:]
            else:
                print("La route est incorrecte")
        self.distance = distance

    def get_ordre(self):
        return self.ordre

    def set_ordre(self, ordre):
        self.ordre = ordre

    def __eq__(self, autre_route):
        return self.ordre == autre_route.ordre

    def __neq__(self, autre_route):
        return self.ordre != autre_route.ordre

    def __lt__(self, autre_route):
        return self.distance < autre_route.distance

    def __gt__(self, autre_route):
        return self.distance > autre_route.distance

    def __le__(self, autre_route):
        return self.distance <= autre_route.distance

    def __ge__(self, autre_route):
        return self.distance >= autre_route.distance

    '''def __repr__(self):
        return "La route est " + str(self.ordre) + " et sa distance est de " + str(self.distance)'''


class Graph:

    def __init__(self, liste_lieux=None):
        if liste_lieux is None:
            self.liste_lieux = [Lieu() for i in range(NB_LIEUX)]
        else:
            self.liste_lieux = liste_lieux
        self.matrice_cout_od = self.calcul_matrice_cout_od()

    def get_liste_lieux(self):
        return self.liste_lieux

    def set_liste_lieux(self, liste_lieux):
        self.liste_lieux = liste_lieux

    def calcul_matrice_cout_od(self):
        matrice_od = []
        for i in range(NB_LIEUX):
            row = []
            for j in range(NB_LIEUX):
                row.append(self.liste_lieux[i].calcul_distance(self.liste_lieux[j]))
            matrice_od.append(row)
        return matrice_od

    def calcul_distance_route(self, ordre):
        lieu_actuel = self.liste_lieux[ordre[0]]
        somme_distance = 0
        for i in range(1, len(ordre)):
            somme_distance += Lieu.calcul_distance(self.liste_lieux[lieu_actuel.nom],
                                                   self.liste_lieux[ordre[i]])
            lieu_actuel = self.liste_lieux[ordre[i]]
        return somme_distance

    def plus_proche_voisin(self, lieu_depart, lieux_voisins):

        ligne = self.matrice_cout_od[lieu_depart.nom]
        indices_restants = [l.nom for l in lieux_voisins]

        # Filtrer la ligne pour ne garder que les colonnes des lieux restants
        ligne_filtree = [ligne[i] for i in indices_restants]
        min_value = {"dist": ligne_filtree[0], "name": None}
        for i, dist in enumerate(ligne_filtree):
            if i != lieu_depart:
                if dist < min_value['dist'] or min_value['dist'] == 0:
                    min_value["dist"], min_value['name'] = dist, lieux_voisins[i].nom

        if min_value['name'] is None and lieux_voisins:
            min_value['name'] = lieux_voisins[0].nom

        lieu_pp = next((lieu for lieu in lieux_voisins if lieu.nom == min_value["name"]), None)
        return lieu_pp


    def route_ppv(self, nom_lieu_depart) -> Route():
        lieu_actuel = self.liste_lieux[nom_lieu_depart]
        ordre = [nom_lieu_depart]
        lieux_restants = self.liste_lieux.copy()
        for lieu in lieux_restants:
            if lieu.nom == nom_lieu_depart:
                lieux_restants.remove(lieu)
        while lieux_restants:
            lieu_suivant = self.plus_proche_voisin(lieu_actuel, lieux_restants)
            ordre.append(lieu_suivant.nom)
            lieux_restants.remove(lieu_suivant)
            lieu_actuel = lieu_suivant
        ordre.append(nom_lieu_depart)
        print("La route est " + str(ordre) + " et sa distance est de " + str(self.calcul_distance_route(ordre)))
        return Route(ordre)
        
    '''def route_ppv(self, lieu_depart) -> Route():
        lieu_actuel = 0
        ordre = [lieu_depart]
        lieux_restants = list(range(0, NB_LIEUX))
        lieux_restants.remove(lieu_depart)
        while lieux_restants:
            lieu_suivant = self.plus_proche_voisin(lieu_actuel, lieux_restants)
            ordre.append(lieu_suivant)
            lieux_restants.remove(lieu_suivant)
            lieu_actuel = lieu_suivant
        ordre.append(lieu_depart.nom)
        return Route(ordre)'''

    def charger_graph(self, fichier_lieux):
        """Charge la liste des lieux à partir d'un fichier CSV."""
        self.liste_lieux = []  # Réinitialisation
        try:
            with open(fichier_lieux, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Ignorer l'en-tête si présent
                for i, row in enumerate(reader):
                    x, y = map(float, row)  # Convertir les coordonnées en flottants
                    self.liste_lieux.append(Lieu(x=x, y=y, nom=i))
            return self.liste_lieux
        except Exception as e:
            print(f"Erreur lors du chargement du fichier des lieux : {e}")

    def charger_matrice_od(self, fichier_matrice):
        """Charge la matrice de distances à partir d'un fichier CSV."""
        try:
            with open(fichier_matrice, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                self.matrice_od = np.array([list(map(float, row)) for row in reader])
        except Exception as e:
            print(f"Erreur lors du chargement de la matrice de distances : {e}")


'''class Affichage:
    def __init__(self, route):
        self.route = route  # La route est une liste de points (tuples)

        # Fenêtre tkinter
        self.root = tk.Tk()
        self.root.title("Groupe Audrey Maeva Kanelle")

        # Canvas pour dessiner
        self.canvas = tk.Canvas(self.root, width=LARGEUR, height=HAUTEUR, bg="white")
        self.canvas.pack()

        # Affichage des points et de la route
        self.afficher_points()
        self.afficher_route()

    def afficher_points(self):
        # Affiche chaque point de la route comme un cercle avec son numéro
        for i, (x, y) in enumerate(self.route):
            # Cercle pour le point
            self.canvas.create_oval(
                x - RAYON, y - RAYON,
                x + RAYON, y + RAYON,
                fill="lightblue", outline="black"
            )

            # Affiche le numéro du point
            self.canvas.create_text(x, y, text=str(i), fill="black")

    def afficher_route(self):
        # Trace les lignes entre les points de la route
        for i in range(len(self.route) - 1):
            x1, y1 = self.route[i]
            x2, y2 = self.route[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", dash=(5, 2))

        # Relie le dernier point au premier pour fermer la route
        x1, y1 = self.route[-1]
        x2, y2 = self.route[0]
        self.canvas.create_line(x1, y1, x2, y2, fill="blue", dash=(5, 2))

    def run(self):
        self.root.mainloop()'''

class Affichage(tk.Tk):
    def __init__(self, graph, route):
        super().__init__()
        self.graph = graph
        self.route = route
        self.route_points = self.change_route(route)  # La route est une liste de points (tuples)

        # Fenêtre tkinter
        self.root = tk.Tk()
        self.root.title("Groupe Audrey Maeva Kanelle")

        # appuyer sur la touche echap pour fermer le programme
        self.bind_all("<Escape>", self.fermer)
        # appuyer sur la touche M pour afficher la matrice de cout
        self.bind_all("<m>", self.afficher_matrice)
        # Forcer le focus sur la fenêtre principale
        self.focus_force()

        # Canvas pour dessiner
        self.canvas = tk.Canvas(self.root, width=LARGEUR, height=HAUTEUR, bg="white")
        self.canvas.pack()

        # Affichage des points et de la route
        self.afficher_route()
        self.afficher_points()

        # zone d'affichage de la matrice de cout
        self.label_matrice = tk.Label(self, text="", anchor="w")
        self.label_matrice.pack(pady=10)

        # zone d'affichage du nombre d'iteration et de la meilleur distance
        self.label_info = tk.Label(self, anchor="w", justify="left")
        self.label_info.pack(pady=10, fill="both", padx=10)

    def change_route(self, route):
        lieux_dict = {lieu.nom: (lieu.x, lieu.y, lieu.nom) for lieu in self.graph.liste_lieux}
        route_heuristique = [lieux_dict[num] for num in route.ordre]
        return route_heuristique

    def fermer(self, event=None):
        print("ESC press detected! Closing window.")  # Debug print
        self.destroy()

    def afficher_points(self):
        # Affiche chaque point de la route comme un cercle avec son numéro
        for i, (x, y, nom) in enumerate(self.route_points):
            if i == 0:
                # Cercle pour le point
                self.canvas.create_oval(
                    x - RAYON, y - RAYON,
                    x + RAYON, y + RAYON,
                    fill="red", outline="black"
                )
            else:
                # Cercle pour le point
                self.canvas.create_oval(
                    x - RAYON, y - RAYON,
                    x + RAYON, y + RAYON,
                    fill="lightgrey", outline="black"
                )

            # Affiche le numéro du point
            self.canvas.create_text(x, y, text=str(nom), fill="black")
            # Affiche l'ordre de passage du point
            self.canvas.create_text(x, y - 30, text=str(i), fill="black")

    def afficher_route(self):
        # Trace les lignes entre les points de la route
        for i in range(len(self.route_points) - 1):
            x1, y1 = self.route_points[i][0], self.route_points[i][1]
            x2, y2 = self.route_points[i + 1][0], self.route_points[i + 1][1],
            print(x1, x2, y1, y2)
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", dash=(5, 2))

        # Relie le dernier point au premier pour fermer la route
        x1, y1 = self.route_points[-1][0], self.route_points[-1][1]
        x2, y2 = self.route_points[0][0], self.route_points[0][1]
        self.canvas.create_line(x1, y1, x2, y2, fill="blue", dash=(5, 2))

    def afficher_matrice(self, event=None):
        # Convertir la matrice en texte pour l'affichage
        matrice_texte = "\n".join(["\t".join(map(str, ligne)) for ligne in self.graph.matrice_cout_od])
        self.label_matrice.config(text=matrice_texte)  # Afficher dans le label

    def mettre_a_jour_label_info(self, texte):
        # Met à jour le label avec un seul texte sans accumulation
        self.label_info.config(text=texte)  # Remplace le texte existant par le nouveau texte

    def run(self):
        self.root.mainloop()


class Affichage:

    def __init__(self, graph, nom_groupe="Groupe Maéva BONNIN, Audrey BOURHIS, Kanelle RICA"):
        self.graph = graph
        self.root = tk.Tk()
        self.root.title(nom_groupe)

        self.canvas = tk.Canvas(self.root, width=Graph.LARGEUR, height=Graph.HAUTEUR, bg="white")
        self.canvas.pack()

        self.info_label = tk.Label(self.root, text="", anchor="w", justify="left")
        self.info_label.pack(fill="x")

        self.root.bind("<Escape>", self.fermer_fenetre)
        self.root.bind("<space>", self.afficher_routes)

        self.dessiner_lieux()

    def dessiner_lieux(self):
        """Dessine les lieux sous forme de cercles avec leur numéro."""
        for i, (x, y) in enumerate(self.graph.liste_lieux):
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 12, "bold"))

    def afficher_routes(self, event=None):
        """Affiche les N meilleures routes en gris et la meilleure en bleu pointillé."""
        if self.graph.matrice_od is None:
            print("Matrice des distances non chargée.")
            return

        # Exemple d'affichage des routes (logique simplifiée)
        n = min(5, len(self.graph.liste_lieux))  # Nombre de routes affichées
        for i in range(n):
            if i == 0:
                couleur = "blue"
                style = (5, 5)
            else:
                couleur = "lightgray"
                style = ()

            for j in range(len(self.graph.liste_lieux) - 1):
                x1, y1 = self.graph.liste_lieux[j]
                x2, y2 = self.graph.liste_lieux[j + 1]
                self.canvas.create_line(x1, y1, x2, y2, fill=couleur, dash=style)
                self.canvas.create_text(x1 + 10, y1, text=str(j + 1), font=("Arial", 10))
        pass

    def fermer_fenetre(self, event=None):
        self.root.quit()

    def run(self):
        self.root.mainloop()


class TSP_GA:
    def __init__(self, graph, file_path, taille_population=10, iterations=10, taux_mutation=0.1, nb_best_routes=2):
        self.graph = graph  # Matrice des distances
        self.file_path = file_path
        self.taille_population = taille_population
        self.iteration = iterations
        self.taux_mutation = taux_mutation
        self.nb_best_routes = nb_best_routes
        self.population = self.generer_population(self.taille_population, self.file_path)


    def generer_population(self):
        population=[]
        for i in range(self.taille_population):
            self.graph.charger_graph(self.file_path)
            liste_lieux = self.graph.get_liste_lieux()
            lieux_depart = liste_lieux[i]
            route = self.graph.route_ppv(lieux_depart.nom)
            route.distance = self.graph.calcul_distance_route(route.ordre)
            population.append(route)
        return population

    def best_routes(self):
        return sorted(self.population, key=lambda route: route.distance)[:self.nb_best_routes]

    def croisement_OX1(self, parent1, parent2):
        """ Croisement OX1 (Order Crossover) """
        taille = len(parent1)
        debut, fin = sorted(random.sample(range(taille), 2))

        enfant = [None] * taille
        enfant[debut:fin] = parent1[debut:fin]  # Garde une section du premier parent

        reste = [lieu for lieu in parent2 if lieu not in enfant]
        index = 0

        for i in range(taille):
            if enfant[i] is None:
                enfant[i] = reste[index]
                index += 1

        return enfant

        '''liste_lieux_restants = liste_lieux.copy()
        premier_lieu = liste_lieux[0]
        ordre = [0]
        liste_lieux_restants.remove(premier_lieu)
        for i in range(NB_LIEUX-1):
            indice_prochain_lieu = Graph.plus_proche_voisin(Graph(), premier_lieu, liste_lieux_restants)
            ordre.append(indice_prochain_lieu)
            print(liste_lieux_restants)
            print(liste_lieux[indice_prochain_lieu])
            liste_lieux_restants.remove(liste_lieux[indice_prochain_lieu])
            premier_lieu = liste_lieux[indice_prochain_lieu]
        ordre.append(0)'''

import numpy as np
import random

NB_LIEUX = 10
LARGEUR = 800
HAUTEUR = 600


class Lieu:
    def __init__(self, x=None, y=None):
        if (x is None):
            x = np.random.rand() * LARGEUR
        if (y is None):
            y = np.random.rand() * HAUTEUR
        self.x = float(x)
        self.y = float(y)

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
        return "(" + str(round(self.x, 2)) + "," + str(round(self.y, 2)) + ")"


class Graph:

    def __init__(self, liste_lieux=None):
        if liste_lieux is None:
            self.liste_lieux = [Lieu() for i in range(NB_LIEUX)]
        else:
            self.liste_lieux = liste_lieux

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

    def plus_proche_voisin(self):
        liste_voisins = []
        for i in range(NB_LIEUX):
            min_dist = self.calcul_matrice_cout_od()[i][0]
            numero_lieu = 0
            for j in range(1,NB_LIEUX):
                valeur = self.calcul_matrice_cout_od()[i][j]
                if (min_dist > valeur and valeur != 0) or min_dist == 0:
                    min_dist = self.calcul_matrice_cout_od()[i][j]
                    numero_lieux = j
            liste_voisins.append(self.liste_lieux[numero_lieux])
        return liste_voisins



    def charger_graph(self):
        pass

    def charger_matrice_od(self):
        pass

    def calcul_distance_route(self):
        lieu = self.plus_proche_voisin()[0]
        somme_distance = 0
        for i in range(1, NB_LIEUX):
            print(Lieu.calcul_distance(lieu, self.plus_proche_voisin()[i]))
            somme_distance += Lieu.calcul_distance(lieu, self.plus_proche_voisin()[i])
        print(somme_distance)

class Route:

    def __init__(self, ordre=None):
        if (ordre is None):
            # créer une route aléatoire
            self.ordre = [0]
            self.ordre.extend(random.sample(range(1, NB_LIEUX), NB_LIEUX - 1))
            self.ordre.append(0)
        else:
            if ordre.length == NB_LIEUX and ordre[0] == ordre[ordre.length - 1]:
                self.ordre = ordre[:]
            else:
                print("La route est incorrecte")

    def get_ordre(self):
        return self.ordre

    def set_ordre(self, ordre):
        self.ordre = ordre


class Affichage:

    def __init__(self, ):
        pass


class TSP_GA:
    pass

graph = Graph()
graph.calcul_distance_route()


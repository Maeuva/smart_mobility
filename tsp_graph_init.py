import numpy
import random
import time
import panda
import tkinter
import csv

class Lieu :
    def __init__(self, x, y, nom) :
        self.x = x
        self.y = y
        self.nom = nom

    def get_x(self) :
        return self.x

    def get_y(self) :
        return self.y

    def get_nom(self) :
        return self.nom

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_nom(self, nom):
        self.nom = nom

    def calcul_distance(self, l2):
         return np.sqrt((l2.x-self.x)**2 + (l2.y-self.y)**2)  


class Graph :
    def __init__(self, liste_lieux, NB_lieux):
        self.liste_lieux = liste_lieux
        self.NB_lieux = NB_lieux

    def get_liste_lieux(self):
        return self.liste_lieux

    def get_NB_lieux(self):
        return self.NB_lieux

    def set_liste_lieux(self, liste_lieux):
        self.liste_lieux = liste_lieux

    def set_NB_lieux(self, NB_lieux):
        self.NB_lieux = NB_lieux

    def calcul_matrice_cout_od(self):
        pass
        # return matrice_od

    def plus_proche_voisin(self):
        pass
        # return plus_proche_voisin_dun_lieu

    def charger_graph(self):
        pass

    def charger_matrice_od(self):
        pass

    def calcul_distance_route(self):
        pass


class Route :

    def __init__(self, ordre):
        self.ordre = ordre

    def get_ordre(self):
        return self.ordre

    def set_ordre(self, ordre):
        self.ordre = ordre


class Affichage :

    def __init__(self, ):
        pass

class TSP_GA :
    pass

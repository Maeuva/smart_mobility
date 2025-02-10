import numpy
import random
import time
import panda
import tkinter
import csv

class Lieu :
    def __init__(self, x, y, nom) :
        self.__x = x
        self.__y = y
        self.__nom = nom

    def get_x(self) :
        return self.__x

    def get_y(self) :
        return self.__y

    def get_nom(self) :
        return self.__nom

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_nom(self, nom):
        self.__nom = nom

    def calcul_distance(self, l2):
         return np.sqrt((l2.x-self.x)**2 + (l2.y-self.y)**2)  


class Graph :
    def __init__(self, liste_lieux, NB_lieux):
        self.__liste_lieux = liste_lieux
        self.__NB_lieux = NB_lieux

    def get_liste_lieux(self):
        #générer des coordonnées aléatoires pour les lieux
        i = 0 
        while i =< Graph.__NB_lieux :
            nombre_aleatoire_x = random.uniform(0,800)
            nombre_aleatoire_y = random.uniform(0,600)
            liste_lieux.append(nombre_aleatoire_x)
            liste_lieux.append(nombre_aleatoire_y)
            i += 1    
        return self.__liste_lieux

    def get_NB_lieux(self):
        return self.__NB_lieux

    def set_liste_lieux(self, liste_lieux):
        self.__liste_lieux = liste_lieux

    def set_NB_lieux(self, NB_lieux):
        self.__NB_lieux = NB_lieux

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
        self.__ordre = ordre

    def get_ordre(self):
        return self.__ordre

    def set_ordre(self, ordre):
        self.__ordre = ordre


class Affichage :

    def __init__(self, ):
        pass

class TSP_GA :
    pass

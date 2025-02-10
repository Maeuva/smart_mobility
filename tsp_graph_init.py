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

    def calcul_distance(self, lieu2):
         return np.sqrt((lieu2.x-self.x)**2 + (lieu2.y-self.y)**2)  


class Graph :
    __NB_lieux = 10
    
    def __init__(self, liste_lieux, NB_lieux):
        self.liste_lieux = liste_lieux
        self.NB_lieux = NB_lieux

    def get_liste_lieux(self):
        return self.liste_lieux

    def set_liste_lieux(self, liste_lieux):
        self.liste_lieux = liste_lieux

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

    def __init__(self, ordre = None):
        if(ordre is None):
            #créer une route aléatoire
            self.ordre = [0]
            self.ordre.extend(random.sample(range(1,Graph.__NB_lieux), Graph.__NB_lieux-1))
            self.ordre.append(0)
        else : 
            if length(ordre) == Graph.__NB_lieux and ordre[0] == ordre[length(ordre)-1] :
                self.ordre = ordre[:]
            else :
                print("La route est incorrecte")

    def get_ordre(self):
        return self.ordre

    def set_ordre(self, ordre):
        self.ordre = ordre


class Affichage :

    def __init__(self, ):
        pass

class TSP_GA :
    pass

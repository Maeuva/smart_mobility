import numpy
import random
import time
import panda
import tkinter
import csv

NB_LIEUX = 10
LARGEUR = 800
HAUTEUR = 600

class Lieu :
    def __init__(self, x=None, y=None) :
        if (x is None) :
            x = np.random.rand()*LARGEUR
        if (y is None) :
            y = np.random.rand()*HAUTEUR
        self.x = float(x)
        self.y = float(y)

    def get_x(self) :
        return self.x

    def get_y(self) :
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def calcul_distance(self, lieu2):
         return np.sqrt((lieu2.x-self.x)**2 + (lieu2.y-self.y)**2)  

    def __repr__(self):
        return "(" + str(round(self.x,2)) + "," + str(round(self.y,2)) + ")"
        

class Graph :
  
    def __init__(self, liste_lieux = None, NB_LIEUX):
        if liste_lieux is None :
            self.liste_lieux = [ Lieu() for i in range(NB_LIEUX)]
        else :            
            self.liste_lieux = liste_lieux

    def get_liste_lieux(self):
        return self.liste_lieux


    def set_liste_lieux(self, liste_lieux):
        self.liste_lieux = liste_lieux

    def calcul_matrice_cout_od(self):
        matrice_od = 
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
    #ordre vaut None par defaut
    def __init__(self, ordre = None):
        #on vérifie si ordre est rempli
        if(ordre is None):
            #créer une route aléatoire
            self.ordre = [0]
            #on ajoute une permutation de nb lieux sans le zero range(1, NB_LIEUX)
            self.ordre.extend(random.sample(range(1,NB_LIEUX), NB_LIEUX-1))
            self.ordre.append(0)
        else : 
            if length(ordre) == NB_LIEUX and ordre[0] == ordre[length(ordre)-1] :
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

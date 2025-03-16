import numpy as np
import random
import time
import pandas as pd
import tkinter as tk
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
  
    def __init__(self, NB_LIEUX, liste_lieux = None):
        if liste_lieux is None :
            self.liste_lieux = [ Lieu() for i in range(NB_LIEUX)]
        else :            
            self.liste_lieux = liste_lieux
    
    def get_liste_lieux(self):
        return self.liste_lieux

    def set_liste_lieux(self, liste_lieux):
        self.liste_lieux = liste_lieux

    def calcul_matrice_cout_od(self):
        matrice_od = []
        for i in range(NB_LIEUX) :
            row = []
            for j in range(NB_LIEUX) : 
                row.append(set_liste_lieux[i].calcul_distance(set_liste_lieux[j]))
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


    def calcul_distance_route(self, liste_coordonnees):
        lieu = liste_coordonnees[0]
        somme_distance = 0
        for i in range(1, NB_LIEUX):
            somme_distance += Lieu.calcul_distance(lieu, liste_coordonnees[i])
            print(Lieu.calcul_distance(lieu, liste_coordonnees[i]))
            lieu = liste_coordonnees[i]
        somme_distance += Lieu.calcul_distance(liste_coordonnees[0], liste_coordonnees[NB_LIEUX-1])
        return somme_distance
    
    def charger_graph(self, fichier_lieux):
        """Charge la liste des lieux à partir d'un fichier CSV."""
        self.liste_lieux = []  # Réinitialisation
        try:
            with open(fichier_lieux, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Ignorer l'en-tête si présent
                for row in reader:
                    x, y = map(float, row)  # Convertir les coordonnées en flottants
                    self.liste_lieux.append((x, y))
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
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
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

class TSP_GA :
    pass

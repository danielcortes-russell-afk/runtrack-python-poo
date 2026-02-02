import math

class Operation:

    def __init__(self, nombre1, nombre2):
        self.nombre1 = 12
        self.nombre2 = 3

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return resultat
    
calcul = Operation(1,5)

### JOB 2
print(f"Le nombre1 est {calcul.nombre1}","\n" f"Le nombre2 est {calcul.nombre2}")
print("--------------------------------")
###

### JOB 3
print(f"La somme de 'calcul' est : {calcul.addition()}")
print("--------------------------------")
###

### JOB 4

class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"
    
client1 = Personne("Daniel", "Cortes-Russell")
client2 = Personne("Romain", "Elies")

print(f"{client1.SePresenter()}", "\n" f"{client2.SePresenter()}")
print("--------------------------------")
###

### JOB 5

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return f"X : {self.x}, Y : {self.y}"
    
    def afficherX(self):
        return f"X : {self.x}"
    def afficherY(self):
        return f"Y : {self.y}"

    def changerX(self, x):
        self.x = x
        return x
    def changerY(self, y):
        self.y = y
        return y


coordonnee = Point(5,0)

print(f"{coordonnee.afficherLesPoints()}")
print(f"{coordonnee.afficherX()}")
print(f"{coordonnee.afficherY()}")
print(f"{coordonnee.changerX(1)} -> {coordonnee.afficherX()}")
print(f"{coordonnee.changerY(5)} -> {coordonnee.afficherY()}")
print("--------------------------------")
###

### JOB 6

class Animal:

    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        return self.age

    def nommer(self, prenom):
        self.prenom = prenom
        return self.prenom

milo = Animal()
milo.nommer("Miloude")

print(f"l'Âge de {milo.prenom} est de {milo.age} ans")
milo.vieillir()
print(f"l'Âge de {milo.prenom} est de {milo.age} ans")
print(f"l'animal se nomme {milo.prenom}")
print("--------------------------------")
###

### JOB 7

class Personnage:

    def __init__(self):
        self.x = 0
        self.y = 0

    def droite(self):
        self.x += 1
        return self.x
    def gauche(self):
        self.x -= 1
        return self.x

    def haut(self):
        self.y += 1
        return self.y
    def bas(self):
        self.y -= 1
        return self.y


    def position(self):
        return self.x, self.y

mario = Personnage()
mario.droite()

print(mario.position())
print("--------------------------------")
###

### JOB 8

class Cercle:

    def __init__(self, radius):
        self.radius = radius

    def changerRadius(self, radius):
        self.radius = radius
        return self.radius

    def circonference(self):
        self.circonference = (self.radius*2)*math.pi
        self.circonference = "{:.2f}".format(self.circonference)
        return self.circonference
    def aire(self):
        self.aire = (math.pi*self.radius)**2
        self.aire = "{:.2f}".format(self.aire)
        return self.aire
    def diametre(self):
        self.diametre = self.radius*2
        return self.diametre


    def afficherInfos(self):
        return f"Rayon : {self.radius}, Diamètre : {self.diametre()}, Circonférence : {self.circonference()}, Aire : {self.aire()}"

rond1 = Cercle(4)
rond2 = Cercle(7)
print(rond1.afficherInfos())
print(rond2.afficherInfos())
print("--------------------------------")
###

### JOB 9

class Produit:

    def __init__(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = 0.2

    def changerPrix(self, prixHT):
        self.prixHT = prixHT
        return self.prixHT
    def changerNom(self, nom):
        self.nom = nom
        return self.nom

    def CalculerPrixTTC(self):
        self.prixttc = self.prixHT*self.TVA
        self.prixttc = "{:.2f}".format(self.prixttc)
        return self.prixttc

    def afficherNom(self):
        return f"Nom du produit : {self.nom}"
    def afficherPrix(self):
        return f"Prix du produit : {self.prixHT}"
    def afficher(self):
        return self.nom, self.prixHT

produit1 = Produit("Télévision", 249.99)
print(f"{produit1.nom} -> Prix TTC : {produit1.CalculerPrixTTC()}$")
print(produit1.afficher())
produit1.changerNom("Télévision 4K")
produit1.changerPrix(399)
print(f"{produit1.nom} -> Prix TTC : {produit1.CalculerPrixTTC()}$")
print(produit1.afficher())


produit2 = Produit("PC Portable", 1280.99)
print(f"{produit2.nom} -> Prix TTC : {produit2.CalculerPrixTTC()}$")
print(produit2.afficher())
produit2.changerNom("Pc Portable Gamer")
produit2.changerPrix(2000)
print(f"{produit2.nom} -> Prix TTC : {produit2.CalculerPrixTTC()}$")
print(produit2.afficher())

print("--------------------------------")
###
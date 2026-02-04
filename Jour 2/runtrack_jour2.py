import math

### JOB 1
class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def mutateurLongueur(self, longueur):
        self.__longueur = longueur
    def mutateurLargeur(self, largeur):
        self.__largeur = largeur
    
    def accesseurs(self):
        return f"Longueur : {self.__longueur}, Largueur : {self.__largeur}"

    
rectangle1 = Rectangle(2,24)
rectangle1.mutateurLargeur(3)

print(rectangle1.accesseurs())
print("----------------------------------------------------------------")
###

### JOB 2 & 3
class Livre:

    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True
        

    def mutateurTitre(self, titre):
        if not isinstance(titre, str):
            raise ValueError("Titre invalide")
        else:
            self.__titre = titre

    def mutateurAuteur(self, auteur):
        if not isinstance(auteur, str):
            raise ValueError("Auteur invalide")
        else:
            self.__auteur = auteur

    def mutateurPages(self, pages):
        if not isinstance(pages, int):
            raise ValueError("Nombre de pages invalide")
        else:
            self.__pages = pages

    def disponible(self):
        return self.__disponible

    def empreinter(self):
        if self.__disponible == True:
            self.__disponible = False
            return f"Vous venez d'empreinter le livre : {self.__titre} !"
        else:
            return "Livre non disponible"

    def rendre(self):
        if self.__disponible == False:
            self.__disponible = True
            return f"Vous venez de rendre le livre : {self.__titre} !"
        else:
            return "Livre est disponible et donc pas à rendre."

    def accesseurs(self):
        return f"Titre : {self.__titre} | Auteur : {self.__auteur} | Nombre de Pages : {self.__pages} | Disponibilité : {self.__disponible}"

    
livre1 = Livre("Paris", "Daniel", 50)

print(livre1.accesseurs())
livre1.mutateurAuteur("Jean")
print(livre1.disponible())
print("---")

print(livre1.empreinter())
print(livre1.empreinter())
print(livre1.rendre())
print("---")

print(livre1.accesseurs())
print("----------------------------------------------------------------")
###

### JOB 4
class Student:

    def __init__(self, nom, prenom, numero):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credits = 0
        self.__level = self.__studentEval()
        

    def add_credits(self, credits):
        if isinstance(credits, int) and credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            raise ValueError("Somme invalide")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très Bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
        

    def studentInfo(self):
        return f"Prénom : {self.__prenom} | Nom : {self.__nom} | Numéro : {self.__numero} | Niveau : {self.__level}."

    
etudiant1 = Student("Doe", "John", 145)
print(etudiant1.studentInfo())
print("---")
etudiant1.add_credits(60)
print(etudiant1.studentInfo())
print("---")
etudiant1.add_credits(10)
print(etudiant1.studentInfo())
print("---")
etudiant1.add_credits(10)
print(etudiant1.studentInfo())

print("----------------------------------------------------------------")
###

### JOB 5
class Voiture:

    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoire = 50
        

    def mutateurMarque(self, newmarque):
        self.__marque = newmarque
    def mutateurModele(self, newmodele):
        self.__modele = newmodele
    def mutateurAnnee(self, newannee):
        self.__annee = newannee
    def mutateurkilometrage(self, newkilometrage):
        self.__kilometrage = newkilometrage

    def accesseurMarque(self):
        return self.__marque
    def accesseurModele(self):
        return self.__modele
    def accesseurAnnee(self):
        return self.__annee
    def accesseurkilometrage(self):
        return self.__kilometrage

    def __demarrer(self):
        if self.__verifier_plein() > 50:
            self.__en_marche = True
    def __arretter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoire

    
voiture = Voiture("BMW", "1", 2005, 0)
print(voiture.verifier_plein())

print("----------------------------------------------------------------")
###

### JOB 6

menu = {
    "Pizza" : 12.5,
    "Burger" : 7.5,
    "Boisson" : 1
}

class Commande:

    def __init__(self, numero, statut):
        self.__liste_plat = {}
        self.__numero = None
        self.__statut = None
        

    def ajouterPlat(self, plat, nombre):
        self.__liste_plat[plat] = nombre
    def annulerCommande(self, plat):
        self.__liste_plat = {}
        self.__statut = "Annulée"


    def __calculerCommande(self):
        prix = 0
        for key in self.__liste_plat:
            prix += self.__liste_plat[key] * menu[key]
        return prix

    def afficherCommande(self):
        return self.__liste_plat, f"Total à payer : {self.__calculerCommande()}"

    
commande1 = Commande(1, "En cours")
commande1.ajouterPlat("Pizza", 5)
commande1.ajouterPlat("Boisson", 10)
print(commande1.afficherCommande())

print("----------------------------------------------------------------")
###

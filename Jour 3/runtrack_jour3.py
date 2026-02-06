import math
import copy
import random

### JOB 1
class Ville:

    def __init__(self, nom, nb_habitant):
        self.__nom = nom
        self.__nb_habitant = nb_habitant

    def augmenterHabitant(self):
        self.__nb_habitant += 1

    def voirHabitant(self):
        return self.__nb_habitant

class Personne:

    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__ville.augmenterHabitant()


v1 = Ville("Paris", 1000000)
v2 = Ville("Marseille", 861635)

p1 = Personne("John", 45, v1)
p2 = Personne("Myrtille", 4, v1)
p3 = Personne("Chloé", 18, v2)

print(v1.voirHabitant())
print(v2.voirHabitant())
print("----------------------------------------------------------------")
###

### JOB 2
class CompteBancaire:

    def __init__(self, numero, nom, prenom, solde):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = False


    def afficherCompte(self):
        return f"MR {self.__nom} {self.__prenom} | Numéro de Compte : {self.__numero})"
    def afficherSolde(self):
        return f"Solde : {self.__solde})"
    
    ##
    def decouvert(self):
        if self.__decouvert == False:
            self.__decouvert = True
        else:
            self.__decouvert = False
    ##

    def versement(self, montant):
        self.__solde += montant
    def retrait(self, montant):
        if self.__decouvert == True:
            if self.__solde - montant >= 0:
                self.__solde -= montant
            else:
                self.__solde -= montant+self.__agios()
        else:
            if self.__solde - montant >= 0:
                self.__solde -= montant
            else:
                raise Exception("Solde insufisant.")
        
    def virement(self, compte, numero, montant):
        compte.versement(montant)
        self.retrait(montant)


    def __agios(self):
        if self.__solde < 100:
            return 10
        elif self.__solde < 500:
            return 50

c1 = CompteBancaire(2, "CR", "Daniel", 500)
c2 = CompteBancaire(1, "Munoz", "Donatien", -200)
c2.decouvert()

c1.versement(100)
c1.retrait(100)

c2.virement(c1, 1, 0)
print(c1.afficherSolde())
print(c2.afficherSolde())
print("----------------------------------------------------------------")

###

### JOB 3
class Tache:

    def __init__(self, titre = "", description = "", statut = ""):
        self.titre = titre
        self.description = description
        self.statut = statut

    def afficherTache(self):
        return [self.titre, self.description, self.statut]

class ListeDeTache:

    def __init__(self, tache):
        self.__tache = [copy.copy(tache.afficherTache())]

    def ajouterTache(self, addtache):
        self.__tache.append(addtache.afficherTache())
    def supprimerTache(self, deltache):
        self.__tache.remove(deltache.afficherTache())

    def marquerCommeFinie(self, tartache):
        self.__tache[self.__tache.index(tartache.afficherTache())][2] = "Terminée"
        

    def afficherListe(self):
        return self.__tache

t1 = Tache("Faire à manger")
t2 = Tache("Ranger la cuisine")

tdl1 = ListeDeTache(t1)
tdl1.ajouterTache(t2)
#tdl1.supprimerTache(t2)

print(tdl1.afficherListe())
tdl1.marquerCommeFinie(t2)
print(tdl1.afficherListe())
print("----------------------------------------------------------------")

###

### JOB 4
class Tache:

    def __init__(self, titre = "", description = "", statut = ""):
        self.titre = titre
        self.description = description
        self.statut = statut

    def afficherTache(self):
        return [self.titre, self.description, self.statut]

class Joueur:

    def __init__(self, nom, numero, position, buts, passes, carton_j, carton_r):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = buts
        self.passes = passes
        self.carton_j = carton_j
        self.carton_r = carton_r


    def marquerUnBut(self):
        self.buts += 1
    def effectuerUnePasseDecisive(self):
        self.passes += 1

    def recevoirCartonJaune(self):
        self.carton_j += 1
    def recevoirCartonRouge(self):
        self.carton_r += 1

    def afficherStatistiques(self):
        return self.nom, self.numero, self.position, self.buts, self.passes, self.carton_j, self.carton_r

class Equipe:

    def __init__(self, nom):
        self.nom = nom
        self.listejoueur = []

    def ajouterJoueur(self, joueur):
        self.listejoueur.append(joueur)

    def mettreAJourStatistiquesJoueur(self, joueur):
        for element in self.listejoueur:
            return element.afficherStatistiques()

    def afficherStatistiquesJoueurs(self):
        liste_temporaire = []
        for element in self.listejoueur:
            liste_temporaire.append(element.afficherStatistiques())
        return liste_temporaire

j1 = Joueur("Daniel", 5, "Aile Gauche", 29, 10, 0, 0)
j2 = Joueur("Jean", 5, "Aile Droite", 19, 20, 0, 0)

equipe1 = Equipe("MonkeyCorp")
equipe1.ajouterJoueur(j1)
equipe1.ajouterJoueur(j2)

print(equipe1.afficherStatistiquesJoueurs())
print("----------------------------------------------------------------")

###

### JOB 5

class Personnage:

    def __init__(self, nom, vie, resistance, heal, damage):
        self.nom = nom
        self.vie = vie
        self.resistance = resistance
        self.heal = heal
        self.damage = damage
        self.__shield = False

    def attaquer(self):
        return self.damage

class Jeu:

    def __init__(self):
        self.niveau = 1 #-> 5

    def changerNiveau(self, niveau):
        self.niveau = niveau

    def lancerJeu(self, joueur, adversaire = None):
        running = True

        #
        turn = "Robot"
        choix = ["Heal","Attaque"]
        last_action = None
        #

        while True:
            if turn == "Robot":
                last_action = random.choice(choix)
                if last_action == "Attaque":
                    joueur.vie -= (adversaire.damage-joueur.resistance)
                else:
                    adversaire.vie += adversaire.heal

                turn = "Joueur"
            else:
                last_action = str(input("Action (Heal/Attaque) : ")).strip() or "Attaque"
                if last_action == "Attaque":
                    adversaire.vie -= (joueur.damage-adversaire.resistance)
                else:
                    joueur.vie += joueur.heal

                turn = "Robot"

            if adversaire.vie <= 0:
                print("Gagné")
                return False
            elif joueur.vie <= 0:
                print("Perdu")
                return False

j1 = Personnage("KyoMei", 1000, 10, 10, 100)
j2 = Personnage("Livai", 1000, 10, 10, 90)

game = Jeu()
game.changerNiveau(5)

print(game.lancerJeu(j1, j2))
print("----------------------------------------------------------------")

###
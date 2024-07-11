#QCM:

# 1-a
# 2-b
# 3-c
# 4-a
# 5-b
# 6-a



#PARTI1:
from abc import ABC, abstractmethod

class Personne(ABC):
    def __init__(self, nom_complet, CIN, age):
        self.nom_complet = nom_complet
        self.CIN = CIN
        self.age = age

    @abstractmethod
    def Afficher_detail(self):
        pass

    @staticmethod
    def liste_premiers(a, b):
        premiers = []
        for n in range(a, b+1):
            if n > 1:
                for i in range(2, n):
                    if (n % i) == 0:
                        break
                else:
                    premiers.append(n)
        return premiers

#PARTIE2:
class Client(Personne):
    clients = 0

    def __init__(self, nom_complet, CIN, age, id_client, budget):
        super().__init__(nom_complet, CIN, age)
        self.id_client = id_client
        self.budget = budget
        Client.clients += 1

    @classmethod
    def afficher_clients(cls):
        print("Nombre total de clients :", cls.clients)

    def __add__(self, other):
        return self.budget + other.budget

    @staticmethod
    def print_star(n):
        for i in range(n, 0, -1):
            print('*' * i)


#PARTIE3:
class Vendeur:
    nb_vendeurs = 0

    def __init__(self, nom_complet, CIN, age, id_vendeur, salaire):
        self.nom_complet = nom_complet
        self.CIN = CIN
        self.age = age
        self._id_vendeur = id_vendeur
        self.__salaire = salaire
        Vendeur.nb_vendeurs += 1

    @classmethod
    def afficher_nombre_total(cls):
        print("Nombre total de vendeurs :", cls.nb_vendeurs)

    def get_id_vendeur(self):
        return self._id_vendeur

    def set_id_vendeur(self, value):
            self._id_vendeur = value


    def get_salaire(self):
        return self.__salaire

    def set_salaire(self, value):
        if value >= 0:
            self.__salaire = value
        else:
            print("Salaire ne peut pas être négatif.")

    def Afficher_detail(self):
        print(f"Nom complet : {self.nom_complet}")
        print(f"CIN : {self.CIN}")
        print(f"Âge : {self.age}")
        print(f"ID vendeur : {self.get_id_vendeur()}")
        print(f"Salaire : {self.get_salaire()}")

#PARTIE4:
class Produit:
    nb_produits = 0

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        Produit.nb_produits += 1

    def Afficher_detail(self):
        print(f"Nom : {self.nom}")
        print(f"Prix : {self.prix}")

    @classmethod
    def afficher_nombre_total(cls):
        print("Nombre total de produits :", cls.nb_produits)


    @staticmethod
    def sort_list(liste_produits):
        # Tri et suppression des doublons sans utiliser les méthodes prédéfinies
        return sorted(set(liste_produits), key=lambda x: x.prix)


#PARTIE5 :
class Vente:
    nb_ventes = 0

    def __init__(self, id_vente, date_vente, vendeur, client, produits, prix_total_vente=0):
        self.id_vente = id_vente
        self.date_vente = date_vente
        self.vendeur = vendeur
        self.client = client
        self.produits = produits
        self.prix_total_vente = prix_total_vente

    def ajouter_produit(self, produit):
        self.produits.append(produit)
        self.prix_total_vente += produit.prix


    def afficher_details(self):
        print(f"ID vente : {self.id_vente}")
        print(f"Date vente : {self.date_vente}")
        print(f"Vendeur : {self.vendeur.nom_complet}")
        print(f"Client : {self.client.nom_complet}")
        print("Produits:")
        for produit in self.produits:
            produit.Afficher_detail()
        print(f"Prix total de la vente : {self.prix_total_vente}")

#PARTIE TEST :

vendeur1 = Vendeur("Vendeur 1", "CIN-1", 30, 1234, 2000)
client1 = Client("Client 1", "CIN-2", 25, 5678, 5000)
produit1 = Produit("Produit 1", 100)
produit2 = Produit("Produit 23", 200)
produit3 = Produit("Produit 9", 100)
print(produit1 == produit3)  # True
vente1 = Vente(1, "2022-01-01", vendeur1, client1, [produit1, produit2])
vente1.ajouter_produit(produit3)
vente1.afficher_details()
Produit.afficher_nombre_total()
Vendeur.afficher_nombre_total()
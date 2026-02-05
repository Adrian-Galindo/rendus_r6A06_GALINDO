from vaches.exceptions import InvalidVacheException
from typing import Any

class vache:
    # --- constantes ---
    AGE_MAX = 25
    POIDS_MAX = 1000.0
    PANSE_MAX = 50.0
    POIDS_MIN_PANSE = 2.0
    RENDEMENT_RUMINATION: float = 0.25

    # --- compteur d'ID (classe) ---
    NEXT_ID : int = 1

    def __init__(self, petit_nom, poids):
        self.id = self.NEXT_ID
        vache.NEXT_ID += 1

        self.petit_nom = petit_nom
        self.age = 0
        self.poids = poids
        self.panse = 0.0

        self.valider_etat()

    def __str__(self):
        return f"Vache {self.id} : {self.petit_nom}, âge {self.age} ans, poids {self.poids} kg, panse {self.panse} L"

    def brouter(self, quantite, nourriture: Any = None):
        if nourriture is not None:
            raise InvalidVacheException("Type de nourriture interdit")
        self.ajouter_panse(quantite)

    def ruminer(self):
        self.valider_rumination_possible()

        panse_avant = self.panse

        # Gain de poids
        gain = vache.RENDEMENT_RUMINATION * panse_avant
        self.poids += gain

        # Hooks (polymorphisme)
        lait = self._calculer_lait(panse_avant)
        self._stocker_lait(lait)

        # Vidage panse
        self.panse = 0.0

        # Hook post-traitement
        self._post_rumination(panse_avant, lait)

        self.valider_etat()

        return lait

    def vieillir(self):
        if self.age >= vache.AGE_MAX:
            raise InvalidVacheException("Âge maximum atteint")
        self.age += 1

    def _calculer_lait(self, panse_avant):
        return 0.0

    def _stocker_lait(self, lait):
        pass

    def _post_rumination(self, panse_avant, lait):
        pass

    def ajouter_panse(self, quantite):
        if quantite <= 0:
            raise InvalidVacheException("Quantité invalide")

        if self.panse + quantite > vache.PANSE_MAX:
            raise InvalidVacheException("Panse pleine")

        self.panse += quantite

    def valider_rumination_possible(self):
        if self.panse <= 0:
            raise InvalidVacheException("Panse insuffisante pour ruminer")

    def valider_etat(self):
        if not self.petit_nom or self.petit_nom.strip() == "":
            raise InvalidVacheException("Nom vide")
        if not (0 <= self.age <= vache.AGE_MAX):
            raise InvalidVacheException("Âge invalide")
        if self.poids < 0 or self.poids > vache.POIDS_MAX:
            raise InvalidVacheException("Poids invalide")
        if self.panse < 0 or self.panse > vache.PANSE_MAX:
            raise InvalidVacheException("Panse invalide")


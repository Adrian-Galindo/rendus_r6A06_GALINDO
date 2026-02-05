from vaches.vache import vache

class vache_a_lait(vache):
    # --- constantes ---
    RENDEMENT_LAIT : float = 1.1
    PRODUCTION_LAIT_MAX : float = 40.0

    # --- attributs d'instance ---
    lait_disponible : float
    lait_total_produit : float
    lait_total_traite : float

    def __init__(self, petitNom, age, poids):
        self.lait_disponible = 0.0
        self.lait_total_produit = 0.0
        self.lait_total_traite = 0.0
        super().__init__(petitNom, age, poids)

    def __str__(self):
        return f"Vache à lait {self.id} : {self.petit_nom}, âge {self.age} ans, poids {self.poids} kg, panse {self.panse} L, lait disponible {self.lait_disponible} L"

    def _calculer_lait(self, panse_avant):
        production_lait = vache_a_lait.RENDEMENT_LAIT * panse_avant
        if production_lait < vache_a_lait.PRODUCTION_LAIT_MAX:
            return production_lait
        else:
            raise ValueError("La production de lait dépasse le maximum autorisé !")

    def _stocker_lait(self, quantite):
        self.lait_disponible += quantite
        self.lait_total_produit += quantite

    def traire(self, quantite):
        if quantite > self.lait_disponible:
            raise ValueError("Quantité de lait à traire dépasse le lait disponible !")
        self.lait_disponible -= quantite
        self.lait_total_traite += quantite
        return quantite
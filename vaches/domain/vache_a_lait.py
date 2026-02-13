from vaches.exceptions import InvalidVacheException
from vaches.domain.vache import vache
from vaches.strategies.standard_milk import StandardMilkStrategy


class vache_a_lait(vache):
    # --- constantes ---
    RENDEMENT_LAIT : float = 1.1
    PRODUCTION_LAIT_MAX : float = 40.0

    # --- attributs d'instance ---
    lait_disponible : float
    lait_total_produit : float
    lait_total_traite : float

    def __init__(self, petitNom, poids, rumination_strategy = StandardMilkStrategy):
        self.lait_disponible = 0.0
        self.lait_total_produit = 0.0
        self.lait_total_traite = 0.0
        super().__init__(petitNom, poids, rumination_strategy)

    def __str__(self):
        return (
            f"Vache à lait {self.id} : {self.petit_nom}, "
            f"âge {self.age} ans, poids {self.poids} kg, panse {self.panse} L, "
            f"Lait disponible : {self.lait_disponible} L, "
            f"Lait total trait : {self.lait_total_traite} L"
        )

    def traire(self, quantite):
        if quantite <= 0.0:
            raise InvalidVacheException("Quantité de lait à traire doit être supérieur a 0 !")
        if quantite > self.lait_disponible:
            raise InvalidVacheException("Quantité de lait à traire dépasse le lait disponible !")
        self.lait_disponible -= quantite
        self.lait_total_traite += quantite
        return quantite
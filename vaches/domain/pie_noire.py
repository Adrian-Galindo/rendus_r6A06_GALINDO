from typing import Dict
from vaches.domain.vache_a_lait import vache_a_lait
from vaches.nourriture.type_nourriture import TypeNourriture
from vaches.exceptions import InvalidVacheException
from vaches.strategies.pie_noire_milk import PieNoireMilkStrategy


class Ration:
    """
    Classe association entre une vache et un type de nourriture.
    Stocke la quantité consommée.
    """
    def __init__(self, vache: "pie_noire", nourriture: TypeNourriture, quantite: float = 0.0):
        self.vache = vache
        self.nourriture = nourriture
        self.quantite = quantite
        vache._ration[nourriture] = self


class pie_noire(vache_a_lait):
    # --- constantes ---
    COEFFICIENT_NUTRITIONNEL: Dict[TypeNourriture, float] = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    # --- attributs d'instance ---
    nb_taches_noires: int
    nb_tache_blanche: int
    _ration: Dict[TypeNourriture, Ration]

    def __init__(
            self,
            petit_nom: str,
            poids: float,
            nb_taches_blanches: int,
            nb_taches_noires: int,
            rumination_strategy=PieNoireMilkStrategy
    ):
        self.nb_taches_noires = nb_taches_noires
        self.nb_tache_blanche = nb_taches_blanches
        self._ration: Dict[TypeNourriture, Ration] = {}  # dictionnaire d'associations

        super().__init__(petit_nom, poids, rumination_strategy)

        self.valider_etat()

    def brouter(self, quantite: float, nourriture: TypeNourriture = None):
        if quantite <= 0:
            raise InvalidVacheException("Quantité invalide")

        if nourriture is None:
            self.ajouter_panse(quantite)
            return

        if nourriture not in self.COEFFICIENT_NUTRITIONNEL:
            raise InvalidVacheException("Type de nourriture invalide")

        # Crée ou récupère la ration
        if nourriture not in self._ration:
            Ration(self, nourriture, 0.0)

        # Met à jour la quantité
        self._ration[nourriture].quantite += quantite

        # Impact sur la panse avec coefficient
        coef = self.COEFFICIENT_NUTRITIONNEL[nourriture]
        self.ajouter_panse(quantite * coef)

    def ruminer(self):
        # Appel de la rumination du parent (gain poids, calcul lait, stock)
        panse_avant = self.panse
        lait = super().ruminer()

        # Hook post-rumination de la stratégie
        self.rumination_strategy.post_rumination(self, panse_avant, lait)

        return lait

    @property
    def ration(self) -> Dict[TypeNourriture, float]:
        """
        Retourne un dictionnaire {type_nourriture: quantite}
        """
        return {nourriture: ration.quantite for nourriture, ration in self._ration.items()}

    def valider_etat(self):
        super().valider_etat()

        if not isinstance(self.nb_taches_noires, int) or self.nb_taches_noires <= 0:
            raise InvalidVacheException("Le nombre de taches noires doit être un entier positif")
        if not isinstance(self.nb_tache_blanche, int) or self.nb_tache_blanche <= 0:
            raise InvalidVacheException("Le nombre de taches blanches doit être un entier positif")

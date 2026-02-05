from vaches.domain.vache_a_lait import vache_a_lait
from vaches.nourriture.type_nourriture import TypeNourriture
from vaches.exceptions import InvalidVacheException
from vaches.domain.ration import Ration

class pie_noire(vache_a_lait):
    # --- constantes ---
    COEFFICIENT_NUTRITIONNEL: dict[TypeNourriture, float] = {
        TypeNourriture.MARGUERITE: 1.1,
        TypeNourriture.HERBE: 1.0,
        TypeNourriture.FOIN: 0.9,
        TypeNourriture.PAILLE: 0.4,
        TypeNourriture.CEREALES: 1.3,
    }

    # --- attributs d'instance ---
    nb_taches_noires: int
    nb_tache_blanche: int
    _ration: dict[TypeNourriture, Ration]

    def __init__(self, petit_nom, poids, age, nb_taches_blanches, nb_taches_noires):
        self.nb_taches_noires = nb_taches_noires
        self.nb_tache_blanche = nb_taches_blanches
        self._ration = {}
        super().__init__(petit_nom, age, poids)

        self.valider_etat()

    def brouter(self, quantite: float, nourriture: TypeNourriture = None):
        if quantite <= 0:
            raise InvalidVacheException("Quantité invalide")

        if nourriture is None:
            # Comportement classique : panse seulement
            self.ajouter_panse(quantite)
            return

        if nourriture not in self.COEFFICIENT_NUTRITIONNEL:
            raise InvalidVacheException("Type de nourriture invalide")

        # Met à jour la ration interne
        if nourriture not in self._ration:
            self._ration[nourriture] = Ration(0.0)
        self._ration[nourriture].quantite += quantite

        # Impact sur la panse avec coefficient
        coef = self.COEFFICIENT_NUTRITIONNEL[nourriture]
        self.ajouter_panse(quantite * coef)

    def ruminer(self):
        lait = super().ruminer()  # panse vidée, lait produit
        self._ration.clear()      # on vide la ration interne
        return lait

    @property
    def ration(self) -> dict[TypeNourriture, float]:
        return {nourriture: ration.quantite for nourriture, ration in self._ration.items()}

    def valider_etat(self):
        super().valider_etat()

        if not isinstance(self.nb_taches_noires, int) or self.nb_taches_noires <= 0:
            raise InvalidVacheException("Le nombre de taches noires doit être un entier positif")
        if not isinstance(self.nb_tache_blanche, int) or self.nb_tache_blanche <= 0:
            raise InvalidVacheException("Le nombre de taches blanches doit être un entier positif")

from vaches.exceptions import InvalidVacheException
from vaches.strategies.protocols.rumination_strategy import RuminationStrategy

class StandardMilkStrategy:

    def calculer_lait(self, vache, panse_avant) -> float:
        production = vache.RENDEMENT_LAIT * panse_avant
        futur_lait_dispo = vache.lait_disponible + production

        if futur_lait_dispo <= vache.PRODUCTION_LAIT_MAX:
            return production
        else:
            raise InvalidVacheException(
                "La production de lait dépasse le maximum autorisé"
            )

    def stocker_lait(self, vache, lait) -> None:
        vache.lait_disponible += lait
        vache.lait_total_produit += lait

    def post_rumination(self, vache, panse_avant, lait) -> None:
        return

strategy : RuminationStrategy = StandardMilkStrategy()
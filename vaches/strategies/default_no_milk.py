from vaches.strategies.protocols.rumination_strategy import RuminationStrategy

class NoMilkStrategy:

    def calculer_lait(self, vache:"vache", panse_avant) -> float:
        return 0.0

    def stocker_lait(self, vache:"vache", lait) -> None:
        return

    def post_rumination(self, vache:"vache", panse_avant, lait) -> None:
        return

strategy : RuminationStrategy = NoMilkStrategy()
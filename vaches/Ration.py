class Ration:
    _quantite : float

    def __init__(self, quantite: float):
        self.quantite = quantite

    def __str__(self) -> str:
        return f"Ration(quantite={self.quantite})"
from vaches.vache_a_lait import vache_a_lait
#from remiseVache.fr.devavance.TypeNourriture import TypeNourriture

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
    _nombre_tache_noire: int
    _nombre_tache_blanche: int
    _ration : dict[TypeNourriture, float]
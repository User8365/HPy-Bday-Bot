"""
================================================================================
LISTE DES ANNIVERSAIRES - ZONE DE MODIFICATION
================================================================================

Ce fichier contient la liste des anniversaires des membres de l'équipe.

Pour ajouter un joueur :
1. Ajoutez un dictionnaire à la liste BIRTHDAYS avec les clés :
   - user_id : ID Discord du joueur (str)
   - day : Jour de naissance (int, 1-31)
   - month : Mois de naissance (int, 1-12)
   - name : Nom d'affichage (str, optionnel mais recommandé)

IMPORTANT : Ne modifiez rien en dehors de cette section.

================================================================================
"""

from typing import List, Dict, Union

# ==============================================================================
# LISTE DES ANNIVERSAIRES - MODIFIABLE
# ==============================================================================

BIRTHDAYS: List[Dict[str, Union[str, int]]] = [
    # Exemple : {"user_id": "123456789012345678", "day": 15, "month": 6, "name": "PseudoJoueur"},
    # Ajoutez vos joueurs ici
]

# ==============================================================================
# FIN DE LA LISTE
# ==============================================================================


def get_todays_birthdays(today_day: int, today_month: int) -> List[Dict[str, Union[str, int]]]:
    """
    Retourne la liste des anniversaires du jour.

    Args:
        today_day: Jour actuel (1-31)
        today_month: Mois actuel (1-12)

    Returns:
        Liste des dictionnaires d'anniversaires correspondant à la date
    """
    return [
        birthday for birthday in BIRTHDAYS
        if birthday["day"] == today_day and birthday["month"] == today_month
    ]

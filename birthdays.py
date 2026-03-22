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
    # Test du jour - à supprimer après vérification
    {"user_id": "1464959985183101072", "day": 22, "month": 3, "name": "TestBot"},
    # Ajoutez vos joueurs ici
    {"user_id": "1359566489358700735", "day":19, "month": 3, "name": "Fabienne"},
    {"user_id": "840859819522261033", "day": 9, "month": 5, "name": "Claudine"},
    {"user_id": "840855337984065547", "day": 7, "month": 6, "name": "André"},
    {"user_id": "769243798756130896", "day": 26, "month": 6, "name": "Laurent"}
   
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

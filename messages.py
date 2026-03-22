"""
================================================================================
ZONE DE MODIFICATION DES MESSAGES D'ANNIVERSAIRE
================================================================================

Cette section contient tous les messages d'anniversaire utilisés par le bot.
Vous pouvez librement :
- Ajouter de nouveaux messages à la liste BIRTHDAY_MESSAGES
- Modifier les messages existants
- Supprimer des messages

IMPORTANT : Ne modifiez rien en dehors de cette section (au-dessus ni en-dessous).

Format des messages :
- {mention} sera remplacé par la mention de l'utilisateur (@username)
- {team_role} sera remplacé par la mention du rôle d'équipe
- Utilisez des emojis pour plus de convivialité
- Chaque message doit être une chaîne de caractères entre guillemets

================================================================================
"""

from typing import List
import random

# ==============================================================================
# LISTE DES MESSAGES D'ANNIVERSAIRE - MODIFIABLE
# ==============================================================================

BIRTHDAY_MESSAGES: List[str] = [
    # 🎉 5 Templates avec mention du rôle d'équipe (thème navigation/festif)
    "🎉⚓ {team_role} ⛵ Un membre de l'équipe fête son anniversaire aujourd'hui ! Bon anniversaire {mention} ! Que le vent vous soit favorable et que votre année soit remplie de victoires virtuelles ! 🏆🌊🎂",

    "🌊🎂 Ahoy {team_role} ! 🏴‍☠️ C'est l'anniversaire de {mention} ! Souhaitons-lui une mer calme, un vent de poupe et une navigation sans écueils pour cette nouvelle année ! ⛵⚓🎉",

    "⛵🎉 {team_role} Hissez les couleurs ! 🏁 {mention} prend un an de plus aujourd'hui ! Bon anniversaire marin d'eau douce ! Puisse ta boussole toujours te mener vers le succès ! ⚓🌅🎂",

    "⚓🎂 {team_role} à l'abordage ! 🚢 L'équipage célèbre aujourd'hui l'anniversaire de {mention} ! Bon vent, bonne mer et excellente navigation pour cette nouvelle année de vie ! 🌊⛵🎉",

    "🏆🌊 {team_role} faites du bruit ! 📯 C'est le grand jour de {mention} ! Joyeux anniversaire ! Que cette année soit parsemée de podiums et que ta route soit toujours vent arrière ! ⛵⚓🎂🎉",

    # 🎉 Messages existants (conservés)
    "🎉🎂 Bon anniversaire {mention} ! Que le vent te soit toujours favorable cette année et toutes les autres ! ⛵",
    
    "⚓ {mention}, joyeux anniversaire ! Une année de plus à ton actif, un cap de plus à franchir serein ! 🎂",
    
    "🌊⛵ Ahoy {mention} ! Joyeux anniversaire ! Puisse ta nouvelle année être calme et vent dans le dos ! 🎉",
    
    "🎂 Bon anniversaire {mention} ! Que ta boussole te guide vers de nouvelles aventures virtuelles ! ⛵⚓",
    
    "🏆 {mention}, toute l'équipe te souhaite un joyeux anniversaire ! Bon vent et bonne navigation ! 🎉",
    
    "🌅 Bon anniversaire {mention} ! Une nouvelle année qui se lève à l'horizon, pleine de promesses ! ⛵🎂",
    
    "⚓🎉 Joyeux anniversaire {mention} ! Que les vagues de la vie t'emportent vers le succès ! 🌊",
    
    "🎂 {mention}, la flotte te souhaite un excellent anniversaire ! Prêt(e) à hisser les voiles pour une nouvelle année ? ⛵",
    
    "⛵🎉 Bon anniversaire {mention} ! Que cette année soit parsemée de bons vents et de belles victoires ! 🏆",
    
    "🌊 {mention}, joyeux anniversaire ! Une bouée de plus franchie sur le parcours de la vie ! 🎂⚓",
]

# ==============================================================================
# FIN DE LA ZONE DE MODIFICATION
# ==============================================================================


def get_random_message() -> str:
    """
    Retourne un message d'anniversaire aléatoire.
    
    Returns:
        Message d'anniversaire formaté (avec {mention} à remplacer)
    """
    return random.choice(BIRTHDAY_MESSAGES)


def format_message(message: str, user_mention: str, team_role_mention: str = "") -> str:
    """
    Formate un message d'anniversaire avec la mention de l'utilisateur et du rôle.

    Args:
        message: Message contenant potentiellement {mention} et {team_role}
        user_mention: Mention Discord de l'utilisateur (@username)
        team_role_mention: Mention du rôle d'équipe (@&role_id), vide si non configuré

    Returns:
        Message formaté
    """
    return message.format(mention=user_mention, team_role=team_role_mention)

"""
Bot Discord d'anniversaires pour équipe Virtual Regatta.

Ce script s'exécute en one-shot (GitHub Actions cron) :
1. Vérifie la date du jour
2. Compare avec la liste des anniversaires
3. Envoie un embed Discord si anniversaire détecté
4. S'arrête

Architecture :
- Communication Discord via API REST (requests)
- Secrets via variables d'environnement uniquement
- Pas de dépendance discord.py
"""

import os
import sys
from datetime import datetime
from typing import Optional

import requests

from birthdays import get_todays_birthdays
from messages import get_random_message, format_message


# ==============================================================================
# CONFIGURATION
# ==============================================================================

# Récupération des secrets via variables d'environnement (GitHub Actions Secrets)
DISCORD_TOKEN: Optional[str] = os.getenv("DISCORD_TOKEN")
CHANNEL_ID: Optional[str] = os.getenv("BIRTHDAY_CHANNEL_ID")
TEAM_ROLE_ID: Optional[str] = os.getenv("TEAM_ROLE_ID")  # Optionnel : mention du rôle d'équipe

# URL de l'API Discord pour envoyer un message dans un canal
DISCORD_API_URL: str = "https://discord.com/api/v10/channels/{channel_id}/messages"

# Couleur de l'embed (orange/navigation en hexadécimal)
EMBED_COLOR: int = 0xE67E22


# ==============================================================================
# FONCTIONS
# ==============================================================================

def validate_config() -> bool:
    """
    Valide que les variables d'environnement requises sont présentes.

    Returns:
        True si configuration valide, False sinon
    """
    if not DISCORD_TOKEN:
        print("[ERREUR] DISCORD_TOKEN non défini dans les variables d'environnement")
        return False

    if not CHANNEL_ID:
        print("[ERREUR] BIRTHDAY_CHANNEL_ID non défini dans les variables d'environnement")
        return False

    return True


def create_birthday_embed(user_id: str, user_name: str, message: str) -> dict:
    """
    Crée la structure d'un embed Discord pour un anniversaire.

    Args:
        user_id: ID Discord de l'utilisateur
        user_name: Nom d'affichage de l'utilisateur
        message: Message d'anniversaire formaté

    Returns:
        Dictionnaire représentant l'embed Discord
    """
    # Mention de l'utilisateur au format Discord
    user_mention = f"<@{user_id}>"

    # Mention du rôle d'équipe si configurée
    team_mention = ""
    if TEAM_ROLE_ID:
        team_mention = f"<@&{TEAM_ROLE_ID}>"

    # Formatage final du message
    formatted_message = format_message(message, user_mention, team_mention)

    # Construction de l'embed
    embed = {
        "title": f"🎉 Joyeux Anniversaire {user_name} !",
        "description": formatted_message,
        "color": EMBED_COLOR,
        "footer": {
            "text": "🎂 Bot d'anniversaires Virtual Regatta"
        },
        "timestamp": datetime.utcnow().isoformat()
    }

    return embed


def send_discord_embed(embed: dict) -> bool:
    """
    Envoie un embed Discord via l'API REST.

    Args:
        embed: Dictionnaire de l'embed à envoyer

    Returns:
        True si succès, False sinon
    """
    url = DISCORD_API_URL.format(channel_id=CHANNEL_ID)

    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "embeds": [embed]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        print(f"[SUCCÈS] Embed envoyé (HTTP {response.status_code})")
        return True

    except requests.exceptions.HTTPError as e:
        print(f"[ERREUR HTTP] Échec de l'envoi : {e}")
        if e.response is not None:
            print(f"Réponse Discord : {e.response.text}")
        return False

    except requests.exceptions.RequestException as e:
        print(f"[ERREUR RÉSEAU] Impossible de contacter Discord : {e}")
        return False


def process_birthdays() -> int:
    """
    Traite les anniversaires du jour et envoie les messages.

    Returns:
        Nombre de messages envoyés
    """
    now = datetime.now()
    today_day = now.day
    today_month = now.month

    print(f"[INFO] Vérification des anniversaires - {now.strftime('%d/%m/%Y')}")

    # Récupération des anniversaires du jour
    todays_birthdays = get_todays_birthdays(today_day, today_month)

    if not todays_birthdays:
        print("[INFO] Aucun anniversaire aujourd'hui")
        return 0

    print(f"[INFO] {len(todays_birthdays)} anniversaire(s) trouvé(s)")

    messages_sent = 0

    for birthday in todays_birthdays:
        user_id = str(birthday["user_id"])
        user_name = str(birthday.get("name", "Marin"))

        print(f"[INFO] Traitement de l'anniversaire : {user_name} (ID: {user_id})")

        # Sélection d'un message aléatoire
        random_message = get_random_message()

        # Création de l'embed
        embed = create_birthday_embed(user_id, user_name, random_message)

        # Envoi Discord
        if send_discord_embed(embed):
            messages_sent += 1
        else:
            print(f"[ERREUR] Échec d'envoi pour {user_name}")

    return messages_sent


# ==============================================================================
# POINT D'ENTRÉE
# ==============================================================================

if __name__ == "__main__":
    print("=" * 60)
    print("BOT D'ANNIVERSAIRES - VIRTUAL REGATTA")
    print("=" * 60)

    # Validation de la configuration
    if not validate_config():
        sys.exit(1)

    # Traitement des anniversaires
    sent_count = process_birthdays()

    print("=" * 60)
    print(f"Traitement terminé - {sent_count} message(s) envoyé(s)")
    print("=" * 60)

    sys.exit(0 if sent_count >= 0 else 1)

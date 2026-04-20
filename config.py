import os
from sample_config import Config


class Development(Config):
    # =========================
    # TELEGRAM API
    # =========================
    APP_ID = int(os.getenv("APP_ID", "0"))
    API_HASH = os.getenv("API_HASH", "")

    # =========================
    # USERBOT INFO
    # =========================
    ALIVE_NAME = os.getenv("ALIVE_NAME", "UserBot")

    # =========================
    # DATABASE
    # =========================
    DB_URI = os.getenv("DB_URI", "")

    # =========================
    # SESSION STRING
    # =========================
    STRING_SESSION = os.getenv("STRING_SESSION", "")

    # =========================
    # BOT TOKEN
    # =========================
    TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN", "")

    # =========================
    # GROUP SETTINGS
    # =========================
    PRIVATE_GROUP_BOT_API_ID = int(os.getenv("PRIVATE_GROUP_BOT_API_ID", "0"))

    # =========================
    # COMMANDS
    # =========================
    COMMAND_HANDLER = "."
    SUDO_COMMAND_HANDLER = "."

    # =========================
    # PLUGINS
    # =========================
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    BADCAT = False

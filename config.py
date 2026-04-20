from sample_config import Config

class Development(Config):
    # =========================
    # REQUIRED CORE SETTINGS
    # =========================

    APP_ID = 39769005  # from my.telegram.org
    API_HASH = "fe798fb4dd08ffcb15c53ed934738ddf"  # from my.telegram.org
    STRING_SESSION = "1BJWap1sBu0KV_230LnyYRoYo_0Drq_ZdsEIbeC2bMnUUMz_KaI7Mx_N816WJJn62LkhmIBEvCXF3ZEVsVkUTMMV2C4L6Uq5XGbjSlGVl1Rk03CBPnDw6vwx8sDlfBimHxDj1-m_3HLRHpLcYfYod5gA9A_2_xNaA3DWYRDeovbFuCvPDAf17yAapC0kBaOZdd8-bGxMIDZjlkDhRQWRUTQoH6kkSj1aFT4MOWJMLwcey9OtUzujG_467IGiaiGaFAWkFTEIr6eh4gPo7DO3MxI_imzxiUzli0CbPA5PQgWBbC_qywptLH5wLurcC5yf3TTOwvSmhUKwlJ7X2Vh11GZPBniYZ2MA="  # from stringsetup.py

    # =========================
    # ASSISTANT BOT (REQUIRED FOR YOU)
    # =========================

    TG_BOT_TOKEN = "8726587897:AAH93X3Tq1MDlXKVQNn_9XLQAudr-d8lmjE"  # from @BotFather
    TG_BOT_USERNAME = "Paradoxs_ai_robot"  # without @

    # =========================
    # USER INFO
    # =========================

    OWNER_ID = 6655806551  # from @userinfobot
    ALIVE_NAME = "PARADOX"

    # =========================
    # DATABASE (Supabase)
    # =========================
    DB_URI = "postgresql://postgres:UWFDzIAFyrylqVOyEepQeuFZZUgldgEL@monorail.proxy.rlwy.net:24362/railway"
    # =========================
    # GROUP IDS (OPTIONAL - SAFE DEFAULTS)
    # =========================

    PRIVATE_GROUP_BOT_API_ID = 0
    PRIVATE_GROUP_ID = -5249718987
    FBAN_GROUP_ID = 0
    PRIVATE_CHANNEL_BOT_API_ID = 0

    # =========================
    # OPTIONAL FEATURES (IGNORE IF UNUSED)
    # =========================

    VC_SESSION = None
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None

    # =========================
    # SAFE DEFAULTS
    # =========================

    LOGGER = True

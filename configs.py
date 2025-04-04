from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
 
    FORCE_SUB = int(getenv("FORCE_SUB", ""))
    ADMIN = list(map(int, getenv("ADMIN", "").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    # database configs
    DB_URL = os.environ.get("DB_URL", "")
    DB_NAME = os.environ.get("DB_NAME", "Cluster1")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/cRu.jpg")
    
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://graph.org/file/28c188cb93dc4c08132f9.mp4").split()

    LOGO = """
RZXBOTS"""

rkn1 = Config()


# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support

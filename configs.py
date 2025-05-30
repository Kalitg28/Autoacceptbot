from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
 
    FORCE_SUB = int(getenv("FORCE_SUB", "-1002327045567"))
    ADMIN = list(map(int, getenv("ADMIN", "").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002364462279"))
    
    # database configs
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://autoacceptbot:autoacceptbot@cluster0.a64dz8p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/4Jy.jpg")
    
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://envs.sh/4J6.jpg").split()

    LOGO = """
RZXBOTS"""

rkn1 = Config()


# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support

from os import path, getenv
import os, time 

class Config:
    API_ID = int(getenv("API_ID", "15043670"))
    API_HASH = getenv("API_HASH", "d131b85fafc3e98cde4c506cccee3f2a")
    BOT_TOKEN = getenv("BOT_TOKEN", "5866366012:AAFbkPvzep2btQ6mtztD8tEhEO6COrrKBKY")
 
    FORCE_SUB = int(getenv("FORCE_SUB", "-1001823248949"))
    ADMIN = list(map(int, getenv("ADMIN", "6051042088").split()))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001930341741"))
    
    # database configs
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://dudemusic111:dudemusic111@cluster0.df3yis2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DB_NAME = os.environ.get("DB_NAME", "Cluster1")
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    RKN_PIC = os.environ.get("RKN_PIC", "https://envs.sh/Lss.jpg")
    
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

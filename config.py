import os
from os import environ 

class Config(object):
    API_HASH = os.environ.get("API_HASH" ,"f12c642a9f02932c1bc82bf4c1ddb776")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6425840613:AAGxXZm89m4D-tHDA4dW9zkWqNx9hfpXFOw")
    TELEGRAM_API = int(os.environ["TELEGRAM_API"]) if "TELEGRAM_API" in os.environ else 14557103
    OWNER = os.environ.get("OWNER","5447134162")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME" ,"th3gardener")
    PASSWORD = os.environ.get("PASSWORD","passw0rd")
    DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://Zara02:zara02@cluster0.i5zmevo.mongodb.net/?retryWrites=true&w=majority")
    LOGCHANNEL = os.environ.get("LOGCHANNEL","-1001780905599")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID","root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    MODES = ["video-video", "video-audio", "video-subtitle","extract-streams"]

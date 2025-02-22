import re
import os
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Fetch required environment variables
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
LOGGER_ID = int(os.getenv("LOGGER_ID", -1000000000000))
MONGO_DB_URI = os.getenv("MONGO_DB_URI", None)

# Optional configurations with defaults
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "Ownergit")
BOT_USERNAME = os.getenv("BOT_USERNAME", "NexikoBot")
BOT_NAME = os.getenv("BOT_NAME", "Nexiko")
ASSUSERNAME = os.getenv("ASSUSERNAME", "MissYumikoo")

# Heroku Deployment
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", None)

# Repository Details
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/DAXXTEAM/DAXXMUSIC")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

# URLs for support
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/ALLTYPECC")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/gitwizardbypass")

# Media and Image URLs
IMAGE_URLS = {
    "start": os.getenv("START_IMG_URL", "https://telegra.ph/file/cfbdee8103102bcb2e5da.jpg"),
    "ping": os.getenv("PING_IMG_URL", "https://telegra.ph/file/00360393a15daf7fc4e9d.jpg"),
    "playlist": "https://telegra.ph/file/d723f4c80da157fca1678.jpg",
    "stats": "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg",
    "telegram_audio": "https://telegra.ph/file/48f39202823b358203234.jpg",
    "telegram_video": "https://telegra.ph/file/e575ae40d6635250974e1.jpg",
    "stream": "https://telegra.ph/file/03efec694e41e891b29dc.jpg",
    "soundcloud": "https://telegra.ph/file/d723f4c80da157fca1678.jpg",
    "youtube": "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg",
    "spotify_artist": "https://telegra.ph/file/d723f4c80da157fca1678.jpg",
    "spotify_album": "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg",
    "spotify_playlist": "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg",
}

# Limits and Durations
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 17000))
DURATION_LIMIT = DURATION_LIMIT_MIN * 60
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "9999999"))

# Auto Assistant Settings
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Spotify API Keys
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "")

# Sessions
STRING_SESSIONS = [os.getenv(f"STRING_SESSION{i}", None) for i in range(1, 8)]

# Utility functions
def validate_url(url):
    return re.match(r"(?:http|https)://", url) is not None

# URL Validations
if not validate_url(SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")
if not validate_url(SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

# Admin and user tracking
BANNED_USERS = filters.user()
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

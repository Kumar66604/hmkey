import os
from os import getenv

API_ID = int(getenv("API_ID", 2238786))
API_HASH = getenv("API_HASH", "e449d6cc630583d0b415b286eedb9192")
BOT_TOKEN = getenv("BOT_TOKEN", "7314075849:AAH0VizMPC60yErn44H_WqWt-_WFfHehr60")
MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hmkey:BiyF6woNU8Lq3uSa@hmkey.fzom8.mongodb.net/?retryWrites=true&w=majority&appName=hmkey")
OWNER_ID = list(map(int, getenv("OWNER_ID", "950958796").split()))

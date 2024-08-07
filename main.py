from pyrogram import Client, filters

API_ID = 15657755
API_HASH = "7cce51d4664d010b90ad690e0d5121ad"
BOT_TOKEN = "6561546458:AAEjlUCOrvYXJ-Bwvw03mwRoKO07gy73NlA"

app = Client(
    "Test-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")

print("BOT SUCCESSFULLY DEPLOYED !!")

app.run()

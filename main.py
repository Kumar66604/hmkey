import datetime, time, os, asyncio,logging 
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
from config import *
from broadcast import *

for file in os.listdir():
    if file.endswith(".session"):
        os.remove(file)
for file in os.listdir():
    if file.endswith(".session-journal"):
        os.remove(file)

app = Client(
    "Test-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(_, m: Message):
        add_user(m.from_user.id)
        keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/PS_BOTz"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/hamstar_key")
                    ],[
                        InlineKeyboardButton("🔑 Get keys", url="http://t.me/HamsterKeyTool_bot/Hamster")
                    ]
                ]
            )
        await m.reply_photo("https://graph.org/file/cde23a18790463438a1d6.jpg", caption="**Manager: @PS_BOTz\n\n 🎉 Updated (in test mode).\n\n 🔑 Keys are free for everyone.\n\n All games:\n 1. Bike Ride 3D\n 2. My Clone Army\n 3. Chain Cube 2048\n 4. Train Miner\n ‼️If 100% progress does not show keys, wait ~30 sec.\n If it still doesn't work, take a break for a longer time (eg 1 hour) and then try again.\n There is a limit on plowing from one IP from the Hamster side.**", reply_markup=keyboard)
    
    

@app.on_message(filters.command("users") & filters.user(OWNER_ID))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
    ★ Usᴇʀs : `{xx}`
★ Gʀᴏᴜᴘs : `{x}`
★ Tᴏᴛᴀʟ ᴜsᴇʀs & ɢʀᴏᴜᴘs : `{tot}` """)   


@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "broadcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "broadcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")          

@app.on_message(filters.command("fcast") & filters.user(OWNER_ID))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")


print("BOT SUCCESSFULLY DEPLOYED !!")

app.run()

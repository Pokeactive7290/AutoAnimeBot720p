import asyncio
from config import STATUS_ID, UPLOADS_ID, UPLOADS_USERNAME
from main.modules.parser import auto_parser
from main import app
from pyrogram import filters, idle
from pyrogram.types import Message
from uvloop import install
from contextlib import closing, suppress
from main.modules.tg_handler import tg_handler

loop = asyncio.get_event_loop()

@app.on_message(filters.command(["start","help","ping","online"]))
async def start(bot, message: Message):
  return await message.reply_text("⭐️ **Bot Is Online.[.](https://telegra.ph/file/c191217ab3c439271c0d4.jpg).**\n\n**Updates :** @AniXDex **| Support :** @AniXDiscuss")

async def start_bot():
  await app.send_message(UPLOADS_ID,f"⭐️ **Bot Started...**\n\n`Uploading Will Start After 10 Minutes`\n\nCheck Status : [Here](https://t.me/{UPLOADS_USERNAME}/{STATUS_ID})")
  print("==================================")
  print("[INFO]: AutoAnimeBot Started Bot Successfully")
  print("==========JOIN @TECHZBOTS=========")

  print("[INFO]: Adding Parsing Task")
  asyncio.create_task(auto_parser())
  asyncio.create_task(tg_handler())
  
  await idle()
  print("[INFO]: BOT STOPPED")
  await app.stop()  
  for task in asyncio.all_tasks():
    task.cancel()

if __name__ == "__main__":
  install()
  with closing(loop):
    with suppress(asyncio.exceptions.CancelledError):
      loop.run_until_complete(start_bot())
      loop.run_until_complete(asyncio.sleep(3.0))

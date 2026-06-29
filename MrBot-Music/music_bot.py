from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME", "music_session")

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.command("join") & filters.group)
async def join_vc(client, message: Message):
    try:
        await client.join_group_call(message.chat.id)
        await message.reply("✅ تم الانضمام!", parse_mode=None)
    except Exception as e:
        await message.reply(f"❌ {e}", parse_mode=None)


@app.on_message(filters.command("play") & filters.group)
async def play_song(client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply("📝 /play <اسم الأغنية>", parse_mode=None)
        return
    await message.reply(f"🎵 جاري تشغيل: {query}", parse_mode=None)


@app.on_message(filters.command("leave") & filters.group)
async def leave_vc(client, message: Message):
    try:
        await client.leave_group_call(message.chat.id)
        await message.reply("👋 تم المغادرة", parse_mode=None)
    except Exception as e:
        await message.reply(f"❌ {e}", parse_mode=None)


if __name__ == "__main__":
    print("🎵 MrBot Music Starting...")
    app.run()
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.bot import bot

router = Router()


@router.message(Command("whisper"))
@router.message(Command("همسة"))
async def send_whisper(message: Message):
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو", parse_mode=None)
        return
    args = message.text.split(maxsplit=1)
    text = args[1] if len(args) > 1 else "همسة سرية 🤫"
    target = message.reply_to_message.from_user
    try:
        await bot.send_message(target.id, f"🤫 همسة من {message.from_user.full_name}:\n\n{text}", parse_mode=None)
        await message.answer("✅ تم إرسال الهمسة!", parse_mode=None)
    except Exception:
        await message.answer("❌ لا يمكن الإرسال. العضو لم يبدأ محادثة معي.", parse_mode=None)
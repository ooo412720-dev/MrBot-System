from aiogram import Router, F
from aiogram.types import Message
import random

router = Router()

GREETINGS = ["هلا", "مرحبا", "أهلاً", "سلام", "hello", "hi"]
THANKS = ["شكرا", "شكراً", "مشكور", "thanks"]
BYE = ["باي", "وداعا", "مع السلامة", "bye"]


@router.message(F.text.lower().in_(GREETINGS))
async def greeting_handler(message: Message):
    replies = ["👋 أهلاً وسهلاً!", "🌹 مرحباً بك!", "✨ أهلاً!"]
    await message.reply(random.choice(replies), parse_mode=None)


@router.message(F.text.lower().in_(THANKS))
async def thanks_handler(message: Message):
    replies = ["🌸 العفو!", "😊 لا شكر على واجب!", "💕 تسلم!"]
    await message.reply(random.choice(replies), parse_mode=None)


@router.message(F.text.lower().in_(BYE))
async def bye_handler(message: Message):
    replies = ["👋 مع السلامة!", "🌙 في أمان الله!", "🌹 إلى اللقاء!"]
    await message.reply(random.choice(replies), parse_mode=None)


@router.message(F.text.lower() == "بوت")
async def bot_mention(message: Message):
    await message.reply(f"نعم {message.from_user.full_name}؟ 🤖", parse_mode=None)


@router.message(F.text.lower() == "همسه")
async def whisper_text(message: Message):
    await message.reply("📌 رد على رسالة العضو واكتب /whisper أو /همسة", parse_mode=None)


@router.message(F.text.lower() == "صلاحياتي")
async def my_perms_text(message: Message):
    await message.reply("📌 اكتب /id أو /ايدي لعرض معلوماتك", parse_mode=None)
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.db import get_or_create_group_settings, get_or_create_user

router = Router()


@router.message(Command("start"))
async def group_start(message: Message):
    if message.chat.type not in ("group", "supergroup"):
        return
    await get_or_create_user(message.from_user.id, message.from_user.username, message.from_user.full_name)
    await get_or_create_group_settings(message.chat.id, message.chat.title)
    await message.answer(
        f"✅ تم تسجيل الجروب: {message.chat.title}\n"
        f"🤖 MrBot جاهز للعمل!\n"
        f"أرسل /help لعرض الأوامر.",
        parse_mode=None
    )
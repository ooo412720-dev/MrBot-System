from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.db import get_or_create_user, get_or_create_group_settings

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await get_or_create_user(message.from_user.id, message.from_user.username, message.from_user.full_name)
    
    if message.chat.type in ("group", "supergroup"):
        await get_or_create_group_settings(message.chat.id, message.chat.title)
        text = (
            f"✅ تم تسجيل الجروب: {message.chat.title}\n"
            f"🤖 MrBot جاهز للعمل!\n"
            f"أرسل /help لعرض الأوامر."
        )
    else:
        text = (
            f"👋 أهلاً {message.from_user.full_name}!\n\n"
            f"🤖 أنا MrBot، بوت إدارة المجموعات.\n\n"
            f"📋 الأوامر:\n"
            f"• /help - قائمة الأوامر\n"
            f"• /id - معلوماتك\n\n"
            f"➕ أضفني لمجموعتك!"
        )
    await message.answer(text, parse_mode=None)
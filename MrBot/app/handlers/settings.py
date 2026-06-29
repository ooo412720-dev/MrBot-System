from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from app.database.db import get_or_create_group_settings

router = Router()


@router.message(Command("settings"))
@router.message(Command("اعدادات"))
async def show_settings(message: Message):
    settings = await get_or_create_group_settings(message.chat.id)
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="👋 الترحيب", callback_data="toggle_welcome")],
        [InlineKeyboardButton(text="🔗 حظر الروابط", callback_data="toggle_antilink")],
        [InlineKeyboardButton(text="🛡️ مكافحة السبام", callback_data="toggle_antispam")],
    ])
    text = (
        f"⚙️ إعدادات الجروب\n\n"
        f"👋 الترحيب: {'✅' if settings.welcome_enabled else '❌'}\n"
        f"🔗 حظر الروابط: {'✅' if settings.antilink_enabled else '❌'}\n"
        f"🛡️ مكافحة السبام: {'✅' if settings.antispam_enabled else '❌'}"
    )
    await message.answer(text, reply_markup=kb, parse_mode=None)
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.db import get_user_points, add_points, add_reputation, get_top_users

router = Router()


@router.message(Command("rank"))
@router.message(Command("مستوى"))
async def show_rank(message: Message):
    up = await get_user_points(message.chat.id, message.from_user.id)
    if up:
        text = f"📊 مستواك\n\n⭐ النقاط: {up.points}\n💎 السمعة: {up.reputation}"
    else:
        text = "📊 مستواك\n\n⭐ النقاط: 0\n💎 السمعة: 0"
    await message.answer(text, parse_mode=None)


@router.message(Command("top"))
@router.message(Command("الأفضل"))
async def show_top(message: Message):
    users = await get_top_users(message.chat.id, 10)
    if users:
        text = "🏆 الأكثر نشاطاً:\n\n"
        for i, up in enumerate(users, 1):
            text += f"{i}. User {up.user_id} — ⭐ {up.points}\n"
        await message.answer(text, parse_mode=None)
    else:
        await message.answer("ℹ️ لا توجد بيانات", parse_mode=None)


@router.message(Command("rep"))
@router.message(Command("سمعة"))
async def give_rep(message: Message):
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو", parse_mode=None)
        return
    target = message.reply_to_message.from_user
    await add_reputation(message.chat.id, target.id, 1)
    await message.answer(f"💎 تم إعطاء سمعة لـ {target.full_name}", parse_mode=None)
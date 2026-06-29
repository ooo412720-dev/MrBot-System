from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.db import get_or_create_group_settings, update_group_setting

router = Router()


@router.message(Command("antilink"))
@router.message(Command("حظر_روابط"))
async def toggle_antilink(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    settings = await get_or_create_group_settings(message.chat.id)
    new_val = not settings.antilink_enabled
    await update_group_setting(message.chat.id, "antilink_enabled", new_val)
    status = "✅ مفعّل" if new_val else "❌ معطل"
    await message.answer(f"🔗 حظر الروابط: {status}", parse_mode=None)


@router.message(Command("antispam"))
@router.message(Command("مكافحة_سبام"))
async def toggle_antispam(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    settings = await get_or_create_group_settings(message.chat.id)
    new_val = not settings.antispam_enabled
    await update_group_setting(message.chat.id, "antispam_enabled", new_val)
    status = "✅ مفعّل" if new_val else "❌ معطل"
    await message.answer(f"🛡️ مكافحة السبام: {status}", parse_mode=None)


@router.message(Command("lock"))
@router.message(Command("قفل"))
async def lock_media(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    args = message.text.split(maxsplit=1)
    lock_type = args[1].lower().strip() if len(args) > 1 else ""
    if lock_type in ("media", "صور"):
        await update_group_setting(message.chat.id, "lock_media", True)
        await message.answer("🔒 تم قفل الصور.", parse_mode=None)
    elif lock_type in ("stickers", "ملصقات"):
        await update_group_setting(message.chat.id, "lock_stickers", True)
        await message.answer("🔒 تم قفل الملصقات.", parse_mode=None)
    elif lock_type in ("forward", "توجيه"):
        await update_group_setting(message.chat.id, "lock_forward", True)
        await message.answer("🔒 تم قفل التوجيه.", parse_mode=None)
    else:
        await message.reply("📝 الاستخدام: /قفل <media/stickers/forward>", parse_mode=None)


@router.message(Command("unlock"))
@router.message(Command("فتح"))
async def unlock_media(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    args = message.text.split(maxsplit=1)
    lock_type = args[1].lower().strip() if len(args) > 1 else ""
    if lock_type in ("media", "صور"):
        await update_group_setting(message.chat.id, "lock_media", False)
        await message.answer("🔓 تم فتح الصور.", parse_mode=None)
    elif lock_type in ("stickers", "ملصقات"):
        await update_group_setting(message.chat.id, "lock_stickers", False)
        await message.answer("🔓 تم فتح الملصقات.", parse_mode=None)
    elif lock_type in ("forward", "توجيه"):
        await update_group_setting(message.chat.id, "lock_forward", False)
        await message.answer("🔓 تم فتح التوجيه.", parse_mode=None)
    else:
        await message.reply("📝 الاستخدام: /فتح <media/stickers/forward>", parse_mode=None)
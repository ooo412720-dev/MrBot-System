from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.bot import bot

router = Router()


@router.message(Command("rules"))
@router.message(Command("قوانين"))
async def show_rules(message: Message):
    from app.database.db import get_or_create_group_settings
    settings = await get_or_create_group_settings(message.chat.id)
    if settings.rules_text:
        await message.answer(f"📜 قوانين الجروب:

{settings.rules_text}", parse_mode=None)
    else:
        await message.answer("ℹ️ لم يتم تعيين قوانين بعد.", parse_mode=None)


@router.message(Command("setrules"))
@router.message(Command("تعيين_قوانين"))
async def set_rules(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    args = message.text.split(maxsplit=1)
    rules = args[1] if len(args) > 1 else None
    if not rules:
        await message.reply("📝 اكتب القوانين بعد الأمر.", parse_mode=None)
        return
    from app.database.db import update_group_setting
    await update_group_setting(message.chat.id, "rules_text", rules)
    await message.answer("✅ تم تعيين قوانين الجروب.", parse_mode=None)


@router.message(Command("id"))
@router.message(Command("ايدي"))
async def show_id(message: Message):
    user = message.from_user
    chat = message.chat
    text = (
        f"🆔 معلومات

"
        f"👤 المستخدم: {user.full_name}
"
        f"🆔 User ID: {user.id}
"
        f"💬 Chat ID: {chat.id}
"
        f"📛 النوع: {chat.type}
"
    )
    if message.reply_to_message:
        target = message.reply_to_message.from_user
        text += f"
📋 المردود عليه:
👤 الاسم: {target.full_name}
🆔 ID: {target.id}"
    await message.answer(text, parse_mode=None)


@router.message(Command("admins"))
@router.message(Command("المشرفين"))
async def list_admins(message: Message):
    try:
        admins = await bot.get_chat_administrators(message.chat.id)
        admin_list = []
        for admin in admins:
            name = admin.user.full_name
            status = "👑 المالك" if admin.status == "creator" else "🔧 مشرف"
            admin_list.append(f"{status} — {name}")
        await message.answer("📋 قائمة المشرفين:

" + "
".join(admin_list), parse_mode=None)
    except Exception as e:
        await message.answer(f"❌ خطأ: {e}", parse_mode=None)


@router.message(Command("link"))
@router.message(Command("رابط"))
async def group_link(message: Message):
    try:
        chat = await bot.get_chat(message.chat.id)
        if chat.username:
            await message.answer(f"🔗 https://t.me/{chat.username}", parse_mode=None)
        elif chat.invite_link:
            await message.answer(f"🔗 {chat.invite_link}", parse_mode=None)
        else:
            await message.answer("ℹ️ لا يوجد رابط.", parse_mode=None)
    except Exception as e:
        await message.answer(f"❌ خطأ: {e}", parse_mode=None)
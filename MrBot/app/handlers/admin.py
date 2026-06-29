from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

from app.bot.bot import bot
from app.core.logger import logger

router = Router()


@router.message(Command("ban"))
@router.message(Command("حظر"))
async def ban_user(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو المراد حظره.", parse_mode=None)
        return
    target = message.reply_to_message.from_user
    try:
        await bot.ban_chat_member(message.chat.id, target.id)
        await message.answer(f"🚫 تم حظر {target.full_name}", parse_mode=None)
    except TelegramBadRequest:
        await message.answer("❌ لا يمكنني حظر هذا العضو.", parse_mode=None)


@router.message(Command("kick"))
@router.message(Command("طرد"))
async def kick_user(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو المراد طرده.", parse_mode=None)
        return
    target = message.reply_to_message.from_user
    try:
        await bot.ban_chat_member(message.chat.id, target.id)
        await bot.unban_chat_member(message.chat.id, target.id, only_if_banned=True)
        await message.answer(f"👢 تم طرد {target.full_name}", parse_mode=None)
    except TelegramBadRequest:
        await message.answer("❌ لا يمكنني طرد هذا العضو.", parse_mode=None)


@router.message(Command("mute"))
@router.message(Command("كتم"))
async def mute_user(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو المراد كتمه.", parse_mode=None)
        return
    target = message.reply_to_message.from_user
    from aiogram.types import ChatPermissions
    permissions = ChatPermissions(can_send_messages=False)
    try:
        await bot.restrict_chat_member(message.chat.id, target.id, permissions)
        await message.answer(f"🔇 تم كتم {target.full_name}", parse_mode=None)
    except TelegramBadRequest:
        await message.answer("❌ لا يمكنني كتم هذا العضو.", parse_mode=None)


@router.message(Command("unmute"))
@router.message(Command("فك_الكتم"))
async def unmute_user(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو المراد فك كتمه.", parse_mode=None)
        return
    target = message.reply_to_message.from_user
    from aiogram.types import ChatPermissions
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_audios=True,
        can_send_documents=True,
        can_send_photos=True,
        can_send_videos=True,
        can_send_other_messages=True,
    )
    try:
        await bot.restrict_chat_member(message.chat.id, target.id, permissions)
        await message.answer(f"✅ تم فك كتم {target.full_name}", parse_mode=None)
    except TelegramBadRequest:
        await message.answer("❌ تعذر فك الكتم.", parse_mode=None)


@router.message(Command("warn"))
@router.message(Command("تحذير"))
async def warn_user(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على رسالة العضو المراد تحذيره.", parse_mode=None)
        return
    target = message.reply_to_message.from_user
    args = message.text.split(maxsplit=1)
    reason = args[1] if len(args) > 1 else "بدون سبب"
    from app.database.db import add_warning
    count = await add_warning(message.chat.id, target.id, reason)
    await message.answer(
        f"⚠️ تحذير {count}/3

"
        f"👤 العضو: {target.full_name}
"
        f"📝 السبب: {reason}",
        parse_mode=None
    )


@router.message(Command("purge"))
@router.message(Command("مسح"))
async def purge_messages(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على الرسالة التي تريد الحذف منها.", parse_mode=None)
        return
    try:
        msg_id = message.reply_to_message.message_id
        deleted = 0
        for i in range(msg_id, message.message_id + 1):
            try:
                await bot.delete_message(message.chat.id, i)
                deleted += 1
            except Exception:
                pass
        await message.answer(f"🧹 تم حذف {deleted} رسالة.", parse_mode=None)
    except Exception as e:
        await message.answer(f"❌ خطأ: {e}", parse_mode=None)


@router.message(Command("pin"))
@router.message(Command("تثبيت"))
async def pin_message(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    if not message.reply_to_message:
        await message.reply("📌 رد على الرسالة المراد تثبيتها.", parse_mode=None)
        return
    try:
        await bot.pin_chat_message(
            message.chat.id,
            message.reply_to_message.message_id,
            disable_notification=False
        )
        await message.answer("📌 تم تثبيت الرسالة.", parse_mode=None)
    except TelegramBadRequest:
        await message.answer("❌ تعذر تثبيت الرسالة.", parse_mode=None)
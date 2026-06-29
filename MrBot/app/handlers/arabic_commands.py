from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


def multi_command(*names):
    def decorator(handler):
        for name in names:
            router.message(Command(name))(handler)
        return handler
    return decorator


@multi_command("ban", "حظر", "طرد_نهائي")
async def ban_arabic(message: Message):
    await message.reply("🚫 استخدم /ban أو /حظر (بالرد على العضو)", parse_mode=None)


@multi_command("kick", "طرد", "اخراج")
async def kick_arabic(message: Message):
    await message.reply("👢 استخدم /kick أو /طرد (بالرد على العضو)", parse_mode=None)


@multi_command("mute", "كتم", "سكوت")
async def mute_arabic(message: Message):
    await message.reply("🔇 استخدم /mute أو /كتم (بالرد على العضو)", parse_mode=None)


@multi_command("id", "ايدي", "هوية")
async def id_arabic(message: Message):
    user = message.from_user
    chat = message.chat
    text = (
        f"🆔 معلومات\n\n"
        f"👤 الاسم: {user.full_name}\n"
        f"🆔 ID: {user.id}\n"
        f"💬 Chat ID: {chat.id}\n"
        f"📛 النوع: {chat.type}"
    )
    await message.answer(text, parse_mode=None)


@multi_command("help", "مساعدة", "اوامر")
async def help_arabic(message: Message):
    text = (
        "📋 قائمة الأوامر\n\n"
        "🛡️ الإدارة:\n"
        "• /ban /حظر - حظر\n"
        "• /kick /طرد - طرد\n"
        "• /mute /كتم - كتم\n\n"
        "👥 المجموعة:\n"
        "• /rules /قوانين - قوانين\n"
        "• /id /ايدي - معلومات\n\n"
        "⚙️ عامة:\n"
        "• /ping /بنج - فحص\n"
        "• /help /مساعدة - هذه القائمة"
    )
    await message.answer(text, parse_mode=None)


@multi_command("ping", "بنج", "فحص")
async def ping_arabic(message: Message):
    await message.answer("🏓 pong", parse_mode=None)
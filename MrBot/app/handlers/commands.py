from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.core.logger import logger

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    """أمر البدء"""
    text = (
        f"👋 أهلاً {message.from_user.full_name}!

"
        f"🤖 أنا MrBot، بوت إدارة المجموعات المتكامل.

"
        f"📋 الأوامر المتاحة:
"
        f"• /help - قائمة الأوامر
"
        f"• /id - معلوماتك
"
        f"• /rules - قوانين الجروب
"
        f"• /settings - إعدادات الجروب

"
        f"➕ أضفني لمجموعتك واجعلني مشرفاً!"
    )
    await message.answer(text, parse_mode=None)


@router.message(Command("help"))
async def help_command(message: Message):
    """قائمة الأوامر"""
    text = (
        "📋 قائمة الأوامر

"
        "🛡️ الإدارة:
"
        "• /ban /حظر - حظر عضو
"
        "• /kick /طرد - طرد عضو
"
        "• /mute /كتم - كتم عضو
"
        "• /warn /تحذير - تحذير عضو
"
        "• /purge /مسح - حذف رسائل
"
        "• /pin /تثبيت - تثبيت رسالة

"
        "👥 المجموعة:
"
        "• /rules /قوانين - قوانين الجروب
"
        "• /id /ايدي - معلوماتك
"
        "• /admins /المشرفين - قائمة المشرفين
"
        "• /link /رابط - رابط الجروب

"
        "👋 الترحيب:
"
        "• /welcome /ترحيب - عرض الترحيب
"
        "• /setwelcome /تعيين_ترحيب - تعيين ترحيب

"
        "📝 الملاحظات:
"
        "• /save /حفظ - حفظ ملاحظة
"
        "• /get /جلب - عرض ملاحظة
"
        "• /notes /ملاحظات - قائمة الملاحظات

"
        "⚙️ عامة:
"
        "• /ping /بنج - فحص البوت
"
        "• /help /مساعدة - هذه القائمة"
    )
    await message.answer(text, parse_mode=None)


@router.message(Command("ping"))
async def ping_command(message: Message):
    """فحص البوت"""
    await message.answer("🏓 pong", parse_mode=None)
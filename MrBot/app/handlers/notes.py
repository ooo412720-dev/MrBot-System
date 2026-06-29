from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.database.db import save_note, get_note, get_notes, delete_note

router = Router()


@router.message(Command("save"))
@router.message(Command("حفظ"))
async def save_note_handler(message: Message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply("📝 الاستخدام: /حفظ <اسم> <نص>", parse_mode=None)
        return
    name = args[1]
    content = args[2]
    await save_note(message.chat.id, name, content, message.from_user.id)
    await message.answer(f"✅ تم حفظ: {name}", parse_mode=None)


@router.message(Command("get"))
@router.message(Command("جلب"))
async def get_note_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply("📝 الاستخدام: /جلب <اسم>", parse_mode=None)
        return
    note = await get_note(message.chat.id, args[1])
    if note:
        await message.answer(note.content, parse_mode=None)
    else:
        await message.answer("❌ غير موجود", parse_mode=None)


@router.message(Command("notes"))
@router.message(Command("ملاحظات"))
async def list_notes_handler(message: Message):
    notes = await get_notes(message.chat.id)
    if notes:
        text = "📋 الملاحظات:\n\n" + "\n".join([f"• {n.name}" for n in notes])
        await message.answer(text, parse_mode=None)
    else:
        await message.answer("ℹ️ لا توجد ملاحظات", parse_mode=None)


@router.message(Command("delete"))
@router.message(Command("حذف"))
async def delete_note_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await message.reply("📝 الاستخدام: /حذف <اسم>", parse_mode=None)
        return
    if await delete_note(message.chat.id, args[1]):
        await message.answer("✅ تم الحذف", parse_mode=None)
    else:
        await message.answer("❌ غير موجود", parse_mode=None)
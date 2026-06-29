from aiogram import Router, F
from aiogram.types import Message
import random

from app.database.db import add_points, get_filters

router = Router()


@router.message(F.text)
async def handle_text(message: Message):
    if message.from_user.is_bot:
        return
    
    # فلاتر
    if message.chat.type in ("group", "supergroup"):
        try:
            filters = await get_filters(message.chat.id)
            for f in filters:
                if f.word.lower() in message.text.lower():
                    await message.reply(f.reply, parse_mode=None)
                    return
        except:
            pass
    
    # نقاط
    try:
        await add_points(message.chat.id, message.from_user.id, 1)
    except:
        pass
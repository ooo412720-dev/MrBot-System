@router.message(Command("welcome"))
@router.message(Command("ترحيب"))
async def show_welcome(message: Message):
    settings = await get_or_create_group_settings(message.chat.id)
    if settings.welcome_text:
        formatted = settings.welcome_text.format(
            name=message.from_user.full_name,
            chat=message.chat.title or "الجروب"
        )
        await message.answer(f"👋 {formatted}", parse_mode=None)
    else:
        await message.answer("ℹ️ لم يتم تعيين ترحيب.", parse_mode=None)


@router.message(Command("setwelcome"))
@router.message(Command("تعيين_ترحيب"))
async def set_welcome(message: Message):
    if not message.from_user.is_chat_admin():
        await message.reply("❌ هذا الأمر للمشرفين فقط!", parse_mode=None)
        return
    args = message.text.split(maxsplit=1)
    text = args[1] if len(args) > 1 else None
    if not text:
        await message.reply("📝 اكتب رسالة الترحيب بعد الأمر.", parse_mode=None)
        return
    await update_group_setting(message.chat.id, "welcome_text", text)
    await message.answer("✅ تم تعيين رسالة الترحيب.", parse_mode=None)
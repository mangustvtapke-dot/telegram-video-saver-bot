import os
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN, SAVE_DIR

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

@dp.message_handler(content_types=[types.ContentType.VIDEO, types.ContentType.VIDEO_NOTE])
async def save_video(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "no_username"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if message.video:
        file_id = message.video.file_id
        original_name = message.video.file_name if message.video.file_name else "video.mp4"
    else:
        file_id = message.video_note.file_id
        original_name = "video_note.mp4"

    file = await bot.get_file(file_id)

    save_name = f"{username}_{user_id}_{timestamp}_{original_name}"
    save_path = os.path.join(SAVE_DIR, save_name)

    await bot.download_file(file.file_path, save_path)

    await message.reply(f"🎉 Видео сохранено!\n📁 Файл: `{save_name}`", parse_mode="Markdown")

    logging.info(f"Saved: {save_path}")

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.answer("Отправь мне видео, и я сохраню его на сервер! 🎥")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

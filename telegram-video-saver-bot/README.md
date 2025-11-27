# Telegram Video Saver Bot

Этот проект — Telegram‑бот, который автоматически сохраняет присланные ему видеоролики на локальный компьютер.

## 🚀 Возможности
- принимает видео и видеосообщения
- сохраняет файлы в папку `saved_videos`
- имя файла содержит username/ID + дату + оригинальное название
- отправляет уведомление о сохранении
- логирование действий

## 📦 Установка
```
pip install -r requirements.txt
```

## ▶️ Запуск
```
python bot.py
```

## 📁 Структура проекта
```
telegram-video-saver-bot/
│ bot.py
│ config.py
│ requirements.txt
│ README.md
└─saved_videos/
```

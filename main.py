from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

TELEGRAM_TOKEN = "8712510143:AAFYpWcZReFqyuoE7IkOr39zyR5UCbj8Shg"
OPENAI_API_KEY = os.getenv("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")

client = OpenAI(api_key="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")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Ты полезный ассистент."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()

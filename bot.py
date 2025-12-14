# Simple Telegram bot example (Python + python-telegram-bot)
# Usage: pip install python-telegram-bot
# This is an educational example — do NOT automate abuse or scams.

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# /start sends a generated code and a link to the page
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    code = '0000'  # for demo; generate securely in production
    url = f"https://your-username.github.io/fake-dia/index.html?code={code}"
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Привіт {user.first_name}! Ось твій код: {code}\nПосилання: {url}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    print('Bot started')
    app.run_polling()

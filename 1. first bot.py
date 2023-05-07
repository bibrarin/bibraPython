import logging
import json
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola soy un bot, qué deseas pequeño saltamontes?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
    
async def suma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        a = int(update.message.text.split()[1])
        b = int(update.message.text.split()[2])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=a + b)
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error, debes ingresar dos numeros")

if __name__ == '__main__':
    application = ApplicationBuilder().token('my_telegram_token').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    application.add_handler(CommandHandler('suma', suma))
    
    application.run_polling()
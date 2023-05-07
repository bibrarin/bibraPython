import logging
import wikipedia
import constantes
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

# Función para manejar el comando "/wiki"
async def wiki(update, context):
    # Obtener el término de búsqueda del usuario a partir del comando
    search_term = ' '.join(context.args)

    # Buscar en Wikipedia el término de búsqueda
    try:
        result = wikipedia.summary(search_term)
        context.bot.send_message(chat_id=update.message.chat_id, text=result)
    except wikipedia.exceptions.PageError:
        context.bot.send_message(chat_id=update.message.chat_id, text='No se encontró ninguna página en Wikipedia para "{}".'.format(search_term))
    except wikipedia.exceptions.DisambiguationError as e:
        context.bot.send_message(chat_id=update.message.chat_id, text='La búsqueda "{}" es ambigua. Por favor, especifique uno de los siguientes términos:\n{}'.format(search_term, '\n'.join(e.options[:10])))



if __name__ == '__main__':
    application = ApplicationBuilder().token(constantes.MY_TELEGRAM_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    application.add_handler(CommandHandler('suma', suma))
    application.add_handler(CommandHandler('wiki', wiki))
    
    application.run_polling()
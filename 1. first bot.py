import logging
import constantes
import requests 
import datetime
import openai
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hola soy un bot, ¿qué deseas pequeño saltamontes?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    
async def suma(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        a = int(update.message.text.split()[1])
        b = int(update.message.text.split()[2])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=a + b)
    except:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error, debes ingresar dos numeros")

async def euribor(update: Update, context: ContextTypes.DEFAULT_TYPE):
        # Conexión con la página web
        url = "https://www.euribordiario.es/euriboractual.html"
        response = requests.get(url)
        fecha_hoy = datetime.date.today()
        fecha_hoy_str = fecha_hoy.strftime('%d/%m/%Y')

        # Análisis del contenido HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Extracción de datos
        title = soup.title.string
        paragraphs = [p.text for p in soup.find_all("p")]

        indice_porcentaje = paragraphs[1].find('%')

        # Si no se encuentra el carácter %, retorna un mensaje de error
        if indice_porcentaje == -1:
            print('No se encontró el carácter %')
        # Si se encuentra el carácter %, obtiene los 10 caracteres anteriores al carácter %
        else:
            caracteres_anteriores = paragraphs[1][max(0, indice_porcentaje - 5):indice_porcentaje]

        await context.bot.send_message(chat_id=update.effective_chat.id, text='Hoy ' + fecha_hoy_str + ' el valor del Euribor es de: ' + caracteres_anteriores + ' %')




async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    openai.api_key = constantes.MY_CHATGPT_TOKEN

    # Contexto del asistente
    messages = [{"role": "system", "content" : "Eres un asistente de partidas de rol de D&D"}]
   # content = input("¿Sobre qué quieres hablar, pequeño saltamontes? ")
    messages.append({"role": "user", "content" : update.message.text})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    response_context = response.choices[0].message.content

    messages.append({"role": "assistant", "content" : response_context})  

    await context.bot.send_message(chat_id=update.effective_chat.id, text= response_context)




if __name__ == '__main__':
    application = ApplicationBuilder().token(constantes.MY_TELEGRAM_TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(CommandHandler('suma', suma))
    application.add_handler(CommandHandler('euribor', euribor))
    application.add_handler(CommandHandler('chat', chat))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    application.add_handler(start_handler)
    
    application.run_polling()
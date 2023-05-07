import logging
import random
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

async def passw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=("Cual quieres que sea la longitud de la contraseña? (8-16): "))
"""  
    length = str(input("Cual quieres que sea la longitud de la contraseña? (8-16): "))
    want_upper = input("Quieres que contenga letras mayúsculas? (y,n): ")
    want_num = input("Quieres que contenga numeros? (y,n): ")
    want_simb = input("Quieres que contenga símbolos? (y,n): ")

    count = 1
    password = ""
    choosed = list()

    while(count <= int(length)):
        lower = chr(random.randrange(97, 122))
        choosed.append(lower)

        if(want_upper == "y"):
            upper = chr(random.randrange(65, 90))
            choosed.append(upper)

        if(want_num == "y"):
            num = random.randint(1,9)
            choosed.append(str(num))

        if(want_simb == "y"):      
            simb = random.choice((chr(random.randrange(33, 47)), chr(random.randrange(58, 64)), chr(random.randrange(91, 96))))
            print(simb)
            choosed.append(simb)

        password += random.choice(choosed)
        count += 1
    return password

print(passw())
"""


if __name__ == '__main__':
    application = ApplicationBuilder().token('my_telegram_token').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), echo))
    application.add_handler(CommandHandler('suma', suma))
    application.add_handler(CommandHandler('passw', passw))
    
    application.run_polling()
import asyncio
import telegram
import json, constantes

### Escribe nombre del bot ###


# Abrir el archivo de configuración y cargar la información
with open('config.json', 'r') as f:
    config = json.load(f)

print(config['my_telegram_token'])
print(constantes.MY_TELEGRAM_TOKEN)

bot = telegram.Bot(token=constantes.MY_TELEGRAM_TOKEN)

async def initialize_bot():
    await bot.initialize()

loop = asyncio.get_event_loop()
loop.run_until_complete(initialize_bot())

# Ahora puedes acceder a las propiedades del bot sin problemas
print(bot.username)
print(json.dumps(bot.to_dict()))







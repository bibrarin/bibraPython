import asyncio
import telegram
import json, constantes

### Escribe nombre del bot ###

bot = telegram.Bot(token=constantes.MY_TELEGRAM_TOKEN)

async def initialize_bot():
    await bot.initialize()

loop = asyncio.get_event_loop()
loop.run_until_complete(initialize_bot())

# Ahora puedes acceder a las propiedades del bot sin problemas
print(bot.username)
print(json.dumps(bot.to_dict()))







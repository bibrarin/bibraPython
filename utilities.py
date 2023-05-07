import json, constantes

## 1. Para llamar a una constante, como el TOKEN de Telegram ##

# 1.1 Abrir el archivo de configuración (config.json) y cargar la información
with open('config.json', 'r') as f:
    config = json.load(f)
print(config['my_telegram_token']) 

# 1.2 En fichero de constantes
print(constantes.MY_TELEGRAM_TOKEN)

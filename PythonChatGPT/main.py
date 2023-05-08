import openai
import constantes

openai.api_key = constantes.MY_CHATGPT_TOKEN

# Contexto del asistente
messages = [{"role": "system", "content" : "Eres un asistente de partidas de rol de D&D"}]


while True:

    content = input("¿Sobre qué quieres hablar, pequeño saltamontes? ")

    if content == "exit":
        break 

    messages.append({"role": "user", "content" : content})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    response_context = response.choices[0].message.content

    messages.append({"role": "assistant", "content" : response_context})  

    print(response_context)

import openai
import constantes
from rich import print
 
openai.api_key = constantes.MY_CHATGPT_TOKEN

with open("../contextoBot.txt", "r") as f:
    contenido = f.read()

    # Contexto del asistente
    messages = [{"role": "system", "content" : contenido}]

    while True:

        print("\n\n[bold blue]Pregunta sobre el mundo de fantasía >: [/bold blue]", end=" ")
        content = input()

        if content == "exit":
            break 

        messages.append({"role": "user", "content" : content})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        response_context = response.choices[0].message.content

        messages.append({"role": "assistant", "content" : response_context})  

        print(f"[bold green]\n\n{response_context}[/bold green]")
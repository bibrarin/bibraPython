import requests
from bs4 import BeautifulSoup

# Conexión con la página web
url = "https://www.euribordiario.es/euriboractual.html"
response = requests.get(url)

# Análisis del contenido HTML
soup = BeautifulSoup(response.content, "html.parser")

# Extracción de datos
title = soup.title.string
paragraphs = [p.text for p in soup.find_all("p")]

# Almacenamiento de datos
print(title)
print(paragraphs)
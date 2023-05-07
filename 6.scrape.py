import requests 
from bs4 import BeautifulSoup
import datetime

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

print('Hoy ' + fecha_hoy_str + ' el valor del Euribor es de: ' + caracteres_anteriores + ' %')


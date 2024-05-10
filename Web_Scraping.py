"""Como ejercicio modifique el script para obtener imagenes, en este caso, de perfiles de github. Luego visualiza la imagen """


import requests                        # se utiliza para realizar solicitudes HTTP.
from PIL import Image                  # se utiliza para vozualizar imagenes
from io import BytesIO                 # permite crear un flujo de bytes en memoria (como un archivo en memoria RAM) en lugar de en el disco duro.
from bs4 import BeautifulSoup as bs    # se utiliza para analizar y extraer datos de páginas web.


github_user = input('Input Github User: ')        # Solicita ingrese el nombre de usuario de GitHub.
url = 'https://github.com/' + github_user          # Crea la URL completa del perfil de GitHub concatenando el nombre de usuario proporcionado con la URL base de GitHub.
print(url)
r = requests.get(url)                              # Realiza una solicitud GET a la URL del perfil de GitHub.
soup = bs(r.content, 'html.parser')                # Analiza el contenido HTML de la página utilizando BeautifulSoup
profile_image = soup.find('img', class_='avatar')  #Busca la etiqueta <img> con el atributo alt igual a “Avatar” (que generalmente corresponde a la imagen de perfil) y extrae la URL de la imagen.

if profile_image:                          #imprime url de la imagen
    print(f"URL de la imagen de perfil: {profile_image['src']}")  
    response = requests.get(profile_image['src'] )           # Realiza la solicitud HTTP para obtener la imagen
    img_data = BytesIO(response.content)

    img = Image.open(img_data)             # Abre la imagen con PIL
    img.show()                             # Muestra la imagen
else:
    print("No se encontró la imagen de perfil para este usuario.")



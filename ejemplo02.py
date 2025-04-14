# coding=utf-8
__author__ = "Adonis Gramaje Victoria"
from bs4 import BeautifulSoup
import requests

# Programa principal
def main():
    print("Web Scrapping con BeautifulSoup")
    print("=" * 30)

    url = "https://www.elmundo.es/quijote/capitulo.html?cual=1"
    
    print("Accediendo a la página:", url)
    
    # Hacer la solicitud HTTP a la página
    resultado = requests.get(url)
    
    if resultado.status_code == 200:
        html = resultado.text
    else:
        print("Error al obtener la página:", resultado.status_code)
        return
    
    print("WEB SCRAPPING")
    print("=" * 30)

    # Usar BeautifulSoup para parsear el HTML
    sopa = BeautifulSoup(html, 'html.parser')
    
    # Prettify para mostrar el HTML formateado
    # print(sopa.prettify())  # Si quieres ver todo el HTML, descomenta esta línea

    # Extraer el contenido del div con id 'contenido'
    contenido_div = sopa.find('div', id='contenido')

    # Si no se encuentra el div, mostramos un error y terminamos el programa
    if not contenido_div:
        print("No se encontró el div con id 'contenido'.")
        return
    
    # Extraemos el texto
    texto = contenido_div.get_text()

    # Limpiar el texto
    txt = texto.replace("Prólogo", "").replace("Capítulo II", "")

    print(txt)

    # Guardamos el texto en un fichero
    nombreFichero = input("Introduzca el nombre del fichero a guardar: ")
    
    with open(nombreFichero, 'w', encoding='utf-8') as fichero:
        fichero.write("Don Quijote de la Mancha:\n")
        fichero.write("=" * 50 + "\n")
        fichero.write(txt)
    
    print(f"El fichero '{nombreFichero}' ha sido escrito.")

if __name__ == "__main__":
    main()

import os
import json
import sys
from get_movies import get_movies
import django

# Asegurarse de que el directorio raíz del proyecto esté en el sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviedle.settings')
django.setup()

def update_movie_files():
    # Define los archivos
    current_file = 'current_movies.json'
    next_file = 'next_movies.json'

    # Si existe el archivo 'next_movies.json', reemplaza 'current_movies.json'
    if os.path.exists(next_file):
        os.replace(next_file, current_file)
        print(f"* Archivo JSON {current_file} actualizado con contenido de {next_file}.\n")

    # Genera el nuevo 'next_movies.json'
    next_movies = get_movies()
    print(f"* Películas del siguiente mes generadas.\n")
    with open(next_file, 'w', encoding='utf-8') as json_file:
        json.dump(next_movies, json_file, ensure_ascii=False, indent=4)
    print(f"* Películas del siguiente mes guardadas correctamente.\n")

if __name__ == "__main__":
    update_movie_files()

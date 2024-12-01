import random
import requests
from django.conf import settings

def get_movies():
    # Define el endpoint base de TMDB
    url = "https://api.themoviedb.org/3/discover/movie"
    
    # Parámetros para la solicitud predefinidos
    base_params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
        "region": "ES",
        "sort_by": "vote_count.desc",
    }

    movies_list = [] # Lista para acumular las películas
    max_pages = 25 # Número máximo de páginas que quieres consultar

    for page in range(1, max_pages + 1):
        params = {**base_params, "page": page}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            results = response.json().get('results', [])
            movies_list.extend(results)
        else:
            print(f"Error fetching movies from page {page}: {response.status_code}")
            break
        
    # Selecciona 30 películas aleatorias si hay suficientes, o todas las disponibles
    if len(movies_list) >= 30:
        selected_movies = random.sample(movies_list, 30)
    else:
        selected_movies = movies_list

    return selected_movies
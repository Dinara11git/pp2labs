# function_arguments.py
"""
Функции с аргументами и примеры работы со списками словарей
"""

movies = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def check_score_greater(movie):
    """Возвращает True, если рейтинг IMDB фильма выше 5.5"""
    return movie['imdb'] > 5.5

def return_movie_category(movies, cat_name):
    """Возвращает список фильмов по категории"""
    return [m for m in movies if m['category'].lower() == cat_name.lower()]

# Примеры
if __name__ == "__main__":
    print("Hitman >", 5.5, ":", check_score_greater(movies[0]))
    print("Фильмы в категории Romance:", return_movie_category(movies, "Romance"))

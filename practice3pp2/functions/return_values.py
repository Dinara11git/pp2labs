# return_values.py
"""
Функции, которые возвращают значения, включая списки и вычисления среднего
"""

movies = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def sublist_movies_high_score(movies):
    """Возвращает список фильмов с рейтингом IMDB > 5.5"""
    return [m for m in movies if m['imdb'] > 5.5]

def avg_imdb_score(movies):
    """Вычисляет средний рейтинг IMDB для списка фильмов"""
    if not movies:
        return 0
    return sum(m['imdb'] for m in movies) / len(movies)

def avg_imdb_acc_to_cat(movies, cat_name):
    """Вычисляет средний рейтинг IMDB для фильмов определенной категории"""
    cat_movies = [m for m in movies if m['category'].lower() == cat_name.lower()]
    return avg_imdb_score(cat_movies)

# Примеры
if __name__ == "__main__":
    print("Фильмы с рейтингом >5.5:", sublist_movies_high_score(movies))
    print("Средний рейтинг всех фильмов:", avg_imdb_score(movies))
    print("Средний рейтинг Romance:", avg_imdb_acc_to_cat(movies, "Romance"))

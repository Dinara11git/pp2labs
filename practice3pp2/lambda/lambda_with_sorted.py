"""
Using lambda with sorted()
"""

movies = [
    {"name": "Movie A", "imdb": 7.0},
    {"name": "Movie B", "imdb": 9.0},
    {"name": "Movie C", "imdb": 6.5}
]

sorted_movies = sorted(movies, key=lambda x: x["imdb"])

print("Movies sorted by IMDB:", sorted_movies)

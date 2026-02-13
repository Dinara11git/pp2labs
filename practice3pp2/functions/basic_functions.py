# basic_functions.py
"""
Примеры простых функций в Python
"""

def grams_to_ounces(x):
    """Преобразует граммы в унции"""
    return 28.3495231 * x

def f_to_c(f):
    """Преобразует температуру из Фаренгейта в Цельсии"""
    return (5.0 / 9.0) * (f - 32)

def formula(R):
    """Вычисляет объем сферы по радиусу R"""
    return (4/3) * 3.141592 * R**3

# Примеры вызова
if __name__ == "__main__":
    print("10 грамм =", grams_to_ounces(10))
    print("100°F =", f_to_c(100))
    print("Объем сферы радиус 5 =", formula(5))

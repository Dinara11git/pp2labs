# args_kwargs.py
"""
Пример функций с *args и **kwargs
"""

def greet(*names, **messages):
    """
    Приветствует несколько людей по именам (*args)
    и выводит дополнительные сообщения (**kwargs)
    """
    for name in names:
        print(f"Hello, {name}!")
    for key, message in messages.items():
        print(f"{key}: {message}")

# Пример вызова
if __name__ == "__main__":
    greet("Alice", "Bob", morning="Good morning!", evening="Good evening!")

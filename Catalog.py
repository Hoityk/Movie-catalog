# catalog.py
# Інтерактивний прототип "Каталог фільмів" (Лабораторна робота №3)

import sys

movies = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "genre": "Sci-Fi",
        "rating": 8.8,
        "description": "A thief who steals corporate secrets through dreams."
    },
    {
        "id": 2,
        "title": "Interstellar",
        "year": 2014,
        "genre": "Sci-Fi",
        "rating": 8.6,
        "description": "A team travels through a wormhole in search of a new home for humanity."
    },
    {
        "id": 3,
        "title": "The Matrix",
        "year": 1999,
        "genre": "Action",
        "rating": 8.7,
        "description": "A hacker discovers a simulated reality."
    }
]


def list_movies():
    """Вивести список всіх фільмів"""
    print("\n📃 Усі фільми:")
    for m in movies:
        print(f"{m['id']}. {m['title']} ({m['year']}) — {m['genre']} — ⭐ {m['rating']}")
    print()


def search_movie():
    """Пошук фільму за назвою"""
    query = input("Введіть назву для пошуку: ").lower()
    results = [m for m in movies if query in m["title"].lower()]

    print("\n🔍 Результати пошуку:")
    if results:
        for m in results:
            print(f"{m['id']}. {m['title']} — ⭐ {m['rating']}")
    else:
        print("Нічого не знайдено.")
    print()


def filter_by_genre():
    """Фільтрація за жанром"""
    genre = input("Введіть жанр: ").capitalize()
    results = [m for m in movies if m["genre"] == genre]

    print(f"\n🎭 Фільми жанру {genre}:")
    if results:
        for m in results:
            print(f"{m['id']}. {m['title']} — ⭐ {m['rating']}")
    else:
        print("Нічого не знайдено.")
    print()


def show_movie_details():
    """Показати деталі фільму"""
    movie_id = int(input("Введіть ID фільму: "))
    movie = next((m for m in movies if m["id"] == movie_id), None)

    if movie:
        print("\n📌 Деталі фільму:")
        print(f"Назва: {movie['title']}")
        print(f"Рік: {movie['year']}")
        print(f"Жанр: {movie['genre']}")
        print(f"Рейтинг: {movie['rating']}")
        print(f"Опис: {movie['description']}\n")
    else:
        print("Фільм не знайдено.\n")


def add_movie():
    """Додавання нового фільму"""
    print("\n➕ Додати фільм")
    title = input("Назва: ")
    year = int(input("Рік: "))
    genre = input("Жанр: ")
    rating = float(input("Рейтинг: "))
    description = input("Опис: ")

    new_id = max(m["id"] for m in movies) + 1

    movies.append({
        "id": new_id,
        "title": title,
        "year": year,
        "genre": genre,
        "rating": rating,
        "description": description
    })

    print("Фільм успішно додано!\n")


def delete_movie():
    """Видалення фільму"""
    movie_id = int(input("Введіть ID фільму для видалення: "))
    global movies
    movies = [m for m in movies if m["id"] != movie_id]
    print("Фільм видалено (якщо існував).\n")


def update_movie():
    """Оновлення фільму"""
    movie_id = int(input("ID фільму для оновлення: "))
    movie = next((m for m in movies if m["id"] == movie_id), None)

    if not movie:
        print("Фільм не знайдено.\n")
        return

    print("\nОставте порожнім, щоб не змінювати поле.")

    new_title = input(f"Нова назва ({movie['title']}): ") or movie['title']
    new_year = input(f"Новий рік ({movie['year']}): ")
    new_year = int(new_year) if new_year else movie['year']
    new_genre = input(f"Новий жанр ({movie['genre']}): ") or movie['genre']
    new_rating = input(f"Новий рейтинг ({movie['rating']}): ")
    new_rating = float(new_rating) if new_rating else movie['rating']
    new_description = input(f"Новий опис ({movie['description']}): ") or movie['description']

    movie.update({
        "title": new_title,
        "year": new_year,
        "genre": new_genre,
        "rating": new_rating,
        "description": new_description
    })

    print("Фільм оновлено!\n")


def main():
    while True:
        print("========== КАТАЛОГ ФІЛЬМІВ ==========")
        print("1. Показати всі фільми")
        print("2. Пошук фільму")
        print("3. Фільтрація за жанром")
        print("4. Деталі фільму")
        print("5. Додати фільм")
        print("6. Видалити фільм")
        print("7. Оновити фільм")
        print("0. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            list_movies()
        elif choice == "2":
            search_movie()
        elif choice == "3":
            filter_by_genre()
        elif choice == "4":
            show_movie_details()
        elif choice == "5":
            add_movie()
        elif choice == "6":
            delete_movie()
        elif choice == "7":
            update_movie()
        elif choice == "0":
            print("Вихід...")
            sys.exit()
        else:
            print("Невірний вибір!\n")


if __name__ == "__main__":
    main()

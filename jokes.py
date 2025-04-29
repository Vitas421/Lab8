import requests

# Запит списку категорій
categories_url = "https://api.chucknorris.io/jokes/categories"
response = requests.get(categories_url)
categories = response.json()

# Виведення списку категорій
print("Доступні категорії:")
print(", ".join(categories))

# Введення категорії з клавіатури
selected_category = input("Введіть одну з категорій: ").strip().lower()

# Перевірка правильності введення
if selected_category not in categories:
    print("Такої категорії не існує.")
else:
    # Формування динамічного запиту
    api_url = f"https://api.chucknorris.io/jokes/random?category={selected_category}"
    joke_response = requests.get(api_url)
    joke_data = joke_response.json()

    # Парсинг і вивід потрібних полів
    print("\nРезультат:")
    print("Категорія:", selected_category)
    print("Дата створення:", joke_data["created_at"])
    print("Анекдот:", joke_data["value"])

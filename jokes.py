import requests

categories_url = "https://api.chucknorris.io/jokes/categories"
response = requests.get(categories_url)
categories = response.json()

print("Доступні категорії:")
print(", ".join(categories))
selected_category = input("Введіть одну з категорій: ").strip().lower()

if selected_category not in categories:
    print("Такої категорії не існує.")
else:
    api_url = f"https://api.chucknorris.io/jokes/random?category={selected_category}"
    joke_response = requests.get(api_url)
    joke_data = joke_response.json()
    
    print("\nРезультат:")
    print("Категорія:", selected_category)
    print("Дата створення:", joke_data["created_at"])
    print("Анекдот:", joke_data["value"])

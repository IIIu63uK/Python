import requests

# Отправляем GET-запрос к API
response = requests.get('https://jsonplaceholder.typicode.com/posts')

# Проверяем статус ответа
if response.status_code == 200:
    # Преобразуем ответ в JSON
    data = response.json()

    # Выводим первые 5 записей
    for post in data[:5]:
        print(post['title'])
else:
    print('Ошибка:', response.status_code)
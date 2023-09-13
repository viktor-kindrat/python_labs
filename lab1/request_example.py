import requests

# URL, до якого ви хочете виконати HTTP-запит
url = "https://randomuser.me/api/"  # або будь-який інший URL

# Виконання GET-запиту до вказаного URL
response = requests.get(url)

# Виведення вмісту відповіді на екран
print(response.text)

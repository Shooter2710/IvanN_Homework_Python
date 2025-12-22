import requests


baseURL = "https://ru.yougile.com"

payload = {
    "login": "",  # <- Ввести "логин"
    "password": "",  # <- Ввести "пароль"
    "companyId": ""  # <- Ввести "ID компании"
}

headers = {"Content-Type": "application/json"}

key = requests.post(baseURL+"/api-v2/auth/keys", json=payload, headers=headers)

print(key.text)

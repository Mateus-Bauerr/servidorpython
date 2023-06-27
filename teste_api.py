import requests

url = "mateus.pythonanywhere.com"  # Substitua pela URL correta do seu aplicativo

data = {
    "word": "hello",
    "language": "fr"
}

response = requests.post(url, json=data)

if response.status_code == 200:
    translation = response.json()["translation"]
    print("Tradução:", translation)
else:
    print("Erro na solicitação:", response.text)

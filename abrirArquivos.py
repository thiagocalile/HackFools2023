import requests
import time

base_url = "https://api.telegram.org/bot6279111723:AAFupEKg0K4Lgc1jORaUp0i2buJzs2lbNSU/sendPhoto"

endereco = [
    "usuarios/@calilecosta/photo1687112628 (2).jpeg",
    "usuarios/@OKuramae/photo1687112628 (1).jpeg",
    "usuarios/@pedrofioravanti/photo1687112628.jpeg"
]
for assinaturas in endereco:
    parameters = {
        "chat_id" : "-990175615",
        "photo" : assinaturas,
        "caption" : "Assina aí pra mim."
    }



resp = requests.get(base_url, data = parameters)
print(resp.text)
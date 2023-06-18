import requests
import time

base_url = "https://api.telegram.org/bot6279111723:AAFupEKg0K4Lgc1jORaUp0i2buJzs2lbNSU/sendPhoto"

endereco = [
    "https://prnt.sc/b36ozWyfYhEq",
    "https://prnt.sc/h3ud_g554qAP"
]
for assinaturas in endereco:
    parameters = {
        "chat_id" : "-990175615",
        "photo" : assinaturas,
        "caption" : "Assina aí pra mim."
    }


    resp = requests.get(base_url, data = parameters)
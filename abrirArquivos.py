import requests
import time

base_url = "https://api.telegram.org/bot6279111723:AAFupEKg0K4Lgc1jORaUp0i2buJzs2lbNSU/sendPhoto"

my_file = open("/content/sample_data/My_Image.png", "rb")

parameters = {
    "chat_id" : "-990175615",
    "caption" : "Assina aí pra mim."
}


files = {
    "photo" : my_file
}

resp = requests.get(base_url, data = parameters, files=files)
print(resp.text)
import requests
import json
import csv

token = "1605657594:AAHEV6lcdI3E92H7Skt-g_UN03kCMANaAc4"
request = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
data = request.json()
print(data)

with open("telegram_data_js.json", "w") as file:
    json.dump(data, file)
    

# # with open("telegram_data.csv", "w") as file:
# #     writer = csv.writer(file)
#     writer.writerows(data)
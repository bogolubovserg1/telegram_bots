import requests
import json

url = "https://tehnadzor.utnkr.ru/rest/report/475158/save/list"

payload = {}
headers = {'Authorization': 'Bearer d8d916cd00c3830d2392a68043a43500'}

response = requests.request("POST", url, headers=headers, data=payload)
message = json.loads(response.text)
last_save_id = message["saves"][0]["id"]


print(response.text, "\n\n")
print(last_save_id)


url2 = f'https://tehnadzor.utnkr.ru/rest/report/475158/save/{last_save_id}/data?chunk=1'

response2 = requests.request("POST", url2, headers=headers, data=payload)

report = json.loads(response2.text)
suma_ks = 0
suma_dor = 0
suma_for = 0

for j in range(3, 6):

    for i in range(1, len(report['data']['rows'])):
        report_data = report['data']['rows'][i]["items"][j]["text"]
        report_number = float(report_data.replace(",", ".").replace(" ", ""))
        if j == 5:
            suma_ks += report_number
        elif j == 3:
            suma_for += report_number
        elif j ==4:
            suma_dor += report_number


print(f"Общая сумма КС-2 {suma_ks}руб.")
print(f"Сумма КС-2 до выверки {suma_for}руб.")
print(f"На доработке {suma_dor}руб.")

print(len(report['data']['rows']))
print(last_save_id)

import requests
import threading


def send_withdraw_request(account_number, account_number1, amount):
    url = 'http://127.0.0.1:8000/api/v1/transfer/'
    headers = {'Content-Type': 'application/json'}
    data = {
        "from_account_number": account_number,
        "to_account_number": account_number1,
        "amount": amount
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.status_code, response.json())


account_number = "123456789"
account_number1 = "987654321"
amount = 100

threads = []
for _ in range(10):
    t = threading.Thread(target=send_withdraw_request, args=(account_number, account_number1, amount))
    t.start()
    threads.append(t)

for t in threads:
    t.join()



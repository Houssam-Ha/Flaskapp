import requests
import time
import threading

def make_request(cookie, url):
    headers = {

        "Cookie": cookie,


    }

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except ValueError:
        print("Invalid JSON response")
        return

    if 'code' in data:
        print(f"Message: {data['message']}")
    else:
        print("Invalid response format")

def run_scripts():
    cookies = [
        "user=285556493003",
    ]

    url = "https://faucetearner.org/api.php?act=faucet"

    while True:
        for cookie in cookies:
            thread = threading.Thread(target=make_request, args=(cookie, url))
            thread.start()
            thread.join()
        time.sleep(20)

run_scripts()

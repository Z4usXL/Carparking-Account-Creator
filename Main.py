import requests
import json
import random
def mm():
    length = random.randint(3, 10)
    number = ''.join(str(random.randint(0, 9)) for _ in range(length))

    email = f"byZeus#{number}@gmail.com"
    return email
DOSYA_ADI = "cpm.txt"
def save_to_file(content):
    with open(DOSYA_ADI, "a", encoding="utf-8") as f:
        f.write(content + "\n")
pp=[""]
proxy=random.choice(pp)
prxy = f"http://{proxy}"
proxies = {
    "http": prxy,
    "https": prxy
}
def worker():
    while not stop_event.is_set():
        url = "https://rantey.com/pages/car-parking-multiplayer/api.php"
        email=mm()
        payload = {
  "email": email,
  "password": "aabbcc11@",
  "ticket": "t03tserverZKp2VkewU5U1ZOuCy2ZIkIHWk-sg2vkTeBWSfXiyiYOezRTu7LcBOkjQYfUo2dcFR7Fo25O__dkyj_4rCJzXC3noSGhUhhH5oinHaVBeNgBdUL0CTV7WRJprqWjotONqUepGi9i6iBk*",
  "randstr": "@tJr",
  "instagram_followed": True,
  "telegram_joined": True,
}
        headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Mobile Safari/537.36",'Origin': "https://rantey.com",'Sec-Fetch-Site': "same-origin"}
        session=requests.session()
        response = session.post(url,data=json.dumps(payload),headers=headers,proxies=proxies)
        data = response.json()
        if data.get("success"):
            acc = data.get("account", {})
            aa=f"""
🚗 === CAR PARKING ACCOUNT CREATED ===

📧 Email        : {acc.get('email')}
🔑 Password     : {acc.get('password')}

💰 --- Balance ---
💵 Money        : {acc.get('money')}
🪙 Coins        : {acc.get('coin')}

🎁 --- Bonus ---
💸 Bonus Money  : {acc.get('bonus_money')}
🪙 Bonus Coins  : {acc.get('bonus_coin')}
"""
            mail_pass = f"{acc.get('email')}:{acc.get('password')}"
            save_to_file(mail_pass)
            print(aa)
        else:
            print(response.text)
    
import threading
import time

stop_event = threading.Event()

threads = []

for i in range(1):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

try:
    stop_event.wait()
except KeyboardInterrupt:
    stop_event.set()

for t in threads:
    t.join()

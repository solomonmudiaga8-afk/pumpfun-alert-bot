
import os
import json
import urllib.request

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = json.dumps({
        "chat_id": CHAT_ID,
        "text": message
    }).encode()

    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req, timeout=15) as response:
        print(response.read().decode())

def main():
    message = (
        "✅ Pump.fun alert bot don connect!\n\n"
        "This na test message. Next, we go connect "
        "the new-token monitoring system."
    )
    send_alert(message)

if __name__ == "__main__":
    main()

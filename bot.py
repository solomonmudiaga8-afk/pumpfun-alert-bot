
import os
import json
import urllib.request
import urllib.error

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def main():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = json.dumps({
        "chat_id": CHAT_ID,
        "text": "Hello bro! Your Pump.fun alert bot test don work!"
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Telegram error details:")
        print(e.read().decode("utf-8"))
        raise

if __name__ == "__main__":
    main()


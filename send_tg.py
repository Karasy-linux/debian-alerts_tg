import config
import requests
import sys


def send_telegram(text):
    
    token = config.BOT_TOKEN
    chat_id = config.CHAT_ID
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": text
    }
    
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Повідомлення надіслано!")
        else:
            print(f"Помилка Telegram: {response.text}")
    except Exception as e:
        print(f"Помилка мережі: {e}")

if __name__ == "__main__":
    # if you want write on konsole: python3 send_tg.py
    message = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Тестове повідомлення"
    send_telegram(message)
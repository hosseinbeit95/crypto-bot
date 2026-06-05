import requests

TOKEN = "8902701930:AAGvfU8HwnRIY6KFABZqy6bOc8qH2zaWx8M"
CHAT_ID = "436233523"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

send("سلام حسین! رباتت فعاله 😎")

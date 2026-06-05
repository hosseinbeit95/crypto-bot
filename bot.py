import requests

TOKEN = "8902701930:AAGvfU8HwnRIY6KFABZqy6bOc8qH2zaWx8M"
CHAT_ID = "436233523"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def binance_listings():
    url = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&page=1&pageSize=20"
    r = requests.get(url).json()
    items = r.get("data", {}).get("articles", [])
    results = []
    for x in items:
        title = x.get("title", "")
        if "list" in title.lower():
            results.append("📌 Binance Listing:\n" + title)
    return results

def binance_delistings():
    url = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&page=1&pageSize=20"
    r = requests.get(url).json()
    items = r.get("data", {}).get("articles", [])
    results = []
    for x in items:
        title = x.get("title", "")
        if "delist" in title.lower():
            results.append("❌ Binance Delisting:\n" + title)
    return results

def cmc_announcements():
    url = "https://api.coinmarketcap.com/data-api/v3/announcement/list?limit=20"
    r = requests.get(url).json()
    items = r.get("data", {}).get("list", [])
    results = []
    for x in items:
        title = x.get("title", "")
        if "list" in title.lower() or "delist" in title.lower():
            results.append("🌍 CMC:\n" + title)
    return results

def coingecko_news():
    url = "https://api.coingecko.com/api/v3/news"
    r = requests.get(url).json()
    items = r.get("data", [])
    results = []
    for x in items:
        title = x.get("title", "")
        if "list" in title.lower() or "delist" in title.lower():
            results.append("🦎 CoinGecko:\n" + title)
    return results

def main():
    msgs = []
    msgs += binance_listings()
    msgs += binance_delistings()
    msgs += cmc_announcements()
    msgs += coingecko_news()

    if not msgs:
        send("هیچ خبر جدیدی درباره لیست/دی‌لیست پیدا نشد.")
    else:
        for m in msgs:
            send(m)

main()

"""Fetch Coinbase Exchange daily BTC-USD closes from 2026-10-30 to now and write data/prices.json."""
import json, datetime, urllib.request
now = datetime.datetime.now(datetime.UTC)
url = ("https://api.exchange.coinbase.com/products/BTC-USD/candles?granularity=86400"
       f"&start=2026-10-30T00:00:00Z&end={now.strftime('%Y-%m-%dT%H:%M:%SZ')}")
req = urllib.request.Request(url, headers={"User-Agent": "btc-bottom-call/1.0"})
rows = json.load(urllib.request.urlopen(req, timeout=30))
prices = [{"date": datetime.datetime.fromtimestamp(r[0], datetime.UTC).strftime("%Y-%m-%d"), "close": r[4]}
          for r in sorted(rows) if r[0] <= 1797292800 + 86400 * 15]
json.dump({"source": "Coinbase Exchange daily candles (BTC-USD, UTC days; latest day may be partial)",
           "updated": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "prices": prices}, open("data/prices.json", "w"), indent=1)
print(prices[-1])

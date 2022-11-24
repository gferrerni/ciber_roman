from pysafebrowsing import SafeBrowsing
import os

API_KEY = os.getenv('API_KEY')

sb = SafeBrowsing(API_KEY)
r = sb.lookup_urls(["http://malware.wicar.org/data/js_crypto_miner.html"])
print(r)
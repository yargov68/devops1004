from datetime import datetime
import requests
print(datetime.now())

def url_caller(url):
response = request.get(url)
if response.status_code == 200:
    print(f"{url} is ok")
for url in ["https://gitub.com", "https://google.com"] :
    url_caller(url)

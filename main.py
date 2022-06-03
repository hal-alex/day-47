import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.co.uk/Soundcore-Bluetooth-Diaphragm-Technology-Waterproof/dp/B08BCHKY52/ref=sr_1_1_sspa?crid=1IH99HYRMESPP&keywords=anker%2Bsoundcore%2Bboost&qid=1654277168&sprefix=%2Caps%2C61&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE3WUVIM0NZRzhJRlcmZW5jcnlwdGVkSWQ9QTAwNzM5MzNUVjlGOUVQQU9DQlMmZW5jcnlwdGVkQWRJZD1BMDUzMzIzMjNQNTNHME1aMFVSSUsmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"

header = {
    "Accept-Language": "en,en-GB;q=0.9,en-US;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
}

result = requests.get(url=URL, headers=header).content

soup = BeautifulSoup(result, "lxml")

price = soup.find_all(name="span", class_="a-offscreen")
selected_price = price[0].text.split("£")[1]
print(selected_price)





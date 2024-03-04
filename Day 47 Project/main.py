import requests as r
import lxml
from bs4 import BeautifulSoup


# url = "https://www.amazon.com/INSIGNIA-42-inch-Class-Smart-NS-42F201NA23/dp/B0BCMND272/ref=sr_1_1?crid=23K2O75KYJFLZ&dib=eyJ2IjoiMSJ9.dAfeKoa8JCiYwZJ8oll1p-bXPGgdTWgC_AMHNd-9d9XIFn3_f-5Il8V3h4OnD2-vh2_aLXnGUuwAroI1QtIikiSNyj6zJxiJieiTUjzhnqWWA5aYRRBRaMylCsI12B-90xei4NoFeec7hmKxlxQA2pMXYJUOG8twntQLZ068vw7gzU7YhtjH6izN0vswINSSBAbEmOQRDK44rM04c7hYskbiv3oLs-551AWqvZCb4sQ.xkcntaY7BTaqgRJ4j-GZMrNtbR7fItqCGKeXOysCLo0&dib_tag=se&keywords=tv&qid=1709576852&sprefix=tv%2Caps%2C73&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"




URL = "https://www.amazon.com/INSIGNIA-42-inch-Class-Smart-NS-42F201NA23/dp/B0BCMND272/ref=sr_1_1?crid=23K2O75KYJFLZ&dib=eyJ2IjoiMSJ9.dAfeKoa8JCiYwZJ8oll1p-bXPGgdTWgC_AMHNd-9d9XIFn3_f-5Il8V3h4OnD2-vh2_aLXnGUuwAroI1QtIikiSNyj6zJxiJieiTUjzhnqWWA5aYRRBRaMylCsI12B-90xei4NoFeec7hmKxlxQA2pMXYJUOG8twntQLZ068vw7gzU7YhtjH6izN0vswINSSBAbEmOQRDK44rM04c7hYskbiv3oLs-551AWqvZCb4sQ.xkcntaY7BTaqgRJ4j-GZMrNtbR7fItqCGKeXOysCLo0&dib_tag=se&keywords=tv&qid=1709576852&sprefix=tv%2Caps%2C73&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"

params = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=params)

insignia_tv= BeautifulSoup(response.content, "html.parser")

price = insignia_tv.find(name="span", class_="a-offscreen").getText()
sale = insignia_tv.find(name="span", class_="a-size-base a-color-price a-color-price").getText()

print(price.getText())
print(F"This item is currently {sale.getText()} off!")
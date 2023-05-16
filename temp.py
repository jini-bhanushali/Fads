from bs4 import BeautifulSoup
import requests

url= "https://www.edmunds.com/volkswagen/jetta/2023/vin/3VWBM7BU5PM027690/?radius=50"

result = requests.get(url)
print(result.text)



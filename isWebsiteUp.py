import requests
import bs4 #pip install beautifulsoup4

product_url="https://docs.python.org/"

res = requests.get(product_url, timeout=5) 

print(res.status_code)

#print(res.text) # print content of website
soup = bs4.BeautifulSoup(res.text, 'html.parser')

elemnt = soup.select(".body > h1:nth-child(1)") # quated value can be find by rightclick text on web, click inspect then right click on highlighted object in inspectwindow and click copy>css selector

# for t in elemnt:
#     print(t)

print(elemnt[0].text)
if elemnt[0].text != "Python 3.12.1 documentation":
    print("website down")
else:
    print("website up")    
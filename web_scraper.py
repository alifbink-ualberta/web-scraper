from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

user_url = input("Enter url: ")

#connect with webpage and get html data.
url_req = urlopen(user_url)
html_code = url_req.read()
url_req.close()

#parse html data.
page_soup = soup(html_code, "html.parser")

#For pages in edition.cnn.com/travel:
#title:
title = page_soup.findAll("h1",{"class":"Article__title"})

print("\n" + title[0].text + "\n\n")


#article
paragraphs = page_soup.findAll("div",{"class":"Paragraph__component"})

for c in paragraphs:
    print(c.span.text)
    print("\n")

from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

user_url = input("Enter url: ")

#connect with webpage and get html data.
url_req = urlopen(user_url)
html_code = url_req.read()
url_req.close()

#parse html data.
page_soup = soup(html_code, "html.parser")

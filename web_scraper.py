from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#connect with webpage and get html data.
def get_webpage(user_url):
    url_req = urlopen(user_url)
    html_code = url_req.read()
    url_req.close()
    return html_code

#parse html data.
def parse_webpage(html_code):
    page_soup = soup(html_code, "html.parser")
    return page_soup

#For pages in edition.cnn.com/travel:
#title:
def print_title(page_soup):
    title = page_soup.findAll("h1",{"class":"Article__title"})
    print("\nTitle: " + title[0].text + "\n\n")

#subtitle


#latest date



#article
def print_paragraphs(page_soup):
    paragraphs = page_soup.findAll("div", class_ = "Paragraph__component")

    print("Article: \n")
    for c in paragraphs:
        print(c.span.text + "\n")


if __name__ == "__main__":
    user_url = input("Enter url: ")
    html_code = get_webpage(user_url)
    page_soup = parse_webpage(html_code)
    print_title(page_soup)
    #print_subtitle(page_soup)
    #print_latestdate(page_soup)
    print_paragraphs(page_soup)

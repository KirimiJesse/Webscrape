from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = Soup(page_html, "html.parser")

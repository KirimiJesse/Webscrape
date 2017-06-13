from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = Soup(page_html, "html.parser")

#grabs each product Total = 12 /test containers.len
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:	
	#brand = container.div.div.a.img["title"]
	title_container =container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	#print("brand"+ brand)
	print("product_name :" + " " + product_name)
	print("shipping :" + " " + shipping)
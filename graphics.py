from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

#opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs each product Total = 12 /test containers.len
containers = page_soup.findAll("div",{"class":"item-container"})
filename = "products.csv"
f = open(filename, "w")

headers = "product_name, shipping\n"

f.write(headers)

for container in containers:	
	#Somehow brand returns an Attribute "NONE" Error so I improvised "Hope it works"
	#brand = container.div.div.a.img["title"] //This should work
	title_container =container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li", {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	brand = product_name.split()[0]

	print("Brand : "+ " " + brand)
	print("Product_name :" + " " + product_name)
	print("Shipping :" + " " + shipping)

	f.write(brand + "," + product_name.replace(",", "/") + "," + shipping + "\n")

f.close()
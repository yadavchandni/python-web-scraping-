from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url= "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphic+card&N=-1&isNodeId=1"
uclient= ureq(my_url)

page_html= uclient.read()
uclient.close()

soup_page= soup(page_html, "html.parser")
#soup_page.h1.text  to extract data

containers=soup_page.findAll("div",{"class":"item-container"})

fname= "product.csv"
fo= open(fname,"w")

for container in containers:
    

    brand= container.div.div.a.img["title"]

    title_container= container.findAll("a",{"class":"item-title"})
    product_name= title_container[0].text


    shipping= container.findAll("li",{"class":"price-ship"})
    ship_price= shipping[0].text.strip()

    print( brand)
    print(product_name)
    print(ship_price)

    fo.write(brand + "," +product_name.replace(",","|") + "," + ship_price + "\n" )
fo.close()

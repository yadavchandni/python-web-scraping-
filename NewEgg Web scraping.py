from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

address= 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&N=-1&isNodeId=1'

my_url= urlopen(address)

page= my_url.read()
my_url.close()

data= bs(page,'html.parser')

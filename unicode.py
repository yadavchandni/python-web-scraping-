from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

address= 'http://www.unicode.org/emoji/charts/index.html'
page= urlopen(address)

page_html = page.read()
page.close()

containers= soup(page_html, "html.parser")

title_name= containers.head.title.text.strip()

print('Title : ',title_name)

mtag= containers.findAll('meta')

print(mtag[0],'\n\n',mtag[1])

words= containers.get_text()
words= words.split()

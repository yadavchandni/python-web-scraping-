from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def scrap(address):
    ur= urlopen(address)
    page= ur.read()
    ur.close()

    soup_page= bs(page, "html.parser")
    
    containers= soup_page.findAll("div",{"class":"_1UoZlX"})

    fname= 'flipkart_mobiles.csv'
    fo= open(fname,"a")

    #fo.write( 'Brand:' + ',' + 'Model:' + ',' + 'Price:' + ',' + 'RAM:' + ',' + 'ROM:' + ',' + 'Processor:' + ',' + 'Camera:' + ',' + 'Battery:' +  '\n')

    for each in containers:
        
        title= ((((each.findAll("div",{"class":"_3wU53n"}))[0].text).split(' ('))[0]).split(None,1)   
        brand= title[0]
        model= title[1]

        #price
        money= ((each.findAll('div',{'class':'_1vC4OE _2rQ-NK'}))[0].text)[1::]
        price=''
        for i in money:
            if i!=',':
                price+=i
        
        #description
        li= each.findAll('li',{'class':'tVe95H'})

        for x in li:

            if 'RAM' in x.text:
                #li[0] containes ram and rom
                mem= x.text.split(' | ',2)
                ram= mem[0]
                rom= mem[1]

            if 'Camera' in x.text:
                #li[2] containes camera
                cam= (x.text.split('Front'))[0]

            if 'Battery' in x.text:
                    #li[3]  containes battery
                    batt= (x.text.split(' '))[0]

            if 'Processor' in x.text:
                
                #li[4] containes processor
                proc= (x.text.split(' Processor'))[0]

        fo.write( brand + ',' + model + ',' + price + ',' + ram + ',' + rom + ',' + proc + ',' + cam + ',' + batt + ',' +  '\n')



    fo.close()





address= input('enter URL of Mobiles at Flipkart.com: ')
scrap(address)

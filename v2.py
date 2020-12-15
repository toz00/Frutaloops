import requests
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from prettytable import PrettyTable
from statistics import mean


op = webdriver.ChromeOptions()
#op.add_argument('headless')
op.add_argument('log-level=3')
op.add_argument('--disable-blink-features=AutomationControlled')
op.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

driver = webdriver.Chrome('./chromedriver.exe',options=op)

table= PrettyTable()

#tiendra inglesa fruits URL, vegetables URL, fruits page number, vegetables page number
tiendaURL = [r'https://www.tiendainglesa.com.uy/busqueda?0,0,*:*,1894,195,0,sortingname%20asc,%5B%5D,false,%5B%5D,%5B%5D,,',
r'https://www.tiendainglesa.com.uy/busqueda?0,0,*:*,1894,196,0,sortingname%20asc,%5B%5D,false,%5B%5D,%5B%5D,,',
3,9
]

#two page of tata's fruit and vegetales
tataURL= ["https://www.tata.com.uy/frescos/frutas-y-verduras?O=OrderByNameASC&ft&pageNumber=1&sc=4",
"https://www.tata.com.uy/frescos/frutas-y-verduras?O=OrderByNameASC&ft&pageNumber=2&sc=4"
]


def tiendacheck(URL):
    """Check and scrap each item in tienda inglesa webpage
    output one sorted by name list [[itemname,itemprice],[...]]
    """
    nomprix = []
    #scrap each URL in URL
    for j in range(URL[2]+URL[3]):

        print ("processing page " + str(j) )

        if (j < URL[2]):

            driver.get(URL[0]+str(j))
            time.sleep(4)
        else:
            driver.get(URL[1]+str(j-URL[2]))
            time.sleep(4)

        #get full html in soup
        soup = BeautifulSoup(driver.page_source,'html.parser')

        #remove div price per kg
        for font in soup.find_all(class_="ProductPriceLight"):
            font.decompose()
        #find all products name containers
        noms = soup.findAll(class_="wCartProductName")


        #find all products price containers
        prix = soup.findAll(class_="tblSearchPrice")

        for i in range(len(noms)):
            nomstr = noms[i].findAll('a')
            nomstr = str(nomstr[0].string)

            prixstr = str(prix[i])
            nomprix.append(
            #find the exact name and price in each container
            [nomstr,
            prixstr[int(prixstr.find('$'))+2:int(prixstr.find("</di"))]]
            )




    nomprix.sort()
    return nomprix


def tatacheck(URL):
    """Check and scrap each item in tata webpage
    output one sorted by name list [[itemname,itemprice],[...]]
    """
    nomprix = []
    #scrap each URL in URL
    for j in range(len(URL)):
        print ("processing page " + str(j) )

        driver.get(URL[j])
        time.sleep(3)

        try:
            #select montevideo and click ok if pop up
            driver.find_element_by_id("state").click()
            time.sleep(0.5)
            driver.find_element_by_id("react-select-2-option-1").click()
            time.sleep(1)

            try:
                submit_button = driver.find_element_by_class_name('bzYhsb')
                time.sleep(0.5)
                submit_button.click()
            except:
                pass
        except:
            pass
        time.sleep(4)

        #get full html in soup
        soup = BeautifulSoup(driver.page_source,'html.parser')

        #find all products name containers
        noms = soup.findAll(class_="iWTsYf")
        #find all products price containers
        prix = soup.findAll(class_="fVUXVk")

        #save names and price in returned list
        for i in range(len(noms)):
            nomstr = str(noms[i])
            prixstr = str(prix[i])
            nomprix.append(
            #find the exact name and price in each container
            [nomstr[int(nomstr.find('sYf">'))+5:int(nomstr.find("</h2>"))],
            prixstr[int(prixstr.find('$'))+1:int(prixstr.find("."))]]
            )




    nomprix.sort()
    return nomprix


tatanomsprix = tatacheck(URL=tataURL)

tiendainglesanomsprix = tiendacheck(URL=tiendaURL)


# create table top labels
table.field_names = ['{0:^40}'.format("Nombre"),'{0:^3}'.format("$$$")]

#populate table with tatanomsprix, items name and price
for i in range(len(tatanomsprix)):

    table.add_row(['{0:^40}'.format(tatanomsprix[i][0]),'{0:^3}'.format(tatanomsprix[i][1])])


for i in range(len(tiendainglesanomsprix)):

    table.add_row(['{0:^40}'.format(tiendainglesanomsprix[i][0]),'{0:^3}'.format(tiendainglesanomsprix[i][1])])

#convert and save table in html
#table_txt = table.get_string()
table_html = table.get_html_string()
with open('output.html','w') as file:
    file.write(table_html)
driver.close()

#convert and save table in html
#table_txt = table.get_string()
table_html = table.get_html_string()
with open('output.html','w') as file:
    file.write(table_html)
driver.close()

#first ugly learning version, please ignore ! :D
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from prettytable import PrettyTable
from statistics import mean
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome('./chromedriver',options=op)

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

table = PrettyTable()

supermercados = ["T. Inglesa","Disco","Geant","Tata","Devoto"]
frutaverdura =["Lugar","Banana", "Tomate", "Naranja", "Palta", "Moron","Palta"]



#banana Agent
print ("start bananas")
banana=[]

#tiendainglesa
banana.append([])
URL = 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Frutas/busqueda?0,0,banana,1894,195,0,rel,%5B%5D,false,%5B%5D,%5B%22group_1%22%5D,'
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='ProductPrice')

for i in range(len(results)):
    resultstr= str(results[i])
    banana[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find("<font class")]))



#disco
banana.append([])
URL = 'https://www.disco.com.uy/frescos/frutas-y-verduras/frutas/Frutas%20tropicales/Banana?PS=20&map=c,c,c,specificationFilter_2851,specificationFilter_3148&sc=4'
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")
try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='precio-por-unidad')

for i in range(len(results)):
    resultstr= str(results[i])

    banana[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></span>")]))

#geant
banana.append([])
URL = 'https://www.geant.com.uy/frescos/frutas-y-verduras/frutas?O=OrderByScoreDESC&FQ=specificationFilter_2851:Frutas%20tropicales&ft=banana&pageNumber=1'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='fjhhzf')


for i in range(len(results)):
    resultstr= str(results[i])
    banana[-1].append(int(resultstr[resultstr.find("x kg")-3:resultstr.find("x kg")-1]))

#tata
banana.append([])
URL = 'https://www.tata.com.uy/buscar?text=banana&whitelabelRFlag=1'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(3)
driver.find_element_by_id("state").click()
time.sleep(0.5)
driver.find_element_by_id("react-select-2-option-1").click()
time.sleep(1)
submit_button = driver.find_element_by_class_name('bzYhsb')
time.sleep(0.5)
try:
    submit_button.click()
except:
    pass
time.sleep(4)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='csCkcm')



resultstr= str(results)
banana[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find(".00")]))



#devoto
banana.append([])
URL = 'https://www.devoto.com.uy/frescos/frutas-y-verduras/frutas/Banana/Frutas%20tropicales?map=c,c,c,specificationFilter_3148,specificationFilter_2851&sc=3'
page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")
try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='precio-por-unidad')


for i in range(len(results)):
    resultstr= str(results[i])
    banana[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></span>")]))


#Tomate Agent
print ("start tomate")
tomate=[]

#tiendainglesa
tomate.append([])
tomate[-1].append(80)
tomate[-1].append(80)
"""
URL = 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Verduras/busqueda?0,0,tomate,1894,196,0,rel,%5B%22Otras%22%5D,false,%5B%5D,%5B%5D,'
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='ProductPrice')

for i in range(results):
    resultstr= str(results[i])
    tomate[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find("$")+4]))
"""


#disco
tomate.append([])
URL = 'https://www.disco.com.uy/frescos/frutas-y-verduras/verduras/tomate?PS=20&sc=4&O=OrderByNameASC'
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")

try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='precio-por-unidad')

del results[1]

for i in range(len(results)):
    resultstr= str(results[i])

    tomate[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></span>")]))

#geant
tomate.append([])
URL = 'https://www.geant.com.uy/frescos/frutas-y-verduras/verduras?O=OrderByScoreDESC&FQ=specificationFilter_3045:Tomate&ft=tomate&pageNumber=1'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='fjhhzf')


for i in range(len(results)):
    resultstr= str(results[i])
    tomate[-1].append(int(resultstr[resultstr.find("x kg")-3:resultstr.find("x kg")-1]))

#tata
tomate.append([])
URL = 'https://www.tata.com.uy/buscar?text=tomate&whitelabelRFlag=1'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(2)
#driver.find_element_by_id("state").click()
#time.sleep(0.5)
#driver.find_element_by_id("react-select-2-option-1").click()
#time.sleep(1)
#submit_button = driver.find_element_by_class_name("styles__Button-sc-15ln7eo-0")
#try:
#    submit_button.click()
#except:
#    pass
time.sleep(4)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='styles__PPUMPrice-sc-12qeqj4-0')


for i in range(1):
    resultstr= str(results[i])
    tomate[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find(".00 x kg")]))



#devoto
tomate.append([])
URL = 'https://www.devoto.com.uy/frescos/frutas-y-verduras/verduras/tomate?PS=20&sc=3&O=OrderByNameASC'
page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")

try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='precio-por-unidad')

del results[4]
del results[1]
for i in range(len(results)):
    resultstr= str(results[i])
    tomate[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></span>")]))


#Naranja Agent
print ("start naranja")
naranja=[]
naranja.append([75,88])

#tiendainglesa
"""
naranja.append([])
URL = 'https://www.tiendainglesa.com.uy/Categoria/Frescos/Frutas/busqueda?0,0,naranja,1894,195,0,rel,%5B%22Otras%22%5D,false,%5B%5D,%5B%5D,'
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='ProductPrice')

for i in range(len(results)):
    resultstr= str(results[i])
    naranja[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find("$")+5]))


"""
#disco
naranja.append([])
URL = 'https://www.disco.com.uy/frescos/frutas-y-verduras/frutas/Naranja?map=c,c,c,specificationFilter_3148&sc=4'
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")

try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='precio-por-unidad')


for i in range(len(results)):
    resultstr= str(results[i])

    naranja[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></span>")]))

#geant
naranja.append([])
URL = 'https://www.geant.com.uy/frescos/frutas-y-verduras/frutas?ft=naranja'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='fjhhzf')


for i in range(len(results)):
    resultstr= str(results[i])
    naranja[-1].append(int(resultstr[resultstr.find("x kg")-3:resultstr.find("x kg")-1]))

#tata
naranja.append([])
URL = 'https://www.tata.com.uy/buscar?text=naranja&whitelabelRFlag=1'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(2)
#driver.find_element_by_id("state").click()
#time.sleep(0.5)
#driver.find_element_by_id("react-select-2-option-1").click()
#time.sleep(1)
#submit_button = driver.find_element_by_class_name("styles__Button-sc-15ln7eo-0")
#try:
#    submit_button.click()
#except:
#    pass
time.sleep(4)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='styles__PPUMPrice-sc-12qeqj4-0')


#for i in range(1):
resultstr= str(results)
naranja[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find(".00 x kg")]))



#devoto
naranja.append([])
URL = 'https://www.devoto.com.uy/frescos/frutas-y-verduras/frutas/Naranja?map=c,c,c,specificationFilter_3148&sc=3'
page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")

try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='precio-por-unidad')


for i in range(len(results)):
    resultstr= str(results[i])
    naranja[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></span>")]))


#palta Agent
print ("start palta")
palta=[]

#tiendainglesa
palta.append([])
URL = 'https://www.tiendainglesa.com.uy/busqueda?0,0,palta,0'
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='ProductPrice')


resultstr= str(results)
palta[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find("$")+4]))



#disco
palta.append([])
URL = 'https://www.disco.com.uy/palta?sc=4'
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")

try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

results = soup.findAll(class_='Product-price')


resultstr= str(results)

palta[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></div>")]))

#geant
palta.append([])
URL = 'https://www.geant.com.uy/busca?ft=palta'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='styles__BestPrice-i707hx-0')



resultstr= str(results)
palta[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find("</p>")]))

#tata
palta.append([])
URL = 'https://www.tata.com.uy/buscar?text=palta'
#page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(2)
#driver.find_element_by_id("state").click()
#time.sleep(0.5)
#driver.find_element_by_id("react-select-2-option-1").click()
#time.sleep(1)
#submit_button = driver.find_element_by_class_name("styles__Button-sc-15ln7eo-0")
#try:
#    submit_button.click()
#except:
#    pass
time.sleep(4)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='fVUXVk')


#for i in range(1):
resultstr= str(results)
palta[-1].append(int(resultstr[resultstr.find("$")+1:resultstr.find(".00")]))



#devoto
palta.append([])
URL = 'https://www.devoto.com.uy/palta?sc=3'
page = requests.get(URL,headers=headers)
driver.get(URL)
time.sleep(3)
submit_button = driver.find_element_by_id("btnConfirmaSucursal")

try:
    submit_button.click()
except:
    pass
time.sleep(5)
soup = BeautifulSoup(driver.page_source,'html.parser')


results = soup.findAll(class_='Product-price')



resultstr= str(results)
palta[-1].append(int(resultstr[resultstr.find("$ <span>")+8:resultstr.find("</span></div>")]))

print ("Naranjas ",naranja)
print ("Bananas ",banana)
print ("Tomates ",tomate)
print ("Palta",palta)

#supermercados = ["Tienda Inglesa","Disco","geant","Tata","devoto"]
#frutaverdura =["Lugar","Banana", "Tomate", "Naranja", "Palta", "Moron","Palta"]

table.field_names=["Lugar","Banana", "Tomate", "Naranja", "Palta"]
for i in range (5):
    table.add_row([supermercados[i],
    "max = " +str(max(banana[i]))+" med: " + str(round(mean(banana[i]),1)),
    "max = " +str(max(tomate[i]))+" med: "+ str(round(mean(tomate[i]),1)),
    "max = " +str(max(naranja[i]))+" med: " + str(round(mean(naranja[i]),1)),
    "max = " +str(max(palta[i]))+" med: "+ str(round(mean(palta[i]),1))
    ])
table_txt = table.get_string()
with open('output.txt','w') as file:
    file.write(table_txt)
print (table)

from bs4 import BeautifulSoup
import requests
import re
import csv
import pandas as loza


response=requests.get("https://www.olx.com.eg/en/ad/%D8%B3%D9%83%D9%88%D8%AF%D8%A7-%D9%83%D9%88%D8%AF%D9%8A%D8%A7%D9%83-%D8%AF%D9%8A%D9%86%D8%A7%D9%85%D9%8A%D9%83-%D9%A5-%D8%B1%D8%A7%D9%83%D8%A8-%D8%AE%D9%84%D9%8A%D8%AC%D9%89-%D9%85%D9%88%D8%AF%D9%8A%D9%84-2021-%D9%88%D8%A7%D9%84%D8%B3%D8%B9%D8%B1-%D9%82%D8%A7%D8%A8%D9%84-%D9%84%D9%84%D8%AA%D9%81%D8%A7%D9%88%D8%B6-ID195093210.html")

page=2
# # #link=requests.get("https://www.olx.com.eg/en/vehicles/cars-for-sale/cairo/?filter=new_used_eq_2%2Cyear_between_2000_to_2023")

while page!=78:
    root = f"https://www.olx.com.eg/en/vehicles/cars-for-sale/cairo/?page={str(page)}&filter=new_used_eq_2%2Cyear_between_2000_to_2023"
    link=requests.get(root)
    soup2=BeautifulSoup(link.content,'html.parser')
    page+=1
    links=soup2.find_all(href = re.compile("/en/ad")) ####han3mel profile aw company
    for i in links:
      sourceFile = open('links.txt', 'a')
      print(i['href'], file = sourceFile)
      sourceFile.close()
OutFile = open("C:\\AUC\\AUC sixth semester\\Database\\uniquelinks.txt","a")
InFile = open("C:\AUC\AUC sixth semester\Database\links.txt", "r")
lines_present = set()
for l in InFile:
   if l not in lines_present:
      OutFile.write(l)
      lines_present.add(l)
OutFile.close()
InFile.close()   
linksfile = open('uniquelinks.txt', 'r')
for line in linksfile:
  print(line)
  url="https://www.olx.com.eg"+line
  response=requests.get(url)
  soup=BeautifulSoup(response.content, 'html.parser')
  title = soup.find('h1', class_='a38b8112')
  s=soup.find_all("span", class_='_7978e49c _2e82a662')#details
  Details = soup.find_all("div", class_="b44ca0b3") 
 
  Description =soup.find_all("div", class_="_0f86855a")
  Features=soup.find_all("div", class_="_27f9c8ac")
  ad_id=soup.find("div", class_="_171225da")
  Loc=soup.find_all("span", class_="_8918c0a8") #this is an array with both the location and the creation date 
  date=soup.find("div", class_="_1075545d e3cecb8b _5f872d11")# this has a string with both loc and date 
  seller=soup.find_all("span", class_="_261203a9 _2e82a662") #index 1 is the name
  joined=soup.find("div", class_="_05330198") #member since
  sellerID = soup.find_all("div", class_="_1075545d d059c029")

#*******************FEATURES FILE***************************
  try:
    a=ad_id.get_text(strip=True)
    a = a.split(' ')  
    de=Details[0].contents[1].get_text(' ' , strip=True)#brand
  except:
    a=[0,0,0]
    de=" "
   
  featfile = open('Featuress.csv', 'a', encoding='utf-8-sig')
  if len(Features)!=0:
    for i in Features:
      for j in i:
        f=j.get_text(',', strip = True)
        featfile.write(a[2]+',')
        featfile.write(de+',')
        featfile.write(f)
        featfile.write('\n')
  featfile.close()
#*******************SELLER FILE***************************
  try:
    seller=seller[1].get_text(" ",strip=True)
  except:
    seller=" "
  sellerFinalID=""
  for data in sellerID:
    for link in data.find_all('a'):
        sellerFinalID=link['href']
     
  try:
    joined=joined.get_text(" ",strip=True).split("Member since ")
    joined=joined[1]

  except:
    joined=" "
  #joined=joined.get_text(" ",strip=True).split("Member since "

  pandasDataFrame = [{"sellerID":sellerFinalID, "Member_since": joined, "name": seller}]
  Sell = loza.DataFrame(pandasDataFrame)
  Sell.to_csv("seller.csv",sep=',', encoding = 'utf-8-sig', mode = "a",index= False, header = False )
 #*******************DETAILS FILE***************************
  #detailsFile = open('details.csv', 'a', encoding='utf-8-sig')
  try:
    a=ad_id.get_text()
    a = a.split(' ')
  except:
    a=[0,0,0]
    a[2]=" " 
  br = " "
  md= " "
  fuel =" "
  cp= " "
  po=" "
  cy=" "
  km_min=" "
  km_max= " "
  trans=" "
  color=" "
  body= " "
  cc_min=" "
  cc_max=" "
  desc=" "
  pt=" "
  
  for i in Details:
    if "Brand" in i.get_text(' ', strip=True):
     br=i.contents[1].get_text(' ' , strip=True)
    elif "Model" in i.get_text(' ', strip=True):
     md=i.contents[1].get_text(' ' , strip=True) 
    elif "Fuel Type" in i.get_text(' ', strip=True):
      fuel=i.contents[1].get_text(' ' , strip=True)
    elif "Price Type" in i.get_text(' ', strip=True):
     pt=i.contents[1].get_text(' ' , strip=True) 
    elif "Price" in i.get_text(' ', strip=True):
     cp=i.contents[1].get_text(' ' , strip=True) 
    elif "Payment Options" in i.get_text(' ', strip=True):
       po=i.contents[1].get_text(' ' , strip=True)
    elif "Year" in i.get_text(' ', strip=True):
      cy=i.contents[1].get_text(' ' , strip=True)
    elif "Kilometers" in i.get_text(' ', strip=True):
      km=i.contents[1].get_text(' ' , strip=True)
    
      if 'to' in km:
        
        km_min= km.split(" to")[0]
        km_max = km.split("to ")[1]
     
      elif 'More than' in km:
        kmss = km.split("More than ")
        km_min= kmss[0]
        km_max = " "
      else:
        km_min=" "
    elif "Transmission Type" in i.get_text(' ', strip=True):             
      trans=i.contents[1].get_text(' ' , strip=True)
    
    elif "Color" in i.get_text(' ', strip=True):
      color=i.contents[1].get_text(' ' , strip=True) 
    elif "Body Type" in i.get_text(' ', strip=True):
      body=i.contents[1].get_text(' ' , strip=True)
    elif "Engine Capacity (CC)" in i.get_text(' ', strip=True):
      cc=i.contents[1].get_text(' ' , strip=True) 
      if '-' in cc:
        
        cc_min = cc.split(" -")[0]
        cc_max= cc.split("- ")[1]
      elif 'More than' in cc:
        ccs= cc.split('More than ')
        cc_min= ccs[0]
        cc_max= " "
  try:
    Description =soup.find_all("div", class_="_0f86855a")
    desc=Description[0].get_text(" ", strip=True)
  except:
    desc=" "
  pandasDataFrame = [{"ad_id": a[2], "brand": br, "make": md, "caryear": cy,"price":cp,"transmission": trans, "body": body, "color": color, "min_CC":cc_min,"max_CC":cc_max, "fuel_type":fuel,"min_Kilos":km_min,"max_Kilos":km_max, "payment_method":po,"Description":desc}]
  deet = loza.DataFrame(pandasDataFrame)
  deet.to_csv("detailss1.csv",sep=',', encoding = 'utf-8-sig', mode = "a",index= False, header = False )


 #*******************ADS FILE***************************
  file = open('adddd.csv', 'a', encoding='utf-8-sig')
  try:
   a=ad_id.get_text(strip=True)
   t=title.get_text(strip=True)
  except AttributeError:
    a=" "
    t=" "
    p=" "
    d=" "

  space=0
  i=0
  c=0
  for j in a:
      if(a[i]==' '):
          space+=1
          c=i+1
      i+=1
  if(space>=2):
      file.write(a[c:])
      file.write(',')

  file.write(t)
  file.write(',')
  if a!=" ":
    for place in Loc[0]:
      p=place.get_text(strip=True)
      file.write(p+',')
    for place in Loc[1]:
      d=place.get_text(strip=True)
      file.write(d)

  file.write('\n')
file.close()

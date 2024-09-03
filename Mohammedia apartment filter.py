from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

features="xml"
html_text = requests.get('https://www.mubawab.ma/fr/st/mohammedia/appartements-a-louer' , 'lxml')
soup = BeautifulSoup(html_text.text , 'lxml')
page_num = soup.find_all('div' , class_="paginationDots sMargTop centered")

for page_num in range(1 , 7):
    url = f'https://www.mubawab.ma/fr/st/mohammedia/appartements-a-louer:p:{page_num}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    prices = soup.find_all('span' , class_ = "priceTag hardShadow float-right floatL")
    apartment_location = soup.find_all('h3' , class_= "listingH3")
    bedrooms = soup.find_all('div' , class_="inBlock w100")

    prices_list = []
    for p in prices: 
        prices_list.append(p.text.strip())


    apartment_location_list = []
    for l in apartment_location :
        location_text = l.text.strip()
        clean_location = re.sub(r'\s*à\s*Mohammedia\s*', '', location_text)
        apartment_location_list.append(clean_location)
    bedrooms_list = []
    for b in bedrooms : 
        bedrooms_list.append(b.text.strip())
    
min_length = min(len(prices_list), len(apartment_location_list), len(bedrooms_list))


prices_list = prices_list[:min_length]
apartment_location_list = apartment_location_list[:min_length]
bedrooms_list = bedrooms_list[:min_length]

df = pd.DataFrame({
    "cost": prices_list,
    "location": apartment_location_list,
    "bedrooms": bedrooms_list
})

df.to_csv(r"D:\vscode\python shi\python projects\rent_price_Mohammedia.csv" , index = False)
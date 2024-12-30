import requests
from bs4 import BeautifulSoup

def get_temp(day, area):
    url = 'https://tw.news.yahoo.com/weather/%E8%87%BA%E7%81%A3/%E8%87%BA%E5%8C%97%E5%B8%82/%E8%87%BA%E5%8C%97%E5%B8%82-2306179' 
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #open up the area
    elements = soup.find_all('li', class_='My(10px)')
    city_links = {}
    for element in elements:
        city_name = element.text.strip()
        city_link = element.find('a')['href']
        city_links[city_name] = city_link

    city_url = city_links[area]
    full_url = 'https://tw.news.yahoo.com' + city_url 
    response = requests.get(full_url)
    soup = BeautifulSoup(response.content, 'html.parser')
        
    # find all class with <dd>
    elements = soup.find_all('dd', class_='Mstart(5px) W(25px) Lh(2rem)')
    data = []
    for element in elements:
        text = element.text.strip()
        if text.endswith('%'):
            text = text[:-1]  
        try:
            number = int(text) 
            data.append(number)
        except ValueError:
            print(f"No data: {text}")
            continue
    #high temp
    elements = soup.find_all('dd', class_='D(n) celsius_D(b) W(25px)')
    data_high = []
    for element in elements:
        text = element.text.strip()
        if text.endswith('°'):
            text = text[:-1] 
        try:
            number = int(text) 
            data_high.append(number)
        except ValueError:
            print(f"No data: {text}")
            continue
    #low temp
    elements = soup.find_all('dd', class_='Pstart(10px) C($lowTemperatureColor) D(n) celsius_D(b) W(25px)')
    data_low = []
    for element in elements:
        text = element.text.strip()
        if text.endswith('°'):
            text = text[:-1]  
        try:
            number = int(text)  
            data_low.append(number)
        except ValueError:
            print(f"No data: {text}")
            continue
    
    return data_high[day], data_low[day], data[day]

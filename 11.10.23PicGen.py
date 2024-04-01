
import os
import openai
from datetime import datetime


from openai import OpenAI
import requests
import shutil

from bs4 import BeautifulSoup


import dotenv
#.env contains 'OPEN_API_KEY'
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')



def picGen():
    response = openai.Image.create(
        prompt=str(input('What do you want to see?')),
        n=1,
        size="1024x1024"
        )
    image_url = response['data'][0]['url']

    print(image_url)



def dallPicGen():
    client = OpenAI()


    response = client.images.generate(
    model="dall-e-3",
    prompt=str(input("What do you want to see?:")),
    size="1024x1024",
    quality="standard",
    n=1,
    )
    
    # Define the target directory
    target_directory = r"C:\Users\Andre\OneDrive\azj\Arcane\images"

    # Ensure the target directory exists, create it if necessary
    os.makedirs(target_directory, exist_ok=True)

    image_url = response.data[0].url

    image_response = requests.get(image_url, stream=True)
    image_response.raise_for_status()

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    filename = f"generated_image_{timestamp}.jpg"

    full_path = os.path.join(target_directory, filename)

    with open(full_path, "wb") as image_file:
        shutil.copyfileobj(image_response.raw, image_file)


# dallPicGen()

    

    # for item in box.find_all('li')[1:7]:
    #     idx +=1
    #     try:
    #         yahoo[item.find('a').get('href')] = {
    #             'link' : item.find('a').get('href'),
    #             'category' : item.get('data-property'),
    #             'title' : item.find_all('a')[1].text,
    #             'tags' : item.get('data-wikis')
    #         }
            

            
    #     except:
    #         continue

    # for link in yahoo.keys():
    #     try:
    #         r = requests.get(link)
    #         soup = BeautifulSoup(r.text, "html.parser")
    #         yahoo[link]['bodyText'] = soup.text
            
    #     except:
    #         continue

    

    # yahoo['title'] = 
   
    # return(yahoo['title'])


# print(yahooPull())


# Assuming 'box' is a BeautifulSoup element

# # Use CSS selector to mimic the XPath
# title_element = box.select_one('body > div:nth-child(3) > div > main > div:nth-child(4) > ul > li:nth-child(6) > div:nth-child(1) > div:nth-child(2) > h3 > a')

# # Check if the title_element exists before extracting text
# if title_element:
#     yahoo['title'] = title_element.get_text(strip=True)
#     return yahoo['title']
# else:
#     return None  # or handle the case where the element is not found

dallPicGen()
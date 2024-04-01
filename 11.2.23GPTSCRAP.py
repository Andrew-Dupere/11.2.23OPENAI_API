import os
import openai
import dotenv
#.env contains 'OPEN_API_KEY'
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def prompt(prompt, model):
    response = openai.Completion.create(
        model=model,
        prompt=prompt
    ).choices[0].text
    return response


def chat_with_gpt(model):
    print(f'Mode: {model} chat starting')

    while True:
        userInput = input(f'<{model}>::: ')
        
        if userInput.lower() == "x":
            print(f'GPT <{model}>| GoodBye')
            break
        
        response = prompt(userInput, model)
        print(f'GPT <{model}>| {response}')

def gptCompletions():

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
        ]
    )
    print(response)

def picGen():    
    response = openai.Image.create(
        prompt=str(input('What do you want to see?')),
        n=1,
        size="1024x1024"
        )
    image_url = response['data'][0]['url']

    print(image_url)


# chat_with_gpt(model='text-davinci-003')

picGen()


# gptCompletions()

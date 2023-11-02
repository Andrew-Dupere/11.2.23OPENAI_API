import os
import openai
import dotenv
#.env contains 'OPEN_API_KEY'

from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

import openai

def chat_with_gpt(model):
    print(f'GPT <{model}>|:::')

    while True:
        userInput = input(f'You: ')
        
        if userInput.lower() == "x":
            print(f'GPT <{model}>| Chat ended.')
            break
        
        response = prompt(userInput, model)
        print(f'GPT <{model}>| {response}')

def prompt(prompt, model):
    response = openai.Completion.create(
        model=model,
        prompt=prompt
    ).choices[0].text
    return response

if __name__ == "__main__":
    model = "text-davinci-003"  
    chat_with_gpt(model)


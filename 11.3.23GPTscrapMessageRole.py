import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

import GPTmodels

def sysUserPrompt():
#good character length with this style

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are an expert financial analyst"},
      {"role": "user", "content": "what is implied volatility>"}
    ]
  )
  return (completion.choices[0].message)


def prompt(prompt, model):
    response = openai.ChatCompletion.create(
        model=model,
        prompt=prompt
    ).choices[0].text
    return response


def chat_with_gpt(model):
    print(f'Model: {model} chat starting')

    while True:
        userInput = input(f'<{model}>::: ')
        
        if userInput.lower() == "x":
            print(f'GPT <{model}>| GoodBye')
            break
        
        response = prompt(userInput, model)
        print(f'GPT <{model}>| {response}')

# print(sysUserPrompt())

# chat_with_gpt('gpt-4-0613')
#messages is a required property

# chat_with_gpt(GPTmodels.turbo)

# print(GPTmodels.turbo)

# sysUserPrompt()
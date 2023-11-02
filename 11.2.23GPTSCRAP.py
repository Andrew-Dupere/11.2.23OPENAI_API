import os
import openai
import dotenv
#.env contains 'OPEN_API_KEY'

from dotenv import load_dotenv
load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

model = "text-davinci-003"

def prompt(prompt):
  
  response = openai.Completion.create(
  model=model,
  prompt=(prompt)
).choices[0].text
  return response

print(prompt(input(f'GPT <{model}>|')))

def contin(prompt):
    model = model
    print(f'GPT <{model}>|')
    while True:
        userInput = input('GPT:::')
        response = prompt(userInput, model)
        print(f'GPT <{model}>| {response}')

'_________________________________________________'

if __name__ == "__main__":
    model = "text-davinci-003"  # Define your GPT model here
    contin(model)


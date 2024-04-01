# from openai import transformers
import transformers
from tiktoken import Tokenizer

model = transformers.GPT2Tokenizer.from_pretrained("text-davinci-003")  # Replace with your model name

text = "Your text goes here."

# Initialize the tokenizer
tokenizer = Tokenizer(model)
tokens = tokenizer.count_tokens(text)

print(f"Token count: {tokens}")

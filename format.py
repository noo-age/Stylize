import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo-16k"
input = "texts/test.txt"
output = "texts/" + input[5:-4] + "_cleaned.txt"
system_message = "You will be given an excerpt of text from a novel. Remove all headers, quotes, and unnecessary newlines. Reformat the text so that it is correctly broken up into paragraphs if necessary. Make sure to separate dialogue into paragraphs as well."

def chunk_string(s, chunk_size=6000):
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

half_cleaned_text = ""

with open(input, 'r') as f:
    text = f.read()
    text = chunk_string(text)
    for element in text:
        completion = openai.ChatCompletion.create(
        model=model,
        temperature=0,
        max_tokens=2048,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": element}
        ]
        )
        half_cleaned_text += completion.choices[0].message.content

half_cleaned_text = half_cleaned_text.replace("\n\n", "\n")

with open(output, "w") as f:
    f.write(half_cleaned_text)

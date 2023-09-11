"""
Takes a specified text file and summarizes each line using GPT.
Appends the summary-original pairs as json objects to a specified .jsonl file. 
Modifies data slightly so it can be used for fine-tuning via the OpenAI API.
IMPORTANT: Change user_system_message depending on author of input.
Note: automatically removes double newlines from input text.
"""

import os
import openai
#from dotenv import load_dotenv
import json

#load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

model = "gpt-4"
jsonl_file = "data/09-06_chat.jsonl"
doc_file = "doc.txt"
user_system_message = ""
compression_system_message = "Summarize the given text in the same tense and point of view."
max_tokens = 1000

#appends prompt+completion string pair as a json object to file.jsonl
def append_to_jsonl(prompt, completion, file):
    data = {
        'messages': [
            {"role": "system", "content": user_system_message},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": completion}
        ]
    }
    json_data = json.dumps(data)
    
    if os.path.exists(file):
        append_write = 'a'  # Append to the existing file.
    else:
        append_write = 'w'  # Create the file if it doesn't exist.

    with open(file, append_write) as file:
        file.write(json_data)
        file.write('\n')
        
def remove_double_newlines(input):
    text = ""
    with open(input, 'r') as f:
        text = f.read()
        
    text = text.replace("\n\n", "\n")
    with open(input, 'w') as f:
        f.write(text)

remove_double_newlines(doc_file)

#reads doc.txt, creates summary of every line, and appends summary-original text pair to data.jsonl
with open(doc_file, 'r') as f:
    lines = f.readlines()
count = 0
for element in lines:
    if element == "":
        continue
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=0,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": compression_system_message},
            {"role": "user", "content": element}
        ]
    )
    append_to_jsonl(completion.choices[0].message.content,element,jsonl_file)
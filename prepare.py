"""
Takes a specified text file and summarizes each line using GPT.
Appends the summary-original pairs as json objects to a specified .jsonl file. 
Modifies data slightly so it can be used for fine-tuning via the OpenAI API.
"""

import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"
jsonl_file = "data/5-28.jsonl"
doc_file = "doc.txt"

#appends prompt+completion string pair as a json object to file.jsonl
def append_to_jsonl(prompt, completion, file):
    data = {
        'prompt': prompt,
        'completion': completion
    }
    
    json_data = json.dumps(data)
    
    if os.path.exists(file):
        append_write = 'a'  # Append to the existing file.
    else:
        append_write = 'w'  # Create the file if it doesn't exist.

    with open(file, append_write) as file:
        file.write(json_data)
        file.write('\n')


#reads doc.txt, creates summary of every line, and appends summary-original text pair to data.jsonl
with open(doc_file, 'r') as f:
    lines = f.readlines()
for element in lines:
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=0,
        max_tokens=256,
        messages=[
            {"role": "system", "content": "You will be given an excerpt from a text. Compress the excerpt as tightly as possible while keeping any important details, such as characters, dialogues, and passage of time. Mention at the beginning of your response whether the text is in first-person, second-person, or third-person."},
            {"role": "user", "content": element}
        ]
    )
    append_to_jsonl(completion.choices[0].message.content + " ->"," " + element + "###", jsonl_file)


        
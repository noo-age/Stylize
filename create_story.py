import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

style_model = "davinci:ft-personal-2023-07-02-00-29-14"
outfile = "out.txt"
infile = "in.txt"

#reads story from infile (paragraphs should be separated by two newlines)
raw_story = ""
with open(infile, 'r') as f:
    raw_story = f.read()

#split story into paragraphs
raw_story = raw_story.replace("\n\n", "\n")
raw_story = raw_story.split("\n")

stylized_story = ""
for paragraph in raw_story:
    style_completion = openai.Completion.create(
        model=style_model,
        prompt=paragraph + " ->",
        max_tokens=512,
        temperature=0.8,
        stop="###"
        )
    stylized_story += style_completion.choices[0].text

with open(outfile, "w") as f:
    f.write(stylized_story)
    
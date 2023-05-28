This repository is intended to allow you to copy an author's style using OpenAI's fine-tuning API.

# to use
Adjust the json_file and doc_file variables at the top of prepare.py. These are the output and input files respectively. Your input file should be a .txt file with your desired text, one line per paragraph or appropriate length of text. The output file should be a .jsonl file. Each line will contain a json object with a "prompt" and "completion." The "prompt" will be a GPT-generated summary of a line of your input file, and the "completion" will be the original line. 

Now that you have a .jsonl file for training, follow the instructions at https://platform.openai.com/docs/guides/fine-tuning to create a fine-tuned model. 

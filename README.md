This repository is intended to allow you to copy an author's style using OpenAI's fine-tuning API.


# to use
Adjust the json_file and doc_file variables at the top of prepare.py. These are the output and input files respectively. Your input file should be a .txt file with your desired text, one line per paragraph or appropriate length of text. The output file should be a .jsonl file. Each line will contain a json object with a "prompt" and "completion." The "prompt" will be a GPT-generated summary of a line of your input file, and the "completion" will be the original line. 

Now that you have a .jsonl file for training, follow the instructions at https://platform.openai.com/docs/guides/fine-tuning to create a fine-tuned model. 

# example

A stranger and I talk in the Alexanderplatz of Berlin. We talk lengthily about the price of bread, noting that it has gone above 5 marks per loaf.

### 

I have never had the pleasure of meeting my alter ego (if I may use the term), but long ago, in a place numberless miles beyond the black wastes wherein grim nations trample an evil past, I did have an exceedingly strange conversation with another stranger (perhaps another I) in the crowded Alexanderplatz of Berlin. I do not recall the date; let us say it was September 1914. It was not a very talkative Frenchest-y stranger who addressed me, but I talked (to myself, in retrospect) with great prolixity about the price of bread, which had just gone up to something over five marks per loaf. I argued with him interminably about that rise, noting with approval that the umbrage it had given rise to among the hungry masses was unappeasable and that proletarian mutterings were swelling to a roar. It pleased me to imagine my fellow stranger slightly bewildered by this strange talk.###

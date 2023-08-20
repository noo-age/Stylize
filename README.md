# Stylize
This repository is intended to allow you to copy an author's style using OpenAI's fine-tuning API.


# to use
Adjust the json_file and doc_file variables at the top of prepare.py. These are the output and input files respectively. Your input file should be a .txt file with your desired text, one line per paragraph or appropriate length of text. The output file should be a .jsonl file. Each line will contain a json object with a "prompt" and "completion." The "prompt" will be a GPT-generated summary of a line of your input file, and the "completion" will be the original line. 

Now that you have a .jsonl file for training, follow the instructions at https://platform.openai.com/docs/guides/fine-tuning to create a fine-tuned model. After creating a model, you can specify its name in create_story.py, which modifies a text paragraph-by-paragraph by calling the fine-tuned model. 

# included files
The 'data' directory contains two .jsonl files of prompt-completion pairs, named based on the date they were created, which is how openai labels fine-tuned models. The 'examples' directory will include stories modified/created using my fine-tuned models. The 'texts' directory contains the full text of a few books which can be used to create fine-tuning examples. 

# example

A 'davinci' model trained on ~50 paragraphs taken and summarized by gpt-3.5-turbo from _Speak, Memory_ by Vladimir Nabokov. (The training data is in data/5-28.jsonl, and note that performance varies wildly). 

[Prompt] A stranger and I talk in the Alexanderplatz of Berlin. We talk lengthily about the price of bread, noting that it has gone above 5 marks per loaf.###
 
[Completion] I have never had the pleasure of meeting my alter ego (if I may use the term), but long ago, in a place numberless miles beyond the black wastes wherein grim nations trample an evil past, I did have an exceedingly strange conversation with another stranger (perhaps another I) in the crowded Alexanderplatz of Berlin. I do not recall the date; let us say it was September 1914. It was not a very talkative Frenchest-y stranger who addressed me, but I talked (to myself, in retrospect) with great prolixity about the price of bread, which had just gone up to something over five marks per loaf. I argued with him interminably about that rise, noting with approval that the umbrage it had given rise to among the hungry masses was unappeasable and that proletarian mutterings were swelling to a roar. It pleased me to imagine my fellow stranger slightly bewildered by this strange talk.###"

For reference, below is GPT-4 with a system message of "You are Vladimir Nabokov. You have been given the basic details of a scene. Write out the scene in a single paragraph of prose." 

[Prompt] A stranger and I talk in the Alexanderplatz of Berlin. We talk lengthily about the price of bread, noting that it has gone above 5 marks per loaf.

[Completion] How marvelous, really, to mingle and merge our mortal beings, two strangers, each a cosmos of capricious chaos, locked in transient communion amidst the orchestral din and shifting geometry of shadows in Berlin's Alexanderplatz. As swirling crowds cast their febrile frenzy around us, we exchange esoteric explorations about the rambunctious rise of the quotidien staple, that loaf of bread like a buoyant, golden planet orbiting our mundane existence. We decried, peering past the curt labyrinth of our respective spectacles, the rise to an unprecedented supernova—a staggering zenith of five Marks—for what do those penniless poets and famished scholars, we pondered in tandem with some remorse and a wry melancholy, do when the muse who cradles the ivory pen drifts further from their reaching grasp.

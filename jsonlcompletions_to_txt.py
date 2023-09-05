import json

with open('data/6-07.jsonl', 'r') as json_file, open('texts/spkmem2.txt', 'w') as txt_file:
    for line in json_file:
        data = json.loads(line)
        if 'completion' in data:
            txt_file.write(data['completion'])
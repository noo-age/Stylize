
with open("texts/crime.txt", "r") as input_file, open("output_novel.txt", "w") as output_file:
    paragraph = []
    for line in input_file:
        line = line.strip()
        if line:
            paragraph.append(line)
        else:
            output_file.write(" ".join(paragraph) + "\n")
            paragraph = []
    if paragraph:
        output_file.write(" ".join(paragraph) + "\n")

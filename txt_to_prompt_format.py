import json
# Read txt file and make each sentence an element in a list
with open('./data/gettys_raw.txt') as f:
    lines = f.readlines()
    sentences = list()
    for line in lines:
        sentences_in_line = line.split(".")
        for sent in sentences_in_line:
            sentences.append(sent)
    
# Make each element in list as prompt completion format
# {"prompt":"", "completion":" Four score and seven years ago"}

with open('./data/output.jsonl', 'a') as the_file:
    for sent in sentences:
        if(len(sent) == 0):
            continue
        the_file.write('{"prompt":"", "completion":"'+ sent + '"}\n')
    
    # output = {}

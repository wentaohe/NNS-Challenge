def strip_nouns(question):
    #q = question.replace('?', '')
    words = question.split(' ')
    nouns = []
    for x in range(len(words)):
        if not words[x].startswith('NN'):
            nouns.append(words[x])
    return ' '.join(nouns)

#print(strip_nouns('how can i activate the NN2055 NN10190?'))
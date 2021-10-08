def find_nouns(question):
    
    #q = question.replace('?', '')
    words = question.split(' ') #get individual words
    nouns = []
    for x in range(len(words)):
        if words[x].startswith('NN'):
            nouns.append(words[x])
    return nouns
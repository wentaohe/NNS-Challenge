def load_questions():
    with open('/Users/wentao/Documents/Telepathy/NNS-Challenge/codes/questions.txt') as file:
        questions = file.readlines()
        questions = [line.rstrip() for line in questions]
    
    return questions
from load_questions import load_questions
from find_nouns import find_nouns
from strip_nouns import strip_nouns

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
    
old_questions = load_questions()
old_nouns_dictionary = dict.fromkeys(range(0, len(old_questions)))

for x in range(len(old_questions)):
    old_nouns_dictionary[x] = find_nouns(old_questions[x])

questions_without_nouns = []
questions_with_nouns = []
questions_with_nouns_stripped = []

for x in range(len(old_nouns_dictionary)):
    if len(old_nouns_dictionary[x])==0:
        questions_without_nouns.append(old_questions[x])
    else:
        questions_with_nouns_stripped.append(strip_nouns(old_questions[x]))
        questions_with_nouns.append(old_questions[x])

#print(questions_with_nouns)
#print(questions_with_nouns_stripped)
#print(questions_without_nouns)

def find_similar(new_question):
    
    model_name = 'bert-base-nli-mean-tokens'
    model = SentenceTransformer(model_name)

    nouns_in_new_question = find_nouns(new_question)
    #print(nouns_in_new_question)
    #print(len(nouns_in_new_question))

    if len(nouns_in_new_question) != 0:
        new_question = strip_nouns(new_question)
        old_sentence_vecs = model.encode(questions_with_nouns_stripped)
        new_sentence_vecs = model.encode(new_question)
    else:
        old_sentence_vecs = model.encode(questions_without_nouns)
        new_sentence_vecs = model.encode(new_question)

    similarity = cosine_similarity(
        [new_sentence_vecs],
        old_sentence_vecs
    )[0]
    sorted_similarity = [s[0] for s in sorted(enumerate(similarity), key=lambda i:i[1])]

    #print(sorted_similarity)
    #print(sorted_similarity[0])

    if len(nouns_in_new_question) != 0:
        print(questions_with_nouns[sorted_similarity[0]])
    else:
        print(questions_without_nouns[sorted_similarity[0]])

#find_nouns('how can i activate the NN2055 NN10190?')
#find_similar('how can i activate the NN2055 NN10190?')
find_similar('how fast can i run?')
#new_nouns = find_nouns('how can i activate the NN2055 NN10190?')
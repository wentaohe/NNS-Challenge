from load_questions import load_questions
from find_nouns import find_nouns
from strip_nouns import strip_nouns
from search_through_dict import search_through_dict

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

old_questions = load_questions()
old_nouns_dictionary = dict.fromkeys(range(0, len(old_questions)))

for x in range(len(old_questions)):
    old_nouns_dictionary[x] = find_nouns(old_questions[x].replace('?', ''))

questions_without_nouns = []
questions_with_nouns = []
questions_with_nouns_stripped = [] 
#stripped all the coded nouns to help with a more accurate understanding of words and syntax

for x in range(len(old_nouns_dictionary)):
    if len(old_nouns_dictionary[x])==0:
        questions_without_nouns.append(old_questions[x])
    else:
        questions_with_nouns_stripped.append(strip_nouns(old_questions[x]))
        questions_with_nouns.append(old_questions[x]) #keep an original list of questions

def find_similar_questions(new_question):
    
    model_name = 'bert-base-nli-mean-tokens'
    model = SentenceTransformer(model_name)

    nouns_in_new_question = find_nouns(new_question.replace('?', ''))
    questions_index_with_the_same_nouns = []

    for noun in nouns_in_new_question:
        questions_index_with_the_same_nouns.extend(search_through_dict(old_nouns_dictionary, noun))

    prioritized_question_with_the_same_nouns = []
    prioritized_question_with_the_same_nouns_stripped = []
    for item in questions_index_with_the_same_nouns:
        prioritized_question_with_the_same_nouns.append(old_questions[item])
        prioritized_question_with_the_same_nouns_stripped.append(strip_nouns(old_questions[item]))

    new_question = strip_nouns(new_question)
    new_sentence_vecs = model.encode(new_question)

    if len(nouns_in_new_question) != 0 and len(questions_index_with_the_same_nouns) != 0:
        old_sentence_vecs = model.encode(prioritized_question_with_the_same_nouns_stripped)
    elif len(nouns_in_new_question) != 0 and len(questions_index_with_the_same_nouns) == 0:
        old_sentence_vecs = model.encode(questions_with_nouns_stripped)
    else:
        old_sentence_vecs = model.encode(questions_without_nouns)
        

    similarity = cosine_similarity(
        [new_sentence_vecs],
        old_sentence_vecs
    )[0]
    sorted_similarity = [s[0] for s in sorted(enumerate(similarity), key=lambda i:i[0])] 
    #so we get to know the original index of these similarities, easy for us to find its related question

    if len(nouns_in_new_question) != 0 and len(questions_index_with_the_same_nouns) != 0:
        print('Potential related questions are:')
        print(prioritized_question_with_the_same_nouns[sorted_similarity[0]], prioritized_question_with_the_same_nouns[sorted_similarity[1]], prioritized_question_with_the_same_nouns[sorted_similarity[2]])
    elif len(nouns_in_new_question) != 0 and len(questions_index_with_the_same_nouns) == 0:
        print('Potential related questions are:')
        print(questions_with_nouns[sorted_similarity[0]], questions_with_nouns[sorted_similarity[1]], questions_with_nouns[sorted_similarity[2]])
    else:
        print('Potential related questions are:')
        print(questions_without_nouns[sorted_similarity[0]],questions_without_nouns[sorted_similarity[1]], questions_without_nouns[sorted_similarity[2]] )

#find_similar_questions('how can i activate the NN2055 NN10190?')
find_similar_questions('how fast can i run?')
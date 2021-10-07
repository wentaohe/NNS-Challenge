from load_questions import load_questions
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

old_questions = load_questions()

def find_similar(new_question):

    model_name = 'bert-base-nli-mean-tokens'
    model = SentenceTransformer(model_name)
    old_sentence_vecs = model.encode(old_questions)
    new_sentence_vecs = model.encode(new_question)
    similarity = cosine_similarity(
        [new_sentence_vecs],
        old_sentence_vecs
    )[0]
    sorted_similarity = [s[0] for s in sorted(enumerate(similarity), key=lambda i:i[1])]
    print(old_sentence_vecs[sorted_similarity[0]])


find_similar('how can i activate the NN2055 NN10190?')
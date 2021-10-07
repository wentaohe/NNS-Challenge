# NNS Challenge
## Code challenge for Telepathy Labs  

### To test, run the file `find_similar_questions.py`

e.g.  
- `find_similar_questions('how can i activate the NN2055 NN10190?')` 
- `find_similar_questions('how fast can i run?')`

![Terminal Example](https://i.ibb.co/gZckJW1/Screen-Shot-2021-10-07-at-7-05-37-PM.png)

### Questions and Tasks

#### Q1 In general, the proposed approach is valid and applicable and I am following this exact approach to this problem.

#### Q2 The problem I am seeing with this approach and the dataset given is that the amount of vocabulary is not enough (merely 1500) for a complicated machine learning/ deep learning system, and all of the sentences in general are pretty short and simple. Majority of the sentences are composed of coded nouns. In this case, I feel like the use of complicated machine learning and deep learning models with multiple layers will tend to overfit and generate a lot of noises.

#### T1 This particular problem can be viewed as finding and solving similarity in highly-dimensional spaces. In this case, the logic of my algorithm is this (Please refer to the `codes` folder in this repository.): 
- Take a sentence and convert it into vectors. (Using `sentence_transformers` and `sklearn.metrics.pairwise` modules, and `bert-base-nli-mean-tokens` for our NLP model.)
- Take all questions in the provided database and convert them into vectors as well.
- Find sentences that have the smallest Euclidean distance or smallest cosine similarity between them.
- We can then sort the semantic similarity between the input and our database to know which questions will be the most similar to the input question.
- We have set three different scenearios for each input question, e.g. 1. questions that contain nouns which can also be found in our databaase, 2. questions that contain nouns which cannot be found in our database, 3. questions that do not contain any nouns. With this particular methods, we get to prioritize which group of data should be compared against first to maximize our accuracy.
- As for the outputs, the program generates three most similar questions from the provided database based on your input for maximum accuracy (you can also adjust the amount of output by simply adding more terms in the `print` function).

#### Q3 Enter any questions you like by running the file `find_similar_questions.py`, and compare it against your own questions.

#### T2 In general we are able to find pretty accurate questions in related to the input questions since we already set three possible scenarios in order to narrow down our scope as well as prioritizing questions in our database that potentionally have a higher chance of matching.
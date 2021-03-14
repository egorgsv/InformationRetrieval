import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
nltk.download()

truedf = pd.read_csv('data/True.csv')
print(truedf.head())

tokens = [word_tokenize(text) for text in truedf['text']]

words = []
for document in tokens:
    words_in_text = [word for word in document if word.isalpha()]
    words.append(words_in_text)
print(words)

# stemming of words
porter = PorterStemmer()
stemmed = []
for document in words:
    steemmed_words = [porter.stem(word) for word in document]
    stemmed.append(steemmed_words)
print(stemmed)

tuples = []
for i in range(len(stemmed)):
    for word in stemmed[i]:
        tuples.append((word, i))
print(tuples)

terms = {}
for term, DOCid in tuples:
    terms.setdefault(term, set()).add(DOCid)

for term in terms:
    terms[term] = sorted(terms[term])
print(terms)

terms['putin']
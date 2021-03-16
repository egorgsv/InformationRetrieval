import nltk
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# nltk.download()

def tokenize(df):
    tokens = [word_tokenize(text) for text in df['text']]
    words = filter(tokens)
    return words


def filter(tokens):
    stop_words = set(stopwords.words("english"))
    words = []
    for document in tokens:
        without_stop_words = [word for word in document if word.isalpha() and (word not in stop_words)]
        words.append(without_stop_words)
    return words


def stem(words):
    # stemming of words
    porter = PorterStemmer()
    stemmed = []
    for document in words:
        stemmed_words = [porter.stem(word) for word in document]
        stemmed.append(stemmed_words)

    tuples = []
    for i in range(len(stemmed)):
        for word in stemmed[i]:
            tuples.append((word, i))

    terms = {}
    for term, DOCid in tuples:
        terms.setdefault(term, set()).add(DOCid)
    for term in terms:
        terms[term] = sorted(terms[term])

    return terms

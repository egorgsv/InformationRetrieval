import nltk
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# nltk.download()

def tokenize(df):
    block = df.copy()
    for index, row in block.iterrows():
        block.loc[index, 'text'] = word_tokenize(row['text'])
    block['text'] = filter(block)
    #block = block['text']
    return block



def filter(tokens):
    """

    Filtering stop words

    """
    stop_words = set(stopwords.words("english"))
    for index, row in tokens.iterrows():
        tokens.loc[index, 'text'] = [word for word in row['text']
                                     if word.isalpha() and (word not in stop_words)]
    return tokens['text']


def stem(words):
    """

    Stemming of words

    DataFrame -> dictionary

    """
    porter = PorterStemmer()
    stemmed = []
    for index, row in words.iterrows():
        words.loc[index, 'text'] = [porter.stem(word) for word in row['text']]

    dictionary = {}
    for docId, row in words.iterrows():
        for word in row['text']:
            if word in dictionary:
                if docId not in dictionary[word]:
                    dictionary[word].append(docId)
            else:
                dictionary[word] = [docId]

    return dictionary

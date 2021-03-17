import nltk
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from src.document import Document


def tokenize(df: pd.DataFrame) -> pd.DataFrame:
    block = df.copy()
    for index, row in block.iterrows():
        block.loc[index, 'text'] = word_tokenize(row['text'])
    block['text'] = filter(block)
    return block


def filter(tokens: pd.DataFrame) -> pd.DataFrame:
    """
    Filtering stop words
    """
    stop_words = set(stopwords.words("english"))
    for index, row in tokens.iterrows():
        tokens.loc[index, 'text'] = [word for word in row['text']
                                     if word.isalpha() and (word not in stop_words)]
    return tokens['text']


def stem(words: pd.DataFrame):
    """
    Stemming of words

    """
    porter = PorterStemmer()
    documents = []
    for index, row in words.iterrows():
        documents.append(Document(index, set([porter.stem(word) for word in row['text']])))

    return documents

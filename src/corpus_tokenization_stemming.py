import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from src.document import Document

stop_words = set(stopwords.words("english"))


def tokenize(df: pd.DataFrame) -> pd.DataFrame:
    block = df.copy()
    block['text'] = block['text'].apply(lambda x: word_tokenize(x))
    block['text'] = block['text'].apply(lambda x: filter(x))
    return block


def filter(tokens):
    """
    Filtering stop words and punctuation

    """

    return [word for word in tokens
            if word.isalpha() and (word not in stop_words)]


def stem(words: pd.DataFrame):
    """
    Stemming of words

    """
    porter = PorterStemmer()
    documents = []
    for index, row in words.iterrows():
        documents.append(Document(index, set([porter.stem(word) for word in row['text']])))

    return documents

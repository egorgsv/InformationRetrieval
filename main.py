import argparse
import pandas as pd
from nltk.stem.porter import PorterStemmer
from src.CorpusTokenizationStemming import *
from src.ParseQuery import reversed_polish_notation
from src.Search import search, OPERATORS
from src.SPIMIClass import SPIMI


def main():
    truedf = pd.read_csv('data/True.csv')
    words = tokenize(truedf)
    print("Tokenization complete!")
    terms = stem(words)
    print("Stemming complete!")

    #index = SPIMI()      Тут надо как-то часть Димы реализовать
    porter = PorterStemmer()
    polish_query = reversed_polish_notation(args.QUERY)
    for i in range(len(polish_query)):
        if polish_query[i] not in OPERATORS:
            polish_query[i] = porter.stem(polish_query[i])
            polish_query[i] = terms[polish_query[i]]
    ans = search(polish_query)
    print(ans)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str)
    args = parser.parse_args()

    main()
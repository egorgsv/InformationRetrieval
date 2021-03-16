import argparse
import pandas as pd
from src.CorpusTokenizationStemming import *
from src.ParseQuery import reversed_polish_notation
from src.Search import search, OPERATORS
from src.SPIMIClass import SPIMI


def main():
    docs_count = 0
    with pd.read_csv("data/True.csv", chunksize=1000) as reader:
        for chunk in reader:
            words = tokenize(chunk)
            terms = stem(words)
            docs_count = docs_count + len(chunk)

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
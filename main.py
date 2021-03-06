import argparse
import nltk
import pandas as pd
from src.corpus_tokenization_stemming import *
from src.parse_query import reversed_polish_notation
from src.search import search, OPERATORS
from src.spimi import Spimi
import tqdm
from termcolor import colored
from src.document import Document
import sys

with open(r"data/flag.txt", 'r') as f:
    n = int(f.read())

with open(r"data/flag.txt", 'w') as f:
    if n == 0:
        nltk.download('stopwords')
        nltk.download('punkt')
    f.write(str(1))


def main():
    docs_count = 0
    chunksize = 1000
    spimi = Spimi()
    if n == 0:
        pbar = tqdm.tqdm(docs_count, position=0, leave=True)
        with pd.read_csv(r"data/True.csv", chunksize=chunksize) as reader:
            for chunk in reader:
                words = tokenize(chunk)
                docs = stem(words)
                spimi.build_block(docs)
                chunk['index'] = chunk.index
                chunk.to_csv('data/block{}.csv'.format(docs_count // chunksize))
                docs_count += len(chunk)
                pbar.update(chunksize)
        spimi.merge_blocks()
        pbar.close()
        del pbar
    else:
        docs_count = 21417

    terms = list()
    porter = PorterStemmer()
    polish_query = reversed_polish_notation(args.QUERY)
    for i in range(len(polish_query)):
        if polish_query[i] not in OPERATORS:
            polish_query[i] = porter.stem(polish_query[i])
            if polish_query[i][0] not in spimi.inverted_index.keys():
                spimi.load_inverted_index_from_file(polish_query[i][0])
            terms += [polish_query[i]]
            if polish_query[i] not in spimi.inverted_index[polish_query[i][0]].keys():
                polish_query[i] = []
            else:
                polish_query[i] = spimi.inverted_index[polish_query[i][0]][polish_query[i]]
    ans = search(polish_query, docs_count)
    if ans == []:
        print("Oops! Данный запрос не найден, попробуйте другой...")
        sys.exit(1)
    for i in ans:
        df = pd.read_csv('data/block{}.csv'.format(i // chunksize), index_col='index')
        for j in terms:
            df.loc[i, 'text'] = df.loc[i, 'text'].replace(' ' + j, colored(' ' + j, 'green'))
            df.loc[i, 'text'] = df.loc[i, 'text'].replace(' ' + j[0].upper() + j[1:],
                                                          colored(' ' + j[0].upper() + j[1:], 'green'))
        print(colored("docID = {}\n".format(i), 'blue'), df.loc[i, 'text'], end='\n\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str)
    args = parser.parse_args()

    main()

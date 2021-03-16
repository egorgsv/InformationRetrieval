import argparse
import pandas as pd
from src.CorpusTokenizationStemming import *
from src.ParseQuery import reversed_polish_notation
from src.Search import search, OPERATORS
from src.spimi import Spimi
import tqdm
from src.document import Document


def main():
    docs_count = 0
    chunksize = 1000
    spimi = Spimi()
    pbar = tqdm.tqdm(docs_count, position=0, leave=True)
    with pd.read_csv("data/True.csv", chunksize=chunksize) as reader:
        for chunk in reader:
            words = tokenize(chunk)
            docs = stem(words)
            spimi.build_block(docs)
            chunk.to_csv('data/block{}.csv'.format(docs_count//chunksize))
            docs_count += len(chunk)
            pbar.update(1)
    spimi.merge_blocks()
    pbar.close();
    del pbar

    porter = PorterStemmer()
    polish_query = reversed_polish_notation(args.QUERY)
    for i in range(len(polish_query)):
        if polish_query[i] not in OPERATORS:
            polish_query[i] = porter.stem(polish_query[i])
            polish_query[i] = spimi.inverted_index[polish_query[i]]
    ans = search(polish_query, docs_count)
    for i in ans:
        df = pd.read_csv(f'data/block{i//chunksize}.csv')
        print(df.loc[i, 'text'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str)
    args = parser.parse_args()

    main()
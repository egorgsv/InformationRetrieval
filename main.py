import argparse
import pandas as pd
from src.CorpusTokenizationStemming import *
from src.ParseQuery import *


def main():
    with pd.read_csv("data/True.csv", chunksize=1000) as reader:
        for chunk in reader:
            words = tokenize(chunk)
            terms = stem(words)
            print(terms)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str)
    args = parser.parse_args()

    print(reversed_polish_notation(str(args.QUERY)))

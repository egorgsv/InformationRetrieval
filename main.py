import argparse
import pandas as pd
from src.CorpusTokenizationStemming import *
from src.utils import *


def main():
    truedf = pd.read_csv('data/True.csv')
    words = tokenize(truedf)
    print("Tokenization complete!")
    terms = stem(words)
    print("Stemming complete!")
    print(terms)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str)
    args = parser.parse_args()

    print(reversed_polish_notation(str(args.QUERY)))

import resource
import sys
import nltk
import argparse
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

from src.utils import *

# nltk.download()


def memory_limit(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, maxsize))


def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory


def main():
    truedf = pd.read_csv('data/True.csv')

    tokens = [word_tokenize(text) for text in truedf['text']]

    words = []
    for document in tokens:
        words_in_text = [word for word in document if word.isalpha()]
        words.append(words_in_text)

    # stemming of words
    porter = PorterStemmer()
    stemmed = []
    for document in words:
        steemmed_words = [porter.stem(word) for word in document]
        stemmed.append(steemmed_words)

    tuples = []
    for i in range(len(stemmed)):
        for word in stemmed[i]:
            tuples.append((word, i))

    terms = {}
    for term, DOCid in tuples:
        terms.setdefault(term, set()).add(DOCid)
    for term in terms:
        terms[term] = sorted(terms[term])


if __name__ == '__main__':
    memory_limit(1024*1024)  # Limitates maximum memory usage to half

    parser = argparse.ArgumentParser()
    parser.add_argument('QUERY', type=str)

    args = parser.parse_args()

    try:
        print(reversed_polish_notation(str(args.QUERY)))
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)


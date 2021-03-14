import resource
import sys
import nltk
import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

#nltk.download()

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
    print(truedf.head())

    tokens = [word_tokenize(text) for text in truedf['text']]

    words = []
    for document in tokens:
        words_in_text = [word for word in document if word.isalpha()]
        words.append(words_in_text)
    print(words)

    # stemming of words
    porter = PorterStemmer()
    stemmed = []
    for document in words:
        steemmed_words = [porter.stem(word) for word in document]
        stemmed.append(steemmed_words)
    print(stemmed)

    tuples = []
    for i in range(len(stemmed)):
        for word in stemmed[i]:
            tuples.append((word, i))
    print(tuples)

    terms = {}
    for term, DOCid in tuples:
        terms.setdefault(term, set()).add(DOCid)
    for term in terms:
        terms[term] = sorted(terms[term])
    print(terms)

    print(terms['putin'])

if __name__ == '__main__':
    memory_limit(1024*1024) # Limitates maximun memory usage to half
    try:
        main()
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)


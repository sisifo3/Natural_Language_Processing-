import operator
from functools import reduce
path = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/'
filename = 'segmentation_words.txt'
path2 = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/ngrams/'
filename2 = 'count_1w.txt'
file = open(path + filename, "rt")
tweets_text = file.read()
file.close()
# print(tweets_text[0])
tweets_text_slp = tweets_text.split('\n')
# print(tweets_text_slp[1])

def segment(text):
    "Return a list of words that is the best segmentation of text."
    if not text: return []
    candidates = ([first]+segment(rem) for first, rem in splits(text))
    return max(candidates, key=Pwords)


def splits(text, l=20):
    "Return a list of all possible (first, rem) pairs, len(first)<=L."
    return [(text[:i+1], text[i+1:])
            for i in range(min(len(text), l))]


def Pwords(words):
    "The Naive Bayes probability of a sequence of words."
    return product(Pw(w) for w in words)


def product(nums):
    "Return the product of a sequence of numbers."
    return reduce(operator.mul, nums, 1)


class Pdist(dict):
    """A probability distribution estimated from counts in datafile."""
    def __init__(self, data=[], N=None, missingfn=None):
        for key, count in data:
            self[key] = self.get(key, 0) + int(count)
        # print(self)
        self.N = float(N or sum(self.values()))
        self.missingfn = missingfn or (lambda k, N: 1./N)

    def __call__(self, key):
        if key in self:
            return self[key]/self.N
        else:
            return self.missingfn(key, self.N)


def datafile(name, sep='\t'):
    """Read key,value pairs from file."""
    # print(type(name))
    for line in open(name):
        yield line.split(sep)


def avoid_long_words(key, N):
    """Estimate the probability of an unknown word."""
    return 10./(N * 10**len(key))


N = 1024908267229
Pw = Pdist(datafile(path2+filename2), N, avoid_long_words)

for j in range(20):
    seg = segment(tweets_text_slp[j])
    print(j)
    print(seg)
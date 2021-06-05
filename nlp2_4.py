import re

path = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/'

text_file = open(path + "belinda_tw.txt", "r+")
tweets_text = text_file.read()
tweets_text = tweets_text.lower()
text_file.close()

print(type(tweets_text))

#corpus = {}
#for i in range(len(tweets_text)):
#    corpus[i, 1] = tweets_text[i]

#print(corpus)

# corpus_last = {}

# for i in range(len(corpus)):
#    y = corpus[i, 1]
#    x = []
#    x = y.split(" ")
#    corpus_last[i, 1] = x

# print(corpus_last)
# load text
# filename = 'metamorphosis_clean.txt'
# file = open(filename, 'rt')
# text = file.read()
# file.close()
# split into words by white space
# words = text.split()
# remove punctuation from each word
# import string
# table = str.maketrans('', '', string.punctuation)
# stripped = [w.translate(table) for w in words]
# print(stripped[:100]






# x es un texto plano que tiene todos los tweets de la forma "1 tweet \n 2 tweet..."
# def cleanse(x):
#    clean_x = re.sub(r'(\n)+'," ",x)
#    clean_x = re.sub(r'"(\s)+"', " X ",clean_x)
#    clean_x = re.sub(r'htt[ps]+://[^\s]*', "",clean_x)
#    clean_x = re.sub(r'[<>]', "",clean_x)
#    clean_x = re.sub(r'u\+', " u",clean_x)
#    clean_x = re.sub(r'[#]', " ",clean_x)
#    clean_x = clean_x.split("X")
#    clean_x = list(set([selection(i) for i in clean_x ]))
#    clean_x.remove("X1X")

#    return clean_x


# tweets = cleanse(tweets_text)
# print(tweets[1])

# tweets_text = re.sub(r'\n', " ", tweets_text)
# tweets_text = re.sub(r'"\s+"', "X", tweets_text)
# tweets_text = re.sub(r'[<>]', "", tweets_text)
# tweets_text = re.sub(r'u\+', " u", tweets_text)
# tweets_text = re.sub(r'htt[ps]+://[^\s]*', "", tweets_text)
# tweets_text = re.sub(r'[@#]', " ", tweets_text)
# tweets_text = re.sub("[^a-záéíóúüñ0-9X]", " ", tweets_text)
# tweets_text = tweets_text.split("X")
# tweets_text = list(set([selection(i) for i in tweets_text]))
# tweets_text.remove("X1X")

# print(tweets_text[1])

# class CorpusC:

#    def corpus_gen(tweets_text):
#        corpus = {}
#        for i in range(len(tweets_text)):
#            corpus[i, 1] = tweets_text[i]

#        return corpus

#    def corpus_last(corpus):
#        corpus_last = {}
#        for i in range(len(corpus)):
#            y = corpus[i, 1]
#            x = []
#            x = y.split(" ")
#            corpus_last[i, 1] = x
#        return corpus_last


# corpus = CorpusC.corpus_gen(tweets_text)
# print(corpus)
# corpus_last = CorpusC.corpus_last(corpus)






# class FreqTw:

#    def freq(self, tweet):
#        ref_tweet = set(tweet)
#        return ref_tweet


# tweet_one = corpus_last[2, 1]
# print(tweet_one)

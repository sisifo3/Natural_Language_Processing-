import re
import string
import math

path = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/'
filename = "tweets_ase.txt"
file = open(path + filename, "rt")
tweets_text = file.read()
file.close()

# En esta sección separamos el texto en difernetes tweets.
# Se modifico el documento .txt

tweets_text_slp = tweets_text.split('"')
# print(len(tweets_text_slp))
tweets_text_s = []
for i in range(len(tweets_text_slp)):
     if len(tweets_text_slp[i]) > 10:
        tweets_text_s.append(tweets_text_slp[i])
# print(len(tweets_text_s))
# la clase CleanTweets en la función split_tweets nos ayuda a separar los tweets en palabras.
# En la función clean_tweets buscamos eliminar carcatéres que no son necesarios.
# Es necesario borrar stop words, en español : 'el', 'que', 'por', 'y', etc.
Spanish_stop_words = ['a', 'la', 'el', 'un', 'por', 'de', 'se', 'les', 'que', 'y', 'es', 'lo', 'los', 'o', 'en'
                      , 'le', 'las', 'al']


class CleanTweets:

    def split_tweets(tweets):
        words = tweets.split()
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in words]
        return stripped

    def clean_tweets(tweets):
        tweets_r = []
        for t in range(len(tweets)):
            a = re.sub(r'^https?.*[\r\n]*', '', tweets[t], flags=re.MULTILINE)
            a = re.sub('U2B07', '', a)
            a = re.sub('U0001F38AU0001F389U0001F382U0001F60D', '', a)
            tweets_r.append(a)

        tweets_ra = [word for word in tweets_r if not word in Spanish_stop_words]

        return tweets_ra


cleaned_tweets = []
tweets_words = []
for k in range(len(tweets_text_s)):
    tweets_words.append(CleanTweets.split_tweets(tweets_text_s[k]))
    cleaned_tweets.append(CleanTweets.clean_tweets((tweets_words[k])))

# print(tweets_words[0])
# print(cleaned_tweets[2])


# Para la frecuencia obtenemos una lista con las palabras unicas, depues comparamos con
# los tweeters individuales, para obtener la frecuencia y por ultimo las funciones de
# similitud dos tipos de frecuencia term frecuency (tf), inverse document frequency (idf)
# idf_t = log(N/nt)


class Frecuency:

    def vector_word(text_f):
        all_words = []
        for tf in text_f:
            for wt in tf:
                all_words.append(wt)
        res = []
        for wors in all_words:
            # print(wors)
            if wors not in res:
                res.append(wors)
        # no_rep_tweet = list(set(all_words))
        # return no_rep_tweet
        return res

    def term_frequency(vector_word, tweet_i):
        counter = 0
        vector_freq = []
        for words in vector_word:
            for words_tw in tweet_i:
                if words == words_tw:
                    counter += 1
            vector_freq.append(counter)
            counter = 0
        return vector_freq

    def nt_freq(cleaned_tweets, vector_word):
        tcounter = 0
        nt_vector = []
        for word in vector_word:
            for ij in range(len(cleaned_tweets)):
                if word in cleaned_tweets[ij]:
                    tcounter += 1
            nt_vector.append(tcounter)
            tcounter = 0
        return nt_vector

    def in_doc_freq(nt_vector):
        idf = []
        for value in nt_vector:
            idf.append(math.log(100/value))

        return idf


# print(cleaned_tweets)
vector_word = Frecuency.vector_word(cleaned_tweets)
# print(vector_word)
vec_freq = Frecuency.term_frequency(vector_word, cleaned_tweets[0])
# print(vec_freq)
nt_vector = Frecuency.nt_freq(cleaned_tweets, vector_word)
# print(nt_vector)
idf_vector = Frecuency.in_doc_freq(nt_vector)
print(len(idf_vector))

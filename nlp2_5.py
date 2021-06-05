import re
import string
import math

path = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/'
filename = "belinda_tw.txt"
file = open(path + filename, "rt")
tweets_text = file.read()
file.close()

# En esta sección separamos el texto en difernetes tweets.
# Se modifico el documento .txt

tweets_text_slp = tweets_text.split('"x"')
tweets_text_s = []
for i in range(len(tweets_text_slp)):
     if len(tweets_text_slp[i]) > 10:
        tweets_text_s.append(tweets_text_slp[i])

# la clase CleanTweets en la función split_tweets nos ayuda a separar los tweets en palabras.
# En la función clean_tweets buscamos eliminar carcatéres que no son necesarios.


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

        return tweets_r


cleaned_tweets = []
tweets_words = []
for k in range(len(tweets_text_s)):
    tweets_words.append(CleanTweets.split_tweets(tweets_text_s[k]))
    cleaned_tweets.append(CleanTweets.clean_tweets((tweets_words[k])))

# print(tweets_words[0])
# print(cleaned_tweets[0])

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
# vec_freq = Frecuency.term_frequency(vector_word, cleaned_tweets[0])
# print(vec_freq)
nt_vector = Frecuency.nt_freq(cleaned_tweets, vector_word)
# print(nt_vector)
idf_vector = Frecuency.in_doc_freq(nt_vector)
# print(idf_vector)


class Similitud:

    def get_Wt(q, d, cleaned_tweets, vector_word, idf):
        twq = cleaned_tweets[q]
        tft_q = Frecuency.term_frequency(vector_word, twq)

        wt_q = []
        for f in range(len(tft_q)):
            wt_q.append(tft_q[f] * idf[f])

        twd = cleaned_tweets[d]
        tft_d = Frecuency.term_frequency(vector_word, twd)

        wt_d = []
        for d in range(len(tft_d)):
            wt_d.append(tft_d[d] * idf[d])

        return wt_q, wt_d

    def similitud(wtq, wtd):
        w_up = []
        w_down_a = []
        w_down_b = []
        for w in range(len(wtq)):
            w_up.append(wtq[w] * wtd[w])
            w_down_a.append(wtq[w] * wtq[w])
            w_down_b.append(wtd[w] * wtd[w])
        sum_wup = sum(w_up)
        sum_wda = sum(w_down_a)
        sum_wdb = sum(w_down_b)
        ssa = math.sqrt(sum_wda)
        ssb = math.sqrt(sum_wdb)
        sim = sum_wup/(ssa*ssb)
        return sim


# Para obtener la simulitud entre dos tweets, en este caso el tweeet 1 y el tweet 2
# madamos llamar a la funcion get_Wt, para que nos de los valores Wtq y Wtd, despues y por ultimo
# llamamos a la funcion similitud_two_tt para obtener la similitud entre dos tweets.
wtq, wtd = Similitud.get_Wt(1, 2, cleaned_tweets, vector_word, idf_vector)
similitud_two_tt = Similitud.similitud(wtq, wtd)
print(wtq)
print(wtd)
print(similitud_two_tt)



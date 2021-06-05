import re
import math as mt
path = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/'


def selection(x):
    if len(x) < 15:
        return "X1X"
    else:
        return x


#x es un texto plano que tiene todos los tweets de la forma "1 tweet \n 2 tweet..."
def cleanse(x):
    clean_x = re.sub(r'(\n)+'," ",x)
    clean_x = re.sub(r'"(\s)+"', " X ",clean_x)
    clean_x = re.sub(r'htt[ps]+://[^\s]*', "",clean_x)
    clean_x = re.sub(r'[<>]', "",clean_x)
    clean_x = re.sub(r'u\+', " u",clean_x)
    clean_x = re.sub(r'[#]', " ",clean_x)
    clean_x = clean_x.split("X")
    clean_x = list(set([selection(i) for i in clean_x ]))
    clean_x.remove("X1X")

    return clean_x


class doctos:
    def __init__(self, no_docto, wordpos):
        self.doctos = [no_docto]
        self.freq = [1]
        self.wordpos = [[wordpos]]

    def update(self, no_docto, wordpos, doccnt):
        if no_docto in self.doctos:
            self.freq[-1] += 1
            self.wordpos[-1].append(wordpos)
        else:
            self.doctos.append(no_docto)
            self.freq.append(1)
            self.wordpos.append([1])


#Clase token, almacena la palabra, el número de documentos donde aparece la palabra
#así como la frecuencia total y una clase documentos con información detallada
class token:
    def __init__(self,word,no_docto,wordpos):
        self.word = word
        self.doccnt = 1
        self.freqcnt = 1
        self.doctos = doctos(no_docto,wordpos)

    def update(self,no_docto, wordpos):
        self.freqcnt += 1
        self.doctos.update(no_docto, wordpos, self.doccnt)
        self.doccnt = len(self.doctos.doctos)

    def __add__(self, new_word):
        if isinstance(new_word, token):
            return boolean_seach([self.word, new_word.word], set(self.doctos.doctos).union(set(new_word.doctos.doctos))," OR ")
        elif isinstance(new_word, boolean_seach):
            return boolean_seach([self.word, new_word.word], set(self.doctos.doctos).union(set(new_word.doctos))," OR ")
        else:
            return "Error de tipo de búsqueda"

    def __mul__(self,new_word):
        if isinstance(new_word,token):
            return boolean_seach([self.word,new_word.word],set(self.doctos.doctos).intersection(set(new_word.doctos.doctos))," AND ")
        elif isinstance(new_word,boolean_seach):
            return boolean_seach([self.word,new_word.word],set(self.doctos.doctos).intersection(set(new_word.doctos))," AND ")
        else:
            return "Error de tipo de búsqueda"

    def __sub__(self,new_word):
        if isinstance(new_word,token):
            return boolean_seach([self.word,new_word.word],set(self.doctos.doctos)-set(new_word.doctos.doctos)," AND ")
        elif isinstance(new_word,boolean_seach):
            return boolean_seach([self.word,new_word.word],set(self.doctos.doctos)-set(new_word.doctos)," AND ")
        else:
            return "Error de tipo de búsqueda"


class boolean_seach:
    def __init__(self,words,doctos,operator):
        self.word = "("+words[0]+operator+words[1]+")"
        self.doctos = list(doctos)
        self.doctos.sort()

    def __add__(self,new_word):
        if isinstance(new_word,token):
            return boolean_seach([self.word,new_word.word],set(self.doctos).union(set(new_word.doctos.doctos))," OR ")
        elif isinstance(new_word,boolean_seach):
            return boolean_seach([self.word,new_word.word],set(self.doctos).union(set(new_word.doctos))," OR ")
        else:
            return "Error de tipo de búsqueda"

    def __mul__(self,new_word):
        if isinstance(new_word,token):
            return boolean_seach([self.word,new_word.word],set(self.doctos).intersection(set(new_word.doctos.doctos))," AND ")
        elif isinstance(new_word,boolean_seach):
            return boolean_seach([self.word,new_word.word],set(self.doctos).intersection(set(new_word.doctos))," AND ")
        else:
            return "Error de tipo de búsqueda"

    def __sub__(self,new_word):
        if isinstance(new_word,token):
            return boolean_seach([self.word,new_word.word],set(self.doctos.doctos)-set(new_word.doctos.doctos)," AND ")
        elif isinstance(new_word,boolean_seach):
            return boolean_seach([self.word,new_word.word],set(self.doctos.doctos)-set(new_word.doctos)," AND ")
        else:
            return "Error de tipo de búsqueda"

#x es un tweet
def vector_encoder(x, diccionario, docto=-1):
    words = diccionario.keys()
    vector_tweet = [auxiliar_encoder(w, diccionario, docto) for w in words]

    return vector_tweet


def auxiliar_encoder(word,diccionario,docto):
    if docto > -1:
        flag = [idx for idx,w in enumerate(diccionario[word].doctos.doctos) if w == docto]
        if len(flag) > 0:
            return diccionario[word].doctos.freq[flag[-1]]*mt.log(99/len(diccionario[word].doctos.doctos))
        else:
            return 0


#def similitud(v_1,v_2):
#    numerador = sum([p*q for p,q in zip(v_1,v_2)])
#    denominador = sum([p**2 for p in v_1]) * sum([q**2 for q in v_2])
#    denominador = mt.sqrt(denominador)

#    return numerador/denominador


corpus = {}
tweets_split = []

text_file = open(path+"belinda_tw.txt","r+")
tweets_text = text_file.read()
tweets_text = tweets_text.lower()
text_file.close()

tweets = cleanse(tweets_text)
print(tweets)

for i in range(len(tweets)):
    tweet = re.sub("[^a-záéíóúüñ0-9]"," ",tweets[i])
    tweet = re.sub("\s+"," ",tweet)
    tweet_words = tweet.split()
    tweets_split.append([tweet_words])
    for j in range(len(tweet_words)):
        if tweet_words[j] in corpus:
            corpus[tweet_words[j]].update(i+1,j+1)
        else:
            corpus[tweet_words[j]] = token(tweet_words[j],i+1,j+1)

print(corpus["belinda"].doctos.doctos)

tw_1 = vector_encoder("fdfgsdf", corpus, 1)
print(len(tw_1))
print(tw_1)

import re

path = '/home/sisifo/Desktop/Ingoodwetrust/libros/NaturalLenguageProcessing/'


def selection(x):
    if len(x) < 10:
        return "X1X"
    else:
        return x


text_file = open(path + "belinda_tw.txt", "r+")
tweets_text = text_file.read()
tweets_text = tweets_text.lower()
text_file.close()

tweets_text = re.sub(r'\n', " ", tweets_text)
tweets_text = re.sub(r'"\s+"', "X", tweets_text)
tweets_text = re.sub(r'[<>]', "", tweets_text)
tweets_text = re.sub(r'u\+', " u", tweets_text)
tweets_text = re.sub(r'htt[ps]+://[^\s]*', "", tweets_text)
tweets_text = re.sub(r'[@#]', " ", tweets_text)
tweets_text = re.sub("[^a-záéíóúüñ0-9X]", " ", tweets_text)
tweets_text = tweets_text.split("X")
tweets_text = list(set([selection(i) for i in tweets_text]))
tweets_text.remove("X1X")

def similitud(w_td,w_tq):
    
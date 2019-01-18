import nltk
from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize
from nltk import PorterStemmer
from stemming.porter2 import  stem
import preprocessor as p
from string import punctuation

class Preprocess (object):
    twit_stopwords = []
    negative_words = []
    def __init__(self):
        negfile = "negativeWords.txt"
        p.set_options(p.OPT.URL, p.OPT.HASHTAG, p.OPT.MENTION, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.RESERVED, p.OPT.NUMBER)
        nltk.download ("stopwords")
#        self.twit_stopwords = set ([w.encode('ascii','ignore') for w in stopwords.words('english')])
        self.twit_stopwords = set ([w for w in stopwords.words('english')])

 #       strlist= b""
 #       fp = open(negfile, "rb")
        strlist= ""
        fp = open(negfile, "r")
        for f in fp:
            strlist += f
        fp.close()
        self.negative_words = strlist.split()

    def clean (self, text):
        cleantext = p.clean(text)
        cleantext = cleantext.lower()

        # remove punctuations
        #Basically first contructing a list comprehension of char such that if punctuation making it " " else keep same char
        # and joining with empty char '' (and not blank char ' ')
        cleantext = ''.join ([c if c not in punctuation else " " for c in cleantext])

        # tokenize
        twit_wordtokens = word_tokenize(cleantext)
        twit_wordtokens = [w for w in twit_wordtokens if not w in self.twit_stopwords or w in self.negative_words]

        #stemming
#        twit_stemtokens = [stem(w).encode('ascii','ignore') for w in twit_wordtokens]
        twit_stemtokens = [stem(w) for w in twit_wordtokens]

        #return b",".join(twit_stemtokens)
        return ",".join(twit_stemtokens)
import nltk
import math
from nltk.book import *

f1 = open('abd.txt').read()

f2 = open('amitava.txt').read()

f3 = open('bd.txt').read()

f4 = open('chan.txt').read()

f5 = open('chandan.txt').read()

f6 = open('jyotirmoy.txt').read()

f7 = open('kunal.txt').read()

f8 = open('mainak.txt').read()

f9 = open('manika.txt').read()

f10 = open('moy.txt').read()

f11 = open('msm.txt').read()

f12 = open('plb.txt').read()

f13 = open('rajashree.txt').read()

f14 = open('rita.txt').read()

f15 = open('samaresh.txt').read()

f16 = open('sandi.txt').read()

f17 = open('sayan.txt').read()

f18 = open('swarnendu.txt').read()

final = f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12+f13+f14+f15+f16+f17+f18

tokens = nltk.word_tokenize(final)

freq = FreqDist(tokens)

TR = freq.values()

distinct_words = set(tokens)

doc_fr = dict.fromkeys(distinct_words,0)

final1 = []

final1.append(f1)

final1.append(f2)

final1.append(f3)

final1.append(f4)

final1.append(f5)

final1.append(f6)

final1.append(f7)

final1.append(f8)

final1.append(f9)

final1.append(f10)

final1.append(f11)

final1.append(f12)

final1.append(f13)

final1.append(f14)

final1.append(f15)

final1.append(f16)

final1.append(f17)

final1.append(f18)

def containing(word,doc):
	if word in doc:
		return 1
	else:
        return 0

for i in doc_fr.keys() :
    for j in final1:
        doc_fr[i] = doc_fr[i]+containing(i,j)

N=len(final1)
df = doc_fr.values()

y = lambda x:math.log10(N/x)

idf = []

for i in df:
    idf.append(y(i))

tfidf = np.multiply(TR,idf)

tfidf_dict = dict.fromkeys(distinct_words,0)

temp = doc_fr.keys()

for i in range(0,len(idf)-1):
    tfidf_dict[temp[i]]=idf[i]

print tfidf_dict
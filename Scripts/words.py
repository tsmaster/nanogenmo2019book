import pycorpora
from util import *
import random

cachedWords = None

def getWordList():
    global cachedWords
    if cachedWords is None:
        cachedWords = dedup(getAdjs() + getAdverbs() + getNouns() + getVerbs())
    return cachedWords

def getRandomWord():
    return random.choice(getWordList())

def getAdjs():
    return pycorpora.get_file("words", "adjs")['adjs']

def getAdverbs():
    return pycorpora.get_file("words", "adverbs")['adverbs']

def getNouns():
    return pycorpora.get_file("words", "nouns")['nouns']

def getVerbs():
    v = []
    for w in pycorpora.get_file("words", "verbs")['verbs']:
        for form in w.values():
            v.append(form)
    return v


if __name__ == "__main__":
    print (getAdjs())
    print (getAdverbs())
    print (getNouns())
    print (getVerbs())
    for i in range(20):
        print(getRandomWord())

import random
import os

def getList(filename):
    corporaDir = "../Corpora"
    extFilename = os.path.join(corporaDir, filename)
    with open(extFilename) as f:
        lines = f.readlines()
        lines = [w.strip() for w in lines]
        lines = [w for w in lines if w]
        return lines

def dedup(wordlist):
    wordset = set(wordlist)
    return list(wordset)

def mutateWord(word):
    mutations = random.randrange(2, 5)
    while mutations > 0:
        i = random.randrange(0, len(word))
        word = modifyString(word, i, mutateChar(word[i]))
        mutations -= 1
    return word

def modifyString(s, i, nc):
    c = list(s)
    c[i]=nc
    return ''.join(c)
                         
def mutateChar(c):
    if isVowel(c):
        return mutateVowel(c)
    else:
        return mutateConsonant(c)

def isVowel(c):
    return c.lower() in "aeiou"

def mutateVowel(c):
    nc = c
    while nc == c:
        nc = random.choice("aeiou")
    return nc

def mutateConsonant(c):
    nc = c
    while nc == c:
        nc = random.choice("bcdfghjklmnpqrstvwxyz")
    return nc

def addArticle(item):
    itemsafe = item.lower()

    if (itemsafe.startswith('a ') or
        itemsafe.startswith('an ')):
        return item

    if isVowel(itemsafe[0]):
        return "an " + item
    return "a " + item

def stripArticle(item):
    itemsafe = item.lower()
    if itemsafe.startswith('a '):
        return item[2:]
    if itemsafe.startswith('an '):
        return item[3:]
    return item




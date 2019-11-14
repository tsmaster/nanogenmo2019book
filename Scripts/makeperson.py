import random
import pycorpora

from tags import *
from util import *

def makeperson():
    pd = {}

    pd[FIRSTNAME_TAG] = mutateName(random.choice(pycorpora.humans.firstNames["firstNames"])).capitalize()
    pd[LASTNAME_TAG] = mutateName(random.choice(pycorpora.humans.lastNames["lastNames"])).capitalize()
    pd[FULLNAME_TAG] = pd[FIRSTNAME_TAG] + " " + pd[LASTNAME_TAG]
    pd[HOMETOWN_TAG] = makeCityName()
    makePronouns(pd)
    pd[RACE_TAG] = random.choice(getList("races.txt"))

    return pd

def makeCityName():
    cities = ["London", "Chicago", "Skara Brae"]
    baseName = random.choice(cities)
    return mutateName(baseName).capitalize()

def mutateName(n):
    mutations = random.randrange(2, 5)
    while mutations > 0:
        i = random.randrange(0, len(n))
        n = modifyString(n, i, mutateChar(n[i]))
        mutations -= 1
    return n

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

def makePronouns(pd):
    d100 = random.randrange(0,100)
    if (d100 < 45):
        pd[HE_SHE_PRONOUN_TAG] = "he"
        pd[HIS_HER_PRONOUN_TAG] = "his"
        pd[GENDER_TAG] = GENDER_MALE_TAG
    elif (d100 < 90):
        pd[HE_SHE_PRONOUN_TAG] = "she"
        pd[HIS_HER_PRONOUN_TAG] = "her"
        pd[GENDER_TAG] = GENDER_FEMALE_TAG
    elif (d100 < 98):
        pd[HE_SHE_PRONOUN_TAG] = "they"
        pd[HIS_HER_PRONOUN_TAG] = "their"
        pd[GENDER_TAG] = GENDER_NEUTER_TAG
    else:
        pd[HE_SHE_PRONOUN_TAG] = "xe"
        pd[HIS_HER_PRONOUN_TAG] = "xis"
        pd[GENDER_TAG] = GENDER_OTHER_TAG
        

if __name__ == "__main__":
    print (makeperson())

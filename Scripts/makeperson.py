import random
import pycorpora

from tags import *
from util import *

import makeplacename

def makeperson():
    pd = {}

    pd[FIRSTNAME_TAG] = mutateWord(makeFirstName()).capitalize()
    pd[LASTNAME_TAG] = mutateWord(random.choice(pycorpora.humans.lastNames["lastNames"])).capitalize()
    pd[FULLNAME_TAG] = pd[FIRSTNAME_TAG] + " " + pd[LASTNAME_TAG]
    pd[HOMETOWN_TAG] = makeplacename.makePlaceName()
    makePronouns(pd)
    pd[RACE_TAG] = random.choice(getList("races.txt"))

    return pd

cachedFirstNameList = None

def makeFirstName():
    global cachedFirstNameList
    
    if cachedFirstNameList is None:
        nameList = pycorpora.humans.firstNames["firstNames"]
        nameList += pycorpora.humans.norwayFirstNamesBoys["firstnames_boys_norwegian"]
        nameList += pycorpora.humans.norwayFirstNamesGirls["firstnames_girls_norwegian"]
        nameList += pycorpora.humans.spanishFirstNames["firstNames"]
        nameList += pycorpora.humans.tolkienCharacterNames["names"]
        for name in pycorpora.humans.britishActors["britishActors"]:
            parts = name.split()
            nameList += parts[0]
        for name in pycorpora.humans.celebrities["celebrities"]:
            parts = name.split()
            nameList += parts[0]
        cachedFirstNameList = dedup(nameList)

    return random.choice(cachedFirstNameList).title()

cachedLastNameList = None

def makeLastName():
    global cachedLastNameList
    
    if cachedLastNameList is None:
        nameList = pycorpora.humans.lastnames["lastNames"]
        nameList += pycorpora.humans.norwayLastNames["lastnames_norwegian"]
        nameList += pycorpora.humans.spanishLastNames["lastNames"]
        nameList += pycorpora.humans.tolkienCharacterNames["names"]
        for name in pycorpora.humans.britishActors["britishActors"]:
            parts = name.split()
            nameList += parts[-1]
        for name in pycorpora.humans.celebrities["celebrities"]:
            parts = name.split()
            nameList += parts[-1]
        cachedLastNameList = dedup(nameList)

    return random.choice(cachedLastNameList).title()


def makePronouns(pd):
    d100 = random.randrange(0,100)
    if (d100 < 45):
        pd[HE_SHE_PRONOUN_TAG] = "he"
        pd[HIS_HER_PRONOUN_TAG] = "his"
        pd[HIM_HER_PRONOUN_TAG] = "him"
        pd[GENDER_TAG] = GENDER_MALE_TAG
    elif (d100 < 90):
        pd[HE_SHE_PRONOUN_TAG] = "she"
        pd[HIS_HER_PRONOUN_TAG] = "her"
        pd[HIM_HER_PRONOUN_TAG] = "her"
        pd[GENDER_TAG] = GENDER_FEMALE_TAG
    elif (d100 < 98):
        pd[HE_SHE_PRONOUN_TAG] = "they"
        pd[HIS_HER_PRONOUN_TAG] = "their"
        pd[HIM_HER_PRONOUN_TAG] = "them"
        pd[GENDER_TAG] = GENDER_NEUTER_TAG
    else:
        pd[HE_SHE_PRONOUN_TAG] = "xe"
        pd[HIS_HER_PRONOUN_TAG] = "xis"
        pd[HIM_HER_PRONOUN_TAG] = "xem"        
        pd[GENDER_TAG] = GENDER_OTHER_TAG
        

if __name__ == "__main__":
    print (makeperson())

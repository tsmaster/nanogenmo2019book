import random
import pycorpora

from tags import *
from util import *

import makeplacename

def makeperson():
    pd = {}

    pd[FIRSTNAME_TAG] = mutateWord(random.choice(pycorpora.humans.firstNames["firstNames"])).capitalize()
    pd[LASTNAME_TAG] = mutateWord(random.choice(pycorpora.humans.lastNames["lastNames"])).capitalize()
    pd[FULLNAME_TAG] = pd[FIRSTNAME_TAG] + " " + pd[LASTNAME_TAG]
    pd[HOMETOWN_TAG] = makeplacename.makePlaceName()
    makePronouns(pd)
    pd[RACE_TAG] = random.choice(getList("races.txt"))

    return pd

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

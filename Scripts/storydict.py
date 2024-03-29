import makeperson
from tags import *

def makeStoryDict():
    storyDict = {}

    h = makeperson.makeperson()
    m = makeperson.makeperson()
    
    storyDict[HERO_TAG] = h
    storyDict[MENTOR_TAG] = m
    h[MENTOR_TAG] = m
    m[MENTEE_TAG] = h

    m[HOMETOWN_TAG] = h[HOMETOWN_TAG]

    return storyDict

def getHeroHeShePronoun(storyDict):
    hero = storyDict[HERO_TAG]
    return hero[HE_SHE_PRONOUN_TAG]

def getHeroHimHerPronoun(storyDict):
    hero = storyDict[HERO_TAG]
    return hero[HIM_HER_PRONOUN_TAG]

def getHeroHisHerPronoun(storyDict):
    hero = storyDict[HERO_TAG]
    return hero[HIS_HER_PRONOUN_TAG]


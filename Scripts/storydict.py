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

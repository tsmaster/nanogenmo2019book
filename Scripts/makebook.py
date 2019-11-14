import nltk
import textblob
import sys
import random
import string

import makechapter
import colors
import makeperson
from util import *
from tags import *

if sys.version_info[0] < 3:
    raise Exception("must use Python 3 or later")

TARGET_WORD_COUNT = 5000

missionObjectsList = dedup(getList("weapons.txt") + getList("armor.txt"))
missionObjectsAdjectivesList = dedup(getList("adjectives.txt") + colors.getColors())
monsterList = getList("monsters.txt")
treasureList = getList("treasure.txt")

def isVowel(c):
    return c in "aeiou"

def makeMissionObject():
    noun = random.choice(missionObjectsList)
    adjective = random.choice(missionObjectsAdjectivesList)
    article = "a"
    if isVowel(adjective[0]):
        article = "an"
    return ' '.join([article, adjective, noun])

def makePlaceName():
    s = ''
    wordLen = random.randrange(4,8)
    for i in range(wordLen):
        s += random.choice(string.ascii_lowercase)
    return s.capitalize()

def makeHonorific(gender):
    table = {GENDER_MALE_TAG: 'sir',
             GENDER_FEMALE_TAG: "ma'am",
             GENDER_NEUTER_TAG: "respected one",
             GENDER_OTHER_TAG: "respected one"}
    return table[gender]

def makeMonsterName():
    return random.choice(monsterList)

def makeTreasure():
    treasureName = random.choice(treasureList)
    treasureAdj = random.choice(missionObjectsAdjectivesList)
    return ' '.join([treasureAdj, treasureName])

def makeCallToActionChapter(storyDict):
    hero = storyDict[HERO_TAG]
    mentor = storyDict[MENTOR_TAG]

    heroGender = hero[GENDER_TAG]
    heroRace = hero[RACE_TAG]
    
    text = "{0} was a {5} {6} that lived in {1}. {1} was a nice town. Nondescript, for now. {2} had a mentor, named {3}. Also nondescript. {4} tells {2} 'I call you to adventure!'. But {2} says 'No {7}! I refuse the call to adventure. I want to stay here in {1} and smoke pipes at Tosci's Power Converters and Pipe shop'.".format(
        hero[FULLNAME_TAG],
        hero[HOMETOWN_TAG],
        hero[FIRSTNAME_TAG],
        mentor[FULLNAME_TAG],
        mentor[FIRSTNAME_TAG],
        heroGender,
        heroRace,
        makeHonorific(mentor[GENDER_TAG])
    )
    return makechapter.Chapter(1, text)

def makeHappilyEverAfterChapter():
    text = "And they all lived happily ever after. That is the end of the story, until we tell another tale."
    return makechapter.Chapter(7, text)

def makeMissionChapter():
    missionObject = makeMissionObject()
    placename = makePlaceName()
    monster = makeMonsterName()
    treasure1 = makeTreasure()
    treasure2 = makeTreasure()
    text = "And then he went on a mission to fetch {0}. He went to {1} and killed a {2}. On the body, he found {3} and {4}.".format(missionObject, placename, monster, treasure1, treasure2)
    return makechapter.Chapter(1, text)

def makePigChapter():
    text = 'And then the Orange Baby Pig said "Yeah, but I\'m going to need you to do me a favor first. I want 100 of the best hamberders. And so he went and got some hamberders. And they were fine, I guess. And the Orange Baby Pig was happy. There must have been a lot of birds around, because you could hear so much happy tweeting.'
    return makechapter.Chapter(45, text)

def renumber(chapterList):
    for i, c in enumerate(chapterList):
        c.chapterNumber = i + 1

def calculateWordCount(chapterList):
    return sum([c.wordcount() for c in chapterList])

def formBook(chapterList):
    text = '\n'.join([str(c) for c in chapterList])
    blob = textblob.TextBlob(text)
    #return str(cycletext(blob))
    return str(blob)

def cycletext(blob):
    langs = ['es', 'fr', 'de', 'it', 'sw', 'sv', 'no', 'is', 'en']
    for lang in langs:
        print("translating to", lang)
        blob = blob.translate(to=lang)
    return blob

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

storyDict = makeStoryDict()

chapters = [
    makeCallToActionChapter(storyDict),
    makeHappilyEverAfterChapter()]

while calculateWordCount(chapters) < TARGET_WORD_COUNT:
    chapters.insert(1, makeMissionChapter())

chapters[44] = makePigChapter()
renumber(chapters)

s = formBook(chapters)
with open("book.txt", "wt") as f:
    f.write(s)


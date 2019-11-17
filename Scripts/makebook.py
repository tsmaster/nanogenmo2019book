import nltk
import textblob
import sys
import random
import string
import time

import makechapter
import colors
import makeperson
import wordwrap
from util import *
from tags import *
import makemobychapter
import storydict
import makefeastchapter
import makepoem
from makepoem import Language, Word

if sys.version_info[0] < 3:
    raise Exception("must use Python 3 or later")

TARGET_WORD_COUNT = 10000

FAKE_GPT2 = True

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
    return makechapter.Chapter(1, hero[FULLNAME_TAG], text)

def makeHappilyEverAfterChapter():
    text = "And they all lived happily ever after. That is the end of the story, until we tell another tale."
    return makechapter.Chapter(7, "Resolutions", text)

def makeMissionChapter():
    missionObject = makeMissionObject()
    placename = makePlaceName()
    monster = makeMonsterName()
    treasure1 = makeTreasure()
    treasure2 = makeTreasure()
    text = "And then he went on a mission to fetch {0}. He went to {1} and killed a {2}. On the body, he found {3} and {4}.".format(missionObject, placename, monster, treasure1, treasure2)
    return makechapter.Chapter(1, "A Mission to fetch a {0} and kill a {1}".format(missionObject, monster), text)

def makePigChapter():
    text = 'And then the Orange Baby Pig said "Yeah, but I\'m going to need you to do me a favor first. I want 100 of the best hamberders. And so he went and got some hamberders. And they were fine, I guess. And the Orange Baby Pig was happy. There must have been a lot of birds around, because you could hear so much happy tweeting.'
    return makechapter.Chapter(45, "An Obstruction", text)

def renumber(chapterList):
    for i, c in enumerate(chapterList):
        c.chapterNumber = i + 1

def calculateWordCount(chapterList):
    return sum([c.wordcount() for c in chapterList])

def formBook(chapterList):
    text = '\n'.join([str(c) for c in chapterList])
    blob = textblob.TextBlob(text)
    #return str(cycletext(blob))
    return wordwrap.wordwrap(str(blob), 65)

def cycletext(blob):
    langs = ['es', 'fr', 'de', 'it', 'sw', 'sv', 'no', 'is', 'en']
    for lang in langs:
        print("translating to", lang)
        blob = blob.translate(to=lang)
    return blob

storyDict = storydict.makeStoryDict()

startTime = time.time()

def reportProgress(chapters):
    cw = calculateWordCount(chapters)
    print("current words: {0} target words: {1}".format(cw, TARGET_WORD_COUNT))
    timeNow = time.time()
    elapsedSeconds = timeNow - startTime
    print("elapsed seconds: {0}".format(elapsedSeconds))
    print("words per second: {0:.2f}".format(cw / elapsedSeconds))

chapters = [
    makeCallToActionChapter(storyDict)]

while calculateWordCount(chapters) < TARGET_WORD_COUNT:
    print ("making mission chapter {0}".format(len(chapters)))
    chapters.append(makeMissionChapter())
    reportProgress(chapters)
    # TODO fetch monster from recent mission
    monster = makeMonsterName()
    print ("making feast of {0} chapter {1}".format(len(chapters), monster))
    chapters.append(makefeastchapter.makeFeastChapter(monster, storyDict))
    reportProgress(chapters)
    # TODO pull item from inventory
    craftItem = makeMissionObject()
    print ("making crafting chapter {0} about {1}".format(len(chapters), craftItem))
    chapters.append(makemobychapter.makeMobyChapter(craftItem, 800, FAKE_GPT2))
    reportProgress(chapters)
    print ("making poem chapter {0}".format(len(chapters)))
    chapters.append(makepoem.makePoemChapter(storyDict))
    reportProgress(chapters)

if len(chapters) > 50:
    pigIndex = 44
else:
    pigIndex = int(len(chapters) / 2)
    
chapters.insert(pigIndex, makePigChapter())

chapters.append(makeHappilyEverAfterChapter())

reportProgress(chapters)

renumber(chapters)

s = formBook(chapters)
with open("book.txt", "wt") as f:
    f.write(s)


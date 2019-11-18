import nltk
import textblob
import sys
import random
import string
import time
import datetime

import makechapter
import colors
import makeperson
import wordwrap
from util import *
from tags import *
import makemobychapter
import storydict
import makefeastchapter
import makepigchapter
import makepoem
from makepoem import Language, Word

if sys.version_info[0] < 3:
    raise Exception("must use Python 3 or later")

TARGET_WORD_COUNT = 12000

FAKE_GPT2 = False

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

def makeMissionParagraph(storyDict):
    missionObject = makeMissionObject()
    placename = makePlaceName()
    monster = makeMonsterName()
    treasure1 = makeTreasure()
    treasure2 = makeTreasure()
    text = "And then {5} went on a mission to fetch {0}. He went to {1} and killed a {2}. On the body, {5} found {3} and {4}.".format(missionObject, placename, monster, treasure1, treasure2, storydict.getHeroHeShePronoun(storyDict))
    return text, missionObject, monster, placename

def makeMissionChapter(storyDict):
    numParas = random.randrange(10, 20)
    text = ""
    for i in range(numParas):
        partext, missionobj, monster, placename = makeMissionParagraph(storyDict)
        text += partext
        text += "\n\n"

    fetchTitle = "A mission to fetch a " + missionobj
    killTitle = "A mission to kill a " + monster
    cityTitle = "A mission to visit " + placename

    chapterTitle = random.choice([fetchTitle, killTitle, cityTitle])

    chapterText = makechapter.Chapter(1, chapterTitle, text)
    return chapterText, monster, missionobj


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
    missionText, missionMonster, missionObj = makeMissionChapter(storyDict)
    chapters.append(missionText)
    reportProgress(chapters)
    print ("making feast of {1} chapter {0}".format(len(chapters), missionMonster))
    chapters.append(makefeastchapter.makeFeastChapter(missionMonster, storyDict))
    reportProgress(chapters)
    print ("making crafting chapter {0} about {1}".format(len(chapters), missionObj))
    chapters.append(makemobychapter.makeMobyChapter(missionObj, 800, FAKE_GPT2))
    reportProgress(chapters)
    print ("making poem chapter {0}".format(len(chapters)))
    chapters.append(makepoem.makePoemChapter(storyDict))
    reportProgress(chapters)

if len(chapters) > 50:
    pigIndex = 44
else:
    pigIndex = int(len(chapters) / 2)
    
chapters.insert(pigIndex, makepigchapter.makePigChapter(storyDict))

chapters.append(makeHappilyEverAfterChapter())

reportProgress(chapters)

renumber(chapters)

s = formBook(chapters)

timeLabel = datetime.datetime.now().strftime("draft_%Y_%m_%d_%H_%M")
draftFilename = "../DraftBooks/{0}_{1}.txt".format(timeLabel, TARGET_WORD_COUNT)
rootFilename = "../book.txt"

for fn in [draftFilename, rootFilename]:
    with open(fn, "wt") as f:
        f.write(s)


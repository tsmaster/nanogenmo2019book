import nltk
import textblob
import sys
import random
import string
import time
import datetime
import argparse

import tracery
from tracery.modifiers import base_english

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
import makeplacename
import makejourney

if sys.version_info[0] < 3:
    raise Exception("must use Python 3 or later")

TARGET_WORD_COUNT = 50000

FAKE_GPT2 = True



def makeHonorific(gender):
    table = {GENDER_MALE_TAG: 'sir',
             GENDER_FEMALE_TAG: "ma'am",
             GENDER_NEUTER_TAG: "respected one",
             GENDER_OTHER_TAG: "respected one"}
    return table[gender]

def makeMentorDescription():
    oldWords = [
        'old',
        'ancient',
        'decrepit',
        'elderly',
        'gray',
        'tired',
        'along in years']
    wiseWords = [
        'wise',
        'well-versed',
        'venerable',
        'educated',
        'knowledgable',
        'perceptive',
        'sensible',
        'shrewd',
        'smart',
        'contemplative',
        'sage',
        'keen',
        'sharp']
    return random.choice(oldWords) + ' and ' + random.choice(wiseWords)

def makeHeroDescription():
    youngWords = [
        'young',
        'youthful',
        'inexerienced',
        'fledgling',
        'green',
        'growing',
        'little',
        'juvenile',
        'raw',
        'childish',
        'childlike',
        'callow',
        ]
    brashWords = [
        'bold',
        'brash',
        'impetuous',
        'headstrong',
        'adventurous',
        'curious',
        'imaginitive',
        'ignorant',
        'unseasoned',
        ]
    return random.choice(youngWords) + ' and ' + random.choice(brashWords)


def makeTownDescription():
    smallWords = [
        'small',
        'wee',
        'tiny',
        'cramped',
        'meager',
        'modest',
        'narrow',
        'paltry',
        'poor',
        'small-scale',
        'slight',
        'diminutive',
        'little',
        'trifling',
        ]
    quaintWords = [
        'curious',
        'quaint',
        'fanciful',
        'peculiar',
        'unusual',
        'whimsical',
        'weird',
        'eccentric',
        'fantastic',
        'idiosyncratic',
        'off the beaten track',
    ]

    return random.choice(smallWords) + ' and ' + random.choice(quaintWords)


def makeReasonToRefuse(storyDict):
    actions = [
        "smoke pipes",
        "shoot billiards",
        "sing songs",
        "buy power converters",
        "catch pocket monsters",
        "read stories",
        "bulls-eye womp rats",
        ]

    locations = [
        "at Tosci's Power Converters and Pipe Shop",
        "at Taasche Station",
        "in Beggar's Canyon",
        "in The Shire",
        "in the City Square",
        "behind the temple",
        "under the bridge",
        ]
    text = "I want to stay here in {0} and {1} {2}".format(
        storyDict[HERO_TAG][HOMETOWN_TAG],
        random.choice(actions),
        random.choice(locations))
    return text

def makeCallToActionChapter(storyDict):
    hero = storyDict[HERO_TAG]
    mentor = storyDict[MENTOR_TAG]

    heroGender = hero[GENDER_TAG]
    heroRace = hero[RACE_TAG]
    
    text = "{0} was a {5} {6} that lived in {1}. {2} was {9}. {1} was a nice town. {1} was {10}. {2} had a mentor, named {3}. {4} was {8}.\n\n{4} told {2} 'I call you to adventure!'.\n\nBut {2} said 'No, {7}! I refuse the call to adventure. {11}'.".format(
        hero[FULLNAME_TAG],
        hero[HOMETOWN_TAG],
        hero[FIRSTNAME_TAG],
        mentor[FULLNAME_TAG],
        mentor[FIRSTNAME_TAG],
        heroGender,
        heroRace,
        makeHonorific(mentor[GENDER_TAG]),
        makeMentorDescription(),
        makeHeroDescription(),
        makeTownDescription(),
        makeReasonToRefuse(storyDict)
    )
    return makechapter.Chapter(1, hero[FULLNAME_TAG], text)

def makeHappilyEverAfterChapter():
    text = "And they all lived happily ever after. That is the end of the story, until we tell another tale."
    return makechapter.Chapter(7, "Resolutions", text)


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

def reportProgress(chapters, startTime):
    cw = calculateWordCount(chapters)
    print("current words: {0} target words: {1}".format(cw, TARGET_WORD_COUNT))
    timeNow = time.time()
    elapsedSeconds = timeNow - startTime
    print("elapsed seconds: {0}".format(elapsedSeconds))
    print("words per second: {0:.2f}".format(cw / elapsedSeconds))


def centerLine(s, pageWidth):
    numSpaces = int((pageWidth / 2) - (len(s)/2))
    padding = ' ' * numSpaces
    return padding + s
    
    
def makeTitlePage(storyDict):
    pageWidth = 70
    titleLine = centerLine("SHAPESHIFTING", pageWidth)
    subtitleLine = centerLine("{0} and the Generation of Adventure".format(storyDict[HERO_TAG][FULLNAME_TAG]), pageWidth)
    
    return titleLine + "\n" + subtitleLine + "\n\n\n\n"

def reroll(storyDict):
    while True:
        print
        print ("do you like this hero?")
        print ("firstname: " + storyDict[HERO_TAG][FIRSTNAME_TAG])
        print ("lastname: " + storyDict[HERO_TAG][LASTNAME_TAG])
        print ("gender: " + storyDict[HERO_TAG][GENDER_TAG])
        print ("race: " + storyDict[HERO_TAG][RACE_TAG])
        print()
        print("1 - fn / 2 - ln / 3 - gender / 4 - race")
        print("g - good / r - reroll / q - quit")
        cmd = input("cmd: ")

        if cmd == 'q':
            return False

        if cmd == 'r':
            storyDict[HERO_TAG] = makeperson.makeperson()

        if cmd == 'g':
            return True

        if cmd == '1':
            storyDict[HERO_TAG][FIRSTNAME_TAG] = makeperson.makeFirstName()

        if cmd == '2':
            storyDict[HERO_TAG][LASTNAME_TAG] = makeperson.makeLastName()

        if cmd == '3':
            makeperson.makePronouns(storyDict[HERO_TAG])

        if cmd == '4':
            storyDict[HERO_TAG][RACE_TAG] = makeperson.makeRace()

        
    

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--interactive",
                        help="give the opportunity to reroll the hero",
                        action="store_true")

    args = parser.parse_args()
    
    storyDict = storydict.makeStoryDict()

    if args.interactive:
        continueGenerating = reroll(storyDict)
        if not continueGenerating:
            sys.exit(-1)

    startTime = time.time()

    chapters = [
        makeCallToActionChapter(storyDict)]

    while calculateWordCount(chapters) < TARGET_WORD_COUNT:
        print ("making mission chapter {0}".format(len(chapters)))
        missionText, missionMonster, missionObj = makejourney.makeJourneyChapter(storyDict)
        chapters.append(missionText)
        reportProgress(chapters, startTime)
    
        dieRoll = random.randrange(10)
        if ((dieRoll < 4) and (not (missionMonster is None))):
            print ("making feast of {1} chapter {0}".format(len(chapters), missionMonster))
            chapters.append(makefeastchapter.makeFeastChapter(missionMonster, storyDict))
            reportProgress(chapters, startTime)
        elif ((dieRoll < 8) and (not (missionObj is None))):
            print ("making crafting chapter {0} about {1}".format(len(chapters), missionObj))
            chapters.append(makemobychapter.makeMobyChapter(missionObj, 600, FAKE_GPT2))
            reportProgress(chapters, startTime)
        else:
            print ("making poem chapter {0}".format(len(chapters)))
            chapters.append(makepoem.makePoemChapter(storyDict))
            reportProgress(chapters, startTime)
    
    if len(chapters) > 50:
        pigIndex = 44
    else:
        pigIndex = int(len(chapters) / 2)
        
    chapters.insert(pigIndex, makepigchapter.makePigChapter(storyDict))
    
    chapters.append(makeHappilyEverAfterChapter())
    
    reportProgress(chapters, startTime)
    
    renumber(chapters)
    
    s = makeTitlePage(storyDict) + '\n' + formBook(chapters)
    
    timeLabel = datetime.datetime.now().strftime("draft_%Y_%m_%d_%H_%M")
    draftFilename = "../DraftBooks/{0}_{1}.txt".format(timeLabel, TARGET_WORD_COUNT)
    rootFilename = "../book.txt"
    
    for fn in [draftFilename, rootFilename]:
        with open(fn, "wt") as f:
            f.write(s)


if __name__ == "__main__":
    main()

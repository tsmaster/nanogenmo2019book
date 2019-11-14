import nltk
import textblob
import sys
import random
import string

import makechapter

if sys.version_info[0] < 3:
    raise Exception("must use Python 3 or later")

TARGET_WORD_COUNT = 5000

def getList(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [w.strip() for w in lines]
        lines = [w for w in lines if w]
        return lines

def dedup(wordlist):
    wordset = set(wordlist)
    return list(wordset)

missionObjectsList = dedup(getList("weapons.txt") + getList("armor.txt"))
missionObjectsAdjectivesList = getList("adjectives.txt")
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

def makeMonsterName():
    return random.choice(monsterList)

def makeTreasure():
    treasureName = random.choice(treasureList)
    treasureAdj = random.choice(missionObjectsAdjectivesList)
    return ' '.join([treasureAdj, treasureName])

def makeCallToActionChapter():
    text = "So there was this guy. He's going to have a name, but for now he's nameless. He lived in a town, which was nice. Nondescript, for now. He's got a mentor. Also nondescript and nameless. The mentor tells the hero 'I call you to adventure!'. But the hero says 'No sir! I refuse the call to adventure. I want to stay here in The Shire and smoke pipes at Tosci's Power Converters and Pipe shop'."
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
    return str(cycletext(blob))

def cycletext(blob):
    langs = ['es', 'fr', 'de', 'it', 'sw', 'sv', 'no', 'is', 'en']
    for lang in langs:
        print("translating to", lang)
        blob = blob.translate(to=lang)
    return blob

chapters = [
    makeCallToActionChapter(),
    makeHappilyEverAfterChapter()]

while calculateWordCount(chapters) < TARGET_WORD_COUNT:
    chapters.insert(1, makeMissionChapter())

chapters[44] = makePigChapter()
renumber(chapters)

s = formBook(chapters)
with open("book.txt", "wt") as f:
    f.write(s)


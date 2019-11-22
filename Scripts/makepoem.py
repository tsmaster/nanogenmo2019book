import random
import jsonpickle
from pincelate import Pincelate
import pronouncing
import words
import util
import rhymelang
from util import *
import storydict
import makechapter

pin = None

class Word:
    def __init__(self, s, phonemes):
        self.word = s
        self.phonemes = phonemes
        self.phoneme_string = ' '.join(self.phonemes)
        self.rhyming_part = pronouncing.rhyming_part(self.phoneme_string)
        self.syllable_count = pronouncing.syllable_count(self.phoneme_string)

    def __str__(self):
        return self.word

def makeStableWord(s):
    global pin
    if pin is None:
        pin = Pincelate()
    for i in range(5):
        so = pin.soundout(s)
        s = pin.spell(so)
    return Word(s, pin.soundout(s))

def addToDictOfLists(dol, k, v):
    oldList = dol.get(k, [])
    newList = oldList + [v]
    dol[k] = newList

class Language:
    def __init__(self):
        self.words = {}
        self.wordsBySylCount = [[] for x in range(10)]

    def copyFrom(self, other):
        self.words = other.words
        self.wordsBySylCount = other.wordsBySylCount

    def addWord(self, word):
        addToDictOfLists(self.words, word.rhyming_part, word)

        sc = word.syllable_count
        while sc >= len(self.wordsBySylCount):
            self.wordsBySylCount += []

        self.wordsBySylCount[sc].append(word)

    def findRhymes(self, s):
        if isinstance(s, Word):
            w = s
        else:
            w = Word(str(s))
        return self.words.get(w.rhyming_part, [])

    def randWord(self):
        return random.choice(list(self.genAllWords()))

    def genAllWords(self):
        for v in self.words.values():
            yield v

    def randWordBySylCount(self, minCount=0, maxCount=-1):
        matchingCounts = []
        for k in range(len(self.wordsBySylCount)):
            if ((k >= minCount) and
                ((maxCount < 0) or (k <= maxCount)) and
                (len(self.wordsBySylCount[k]) > 0)):
                matchingCounts.append(k)
        chosenCount = random.choice(matchingCounts)
        return random.choice(self.wordsBySylCount[chosenCount])

    def writeToDisk(self, filename):
        encoded = jsonpickle.encode(self)
        
        with open(filename, "wt") as nsJson:
            nsJson.write(encoded)


def readLangFromDisk(filename):
    with open(filename, "rt") as nsJson:
        encoded = nsJson.read()
        
        lang = jsonpickle.decode(encoded)
        return lang

def addWordsToLanguage(lang, n):
    wl = list(words.getWordList())
    random.shuffle(wl)
    for ew in wl:
        if n <= 0:
            return
        try:
            mw = util.mutateWord(ew)
            w = makeStableWord(mw)
            #w = Word(ew)
            print(n, w)
            lang.addWord(w)
            n = n - 1
        except KeyError:
            pass

def getSylCountForWordList(wl):
    return sum([w.syllable_count for w in wl])

def makeLine(lang, sylCount, rhymeLine):
    words = []

    if not (rhymeLine is None):
        rhymeWord = rhymeLine[-1]
        rhymeList = lang.findRhymes(rhymeWord)
        if len(rhymeList) == 0:
            selRhyme = rhymeWord
        else:
            selRhyme = random.choice(rhymeList)
        words.append(selRhyme)
    while (getSylCountForWordList(words) < sylCount):
        scfwl = getSylCountForWordList(words)
        sylRemain = sylCount - scfwl
        cw = lang.randWordBySylCount(1, sylRemain)
        if cw.syllable_count <= sylRemain:
            words.insert(0, cw)
    return words

class WordTooLongForLineException(Exception):
    pass

class InsufficientRhymeException(Exception):
    pass

def makeLineEndsWithWord(lang, sylCount, word):
    words = [word]
    if word.syllable_count > sylCount:
        raise WordTooLongForLineException

    while (getSylCountForWordList(words) < sylCount):
        scfwl = getSylCountForWordList(words)
        sylRemain = sylCount - scfwl
        cw = lang.randWordBySylCount(1, sylRemain)
        if cw.syllable_count <= sylRemain:
            words.insert(0, cw)
    return words

def makePoem(lang, pairs):
    rhymeLines = {}
    s = ""
    for sylCount, rhymeKey in pairs:
        line = makeLine(lang, sylCount, rhymeLines.get(rhymeKey, None))
        if not (rhymeKey in rhymeLines):
            rhymeLines[rhymeKey] = line
        lineWords = [str(w) for w in line]
        s += ' '.join(lineWords)
        s += "\n"

    return s


poemPatterns = {
    'limerick': [(9, 'A'), (9, 'A'), (5, 'B'), (5, 'B'), (9, 'A')],
    'haiku': [(5, 'A'), (7, 'B'), (5, 'C')],
    'sonnet-eng': [
        (10, 'A'), (10, 'B'),
        (10, 'A'), (10, 'B'),
        (10, 'C'), (10, 'D'),
        (10, 'C'), (10, 'D'),
        (10, 'E'), (10, 'F'),
        (10, 'E'), (10, 'F'),
        (10, 'G'), (10, 'G')],
    'sonnet-ital': [
        (10, 'A'), (10, 'B'), (10, 'B'), (10, 'A'),
        (10, 'A'), (10, 'B'), (10, 'B'), (10, 'A'),
        (10, 'C'), (10, 'D'), (10, 'E'),
        (10, 'C'), (10, 'D'), (10, 'E')],
    'sonnet-dave': [
        (10, 'A'), (10, 'A'), (10, 'A'),
        (10, 'B'), (10, 'B'), (10, 'B'),
        (10, 'C'), (10, 'C'),
        (10, 'D'), (10, 'D'), (10, 'D'),
        (10, 'E'), (10, 'E'), (10, 'E'),
    ],
    'fib': [
        (1, 'A'), (2, 'B'), (3, 'A'),
        (5, 'A'), (8, 'B'), (13, 'A')],
    'pi': [
        (3, 'A'), (1, 'A'), (4, 'B'),
        (1, 'A'), (5, 'A'), (9, 'A'),
        (2, 'B'), (6, 'B'), (5, 'A'),
        (4, 'B')],
    'prime': [
        (2, 'A'),
        (3, 'B'), (5, 'B'), (7, 'B'),
        (11, 'C'), (13, 'C'),
        (17, 'D'), (19, 'D')],
}

def printPoems():
    for pk in poemPatterns:
        print (pk)
        print (makePoem(lang, poemPatterns[pk]))
        print ()

def findRhymeKeys(lang, numRhymes):
    for k, words in lang.words.items():
        if len(words)>= numRhymes:
            yield k

def genBindings(rhymeSections, rhymeCountsDict):
    # rhymeSections is a list of sections
    # rhymeCountsDict maps chars to counts
    # the binding returns a dictionary mapping chars to sections

    chars = list(rhymeCountsDict.keys())
    while True:
        random.shuffle(chars)
        usedSections = []
        outDict = {}
        for c in chars:
            while True:
                sect = random.choice(rhymeSections)
                if sect in usedSections:
                    continue
                outDict[c] = sect
                usedSections.append(sect)
                break
        yield outDict

def isSubstringOfAny(rhymeWord, usedWords):
    rws = str(rhymeWord)
    for w in usedWords:
        ws = str(w)
        if ((ws in rws) or
            (rws in ws)):
            return True
    return False

def genPoemsFromPattern(lang, pattern):
    rhymeCountsDict = {}
    for syl, rhymeKey in pattern:
        count = rhymeCountsDict.get(rhymeKey, 0)
        rhymeCountsDict[rhymeKey] = count + 1
    maxKeys = 0
    for key, val in rhymeCountsDict.items():
        maxKeys = max(maxKeys, val)
    rhymeKeys = list(findRhymeKeys(lang, maxKeys))
    random.shuffle(rhymeKeys)
    for b in genBindings(rhymeKeys, rhymeCountsDict):
        try:
            # b is a map of rhymeKeys ('A', 'B') to word rhyming sections (e.g. 'AH T EN')
            lastWords = ['?'] * len(pattern)
            lines = ['?'] * len(pattern)
            for lineNum, pat in enumerate(pattern):
                sylCount, rhymeChar = pat
                rhymeSect = b[rhymeChar]

                foundRhyme = False
                candWords = lang.words[rhymeSect][:]
                random.shuffle(candWords)
                for rhymeWord in candWords:
                    rhymeWord = random.choice(lang.words[rhymeSect])
                    if (not (isSubstringOfAny(rhymeWord,lastWords))):
                        foundRhyme = True
                        break
                if not foundRhyme:
                    raise InsufficientRhymeException()
                lastWords[lineNum] = rhymeWord
                lineAsWordList = makeLineEndsWithWord(lang, sylCount, rhymeWord)
                lines[lineNum] = ' '.join([str(w) for w in lineAsWordList])
            poem = '\n'.join(lines)
            yield (poem + '\n\n')
        except WordTooLongForLineException:
            print("too long, trying again")
        except InsufficientRhymeException:
            print("bad rhyme, trying again")

def genLimericks(lang):
    rhymeKeys = list(findRhymeKeys(lang, 3))
    random.shuffle(rhymeKeys)

    keypairs = []
    
    for a in rhymeKeys:
        for b in rhymeKeys:
            if b == a:
                continue
            keypairs.append((a,b))

    random.shuffle(keypairs)

    while True:
        for a,b in keypairs:
            aWords = random.sample(lang.words[a], 3)
            bWords = random.sample(lang.words[b], 2)
                
            line1 = makeLineEndsWithWord(lang, 9, aWords[0])
            line2 = makeLineEndsWithWord(lang, 9, aWords[1])
            line3 = makeLineEndsWithWord(lang, 5, bWords[0])
            line4 = makeLineEndsWithWord(lang, 5, bWords[1])
            line5 = makeLineEndsWithWord(lang, 9, aWords[2])
    
            s = ""
            for line in [line1, line2, line3, line4, line5]:
                words = [str(w) for w in line]
                s = s + ' '.join(words)
                s += "\n"
            yield s


def foreverLimericks(lang):
    while True:
        for i, lim in enumerate(genLimericks(lang)):
            if i > 5:
                break
            print (i)
            print (lim)
            print ()
        
        addWordsToLanguage(lang, 100)
        lang.writeToDisk("nonsense.json")

def makeLimerickChapterText(lang):
    numPars = random.randrange(5, 25)

    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns['limerick'])):
        if i > numPars:
            break
        output += lim
    return output

def makeEngSonnetChapterText(lang):
    numPars = random.randrange(4, 16)
    patName = 'sonnet-eng'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output

def makeItalSonnetChapterText(lang):
    numPars = random.randrange(4, 16)
    patName = 'sonnet-ital'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output

def makeMixedSonnetChapterText(lang):
    numPars = random.randrange(4, 16)

    output = ""

    engGen = genPoemsFromPattern(lang, poemPatterns['sonnet-eng'])
    italGen = genPoemsFromPattern(lang, poemPatterns['sonnet-ital'])
    
    for i in range(0, numPars, 2):
        output += next(engGen)
        output += next(italGen)
    return output

def makeDaveSonnetChapterText(lang):
    numPars = random.randrange(4, 16)
    patName = 'sonnet-dave'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output

def makeHaikuChapterText(lang):
    numPars = random.randrange(5, 20)
    patName = 'haiku'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output

def makeFibChapterText(lang):
    numPars = random.randrange(5, 10)
    patName = 'fib'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output

def makePiChapterText(lang):
    numPars = random.randrange(3, 10)
    patName = 'pi'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output

def makePrimeChapterText(lang):
    numPars = random.randrange(7, 13)
    patName = 'prime'
    
    output = ""
    for i, lim in enumerate(genPoemsFromPattern(lang, poemPatterns[patName])):
        if i > numPars:
            break
        output += lim
    return output



def makePoemChapter(storyDict):
    lang = readLangFromDisk("nonsense.json")
    #print("lang:", type(lang))
    if type(lang) == type({'a':1}):
        newLang = Language()
        newLang.words = lang['words']
        newLang.wordsBySylCount = lang['wordsBySylCount']
        print("rewrote lang")
        lang = newLang
    monsterList = getList("monsters.txt")
    monster = random.choice(monsterList)
    output = "This reminds me of a poem told to me by a {0}.\n\n".format(monster)

    makeBodies = [
        makeLimerickChapterText,
        makeEngSonnetChapterText,
        makeItalSonnetChapterText,
        makeMixedSonnetChapterText,
        makeHaikuChapterText,
        makeDaveSonnetChapterText,
        makeFibChapterText,
        makePiChapterText,
        makePrimeChapterText,
    ]

    bodyFact = random.choice(makeBodies)
    
    output += bodyFact(lang)
    title = "a {0} poem".format(monster).title()
    return makechapter.Chapter(1, title, output)

if __name__ == "__main__":
    lang = readLangFromDisk("nonsense.json")

    sd = storydict.makeStoryDict()
    print(makePoemChapter(sd))


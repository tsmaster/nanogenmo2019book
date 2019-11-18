import makepoem
from makepoem import Language, Word
import sys

def removeWordsFromLang(lang, wordsToRemove):
    newWordDict = {}
    for rhymeKey, wordList in lang.words.items():
        wordDict = {}
        for w in wordList:
            if w in wordsToRemove:
                continue
            wordDict[w.word] = w
        newWordList = []
        for k,w in wordDict.items():
            newWordList.append(w)
        newWordList.sort(key = lambda w: w.word)

        newWordDict[rhymeKey] = newWordList
    lang.words = newWordDict

    lang.wordsBySylCount = [[], []]
    for rhymeKey, wordList in lang.words.items():
        for w in wordList:
            wc = w.syllable_count
            while wc >= len(lang.wordsBySylCount):
                lang.wordsBySylCount.append([])
            lang.wordsBySylCount[wc].append(w)

    


if __name__ == "__main__":
    words = sys.argv[1:]
    print ("found words " + str(words))
    
    lang = makepoem.readLangFromDisk("nonsense.json")
    removeWordsFromLang(lang, words)
    lang.writeToDisk("nonsense.json")
    
        
        

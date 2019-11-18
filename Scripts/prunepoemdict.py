import makepoem
from makepoem import Language, Word

if __name__ == "__main__":
    lang = makepoem.readLangFromDisk("nonsense.json")
    newWordDict = {}
    for rhymeKey, wordList in lang.words.items():
        wordDict = {}
        for w in wordList:
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

    lang.writeToDisk("nonsense.json")
    
    
        
        

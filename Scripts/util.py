def getList(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = [w.strip() for w in lines]
        lines = [w for w in lines if w]
        return lines

def dedup(wordlist):
    wordset = set(wordlist)
    return list(wordset)




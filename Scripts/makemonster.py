import random
import util
import pycorpora



monsterList = None

def getMonster():
    if monsterList is None:
        makeMonsterList()
    return random.choice(monsterList)

def getMonsterList():
    if monsterList is None:
        makeMonsterList()
    return monsterList

def makeMonsterList():
    global monsterList
    
    monsterList = util.getList("monsters.txt")
    monsterFile = pycorpora.get_file("mythology", "greek_monsters")
    monsterList += monsterFile["greek_monsters"]
    monsterFile = pycorpora.get_file("mythology", "monsters")
    monsterList += monsterFile["names"]

    monsterList = util.dedup(monsterList)


if __name__ == "__main__":
    for i in range(20):
        print (getMonster())
    

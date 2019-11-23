import random
import util

coins = [
    "gold pieces",
    "silver pieces",
    "platinum pieces",
    "electrum pieces",
    "copper pieces",
    "mithril coins",
]
    

class Inventory:
    def __init__(self):
        self.bag = {}

    def getItems(self):
        return list(self.bag.keys())

    def getItemCount(self, itemName):
        return self.bag.get(itemName, 0)

    def addItem(self, itemName, count=1):
        oldCount = self.getItemCount(itemName)
        self.bag[itemName] = oldCount + count

    def removeItem(self, itemName, count=1):
        oldCount = self.getItemCount(itemName)
        newCount = oldCount - count        
        if newCount < 0:
            raise ArgumentError
        if newCount == 0:
            del(self.bag[itemName])
        else:
            self.bag[itemName] = newCount

    def pocketChange(self):
        c = coins[:]
        random.shuffle(c)
        for cv in c:
            coinCount = self.getItemCount(cv)
            if coinCount > 0:
                return (random.randrange(1, coinCount+1),
                        cv)
        return None

    def report(self):
        s = ""
        for itemName in self.getItems():
            itemCount = self.getItemCount(itemName)
            if itemCount >= 0:
                s += "{0} {1}\n".format(itemCount, util.stripArticle(itemName))
        return s

    def getRandNonCoinObject(self):
        items = self.getItems()
        random.shuffle(items)

        for itemName in items:
            if itemName in coins:
                continue
            itemCount = self.getItemCount(itemName)
            if itemCount > 0:
                return itemName
        return None
                

        



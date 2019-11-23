import random

import tracery
from tracery.modifiers import base_english

import pycorpora

import util
import colors
import makeplacename
import storydict
import makechapter
import makeperson
import makemonster
import inventory

from tags import *

missionObjectsList = util.dedup(util.getList("weapons.txt") + util.getList("armor.txt"))
missionObjectsAdjectivesList = util.dedup(util.getList("adjectives.txt") + colors.getColors())
treasureList = util.getList("treasure.txt")


def makeMissionObject():
    noun = random.choice(missionObjectsList)
    adjective = random.choice(missionObjectsAdjectivesList)
    article = "a"
    if util.isVowel(adjective[0]):
        article = "an"
    return ' '.join([article, adjective, noun]).lower()

def makeTreasure():
    treasureName = random.choice(treasureList)
    treasureAdj = random.choice(missionObjectsAdjectivesList)
    return ' '.join([treasureAdj, treasureName]).lower()

def makeMissionParagraph(storyDict):
    missionObject = makeMissionObject()
    placename = makeplacename.makePlaceName()
    monster = makemonster.getMonster()
    treasure1 = makeTreasure()
    treasure2 = makeTreasure()

    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()
    text = "And then {5} went on a mission to fetch {0}. {6} went to {1} and killed a {2}. On the body, {5} found a {3} and a {4}.".format(missionObject, placename, monster, treasure1, treasure2, heShe, heSheCap)
    return text, missionObject, monster, placename

def makeLocation(cityName):
    locations = [
        "In the forests around {0}",
        "In the sewers beneath {0}",
        "In a dark alley of {0}",
        "In a basement of a deserted house",
        "In the attic of an abandoned mansion",
        "In a vault underneath a temple",
        "In a dungeon near {0}",
        "In a deep cave",
        "In a fortress overlooking {0}",
        "In the ruins of a dwarven fortress",
        "In a shadowy store of {0}",
    ]
    randLoc = random.choice(locations)
    return randLoc.format(cityName)

def makeFetchChapter(storyDict):
    missionObject = makeMissionObject()
    placename = makeplacename.makePlaceName()

    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()

    location = makeLocation(placename)

    questGiver = makeperson.makeperson()
    qgFirstName = questGiver[FIRSTNAME_TAG]
    qgFullName = questGiver[FULLNAME_TAG]

    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]

    inv = storyDict[HERO_INVENTORY_TAG]
    
    success = (random.randrange(0, 10) > 3)

    if not success:
        text = "And then {0} went on a journey to {1}. In {1}, {3} met {5}. {6} sent {7} on a mission to find {4}. {7} explored around {1}, but could not find it.".format(
            heShe,
            placename,
            location,
            heShe,
            missionObject,
            qgFullName,
            qgFirstName,
            heroFirstName,
        )
        
        title = "Searching for {0}".format(missionObject).title()
    else:
        keep = (random.randrange(0, 10) < 3)

        if keep:
            text = "And then {0} went on a journey to {1}. In {1}, {3} met {5}. {6} sent {7} on a mission to find {4}. {7} explored around {1}. {2}, {3} found {4}, which {3} left town with.".format(
                heShe,
                placename,
                location,
                heShe,
                missionObject,
                qgFullName,
                qgFirstName,
                heroFirstName,
            )

            inv.addItem(missionObject)

            title = "Finding {0}".format(missionObject).title()
        else:
            text = "And then {0} went on a journey to {1}. In {1}, {3} met {5}. {6} sent {7} on a mission to find {4}. {7} explored around {1}. {2}, {3} found {4}, which {3} returned to {6}. {6} paid {7} generously for the quest.".format(
                heShe,
                placename,
                location,
                heShe,
                missionObject,
                qgFullName,
                qgFirstName,
                heroFirstName,
            )

            inv.addItem(random.choice(inventory.coins), random.randrange(100,1000))

            title = "Fetching {0}".format(missionObject).title()
            

    chapterDict = {
        'text': text,
        'title': title,
        'monster': None,
        'object': missionObject}
    return chapterDict

def makeKillMonsterChapter(storyDict):
    monster = makemonster.getMonster()
    placename = makeplacename.makePlaceName()

    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()

    location = makeLocation(placename)

    questGiver = makeperson.makeperson()
    qgFirstName = questGiver[FIRSTNAME_TAG]
    qgFullName = questGiver[FULLNAME_TAG]

    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]
    
    text = "And then {0} went on a journey to {1}. In {1}, {3} met {5}. {6} sent {7} on a mission to kill a {4}. {7} explored around {1}. {2}, {3} found a {4}, which {3} fought and killed. {6} paid {7} generously for the quest.".format(
        heShe,
        placename,
        location,
        heShe,
        monster,
        qgFullName,
        qgFirstName,
        heroFirstName,
    )

    inv = storyDict[HERO_INVENTORY_TAG]
    inv.addItem(random.choice(inventory.coins), random.randrange(100,1000))

    title = "Fighting a {0}".format(monster).title()
    chapterDict = {
        'text': text,
        'title': title,
        'monster': monster,
        'object': None
        }
    return chapterDict

def makeBarChapter(storyDict):
    placename = makeplacename.makePlaceName()

    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()

    location = makeLocation(placename)

    questGiver = makeperson.makeperson()
    qgFirstName = questGiver[FIRSTNAME_TAG]
    qgFullName = questGiver[FULLNAME_TAG]

    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]
    hisHer = storyDict[HERO_TAG][HIS_HER_PRONOUN_TAG]

    food = random.choice(util.getList('meat.txt'))
    drink = random.choice(util.getList('alcohol.txt'))

    establishmentType = random.choice([
        "a pub",
        "an inn",
        "a bar",
        "a restaurant",
        "a beerhouse"])

    rules = {
        'name' : [
            'the #object# and #object#',
            'the #adj# #object#',
            ],
        'object' : [
            '#monster#',
            '#inan_object#',
            ],
        'monster' : makemonster.getMonsterList(),
        'inan_object': [
            'cup',
            'table',
            'beer',
            'sword',
            'shield',
            'castle',
            'temple',
            'fire',
            'glass',
            'tankard',
            'keg',
            'plate',
            'spoon',
            'fork',
            'knife',
            ],
        'adj' : missionObjectsAdjectivesList,
        }
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    
    barName = str(grammar.flatten("#name#")).title()
    
    text = "And then {7} went on a journey to {1}. In {1}, {0} went to {2} named {3}. At {3}, {0} ate {4} and drank {5}. Refreshed, {0} went on {6} way.".format(
        heShe,
        placename,
        establishmentType,
        barName,
        food,
        drink,
        hisHer,
        heroFirstName,
    )

    title = "Drinking at {0}".format(barName).title()
    chapterDict = {
        'text': text,
        'title': title,
        'monster': None,
        'object': None
        }
    return chapterDict


def makeBuySellChapter(storyDict):
    placename = makeplacename.makePlaceName()
    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()
    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]

    shopKeeper = makeperson.makeperson()
    skfn = shopKeeper[FIRSTNAME_TAG]

    goodsName = random.choice([
        "weapons",
        "armor",
        "equipment",
        "barding",
        "dry goods",
        ])
    shopType = random.choice([
        "shop",
        "shoppe",
        "retailerie",
        "store",
        "trading post",
        "tent",
        "market",
        ])
    
    shopName = "{0}'s {1} {2}".format(
        skfn,
        goodsName.title(),
        shopType.title())
    
    text = "And then {0} travelled to {1}. In {1}, {2} went to {3}. ".format(
        heroFirstName,
        placename,
        heShe,
        shopName,
    )

    inv = storyDict[HERO_INVENTORY_TAG]
    
    soldItem = inv.getRandNonCoinObject()
    if not (soldItem is None):
        currency = random.choice(inventory.coins)
        sellPrice = random.randrange(50, 5000)

        soldItemWithArticle = util.addArticle(soldItem)
    
        text += "{0} sold {1} for {2} {3}. ".format(
            heroFirstName,
            soldItemWithArticle,
            sellPrice,
            currency)

        inv.addItem(currency, sellPrice)
        inv.removeItem(soldItem, 1)

    pocketChange = inv.pocketChange()
    if not (pocketChange is None):
        coinCount, currency = pocketChange

        equipment = random.choice([
            "potion",
            "shield",
            "hat",
            "helmet",
            "sword",
            "shield",
            "packet of rations",
            "rope",
        ])

        equipmentWithArticle = util.addArticle(equipment)
    
        text += "{0} bought {1} for {2} {3}. ".format(
            heroFirstName,
            equipmentWithArticle,
            coinCount,
            currency)

        inv.addItem(equipment)
        inv.removeItem(currency, coinCount)

    title = "Trading at {0}".format(shopName)
    chapterDict = {
        'text': text,
        'title': title,
        'monster': None,
        'object': None
        }
    return chapterDict

def makeDeity():
    deityList = util.getList("deities.txt")
    
    deityFile = pycorpora.get_file("mythology", "egyptian_gods")
    deityList += list(deityFile["egyptian_gods"].keys())
    
    deityFile = pycorpora.get_file("mythology", "greek_gods")
    deityList += deityFile["greek_gods"]
    
    deityFile = pycorpora.get_file("mythology", "greek_titans")
    deityList += deityFile["greek_titans"]

    deityFile = pycorpora.get_file("mythology", "lovecraft")
    deityList += deityFile["deities"]
    deityList += deityFile["supernatural_creatures"]

    deityFile = pycorpora.get_file("mythology", "norse_gods")
    deityList += deityFile["norse_deities"]

    deityFile = pycorpora.get_file("mythology", "roman_deities")
    deityList += deityFile["roman_deities"]

    deityList = util.dedup(deityList)
    return random.choice(deityList)

def makeHealChapter(storyDict):
    placename = makeplacename.makePlaceName()
    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()
    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]
    himHer = storydict.getHeroHimHerPronoun(storyDict)

    godName = makeDeity()

    inv = storyDict[HERO_INVENTORY_TAG]
    pc = inv.pocketChange()
    if pc is None:
        text = "And then {0} travelled to {1}. In {1}, {2} went to a temple of {3} for healing. The priest laid hands on {4}, which had little effect.".format(
            heroFirstName,
            placename,
            heShe,
            godName,
            himHer,
            heSheCap
        )
    else:
        text = "And then {0} travelled to {1}. In {1}, {2} went to a temple of {3} for healing. The priest laid hands on {4}. {5} gave a generous tithe and left refreshed.".format(
            heroFirstName,
            placename,
            heShe,
            godName,
            himHer,
            heSheCap
        )
        coinCount, coinName = pc
        inv.removeItem(coinName, coinCount)

    title = "Seeking Healing from {0}".format(godName)
    chapterDict = {
        'text': text,
        'title': title,
        'monster': None,
        'object': None
        }
    return chapterDict



def makePrayChapter(storyDict):
    placename = makeplacename.makePlaceName()
    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()
    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]
    himHer = storydict.getHeroHimHerPronoun(storyDict)

    godName = makeDeity()
    
    text = "And then {0} travelled to {1}. In {1}, {2} went to a temple of {3} to pray.".format(
        heroFirstName,
        placename,
        heShe,
        godName,
    )

    title = "Praying to {0}".format(godName)
    chapterDict = {
        'text': text,
        'title': title,
        'monster': None,
        'object': None
        }
    return chapterDict


def makeConsultMysticChapter(storyDict):
    placename = makeplacename.makePlaceName()
    heShe = storydict.getHeroHeShePronoun(storyDict)
    heSheCap = heShe.capitalize()
    heroFirstName = storyDict[HERO_TAG][FIRSTNAME_TAG]
    himHer = storydict.getHeroHimHerPronoun(storyDict)

    godName = makeDeity()
    
    text = "And then {0} travelled to {1}. In {1}, {2} went to a temple of {3} to ask for divine guidance. The priest said a prayer to ask for {3}'s help.".format(
        heroFirstName,
        placename,
        heShe,
        godName,
    )

    title = "Asking for {0}'s Blessing".format(godName)
    chapterDict = {
        'text': text,
        'title': title,
        'monster': None,
        'object': None
        }
    return chapterDict






def makeJourneyChapter(storyDict):
    numParas = random.randrange(10, 20)
    text = ""

    childMakers = [
        makeFetchChapter,
        makeKillMonsterChapter,
        makeBarChapter,
        makeBuySellChapter,
        makeHealChapter,
        makePrayChapter,
        makeConsultMysticChapter,
    ]

    lastMonster = None
    lastObject = None
    
    for i in range(numParas):
        maker = random.choice(childMakers)
        chapterDict = maker(storyDict)
        chapMonster = chapterDict['monster']
        chapObject = chapterDict['object']
        if not (chapMonster is None):
            lastMonster = chapMonster
        if not (chapObject is None):
            lastObject = chapObject
        text += chapterDict['text']
        chapterTitle = chapterDict['title']
        text += "\n\n"

    chapterText = makechapter.Chapter(1, chapterTitle, text)
    return chapterText, lastMonster, lastObject

if __name__ == "__main__":
    sd = storydict.makeStoryDict()
    ct, lm, lo = makeJourneyChapter(sd)
    
    print(ct)
    print("last monster:", lm)
    print("last object:", lo)

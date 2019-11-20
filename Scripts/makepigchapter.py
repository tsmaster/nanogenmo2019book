import random
import tracery
from tracery.modifiers import base_english

from tags import *
import util
import makechapter

def makePigChapter(storyDict):
    hamberder_count = random.randrange(50,150)
    
    text = 'And then the Orange Baby Pig said "Yeah, but I\'m going to need you to do me a favor first. I want {1} of the best hamberders. I want so many hamberders that you\'re going to get tired of hamberders." And so {0} went and got some hamberders.\n\n'.format(storyDict[HERO_TAG][FIRSTNAME_TAG], hamberder_count)

    rules = {
        'burgerdesc' : [
            '#burgername# with #toppingphrase#',
            'plain #burgername#',
        ],
        'burgername' : [
            'hamberders',
            'cheeseberders',
            'bacon cheeseberders',
            'chili cheeseberders',
            'garden berders'],
        'toppingphrase': [
            '#topping#',
            '#topping# and #topping#',
            '#topping#, #topping#, and #topping#',
            '#topping#, and #topping#, but no #topping#'
            ],
        'topping': util.getList("berdertoppings.txt"),
        }
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)

    counts = []

    while True:
        # make sure no singletons
        while 1 in counts:
            print("removing singleton berder")
            counts.remove(1)
        if sum(counts) == hamberder_count:
            print("got enough berders")
            break
        if (sum(counts) < hamberder_count):
            sc = sum(counts)
            toGo = hamberder_count - sc
            if ((toGo > 1) and (toGo < 15)):
                counts.append(toGo)
                break
            counts.append(random.randrange(5, 15))
        if (sum(counts) > hamberder_count):
            print("too many berders")
            sc = sum(counts)
            excess = sc - hamberder_count
            while excess > 0:
                maxB = max(counts)
                maxI = counts.index(maxB)
                counts[maxI] -= 1
            break

    print("berder counts:", counts)
    print("berder target:", hamberder_count)
    print("alg total:", sum(counts))

    descs = []
    
    for c in counts:
        while True:
            desc = grammar.flatten('#burgerdesc#')
            if not desc in descs:
                descs.append(desc)
                break
        berder_line = "{0} {1}\n".format(c, desc)
        text += berder_line
    text += '\n'

    text += "And they were fine, I guess. And the Orange Baby Pig was happy. There must have been a lot of birds around, because you could hear so much happy tweeting."

    return makechapter.Chapter(45, "An Obstruction", text)

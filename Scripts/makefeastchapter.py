import random

import tracery
from tracery.modifiers import base_english

import makechapter
import storydict
from tags import *
import util
import words

def makeOrdinal(num):
    ordDict = {0: "zeroth",
               1: "first",
               2: "second",
               3: "third",
               4: "fourth",
               5: "fifth",
               6: "sixth",
               7: "seventh",
               8: "eighth",
               9: "ninth",
               10: "tenth",
               11: "eleventh",
               12: "twelfth",
               13: "thirteenth",
               14: "fourteenth",
               15: "fifteenth",
               16: "sixteenth",
               17: "seventeenth",
               18: "eighteenth",
               19: "nineteenth"}
    if num in ordDict:
        return ordDict[num]
    return "{0}th".format(num)

class Course:
    def __init__(self, shortDesc, longDesc):
        self.shortDesc = shortDesc
        self.longDesc = longDesc

def makeRandomCourse():
    courseFactories = [makeSaladCourse,
                       makeSoupCourse,
                       makeCruditeCourse,
                       makeAppetizerCourse,
                       makeEntreeCourse]
    f = random.choice(courseFactories)
    return f()

def makeSaladCourse():
    rules = {
        'greens': [
            'arugala',
            'baby beet greens',
            'bibb lettuce',
            'bok choi',
            'butter lettuce',
            'cabbage',
            'chicory',
            'cress',
            'elf herb',
            'endive',
            'escarole',
            'frisée',
            'green leaf lettuce',
            'iceberg lettuce',
            'kale',
            'looseleaf lettuce',
            'mizuna',
            'mâche',
            'napa cabbage',
            'oakleaf',
            'purple cabbage',
            'radicchio',
            'red leaf lettuce',
            'romaine lettuce',
            'spinach',
            'tatsoi',
            'lettuce',
        ],
        'green_base': [
            "#greens# and #greens#",
            "#greens# tossed with #greens#",
            "a simple presentation of #greens#",
            "#greens#, #greens#, and #greens#"
        ],
        'toppings': [
            'croutons',
            'sunflower seeds',
            'sesame seeds',
            'wonton strips',
            'black beans',
            'corn strips',
            'roasted pumpkin seeds',
            '#dressing#'
            ],
        'dressing': [
            'ranch dressing',
            'blue cheese dressing',
            'thousand island dressing',
            'italian dressing',
            'peppercorn ranch dressing',
            'lite ranch dressing',
            'parmesan buttermilk dressing'
            ],
        'topping_phrase': [
            '#toppings#',
            '#toppings# and #toppings#',
            '#toppings#, #toppings#, and #toppings#',
            '#toppings# and #toppings#, drizzled with #dressing#'],
            
        'origin': "#green_base# topped with #topping_phrase#"
        }
    grammar = tracery.Grammar(rules)
    grammar. add_modifiers(base_english)
    return Course("salad", str(grammar.flatten("#origin#")))

def makeSoupCourse():
    soups = util.getList("soups.txt")
    return Course("soup", random.choice(soups))

def makeCruditeCourse():
    rules = {
        'crudite': [
            'carrots',
            'celery',
            'radishes',
            'parsnips',
            'daikon',
            'bush carrots',
            'celeriac',
            'parsley root',
            'tragopogon',
            'jicama',
            'cassava',
            'cucumber sticks',
            'cucumber wedges',
            'cucumber slices',
            'baby carrots',
            'green bell pepper strips',
            'red bell pepper strips',
            'broccoli',
            'cauliflower',
            'fennel',
            'asparagus spears',
            'romanescu',
            'baby corn',
            'brussels sprouts',
            ],
        'crudite_plate': [
            '#crudite#, #crudite#, #crudite#, and #crudite#'
            ]
        }
    
    grammar = tracery.Grammar(rules)
    grammar. add_modifiers(base_english)
    return Course("crudite", str(grammar.flatten("#crudite_plate#")))

def makeAppetizerCourse():
    rules = {
        'foods' : [
            'angels on horseback',
            'pigs in blankets',
            'antipasto',
            'potato fritters',
            'fritters filled with #filling#',
            'blooming onion',
            'chicken wings',
            'bruschetta',
            'canapé',
            'carpaccio',
            'caviar',
            'chaat',
            'chicken fingers',
            '#meat# satay',
            '#filling# puff',
            '#filling# rangoon',
            'crostini',
            'crudités',
            '#filling# dumplings',
            'deviled eggs',
            'devils on horseback',
            'ants on a tree',
            'peanut butter in celery',
            'eggplant salad',
            'fried mushrooms',
            'garlic knot',
            'bread sticks',
            'gravlax',
            'haggis pakora',
            'jalapeño popper',
            'fried cheese sticks',
            'malakoff',
            'matbucha',
            'meze',
            'mozzerella sticks',
            'nachos',
            'onion rings',
            'funions',
            'pakora',
            'doritos',
            'potato chips',
            'fritos',
            'paneer tikka',
            'shish kebabs',
            'papadum',
            'pizzetta',
            'english muffin pizzas',
            'personal pizzas',
            'pizza pockets',
            'deep fried ravioli',
            'poke',
            'potato skins',
            'jo jos',
            'potato wedges',
            'prawn cocktail',
            'shrimp cocktail',
            'pu pu platter',
            'rocky mountain oysters',
            'bacon wrapped scallops',
            'bacon wrapped tofu',
            'bacon wrapped bacon',
            'rumaki',
            'tapas',
            '#meat# tartare',
            'stuffed mushrooms',
            'sushi',
            '#meat# nigiri',
            '#meat# sashimi',
            ],
        'filling': [
            'chard',
            'spinach',
            'ricotta cheese',
            'cheddar cheese',
            'melted cheese',
            'cream cheese',
            'pate',
            'vegetable mash',
            'crab',
            'creamed #meat#',
        ],
        'meat': util.getList('meat.txt'),
        'apps': [
            '#foods#',
            '#foods# and #foods#',
            ]
        }

    grammar = tracery.Grammar(rules)
    grammar. add_modifiers(base_english)
    return Course("hors d'oeuvre", str(grammar.flatten("#apps#")))


def makeEntreeCourse():
    rules = {
        'meat' : util.getList('meat.txt'),
        'preparation': [
            'roasted',
            'grilled',
            'raw',
            'boiled',
            'charred',
            'pressed',
            'jellied',
            'aged',
            'seared',
            'dried',
            'jerked',
            'spiced',
            'salted',
            'pickled',
            ],
        'prepared_meat': [
            "#preparation# #meat#",
            "#preparation# and #preparation# #meat#",
            ],
        'topping': [
            'asparagus',
            'bacon',
            'bread crumbs',
            'panko',
            'cheese',
            '#winesauce#',
            '#sauce#',
            ],
        'sauce': util.getList("sauces.txt"),
        'winesauce': [
            'red wine sauce',
            'golden wine sauce',
            'white wine sauce',
            'tawny port sauce',
            ],

        'starch': [
            'potatoes',
            'mashed potatoes',
            'fingerling potatoes',
            'new potatoes',
            'rice',
            'wild rice',
            'long grain rice',
            'rice pilaf',
            '#pasta#',
            ],

        'pasta': util.getList("pasta.txt"),

        'meatcourse': [
            '#prepared_meat#',
            '#prepared_meat# topped with #topping#',
            '#prepared_meat# served with #topping#, #topping#, and #topping#',
            '#prepared_meat# stuffed inside a #prepared_meat#',
            '#prepared_meat# on a bed of #starch#',
            ]
        }

    grammar = tracery.Grammar(rules)
    grammar. add_modifiers(base_english)
    return Course("entree", str(grammar.flatten("#meatcourse#")))

def makeDessertCourse():
    rules = {
        'dessert': [
            '#cookies#',
            '#cakes#',
            '#pies#',
            '#candies#',
            '#puddings#',
            '#deepfried#',
            '#frozen#',
            '#jellied#',
            '#pastries#',
            '#sweetsoups#',
            '#dessertwines#',
            ],
        'cookies': util.getList("cookies.txt"),
        'cakes': util.getList("cakes.txt"),
        'pies': [
            'apple pie',
            'pecan pie',
            'pi day pie',
            'mince meat pie',
            'pumpkin pie',
            'blackberry pie',
            'strawberry cream pie',
            'lemon meringue pie',
            ],
        'candies': util.getList("candies.txt"),
        'puddings': util.getList("puddings.txt"),
        'deepfried': [
            'churros',
            'doughnuts',
            'donuts',
            'chinese doughnuts',
            'fritters',
            ],
        'frozen':[
            'ice cream',
            'custard',
            'gelato',
            'sherbet',
            'granita',
            ],
        'jellied': [
            'grass jelly',
            'annin tofu',
            'gelatin dessert',
            'orange jello',
            'jello shots',
            'trifle',
            ],
        'pastries': util.getList("pastries.txt"),
        'sweetsoups': [
            'chocolate soup',
            'strawberry soup',
            'melon soup',
            'blueberry soup',
            ],

        'dessertwines': [
            'port',
            'muscat',
            'sherry',
            'bristol cream',
            'passum wine',
            'madeira',
            'raisin wine',
            'ice wine',
            'sauternes'],
    }
        
    grammar = tracery.Grammar(rules)
    grammar. add_modifiers(base_english)
    return Course("dessert", str(grammar.flatten("#dessert#")))


def makeFeastChapter(monster, storyDict):

    hg = storyDict[HERO_TAG][GENDER_TAG]
    if hg == GENDER_MALE_TAG:
        dim_hero = "boy"
    elif hg == GENDER_FEMALE_TAG:
        dim_hero = "girl"
    else:
        dim_hero = "one"

    nonsense1 = util.mutateWord(words.getRandomWord())

        
    output = "And hast thou killed the {0}?\n".format(monster)
    output += "Come to my arms, my beamish {0}!\n".format(dim_hero)
    output += "O {0} day! Callooh! Callay!\n".format(nonsense1)
    output += "We must have a feast!\n\n"

    num_courses = random.randrange(5, 15)

    courseWords = []
    
    for courseIndex in range(num_courses):
        courseDisplayNum = courseIndex + 1
        courseOrdinalWord = makeOrdinal(courseDisplayNum)
        while True:
            course = makeRandomCourse()
            if ((courseIndex == 0) or
                (course.shortDesc != courseWords[-1])):
                courseWords.append(course.shortDesc)
                break
        
        output += "The {0} course was {1}. It consisted of {2}.\n\n".format(
            courseOrdinalWord,
            course.shortDesc,
            course.longDesc)

    num_dessert_courses = random.randrange(0,4)
    for desIndex in range(num_dessert_courses):
        courseDisplayNum = num_courses + desIndex + 1
        courseOrdinalWord = makeOrdinal(courseDisplayNum)
        course = makeDessertCourse()

        output += "The {0} course was {1}. It consisted of {2}.\n\n".format(
            courseOrdinalWord,
            course.shortDesc,
            course.longDesc)

    dessertCourse = makeDessertCourse()
    output += "The final course was dessert. It consisted of {0}.".format(
        dessertCourse.longDesc)

    title = "The feast of the "+monster
    title = title.title()
    return makechapter.Chapter(1, title, output)
        
        
if __name__ == "__main__":
    print(makeFeastChapter("jabberwock", storydict.makeStoryDict()))

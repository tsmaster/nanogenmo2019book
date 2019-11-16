import random

import tracery
from tracery.modifiers import base_english

import makechapter
import storydict
from tags import *

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
    soups = [
        "Bird's nest soup",
        "Fisherman's Soup",
        "Rumford's Soup",
        'Acquacotta',
        'Afang',
        'Aguadito',
        'Ajiaco',
        'Analı kızlı soup',
        'Ash-e doogh',
        'Atama soup',
        'Avgolemono',
        'Avocado soup',
        'Bacon soup',
        'Bak kut teh',
        'Bakso',
        'Barley',
        'Beef noodle soup',
        'Beer soup',
        'Bergen fish soup',
        'Binignit',
        'Borscht',
        'Borscht',
        'Bouillabaisse',
        'Bouillon',
        'Bourou-Bourou',
        'Bread soup',
        'Brenebon',
        'Brown Windsor soup',
        'Brown veal',
        'Bun bo Hue',
        'Buridda',
        'Butajiru',
        'Cabbage soup',
        'Caldillo de congrio',
        'Caldillo de perro',
        'Caldo verde',
        'Callaloo',
        'Canh chua',
        'Canja de Galinha',
        'Carp soup',
        'Carrot soup',
        'Cazuela',
        'Chestnut bisque',
        'Chicken noodle soup',
        'Chicken soup',
        'Chicken vegetable soup',
        'Chupe Andino',
        'Chupe',
        'Cioppino',
        'Cock-a-leekie',
        'Cold borscht',
        'Consommé',
        'Corn chowder',
        'Crab bisque',
        'Cream of Crab',
        'Cream of apple soup',
        'Cream of asparagus soup',
        'Cream of asparagus',
        'Cream of broccoli soup',
        'Cream of broccoli',
        'Cream of celery',
        'Cream of chicken',
        'Cream of mushroom soup',
        'Cream of potato',
        'Cream of tomato',
        'Crème Ninon',
        'Cucumber soup',
        'Cucumber soup',
        'Cullen skink',
        'Curry Mee',
        'Dalithoy',
        'Dashi',
        'Duck soup noodles',
        'Edikang Ikong',
        'Editan',
        'Egg drop soup',
        'Egusi soup',
        'Eru',
        'Ezogelin soup',
        'Fanesca',
        'Fish soup bee hoon',
        'Fish',
        'French onion soup',
        'French onion soup',
        'Fruktsoppa',
        'Fufu and Egusi soup',
        'Fumet',
        'Garmugia',
        'Gazpacho',
        'Ginataan',
        'Ginestrata',
        'Goat meat pepper soup',
        'Gogi guksu',
        'Golden Mushroom',
        'Gomguk',
        'Goulash soup',
        'Ground nut soup',
        'Gumbo',
        'Harira',
        'Hot and sour soup',
        'Joumou',
        'Kawlata',
        'Kharcho',
        'Kimchi Guk',
        'Kusksu',
        'Kwāti',
        'Lagman',
        'Laksa',
        'Leek soup',
        'Lentil soup',
        'Lettuce soup',
        'Lobster bisque',
        'Lobster stew',
        'Log-log',
        'Lohikeitto',
        'Lung fung soup',
        'Lyvzha',
        'Maccu',
        'Manhattan clam chowder',
        'Maryland crab soup',
        'Matzah ball soup',
        'Melon soup',
        'Minestrone',
        'Miso soup',
        'Miyeok guk',
        'Mohinga',
        'Mulligan Stew',
        'Mulligatawny',
        'Naengmyeon',
        'Nettle soup',
        'New England clam chowder',
        'Nikujaga',
        'Okra soup',
        'Okroshka',
        'Oxtail soup',
        'Palm nut soup',
        'Panada',
        'Panadelsuppe',
        'Pasta fagioli',
        'Patriotic soup',
        'Pea soup',
        'Peanut soup',
        'Philadelphia Pepper Pot',
        'Phở',
        'Pickle soup',
        'Pork blood soup',
        'Pozole',
        'Psarosoupa',
        'Pumpkin',
        'Ramen',
        'Rasam',
        'Rassolnik',
        'Rawon',
        'Ribollita',
        'Rishtay / Rqaq o Adas',
        'Saimin Wonton Soup',
        'Salmorejo',
        'Sambar',
        'Samgyetang',
        'Sauerkraut soup',
        'Sayur Asem',
        'Sayur Lodeh',
        'Sayur lodeh',
        'Scotch Broth',
        'Seafood chowder',
        'Shark fin soup',
        'Shchav',
        'Shchi',
        'She-crab soup',
        'Shrimp bisque',
        'Sliced fish soup',
        'Snert',
        'Solyanka',
        'Sop saudara',
        'Sopa de Gato',
        'Sorrel soup',
        'Soto ayam',
        'Soto',
        'Soup No. 5',
        'Soup alla Canavese',
        'Sour cherry soup',
        'Sour fish soup',
        'Sour rye soup', 
        'Spinach soup',
        'Split pea',
        'Spring soup',
        'Squash bisque',
        'Stone soup',
        'Stracciatella',
        'Sup Kambing',
        'Swedish fruit soup',
        'Taco soup',
        'Talbina',
        'Tarator',
        'Tarhana',
        'Tekwan',
        'Tinola',
        'Tom Yum',
        'Tomato bisque',
        'Tomato soup',
        'Tongseng',
        'Tortilla soup',
        'Tteokguk',
        'Turkey soup',
        'Tāng Fěn',
        'Tāng miǎn',
        'Ukha or yushka',
        'Ukraine',
        'Vegetable soup',
        'Vichyssoise',
        'Vori vori',
        'Watercress soup',
        'Waterzooi',
        'Wedding soup',
        'White beef',
        'White veal',
        'Wine soup',
        'Winter melon',
        'Yellow pea soup',
        'Zuppa pavese',
        'green borscht',
        'green shchi',
        'kapusniak',
        'kapustnica',
        'shchav',
        'sorrel soup',
        'white borscht',
        'zelnacka',
        'Íslensk Kjötsúpa',
        'Šaltibarščiai',
        'żur',
    ]            
            
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
            '#antipasto#',
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
        'meat': [
            'chicken',
            'beef',
            'pork',
            'squid',
            'salmon',
            'rabbit',
            'mutton',
            'goat'
        ],
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
        'meat' : [
            'chicken',
            'pidgeon',
            'ortolan',
            'peacock',
            'duck',
            'goose',
            'starling',
            'wren',
            'dragon',
            'drake',
            'young elf',
            'veal',
            'beef',
            'ham',
            'pork',
            'bacon',
            'back bacon',
            'mutton',
            'goat',
            'goblin',
            'roc',
            'ram',
            'mountain goat',
            'bear',
            'rhinocerous',
            'hippopotamus',
            'giraffe',
            'salmon',
            'tuna',
            'shark',
            'whale',
            'dolphin',
            'man',
            'sahuagin',
            'kelpie',
            'mermaid',
            'unicorn',
            'shrimp',
            'rat',
            'cat',
            'dog',
            'lion',
            'tiger',
            'elephant',
            ],
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
            'cheese',
            'chili sauce',
            '#winesauce#',
            'beurre blanc',
            'gravy',
            'cornmeal gravy',
            'redeye ham gravy',
            'soy sauce',
            'scallions',
            'ginger',
            'wasabi',
            'horseradish',
            'redeye roast beef gravy',
            'soy sauce',
            'tomato gravy',
            'chutney',
            'relish',
            'sawmill gravy',
            'shrimp gravy',
            'cheese sauce',
            'cream gravy',
            'salt pork and milk gravy',
            'chicken gravy',
            'hamburger gravy',
            'chili gravy',
            'chili',
            'spaghetti sauce',
            'marinara',
            'green chili sauce',
            'enchilada sauce',
            'mole',
            'anchovy essence',
            'avgolemono',
            'avocado sauce',
            'barbecue sauce',
            'bread sauce',
            'capital sauce',
            'cocktail sauce',
            'tartar sauce',
            'mayonnaise',
            'ketchup',
            'catsup',
            'green ketchup',
            'mustard',
            'dijon mustard',
            'sweet mustard',
            'deli mustard',
            'coffee sauce',
            'corn sauce',
            'coulis',
            'duck sauce',
            'fish sauce',
            'egusi sauce',
            'fry sauce',
            'mignonette sauce',
            'mint sauce',
            'cream of mushroom soup',
            'cream of corn soup',
            'mushroom ketchup',
            'normande sauce',
            'pan sauce',
            'peppercorn sauce',
            'rainbow sauce',
            'ravigote sauce',
            'romesco',
            'salad dressing',
            'salsa',
            'fresh salsa',
            'sauce andalouse',
            'sauce vin blanc',
            'sofrito',
            'sour cream sauce',
            'steak sauce',
            'sweet chili sauce',
            'peanut sauce',
            'tomato sauce',
            'vinaigrette',
            'wine sauce',
            'hot and sour sauce',
            'mongolian sauce',
            'mushroom sauce',
            'worcestershire sauce',
            'HP sauce',
            'Bordelaise sauce',
            'Chateaubriand sauce',
            'Charcutiere sauce',
            'Chaudfroid sauce',
            'Demi glace',
            'Poutine',
            'Romesco sauce',
            'Sauce Africaine',
            'Sauce au Poivre',
            'Sauce Robert',
            'Beurre blanc',
            'Beurre manie',
            'Beurre monté',
            'Café de Paris',
            'Meuniere sauce',
            'Remoulade sauce',
            'Aioli',
            'Béarnaise sauce',
            'Garlic sauce',
            'Hollandaise sauce',
            'Remoulade',
            'Salad cream',
            'Tartar sauce',
            'Bagna càuda',
            'Garum',
            'Ketchup',
            'Pique sauce',
            'Mustard sauces',
            'Mustard',
            'Phrik nam pla',
            'Buffalo Sauce',
            'Chili sauce',
            'Datil pepper sauce',
            'Enchilada sauce',
            'Pique Sauce',
            'Sriracha sauce',
            'Tabasco sauce',
            'Neapolitan ragù sauce',
            'Amatriciana sauce',
            'Barese ragù',
            'Bolognese',
            'Carbonara',
            'Cincinnati chili',
            'Neapolitan ragù',
            'Picadillo',
            'Ragù',
            'Sloppy Joe',
            'Sauces',
            'Fresh-ground pesto sauce',
            'Chimichurri',
            'Gremolata',
            'Mujdei',
            'Onion sauce',
            'Persillade',
            'Pesto',
            'Pico de gallo',
            'Latin American Salsa cruda',
            'Salsa verde',
            'Sauce gribiche',
            'Sauce vierge',
            'Tkemali',
            'Crème anglaise',
            'peach sauce',
            'Apple sauce',
            'Blueberry sauce',
            'Butterscotch sauce',
            'Caramel',
            'Chocolate gravy',
            'Chocolate syrup',
            'Cranberry sauce',
            'Crème anglaise',
            'Custard',
            'Fudge sauce',
            'Hard sauce',
            'Mango sauce',
            'Peach sauce',
            'Plum sauce',
            'Strawberry sauce',
            'Maple Syrup',
            'Tkemali',
            'Zabaione',
            'Mornay sauce',
            'Caruso sauce',
            'Béchamel sauce',
            'Mushroom sauce',
            'Mornay sauce',
            'Sauce Allemande',
            'Sauce Américaine',
            'Suprême sauce',
            'Velouté sauce',
            'Yogurt sauce',
            'hollandaise',
            'Béchamel',
            'Velouté',
            'Espagnole',
            'Roux',
            'red curry sauce',
            'yellow curry sauce',
            'massaman curry sauce',
            'pineapple curry sauce',
            'rogan josh sauce',
            'biryani sauce',
            'balti sauce',
            'kormi sauce',
            'coconut curry sauce',
            'yogurt and coconut korma sauce',
            'bhuna sauce',
            'mild curry sauce',
            'dhansak sauce',
            'madras sauce',
            'butter chicken sauce',
            'vindaloo sauce',
            'jalfrezi sauce',
            'pasandra sauce',
            'fiery phal sauce',
            'masala chicken sauce',
            'saag masala sauce',
            'tikka masala sauce',
            'dopiaza sauce',
            ],
        'winesauce': [
            'red wine sauce',
            'golden wine sauce',
            'white wine sauce',
            'tawny port sauce',
            ],

        'meatcourse': [
            '#prepared_meat#',
            '#prepared_meat#, topped with #topping#',
            '#prepared_meat#, served with #topping#, #topping#, and #topping#',
            '#prepared_meat#, stuffed inside a #prepared_meat#',
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
        'cookies':[
            'peanut butter cookies',
            'oreos',
            'chocolate chip cookies',
            'sugar cookies',
            'shortbread',
            'no-bake cookies',
            'digestive biscuits',
            'graham crackers',
            'oatcakes',
            'tim tams',
            'Aachener Printen',
            'Abernethy',
            'Acıbadem kurabiyesi',
            'Afghan biscuits',
            'Alfajor',
            'Almond biscuit',
            'Almond cake',
            'almond cookie',
            'Amaretti di Saronno',
            'macaroon',
            'macaron',
            'macron',
            'Animal cracker',
            'ANZAC biscuit',
            'New Zealand',
            'Aparon',
            'Apas',
            'Apple cider cookie',
            'Ballokume',
            'Barquillo',
            'Barquiron',
            'Basler Läckerli',
            'Bath Oliver',
            'Berger Cookie',
            'Berner Haselnusslebkuchen',
            'Berner Honiglebkuchen',
            'Biscocho',
            'Biscotti',
            'Biscuit',
            'biscochito',
            'Black and white cookie',
            'Half-Moon cookie',
            'Boortsog',
            'bawyrsak',
            'Bourbon biscuit',
            'Bredela',
            'Bredele',
            'Bredle',
            'Winachtsbredele',
            'Broas',
            'Butter cookie',
            'Butter pecan',
            'Camachile cookie',
            'Caramel shortbread',
            'Millionaire\'s Shortbread',
            'Carrot cake cookie',
            'Cat\'s tongue cookie',
            'Cavallucci',
            'Caycay',
            'Charcoal biscuit',
            'Chocolate biscuit',
            'Chocolate chip cookie',
            'Chocolate-coated marshmallow treats',
            'Chocolate Teacake',
            'Christmas cookies',
            'Cuchuflís or Cubanitos',
            'Coconut macaroon',
            'Cornish fairings',
            'Coyotas',
            'Cream cracker',
            'Cuccidati',
            'Custard cream',
            'Digestive biscuit',
            'Dutch letter',
            'Empire biscuit',
            'Fig roll',
            'Florentine Biscuit',
            'Flour kurabiye',
            'Fortune cookie',
            'Fudge cookie',
            'Galletas de bato',
            'Galletas de patatas',
            'Galletas del Carmen',
            'Galletas pesquera',
            'Garibaldi biscuit',
            'Ghorabiye',
            'Ghoriba',
            'Gingerbread',
            'Gingerbread man',
            'Ginger snaps',
            'Half-moon cookie',
            'Hamantash',
            'Jacobina',
            'Jammie Dodgers',
            'Joe Frogger',
            'Jodenkoek',
            'Jumble',
            'Kaasstengels',
            'Kahk',
            'Khapse',
            'Kichel',
            'Kleicha',
            'Koulourakia',
            'Kourabiedes',
            'Krumiri',
            'Krumkake',
            'Kue gapit',
            'Kue satu',
            'Lady Finger',
            'Lebkuchen',
            'Lengua de gato',
            'Lincoln biscuit',
            'Linga',
            'Linzer torte',
            'Ma\'amoul',
            'Macaroon',
            'Macaron',
            'Malted milk biscuit',
            'Mamón tostado',
            'Maple leaf cream cookies',
            'Marie biscuit',
            'Masa podrida',
            'Moravian spice cookies',
            'Nice biscuit',
            'Nocciolini di Canzo',
            'Oat crisps',
            'Oatmeal raisin cookies',
            'Otap',
            'Paciencia',
            'Paborita',
            'Panellets',
            'Paprenjak',
            'Party ring',
            'Petit-Beurre',
            'Pfeffernüsse',
            'Piaya',
            'Pignolo',
            'Piñata cookie',
            'Pinwheel cookies',
            'Polvorón',
            'Pizzelle',
            'Puto seco',
            'Putri salju',
            'Rainbow cookie',
            'Reshteh Khoshkar',
            'Ricciarelli',
            'Rich tea',
            'Rosca',
            'biscocho de rosca',
            'Rosette',
            'Rosquillo',
            'Rum ball',
            'Russian tea cake',
            'Sandwich cookie',
            'Semprong',
            'Shortbread',
            'Silvana',
            'Snickerdoodle',
            'Speculaas',
            'Springerle',
            'Spritzgebäck',
            'Stroopwafel',
            'Sugar cookie',
            'Tahini cookie',
            'Tareco',
            'Teiglach',
            'Tirggel',
            'Toll House Cookie',
            'Troll House Cookies',
            'Toruń gingerbread',
            'Ube crinkles',
            'Ugoy-ugoy',
            'Uraró',
            'Vanillekipferl',
            'Wafer',
            'Wibele',
            'Camachile cookie',
            'Half-moon cookie',
            'Lengua de gato',
            'Paciencia',
            'Sandies',
            ],
        'cakes': [
            'birthday cake',
            'king cake',
            'pan cake',
            ],
        'pies': [
            'apple pie',
            'pecan pie',
            'pi day pie',
            ],
        'candies': [
            'chocolate truffles',
            'chocolate coated strawberries',
            'caramels',
            'nonpareils',
            ],
        'puddings': [
            'banana pudding',
            'chocolate pudding',
            'vanilla pudding',
            'butterscotch pudding',
            ],
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
        'pastries': [
            'croissant',
            'shortbread',
            ],
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
            'madeira',
            'sauternes'],
    }
        
    grammar = tracery.Grammar(rules)
    grammar. add_modifiers(base_english)
    return Course("dessert", str(grammar.flatten("#dessert#")))


def makeFeastChapter(monster, storyDict):

    hg = storyDict[HERO_TAG][GENDER_TAG]
    if hg == GENDER_MALE_TAG:
        dim_hero = "son"
    elif hg == GENDER_FEMALE_TAG:
        dim_hero = "daughter"
    else:
        dim_hero = "child"
        
    output = "And hast thou killed the {0}, my {1}? ".format(monster, dim_hero)

    output += "Calloo! Callay! "
    output += "We must have a feast!\n\n"

    num_courses = random.randrange(5, 15)

    for courseIndex in range(num_courses):
        courseDisplayNum = courseIndex + 1
        courseOrdinalWord = makeOrdinal(courseDisplayNum)
        course = makeRandomCourse()
        
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

    return makechapter.Chapter(1, "The feast of the "+monster, output)
        
        
if __name__ == "__main__":
    print(makeFeastChapter("jabberwock", storydict.makeStoryDict()))
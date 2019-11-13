# nanogenmo2019book
The source code for my National Novel Generation Month book

## Idea
Over the summer, I collaborated with GPT-2 to make a tabletop role playing game ruleset/accessory called "Shapeshifting". It contained a large number of monsters, weapons, and magic items.

My goal for NaNoGenMo2019 is to take pieces of data from Shapeshifting as random tables, and tell a vaguely Campbellian Hero's Journey tale about a hero going out, slaying a bunch of monsters, perhaps facing some villains, and returning home, happily ever after.

## Technologies
I'm familiar with Python, so that seems like a place to start. I've used Tracery for generation before, which seems like a piece of what I want, but I want to build more structure than what I've done before with Tracery.

## Approach
Campbell's Hero's Journey has 17 stages, which gives me some amount of structure to work with. Each Campbell stage might not form an entire chapter, and some stages might have multiple chapters.

I don't intend to spin the plot as I'm generating text - instead, my thinking is that I'll generate a lot of the nouns (the hero's name, the villain's name, the names of important locations) up front, and then connect the dots along the way.

Part of this may involve generating a list of e.g. monsters, then sorting the list based on some sort of "fierceness" annotation I have about monster types. I might add adjectival modifiers ("weak", "young", "medium", "dark", "enchanted") to modify the fierceness of an enemy, to provide some variety. This will give room to fight a collection of enemies within a category.


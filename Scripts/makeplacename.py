import random
import pycorpora
import util

cachedCities = None

def getCachedCities():
    global cachedCities
    
    if not (cachedCities is None):
        return cachedCities
    cachedCities = util.getList("cities.txt")

    fileList = pycorpora.get_file("geography", "canadian_municipalities")
    for e in fileList["municipalities"]:
        cachedCities.append(e["name"])

    fileList = pycorpora.get_file("geography", "countries_with_capitals")
    for e in fileList["countries"]:
        cachedCities.append(e["capital"])
        
    fileList = pycorpora.get_file("geography", "english_towns_cities")
    cachedCities += fileList["towns"]
    cachedCities += fileList["cities"]

    fileList = pycorpora.get_file("geography", "japanese_prefectures")
    for e in fileList["regions"]:
        cachedCities.append(e["region"])
        cachedCities += e["prefectures"]
        
    fileList = pycorpora.get_file("geography", "norwegian_cities")
    for e in fileList["cities"]:
        cachedCities.append(e["city"])
    
    return cachedCities
    


def makePlaceName():
    cities = getCachedCities()
    baseName = random.choice(cities)
    return util.mutateWord(baseName).capitalize()

if __name__ == '__main__':
    for i in range(20):
        print(makePlaceName())

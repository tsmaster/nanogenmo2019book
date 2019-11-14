from util import *
import pycorpora

cachedColors = None

def getColors():
    global cachedColors
    if cachedColors is None:
        cachedColors = dedup(getListedColors() + getCorporaColors())
    return cachedColors

def getListedColors():
    return getList("colors.txt")

def getCorporaColors():
    fileList = ['crayola', 'palettes', 'xkcd']
    
    colorList = getWikipediaColors() + getPaintsColors() + getWebColors() + getDuluxColors() + getCrayolaColors() + getXKCDColors()

    return dedup(colorList)
    
def getWikipediaColors():
    colors = []
    fileList = pycorpora.get_file("colors", "wikipedia")
    for entry in fileList:
        name = entry['name']
        colors.append(name)
    return colors

def getPaintsColors():
    colorList = []
    colorFile = pycorpora.get_file("colors", "paints")
    for entry in colorFile["colors"]:
        name = entry['color']
        colorList.append(name)
    return colorList
    
def getWebColors():
    colorList = []
    colorFile = pycorpora.get_file("colors", "web_colors")
    for entry in colorFile["colors"]:
        name = entry['color']
        colorList.append(name)
    return colorList

def getDuluxColors():
    colorList = []
    colorFile = pycorpora.get_file("colors", "dulux")
    for entry in colorFile:
        name = entry['name']
        colorList.append(name)
    return colorList

def getCrayolaColors():
    colorList = []
    colorFile = pycorpora.get_file("colors", "crayola")
    for entry in colorFile["colors"]:
        name = entry['color']
        colorList.append(name)
    return colorList
    
def getXKCDColors():
    colorList = []
    colorFile = pycorpora.get_file("colors", "crayola")
    for entry in colorFile["colors"]:
        name = entry['color']
        colorList.append(name)
    return colorList
    
    
    
if __name__ == "__main__":
    print(getColors())

import makepoem
from makepoem import Language, Word

if __name__ == "__main__":
    lang = makepoem.readLangFromDisk("nonsense.json")
    makepoem.foreverLimericks(lang)

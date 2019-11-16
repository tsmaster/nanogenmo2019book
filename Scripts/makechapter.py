import nltk
from textblob import TextBlob

class Chapter:
    def __init__(self, chapterNumber, chapterTitle, text):
        self.chapterNumber = chapterNumber
        self.chapterTitle = chapterTitle
        self.text = text
        if self.text[-1] != "\n":
            self.text += "\n"

    def __str__(self):
        return '''
---
Chapter {0} : {2}
---

{1}
'''.format(self.chapterNumber, self.text, self.chapterTitle)

    def wordcount(self):
        s = str(self)
        words = s.split()
        words = [w.strip() for w in words]
        words = [w for w in words if w]
        return len(words)


def test():
    c = Chapter(1, "Hello, World!")
    c2 = Chapter(2, "It was the best of times")
    c3 = Chapter(3, "It was the worst of times")
    chapters = [c, c2, c3]
    chapterStrings = [str(x) for x in chapters]
    bookText = '\n'.join(chapterStrings)
    with open("test.txt", "wt") as f:
        f.write(bookText)


if __name__ == "__main__":
    test()

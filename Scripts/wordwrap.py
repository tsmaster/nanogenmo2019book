def wordwrap(s, wrap_col):
    paragraphs = s.split('\n')
    for pi, p in enumerate(paragraphs):
        paragraphs[pi] = wrapParagraph(p, wrap_col)

    return "\n".join(paragraphs)

def wrapParagraph(p, wrap_col):
    if not p:
        return ''

    if len(p) == 0:
        return ''
    if len(p) < wrap_col:
        return p
    
    first_line = p[:wrap_col]
    try:
        breakIndex = first_line.rindex(' ')
        
        first = first_line[:breakIndex]
        rest = p[breakIndex + 1:]
        return first + '\n' + wrapParagraph(rest, wrap_col)        
    except ValueError:
        rest = p[wrap_col:]
        return first_line + '\n' + wrapParagraph(rest, wrap_col)



def test():
    with open("book.txt", "rt") as f:
        text = f.read()
        print (wordwrap(text, 65))

if __name__ == "__main__":
    test()
    

        
    

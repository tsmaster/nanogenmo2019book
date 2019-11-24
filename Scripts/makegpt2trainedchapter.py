import gpt_2_simple as gpt2
import tensorflow as tf
import os
import requests

import makechapter

model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
    print(f"Downloading {model_name} model...")
    gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

sess = None

def trainModel():
    data_dir = "../DataSets/"
    
    files = [#"shakespeare.txt",
        "moby_dick.txt",
        "don_quixote.txt",
        "3musketeers.txt",
        "ct_yankee.txt",
        "gulliver.txt",
        "ivanhoe.txt",
        "morte_darthur_i.txt",
        "morte_darthur_ii.txt",
        "robin_hood.txt",
        "robin_hood_pyle.txt",
        "wizard_of_oz.txt",
       ]
    
    file_name = "../DataSets/shakespeare.txt"
    if not os.path.isfile(file_name):
        url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
        data = requests.get(url)
        	
        with open(file_name, 'w') as f:
            f.write(data.text)

    sess = gpt2.start_tf_sess()
    data = ""
    
    for fn in files:
        extFn = data_dir + fn
    
        with open(extFn, "rt") as df:
            data += df.read()
    
    gpt2.finetune(sess,
                  extFn,
                  model_name=model_name,
                  steps=100)   # steps is max number of training steps


def makeParagraph(sess, prompt, parLen):
    output = gpt2.generate(sess,
                           prefix=prompt,
                           length=parLen,
                           return_as_list=True)[0]

    under = " "

    output = output.replace(under, '')
    
    try:
        dotIndex = output.rindex('.')
    except ValueError:
        dotIndex = -1
        
    if dotIndex > -1:
        return output[:dotIndex + 1]

    try:
        spaceIndex = output.rindex(' ')
    except ValueError:
        spaceIndex = -1
        
    if spaceIndex > -1:
        return output[:spaceIndex + 1]
        
    return output

def makeCraftChapter(itemName, parLen):
    global sess
    if sess is None:
        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess)

    parBreak = "\n\n"
    
    output = makeParagraph(sess, "When making {0} from scratch, the first thing you have to do is ".format(itemName), parLen)
    output += parBreak
    print("P1")
    output += makeParagraph(sess, "The difficult part about finding the materials to make {0} is ".format(itemName), parLen)
    output += parBreak
    print("P2")
    output += makeParagraph(sess, "When crafing {0}, pay attention to".format(itemName), parLen)
    output += parBreak
    print("P3")
    output += makeParagraph(sess, "However, one can never", parLen)
    output += parBreak
    print("P4")
    output += makeParagraph(sess, "The final step when making {0} is to".format(itemName), parLen)
    output += parBreak
    print("P5")
    output += makeParagraph(sess, "To properly maintain {0}, you should".format(itemName), parLen)
    print("P6")
    title = "The making of " + itemName
    return makechapter.Chapter(1, title.title(), output)

if __name__ == "__main__":
    c = makeCraftChapter("a sword", 300)
    print(c)
    print ("wordcount:", c.wordcount())
    

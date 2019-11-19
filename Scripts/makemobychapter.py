# Import required libraries
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import logging
from tqdm import trange

import torch
import torch.nn.functional as F
import numpy as np

from transformers import GPT2Config, OpenAIGPTConfig, XLNetConfig, TransfoXLConfig, XLMConfig, CTRLConfig

from transformers import GPT2LMHeadModel, GPT2Tokenizer

import makechapter

### 
### 
### # Load pre-trained model tokenizer (vocabulary)
### tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
### 
### # Load pre-trained model (weights)
### model = GPT2LMHeadModel.from_pretrained('gpt2')
### 
### # Set the model in evaluation mode to deactivate the DropOut modules
### model.eval()
### model.to('cuda')
### 
### # Encode a text inputs
### textCar = "What is the fastest car in the"
### textSword = "In order to make a sword, you must first "
### text = textSword
### endToken = "<|endoftext|>"
### cmdLine = """
### python3 pytorch-transformers/examples/run_generation.py --model_type=gpt2 --length=100### ### ### ### 0 --model_name_or_path=gpt2 --seed=19 --prompt="When one sets
### out to make a sword from scratch, one must first " --stop_token="<|endoftext|>"
### """


def top_k_top_p_filtering(logits, top_k=0, top_p=0.0, filter_value=-float('Inf')):
    """ Filter a distribution of logits using top-k and/or nucleus (top-p) filtering
        Args:
            logits: logits distribution shape (batch size x vocabulary size)
            top_k > 0: keep only top k tokens with highest probability (top-k filtering).
            top_p > 0.0: keep the top tokens with cumulative probability >= top_p (nucleus filtering).
                Nucleus filtering is described in Holtzman et al. (http://arxiv.org/abs/1904.09751)
        From: https://gist.github.com/thomwolf/1a5a29f6962089e871b94cbd09daf317
    """
    top_k = min(top_k, logits.size(-1))  # Safety check
    if top_k > 0:
        # Remove all tokens with a probability less than the last token of the top-k
        indices_to_remove = logits < torch.topk(logits, top_k)[0][..., -1, None]
        logits[indices_to_remove] = filter_value

    if top_p > 0.0:
        sorted_logits, sorted_indices = torch.sort(logits, descending=True)
        cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)

        # Remove tokens with cumulative probability above the threshold
        sorted_indices_to_remove = cumulative_probs > top_p
        # Shift the indices to the right to keep also the first token above the threshold
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0

        # scatter sorted tensors to original indexing
        indices_to_remove = sorted_indices_to_remove.scatter(dim=1, index=sorted_indices, src=sorted_indices_to_remove)
        logits[indices_to_remove] = filter_value
    return logits

def sample_sequence(model, length, context, num_samples=1, temperature=1,
                    top_k=0, top_p=0.0, repetition_penalty=1.0,
                    is_xlnet=False, is_xlm_mlm=False, xlm_mask_token=None, xlm_lang=None,
                    device='cpu'):
    context = torch.tensor(context, dtype=torch.long, device=device)
    context = context.unsqueeze(0).repeat(num_samples, 1)
    generated = context
    with torch.no_grad():
        for _ in trange(length):
            inputs = {'input_ids': generated}
            outputs = model(**inputs)  
            next_token_logits = outputs[0][:, -1, :] / (temperature if temperature > 0 else 1.)

            # repetition penalty from CTRL (https://arxiv.org/abs/1909.05858)
            for i in range(num_samples):
                for _ in set(generated[i].tolist()):
                    next_token_logits[i, _] /= repetition_penalty
                
            filtered_logits = top_k_top_p_filtering(next_token_logits, top_k=top_k, top_p=top_p)
            if temperature == 0: # greedy sampling:
                next_token = torch.argmax(filtered_logits, dim=-1).unsqueeze(-1)
            else:
                next_token = torch.multinomial(F.softmax(filtered_logits, dim=-1), num_samples=1)
            generated = torch.cat((generated, next_token), dim=1)
    return generated

model = None
tokenizer = None
device = None

def makeGPT2():
    global model, tokenizer, device
    
    modelType = "gpt2"
    modelNameOrPath = "gpt2"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model_class, tokenizer_class = GPT2LMHeadModel, GPT2Tokenizer
    tokenizer = tokenizer_class.from_pretrained(modelNameOrPath)
    model = model_class.from_pretrained(modelNameOrPath)
    model.to(device)
    model.eval()


def makeParagraph(prompt, length):
    if model is None:
        makeGPT2()
        
    context_tokens = tokenizer.encode(prompt, add_special_tokens=False)    
    stop_token = "<|endoftext|>"
    
    out = sample_sequence(
        model=model,
        length=length,
        context=context_tokens,
        device=device)

    out = out[:, len(context_tokens):].tolist()

    output = prompt
    
    for o in out:
        text = tokenizer.decode(o, clean_up_tokenization_spaces=True)
        text = text[:text.find(stop_token)]
        output = output + text

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

def makePlaceholderMobyChapter(itemName, parLen):
    import words
    chapterLen = int(parLen * 4.5)
    output = "This is a placeholder chapter about making {0}. I'm shooting for {1} words in this chapter. ".format(itemName, chapterLen)
    while (len(output.split()) < chapterLen):
        output += words.getRandomWord() + " "
    return makechapter.Chapter(1, "A placeholder chapter about "+itemName, output)

def makeMobyChapter(itemName, parLen=100, placeholder=False):
    if placeholder:
        return makePlaceholderMobyChapter(itemName, parLen)
    
    parBreak = "\n\n"
    
    output = makeParagraph("The first thing one must do when making {0} is to".format(itemName), parLen)
    output += parBreak
    output += makeParagraph("The difficult part about finding the materials to make {0} is".format(itemName), parLen)
    output += parBreak
    output += makeParagraph("When crafing {0}, pay attention to".format(itemName), parLen)
    output += makeParagraph("However, one can never", parLen)
    output += parBreak
    output += makeParagraph("The final step when making {0} is to".format(itemName), parLen)
    output += parBreak
    output += makeParagraph("To properly maintain {0}, you should".format(itemName), parLen)
    
    return makechapter.Chapter(1, "The making of " + itemName, output)
        

if __name__ == "__main__":
    #print(makeParagraph("This is a test of making a", 45))
    #print(makeParagraph("This is a second attempt to", 50))
    c = makeMobyChapter("flaming sword")
    print (c)
    print ("wordCount:", c.wordcount())
          

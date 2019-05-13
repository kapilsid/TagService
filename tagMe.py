import nltk
import re
from nltk.corpus import stopwords
import json
from nltk.tokenize import word_tokenize, sent_tokenize

from sentiments.tagsentiment import *
from nerspacy import *

stop_words = set(stopwords.words('english'))

grammar = r"""
  NP: {<DT|JJ|RB|VBG|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

def NEtag(mtext):
   sents = sent_tokenize(mtext)
   tags = []
   for sent in sents:
      tokens = word_tokenize(sent)
      str = nltk.pos_tag(tokens)
      #chk = nltk.ne_chunk(str)
      cp = nltk.RegexpParser(grammar)
      chk = cp.parse(str)

      #print(chk)
      NN = []
      for subtree in chk.subtrees(filter=lambda t: t.label() == 
      'NP'):
           NN.append(subtree)  
      #tags.append(chk)
      #chk = chunk(str)
   return NN


def NPtag(str):
    cp = nltk.RegexpParser(grammar)
    chk = cp.parse(str)
    NN = []
    for subtree in chk.subtrees(filter=lambda t: t.label() == 
      'NP'):
         NN.append(" ".join([word for (word,pos) in subtree])) 
    return NN

def postag(mtext):
   sents = sent_tokenize(mtext)
   tags = []
   for sent in sents:
      tokens = word_tokenize(sent)
      str = nltk.pos_tag(tokens)
      chk = NPtag(str)
      sentis = xtractSentin(sent)
      ner = xtractSpacyNE(sent)
      #print(ner)
      tag = json.dumps({"tag":str,"ne":chk,"sent":sent,"sentis":sentis,"ner":ner})
      #entities = nltk.chunk.ne_chunk(str)
      tags.append(tag)
      #chk = chunk(str)
   return tags

def postagXML(mtext):
   sents = sent_tokenize(mtext)
   tags = []
   for sent in sents:
      tokens = word_tokenize(sent)
      str = nltk.pos_tag(tokens)
      #tags.append(chunk(str))
      xml = toXML(str)
      chk = chunk(str)
      tag = json.dumps({"xml": xml,"chunk":chk,"sent":sent})
      tags.append(tag)
   return tags

def chunk(tags):
    cp = nltk.RegexpParser(grammar)
    #print(cp.parse(tags))
    y = cp.parse(tags)
    return(y) 

def toXML(tags):
    li = []
    for tag in tags:
        word = tag[0]
        if word.isalpha():
           pos = tag[1]
           x = "<{}>{}</{}>".format(pos,word,pos)
           li.append(x)
    return ''.join(li)


def echo(mtext):
   return mtext
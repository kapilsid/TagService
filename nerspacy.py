import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

from xtractknowledge import kpanel

# mtext = "But Google is starting from behind. The company made a late push into hardware, and Apple's Siri, available on iPhones, and Amazon's Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption."
# doc = nlp(mtext)

# print([(X.text, X.label_) for X in doc.ents])
# doc = nlp(mtext)
# print(doc.ents)

def xtractSpacyNE(mtext):
    """Extracts Name Entities from the text
    Calls Kpanel for crawling the knowldge panel from google search.

    Args:
      mtext: text 

    Returns:
      knowledge about entity   

   """    
   doc = nlp(mtext)
   x =  [(X.text, X.label_) for X in doc.ents]
   p = []
   for (text,label) in x:
      print(text)
      if label == 'ORG' or label == 'PERSON':
         det = kpanel.searchEntity(text)
         if det is not None:
            p.append((text,label,det))
         else:
            p.append((text,label))     
      else:
         p.append((text,label)) 

      return p

def xtractSpacyNP(chunks):
  """Extracts Name Phrases from the text
    Calls Kpanel for crawling the knowldge panel from google search.

    Args:
      mtext: text 

    Returns:
      knowledge about entity   

   """  
   p = []
   for (text,label) in x:
      print(text)
      if label == 'ORG' or label == 'PERSON':
          det = kpanel.searchEntity(text)
          if det is not None:
              p.append((text,label,det))
          else:
              p.append((text,label))     
      else:
          p.append((text,label)) 

      return p

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import json
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

stop_words = set(stopwords.words('english'))

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

def prepare_text_for_lda(text):
    """Prepare text for lda analysis by replacing token with is lemma 
    and only taking significant words    
    Args:
        text: text

    Returns:
        list of tokens     

   """ 
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

def getTokens(mtext):
     
    text_data = []
    sents = sent_tokenize(mtext)
    for sent in sents:
      tokens = prepare_text_for_lda(sent)
      text_data.append(tokens)  

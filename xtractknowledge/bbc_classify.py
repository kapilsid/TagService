from sklearn.naive_bayes import MultinomialNB
from bbc import load_bbc
import numpy as np 
import random as random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

vocab, X, y, keys = load_bbc(path=".\\bbc-corpus\\bbc")
   

classif = MultinomialNB()

classif.fit(X,y)


def readFeatureFromFile(fpath) :
    """Create features from the file.    
    Args:
        fpath: filename 

    Returns:
       dictionary of tokens with occurance    

    """ 
    featureVector = np.zeros(len(vocab))
    newsArticle = open(fpath, 'r')
    for line in newsArticle:
        for word in line.replace('\n','').split(' '):
            if word in vocab:
                featureVector[vocab[word]] += 1
    newsArticle.close()
    return featureVector

def extractFeatures(tokens):
    """Create features from the token list.    
    Args:
        tokens: list 

    Returns:
       dictionary of tokens with occurance    

    """ 
    featureVector = np.zeros(len(vocab))
    for word in tokens:
        if word in vocab:
           featureVector[vocab[word]] += 1
    return featureVector

def xtractTokens(mtext):
    """Extract tokens from tags which are significant len > 3 and 
    not in stop_words.    
    Args:
        mtext: text

    Returns:
       list of tokens    

    """ 
    sents = sent_tokenize(mtext)
    tags = []
    for sent in sents:
        tokens = word_tokenize(sent)
        tokens = [token for token in tokens if len(token) > 3]
        tokens = [token for token in tokens if token not in stop_words]
        tags.extend(tokens) 
    return tags

def predictTopic(mText):
    """Predict Topic from the text.    
    Args:
        mtext: text

    Returns:
        highest probable detected topic    

    """ 
    tokens = xtractTokens(mText)
    print(tokens)
    featureVector = [extractFeatures(tokens)]
    mclass = classif.predict(featureVector) 
    return keys[mclass[0]]
    


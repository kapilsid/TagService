from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk import tokenize
from nltk.tokenize import word_tokenize, sent_tokenize

sid = SentimentIntensityAnalyzer()

def getSentiments(mtext):
    """Detects sentiment from the text.    
    Args:
        mtext: text

    Returns:
        sentiments for each sentence with polarity    

    """ 
    sents = sent_tokenize(mtext)
    sentiments = []
    for sentence in sents:
        print(sentence)
        ss = sid.polarity_scores(sentence)
        #for k in sorted(ss):
        #    print('{0}: {1}, '.format(k, ss[k]), end='')
        sentiments.append(ss)
    return sentiments

def xtractSentin(sentence):
    ss = sid.polarity_scores(sentence)
    return ss
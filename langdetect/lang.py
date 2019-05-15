from langid.langid import LanguageIdentifier, model

identifier = LanguageIdentifier.from_modelstring(model,norm_probs=True)

def detect(mText):
    """Detects the language from the text.    
    Args:
        mText: the text

    Returns:
        Language- Example en for English    

    """ 
    x = identifier.classify(mText)
    return(x) 

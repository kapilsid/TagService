from langid.langid import LanguageIdentifier, model

identifier = LanguageIdentifier.from_modelstring(model,norm_probs=True)

def detect(mText):
   x = identifier.classify(mText)
   return(x) 

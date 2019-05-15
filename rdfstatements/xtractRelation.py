import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sem import relextract


mtext = """
This foundation, combined with a rapidly growing market and a category leading product make Icertis an exciting customer-centric execution company, with an employee-centric culture.
"""


grammar = r"""
  NP: {<DT|JJ|RB|VBG|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
  CLAUSE: {<NP><VP>}           # Chunk NP, VP
  """

def extractConj(sent):
    """Breaks the sentence based on the specified grammar from 
    NP:Noun Phrase, PP:Particple, VP:Verb.    
    Args:
        sent: sentence

    Returns:
        list of chunks    

    """ 
    
    Digdug = nltk.RegexpParser(r""" 
    CHUNK_AND_CHINK:
    {<.*>+}          # Chunk everything
    }<CC>+{      # Chink sequences of CC
    """)
    #sentence = nltk.pos_tag(nltk.word_tokenize("There are no large collections present but there is spinal canal stenosis."))
    tokens = word_tokenize(sent)
    str = nltk.pos_tag(tokens)
    result = Digdug.parse(str)

    for subtree in result.subtrees(filter=lambda t: t.label() == 
    'CHUNK_AND_CHINK'):
                print (subtree)

sents = sent_tokenize(mtext)
tags = []
for sent in sents:
    tokens = word_tokenize(sent)
    str = nltk.pos_tag(tokens)
    #chk = nltk.ne_chunk(str)
    cp = nltk.RegexpParser(grammar)
    chk = cp.parse(str)

    print(chk)
    NN = []
    for subtree in chk.subtrees(filter=lambda t: t.label() == 
    'NP'):
        NN.append(" ".join([word for (word,pos) in subtree]))
        #print (subtree)
    for x in NN:
        print(x) 
    pairs = relextract.tree2semi_rel(chk)
    reldicts = relextract.semi_rel2reldict(pairs)
    print(reldicts)
    for x in reldicts:
        #for k,v in x:
        print("subjtext",x["subjtext"])
        print("objtext",x["objtext"])
        
        #print(type(x)) 

        #break
    #extractConj(sent)

    

#return [r for r in reldicts
#        if r['subjclass'] == subjclass and
#            r['objclass'] == objclass and
#            len(r['filler'].split()) <= window and
#            pattern.match(r['filler'])]
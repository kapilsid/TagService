from tagMe import *
from bbc_classify import *
from predict20 import *

from nerspacy import *

mtext = """
A Jana Sena Party candidate in Andhra Pradesh was arrested on Thursday after he broke an Electronic Voting Machine or EVM on Thursday as polling for the Lok Sabha and assembly elections began in the state.
Madhusudan Gupta threw the EVM on the floor at a polling station in the Guntakal Assembly constituency of Anantapur district, the police said.

Mr Gupta, who had come to cast his vote at the polling station in Gutti, was angry with the polling staff over names of assembly and parliament constituencies not being displayed properly, news agency IANS reported.

In a video of the incident, he is seen lifting the EVM and throwing it on the floor.
The machine was damaged in the incident. Mr Gupta was immediately arrested, the police added.

Voters is underway at polling stations in Andhra Pradesh to elect 175 assembly and 25 Lok Sabha members.

According to news agency PTI, there have been reports of glitches in EVMs resulting in delays in polling in many places.

Chief Minister N Chandrababu Naidu and his family members cast their votes at a polling station in Undavalli village in the state capital region Amaravati.

His son Nara Lokesh is the TDP candidate from Mangalagiri Assembly segment that covers Undavalli.

YSR Congress president Y S Jaganmohan Reddy cast his vote in his native Pulivendula in Kadapa district, from where he is seeking re-election.

State Chief Electoral Officer Gopal Krishna Dwivedi cast his vote in Tadepalli and said there were complaints about technical glitches in EVMs in about 50 places.

Technical teams were on the job to rectify the defects and enable polling, he said.

There are nearly four crore registered voters in the state of whom about 10 lakh are first-time voters between 18 and 19 years of age.

As many as 2,118 and 319 candidates are in the contest for 175 Assembly and 25 Lok Sabha seats respectively.

Polling will end at 5 pm in the Left-wing extremism-affected areas, mostly those bordering Odisha and Chhattisgarh.
"""

mtext = """
But Google is starting from behind. The company 
made a late push into hardware, and Apple Siri, available on iPhones, and Amazon
Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption.
"""

# arr  = postag(mtext)
# #arr = predictClass(mtext)
# #arr[0].draw()
# print(arr)

sents = sent_tokenize(mtext)
tags = []
for sent in sents:
    print(sent)
    tokens = word_tokenize(sent)
    print(tokens)
    str = nltk.pos_tag(tokens)
    print(str)
    chk = NPtag(str)
    print(str)
    sentis = xtractSentin(sent)
    print(sentis)
    ner = xtractSpacyNE(sent)
    morener = xtractSpacyNE(chk)
    #print(ner)
    tag = json.dumps({"tag":str,"ne":chk,"sent":sent,"sentis":sentis,"ner":ner})
    #entities = nltk.chunk.ne_chunk(str)
    tags.append(tag)
    #chk = chunk(str)
print(tags)
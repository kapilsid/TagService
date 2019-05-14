"# TagService"

Tag Service tags the unstrutured free text. Currently in works only for English.
The service extracts the noun entities and scraps the entities on the google.
It detects and returns-
1.  Language
2.  Sentiment of each Sentences of the text
3.  Noun Entities of each sentences
4.  Noun Phrases of each sentences
5.  Web knowledge about the noun entities on google
6.  WIP - 
    1) Analyze the sentences into Subject - Predicate  - Object -- create RDF statments.
    2) Morphologically assign pronouns to their associated noun entities.
    3) Allow SPQRQL queries in the RDF statements
    4) Enable Noun entities search based on the required ontology.

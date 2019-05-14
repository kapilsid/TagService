from db.SQLiteDB import SQLiteDB 
from db.NLPQuery import NLPQuery
from datetime import datetime

mtext = """
But Google is starting from behind. The company 
made a late push into hardware, and Apple Siri, available on iPhones, and Amazon
Alexa software, which runs on its Echo and Dot devices, have clear leads in consumer adoption.
"""

dbfile = "./queries.sqlite"

db = SQLiteDB(dbfile)
query = NLPQuery(db)
now = str(datetime.now())
params = (mtext,now)
query.add_query(params)
result = query.selectAllDict()

for row in result:
    print(row)

# query.resetAll()    



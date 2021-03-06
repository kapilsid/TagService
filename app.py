from flask import Flask
from flask import request,jsonify
from flask_cors import CORS
from tagMe import *
from predict20 import *
from sentiments import tagsentiment
from langdetect import lang
from db.SQLiteDB import SQLiteDB 
from db.NLPQuery import NLPQuery
from datetime import datetime

app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})
dbfile = "./queries.sqlite"

def add2DB(mtext):
    """Adds each tag query request to the database.  
    It currently uses SQLite as database which can be easily replaced by
    other database. 
    """

    db = SQLiteDB(dbfile)
    query = NLPQuery(db)
    now = str(datetime.now())
    params = (mtext,now)
    query.add_query(params)
    
    

@app.route("/tag",methods=["GET", "POST"])
def tag():
    """Entry point of this service. It analyzes and tags the text.
    Expects the parameters in mtext var in json format. 
    """
    
    content = request.get_json()
    mtext = content['mtext']
    tags = postag(mtext)
    topic = predictClass(mtext)
    mylang = lang.detect(mtext)
    add2DB(mtext)    
    #sentis = getSentiments(mtext)

    response = jsonify({"tags": tags,"topic":topic,"lang":mylang})
    return(response)



if __name__ == '__main__':
    app.run(host='0.0.0.0')

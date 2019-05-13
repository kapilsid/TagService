from flask import Flask
from flask import request,jsonify
from flask_cors import CORS
from  tagMe import *
from predict20 import *
from sentiments import tagsentiment
from langdetect import lang

app = Flask(__name__)


cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/tag",methods=["GET", "POST"])

def tag():
    content = request.get_json()
    mtext = content['mtext']
    tags = postag(mtext)
    topic = predictClass(mtext)
    mylang = lang.detect(mtext)
    
    #sentis = getSentiments(mtext)
    response = jsonify({"tags": tags,"topic":topic,"lang":mylang})
    return(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

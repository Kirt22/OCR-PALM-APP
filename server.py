from flask import Flask, jsonify
import google.generativeai as palm

palm.configure(api_key="AIzaSyCpcfv9X8QinCGUeqlxn-EA4t6-1R6k1sY")

app = Flask(__name__)

@app.route('/api/hello/<question>', methods=['GET'])
def hello(question):
    answer = BARDresponse(question)
    json_ans = {"message" : answer}
    return jsonify(json_ans)    

def BARDresponse(question):
    response = palm.chat(prompt=question)
    return response.last

app.run()
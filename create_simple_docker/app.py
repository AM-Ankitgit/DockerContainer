from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET'])
def get_hellow():
    return "Hellow users"

app.run(host='0.0.0.0',port=5000)

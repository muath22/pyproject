
#from flask import Flask
#app = Flask(__name__)
#
#@app.route('/')
#def hello():
 #   return 'Hello World! \n'
#
#if __name__ == "__main__":
    #app.run(host="0.0.0.0", debug=True)
    
import datetime as dt
from flask import Flask, request, jsonify
import json

app = Flask("__name__")

@app.route('/')
def index():
    return jsonify({'author': 'rashid a aljohani', 'data': dt.datetime.now()}), 201


@app.route('/auth', methods=['POST'])
def auth():

    if request.json:
        req = request.get_json()
        if req['username'] == req['password']:
            return jsonify({'status': '201'}), 201

    return jsonify({'status': '401'}), 401


if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0', port=3001)
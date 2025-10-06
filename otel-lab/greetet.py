from argparse import ArgumentParser
from flask import Flask
import requests



app = Flask(__name__)
peer=''
OK='OK'
FAIL='FAIL'

@app.route('/goodbye',methods=['POST'])
def goodbyeBack():
    global peer
    return OK
@app.route('/goodbye',methods=['GET'])
def goodbye():
    global peer
    url =f"http://{peer}/goodbye"
    res = requests.post(url=url,json={})
    return OK

@app.route('/hello',methods=['POST'])
def greetBack():
    global peer
    url =f"http://{peer}/goodbye"
    res = requests.post(url=url)
    return OK

@app.route('/hello',methods=['GET'])
def greet():
    global peer
    url =f"http://{peer}/hello"
    res = requests.post(url=url,json={})
    return OK
if __name__ == 'main':
    parser = ArgumentParser()
    parser.add_argument('--peer',type=str)
    args = parser.parse_args()
    peer = args.peer
    app.run(host='0.0.0.0')
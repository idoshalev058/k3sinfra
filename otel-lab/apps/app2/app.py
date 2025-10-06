# Directory structure (single-file code view):

# === app1/app.py ===
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'OK', 200

# no other routes defined -> other paths return 404 by default

if __name__ == '__main__':
    # keep it tiny and single-threaded for easy testing in pods
    app.run(host='0.0.0.0', port=8080)





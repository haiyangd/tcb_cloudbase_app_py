import os
import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Welcome to CloudBase!\n'
    
def dead_loop():
    while True:
        pass

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
    dead_loop()

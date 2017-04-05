from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '{"exits": {"exit1":true,"exit2":false},"blocks": [[5,4], [3,2]]}'

if __name__ == "__main__": 
    app.run()
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "This is my app"


if __name__=="__main__":
    app.run()
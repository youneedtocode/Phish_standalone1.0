from flask import Flask, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['thephish']
verdicts = db['verdicts']

@app.route('/')
def index():
    # Fetch all verdicts from the MongoDB collection
    all_verdicts = verdicts.find()
    return render_template('index.html', verdicts=all_verdicts)

if __name__ == '__main__':
    app.run(debug=True)


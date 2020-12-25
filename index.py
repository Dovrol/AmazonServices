from flask import Flask, request
import random

app = Flask(__name__)

lifters = ['Taylor Atwood', 'Chris Duffin', 'Stefi Cohen', 'Russel Orhii']


@app.route('/')
def hello_world():
    return 'Hello, changes'


@app.route('/test')
def testRoute():
    return 'Test'


@app.route('/lifter')
def getLifter():
    return f'{random.choice(lifters)}, Total: {random.randint(100, 1000)}'


@app.route('/wilks', methods=['POST'])
def wilks():
    squat = request.json["SQUAT"]
    bench = request.json["BENCH"]
    deadlift = request.json["DEADLIFT"]

    return f'{squat + bench + deadlift}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

import json
import flask
app = flask.Flask(__name__)


@app.route("/") 
def hello_world(): 
    with open("testdata.json", "r") as objec:
        data = json.load(objec)
        return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

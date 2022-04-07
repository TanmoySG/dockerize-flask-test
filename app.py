import flask
app = flask.Flask(__name__)


@app.route("/") 
def hello_world(): 
	return "<p>Hello, World from the Container!</p>"


if __name__ == '__main__':
    app.run(debug=True)

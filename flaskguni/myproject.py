from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "<h1 style='color:blue'>Hello, World!</h1>"

if __name__ == "__main__":
	app.run(host="0.0.0.0")

from flask import Flask

# creates a flask application
app = Flask(__name__)

# route to a website incl path following the home
@app.route('/')
def hello_world():
  return "Hello, Steven"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
from flask import Flask, render_template, jsonify

# creates a flask application
app = Flask(__name__)

stocks = [
  {
    'symbol': 'ABNB',
    'name': 'Airbnb',
    'sector': 'Travel',
    'price': 134.00
  },
  {
    'symbol': 'AMZN',
    'name': 'Amazon',
    'sector': 'Commerce',
    'price': 138.76
  },
  {
    'symbol': 'MSFT',
    'name': 'Microsoft',
    'sector': 'Technology',
    'price': 322.08
  }  
]


# route to a website incl path following the home
@app.route('/')
def hello_world():
  return render_template('home.html',
                        stocks=stocks)

# route to a susite with details
@app.route('/api/stocks')
def list_stocks():
  return jsonify(stocks)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
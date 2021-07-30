import flask

from flask import Flask, render_template


app = Flask(__name__)

# Def the homepage
@app.route("/")
def home():
    return render_template('index.html')

# Def the Invesstors page
@app.route("/investors")
def investors():
    return render_template('investors.html')

# Def the Portfolios page
@app.route("/portfolios")
def portfolios():
    return render_template('portfolios.html')

# Def the Companies page
@app.route("/etfs")
def companies():
    return render_template('etfs.html')

# Def the Stocks page
@app.route("/stocks")
def stocks():
    return render_template('stocks.html')

# Def the Orders page
@app.route("/orders")
def orders():
    return render_template('orders.html')

if __name__ == "__main__":
    app.run(debug=True)

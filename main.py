import flask

from flask import Flask, render_template


app = Flask(__name__)

# Def the homepage
@app.route("/")
def home():
    return render_template('index.html')

# Def the Invesstors page
@app.route("/Investors")
def investors():
    return "Investors page"

# Def the Portfolios page
@app.route("/Portfolios")
def portfolios():
    return "Portfolios page"

# Def the Companies page
@app.route("/Companies")
def companies():
    return "Companies page"

# Def the Stocks page
@app.route("/Stocks")
def stocks():
    return "Stocks page"

# Def the Orders page
@app.route("/Orders")
def orders():
    return "Orders page"

# Def the Order_Details page
@app.route("/Order_Details")
def orders_details():
    return "Order_Details page"

if __name__ == "__main__":
    app.run(debug=True)

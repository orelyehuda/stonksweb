from flask import Flask, render_template, json
from flask import request, redirect

import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes 

# Def the homepage
@app.route("/")
def home():
    return render_template('index.html')

# Def the Stocks page
@app.route("/stocks", methods=['POST','GET'])
def stocks():

    # GET --> requestes data from the db
    if request.method == "GET":

    	print("Fetching and rendering stocks web page")
    	query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks;"
    	result = db.execute_query(db_connection, query).fetchall()
    	print(result)
    	return render_template('stocks.html', stock_rows=result)

# Def the add_stock webpage that is used to add a new stock
@app.route("/add_stock", methods=['POST','GET'])
def add_stock():
    print("added stock!")
    cid = request.form['companyid']
    stocksy = request.form['stocksym']
    sharep = request.form['shareprice']
    marketc = request.form['marketcap']
 
    query = 'INSERT INTO Stocks (stock_id, company_id, stock_symbol, share_price, market_cap) VALUES (%s,%s,%s,%s,%s)'
    data = (str(cid), str(stocksy), str(sharep), str(marketc))
    db.execute_query(db_connection, query, data)

    query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('stocks.html', stock_rows=result)

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

# Def the Orders page
@app.route("/orders")
def orders():
    return render_template('orders.html')

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))
    app.run(port=port, debug=True)

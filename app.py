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

    query = 'INSERT INTO Stocks (company_id, stock_symbol, share_price, market_cap) VALUES (%s,%s,%s,%s);'
    data = (str(cid), str(stocksy), str(sharep), str(marketc))
    db.execute_query(db_connection, query, data)

    query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return redirect(request.referrer)


# Def the Stocks page
@app.route("/orders", methods=['POST','GET'])
def orders():
    # GET --> requestes data from the db
    if request.method == "GET":
        print("Fetching and rendering orders web page")

        query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('orders.html', order_rows=result)

# Def the add_stock webpage that is used to add a new stock
@app.route("/add_order", methods=['POST','GET'])
def add_order():
    print("added order!")
    pid = request.form['pid']
    stocksy = request.form['stocksym']
    otype = request.form['otype']

    query = 'INSERT INTO Orders (portfolio_id, stock_symbol, order_type) VALUES (%s,%s,%s);'
    data = (str(pid), str(stocksy), str(otype))
    db.execute_query(db_connection, query, data)

    query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders;"
    result = db.execute_query(db_connection, query).fetchall()
    print(result)
    return redirect(request.referrer)


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

def redirect_url(default='index'):
    return request.args.get('next') or \
        request.referrer or \
        url_for(default)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9112))
    app.run(port=port, debug=True)

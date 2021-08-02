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
        query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks order by stock_id;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('stocks.html', stock_rows=result)

    if request.method == "POST":
        val  = request.form['sortby']

        if(str(val) == 'Price'):
            query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks order by share_price;"
        elif(str(val) == "Market_Cap"):
            query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks order by market_cap;"
        elif(str(val) == "Stock_ID"):
            query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks order by stock_id;"
        else:
            query = "SELECT stock_id, company_id, stock_symbol, share_price, market_cap from Stocks order by company_id;"

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

    return redirect(request.referrer)


# Def the Orders page
@app.route("/orders", methods=['POST','GET'])
def orders():
    # GET --> requestes data from the db
    if request.method == "GET":
        print("Fetching and rendering orders web page")

        query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('orders.html', order_rows=result)

    if request.method == "POST":

        val  = request.form['searchby']

        if(str(val) == 'orderID'):
            query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders order by order_id;"
        elif(str(val) == 'date'):
            query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders order by order_date_time;" 
        elif(str(val) == 'portID'):
            query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders order by portfolio_id;"
        elif(str(val) == 'ostat'):
            query = "SELECT order_id, portfolio_id, stock_symbol, order_type, order_date_time, order_status from Orders order by order_status;"  
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('orders.html', order_rows=result)

# Def the add_order webpage that is used to add a new order
@app.route("/add_order", methods=['POST','GET'])
def add_order():
    print("added order!")
    pid = request.form['pid']
    stocksy = request.form['stocksym']
    otype = request.form['otype']

    query = 'INSERT INTO Orders (portfolio_id, stock_symbol, order_type) VALUES (%s,%s,%s);'
    data = (str(pid), str(stocksy), str(otype))
    db.execute_query(db_connection, query, data)

    return redirect(request.referrer)

# Def the Portfolios page
@app.route("/portfolios")
def portfolios():
   # GET --> requestes data from the db
    if request.method == "GET":
        print("Fetching and rendering portfolios web page")

        query = "SELECT portfolio_id, buying_power, date_created from Portfolios;"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('portfolios.html', portfolio_rows=result)

# Def the add_portfolio webpage that is used to add a new portfolio
@app.route("/add_portfolio", methods=['POST','GET'])
def add_portfolio():
    print("added portfolio!")
    bpower = request.form['buyp']

    query = 'INSERT INTO Portfolios (buying_power) VALUES (%s);'
    data = [bpower]
    db.execute_query(db_connection, query, data)

    return redirect(request.referrer)


# Def the Investors page
@app.route("/investors")
def investors():
    # GET --> requestes data from the db
    if request.method == "GET":
        print("Fetching and rendering investors web page")

        query = "SELECT investor_id, portfolio_id, first_name, last_name, email from Investors"
        result = db.execute_query(db_connection, query).fetchall()
        print(result)
        return render_template('investors.html', investor_rows=result)

# Def the add_investor webpage that is used to add a new portfolio
@app.route("/add_investor", methods=['POST','GET'])
def add_investor():
    print("added investor!")
    pid = request.form['pid']
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']

    query = 'INSERT INTO Investors (portfolio_id, first_name, last_name, email) VALUES (%s, %s, %s, %s);'
    data = (str(pid), str(fname), str(lname), str(email))
    db.execute_query(db_connection, query, data)

    return redirect(request.referrer)


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

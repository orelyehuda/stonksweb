from flask import Flask, render_template, json
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
@app.route("/stocks")
def stocks():
	query = "SELECT * FROM Stocks;"
	cursor = db.execute_query(db_connection=db_connection, query=query)
	results = cursor.fetchall()
	return render_template('stocks.html',stonks_stocks=results)

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
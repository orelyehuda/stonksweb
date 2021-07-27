CREATE TABLE Portfolios(
    portfolio_id int UNIQUE AUTO_INCREMENT NOT NULL,
    buying_power float,
    date_created datetime NOT NULL,
    PRIMARY KEY (portfolio_id)
);

CREATE TABLE Investors(
    investor_id int UNIQUE AUTO_INCREMENT NOT NULL,
    portfolio_id int UNIQUE NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (investor_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id)
);

CREATE TABLE Companies(
    company_id int UNIQUE AUTO_INCREMENT NOT NULL,
    ceo varchar(255) NOT NULL,
    headquarter varchar(255) NOT NULL,
    number_employee int NOT NULL,
    PRIMARY KEY (company_id)
);

CREATE TABLE Stocks(
    stock_id int UNIQUE AUTO_INCREMENT NOT NULL,
    company_id int UNIQUE NOT NULL,
    stock_symbol varchar(255) UNIQUE NOT NULL,
    share_price float NOT NULL,
    market_cap float NOT NULL,
    PRIMARY KEY (stock_id),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);

CREATE TABLE Orders(
    order_id int UNIQUE AUTO_INCREMENT NOT NULL,
    portfolio_id int NOT NULL,
    order_type varchar(255) NOT NULL,
    order_date_time datetime NOT NULL,
    order_status varchar(255) NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id)
);

CREATE TABLE Order_Details(
    order_id int UNIQUE NOT NULL,
    stock_id int NOT NULL,
    quantity int NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

CREATE TABLE ETFs(
    etf_id int UNIQUE AUTO_INCREMENT NOT NULL,
    etf_symbol varchar(255) UNIQUE NOT NULL,
    PRIMARY KEY (etf_id)
);

CREATE TABLE ETFs_Stocks(
    etf_id int UNIQUE NOT NULL,
    stock_id int UNIQUE NOT NULL,
    FOREIGN KEY (etf_id) REFERENCES ETFs(etf_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

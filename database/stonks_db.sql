DROP TABLE IF EXISTS `Order_Details`;
DROP TABLE IF EXISTS `ETFs_Stocks`;
DROP TABLE IF EXISTS `Orders`;
DROP TABLE IF EXISTS `Investors`;
DROP TABLE IF EXISTS `Portfolios`;
DROP TABLE IF EXISTS `Stocks`;
DROP TABLE IF EXISTS `Companies`;
DROP TABLE IF EXISTS `ETFs`;



CREATE TABLE Portfolios(
    portfolio_id int(11) UNIQUE AUTO_INCREMENT NOT NULL,
    buying_power float NOT NULL,
    date_created datetime DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (portfolio_id)
);
INSERT INTO Portfolios (portfolio_id, buying_power, date_created) 
VALUES -- (:porfolio_id_input, :buying_power_input, :date_created_input)
(1,  20133.76, '2020-03-15'),
(2, 334.44, '2019-02-22'),
(3, 120432.12, '2021-06-04');

CREATE TABLE Orders(
    order_id int(11) UNIQUE AUTO_INCREMENT NOT NULL,
    portfolio_id int(11) NOT NULL,
    stock_symbol varchar(255) NOT NULL,
    order_type varchar(255) NOT NULL,
    order_date_time datetime DEFAULT CURRENT_TIMESTAMP,
    order_status varchar(255) DEFAULT 'Pending' NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id)
);

INSERT INTO Orders (order_id, portfolio_id,stock_symbol, order_type, order_date_time, order_status)
VALUES -- (:order_id_input, :portfolio_id_input, :order_type_input, :order_date_time_input, :order_status_input)
(1, 1, 'GME', 'Buy', '2021-05-05', 'Pending'),
(2, 1, 'AMC', 'Buy','2021-04-10', 'Filled'),
(3, 2, 'BBL', 'Buy', '2021-02-01', 'Filled');


CREATE TABLE Investors(
    investor_id int(11) UNIQUE AUTO_INCREMENT NOT NULL,
    portfolio_id int(11) UNIQUE NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    PRIMARY KEY (investor_id),
    FOREIGN KEY (portfolio_id) REFERENCES Portfolios(portfolio_id)
);

INSERT INTO Investors (investor_id, portfolio_id, first_name, last_name, email)
VALUES -- (:investor_id_input, :portfolio_id_input, :first_name_input, :last_name_input, :email_input)
(1, 001, 'Orel', 'Borry', 'orel.borry@bestemail.com'),
(2, 002, 'Lucas', 'Yehuda', 'lucas.yehuda@bestemail.com'),
(3, 003, 'David', 'Ostroff', 'david.ostroff@bestemail.com');

CREATE TABLE Companies(
    company_id int(11) UNIQUE AUTO_INCREMENT NOT NULL,
    ceo varchar(255) NOT NULL,
    headquarter varchar(255) NOT NULL,
    number_employee int NOT NULL,
    PRIMARY KEY (company_id)
);

INSERT INTO Companies (company_id, ceo, headquarter, number_employee)
VALUES -- (:company_id_input, :ceo_input, :headquarter_input, :number_employee_input)
(101, 'Matthew Furlong', 'Grapevine, Texas', 12000),
(102, 'Adam M. Aron', 'Leawood, Kansas', 28468),
(103, 'David B. Baszucki', 'San Mateo, California', 1054);


CREATE TABLE Stocks(
    stock_id int(11) UNIQUE AUTO_INCREMENT NOT NULL,
    company_id int(11) NOT NULL,
    stock_symbol varchar(255) UNIQUE NOT NULL,
    share_price float NOT NULL,
    market_cap float NOT NULL,
    PRIMARY KEY (stock_id),
    FOREIGN KEY (company_id) REFERENCES Companies(company_id)
);


INSERT INTO Stocks (stock_id, company_id, stock_symbol, share_price, market_cap)
VALUES -- (:stock_id_input, :company_id_input, :stock_symbol_input, :share_price_input, :market_cap_input)
(1, 101, 'GME', 172.99, 22.08),
(2, 102, 'AMC', 34.92, 26.56),
(3, 103, 'RBLX', 79.50, 53.41);


CREATE TABLE Order_Details(
    order_id int(11) UNIQUE NOT NULL,
    stock_id int(11) NOT NULL,
    quantity int(11) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

CREATE TABLE ETFs(
    etf_id int(11) UNIQUE AUTO_INCREMENT NOT NULL,
    etf_symbol varchar(255) UNIQUE NOT NULL,
    PRIMARY KEY (etf_id)
);

CREATE TABLE ETFs_Stocks(
    etf_id int(11) UNIQUE NOT NULL,
    stock_id int(11) UNIQUE NOT NULL,
    FOREIGN KEY (etf_id) REFERENCES ETFs(etf_id),
    FOREIGN KEY (stock_id) REFERENCES Stocks(stock_id)
);

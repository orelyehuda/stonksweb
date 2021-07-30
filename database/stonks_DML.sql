INSERT INTO Portfolios (portfolio_id, buying_power, date_created) 
VALUES -- (:porfolio_id_input, :buying_power_input, :date_created_input)
(1,  20133.76, '2020-03-15'),
(2, 334.44, '2019-02-22'),
(3, 120432.12, '2021-06-04');

INSERT INTO Investors (investor_id, portfolio_id, first_name, last_name, email)
VALUES -- (:investor_id_input, :portfolio_id_input, :first_name_input, :last_name_input, :email_input)
(1, 001, 'Orel', 'Borry', 'orel.borry@bestemail.com'),
(2, 002, 'Lucas', 'Yehuda', 'lucas.yehuda@bestemail.com'),
(3, 003, 'David', 'Ostroff', 'david.ostroff@bestemail.com');

INSERT INTO Companies (company_id, ceo, headquarter, number_employee)
VALUES -- (:company_id_input, :ceo_input, :headquarter_input, :number_employee_input)
(101, 'Matthew Furlong', 'Grapevine, Texas', 12000),
(102, 'Adam M. Aron', 'Leawood, Kansas', 28468),
(103, 'David B. Baszucki', 'San Mateo, California', 1054);

INSERT INTO Stocks (stock_id, company_id, stock_symbol, share_price, market_cap)
VALUES -- (:stock_id_input, :company_id_input, :stock_symbol_input, :share_price_input, :market_cap_input)
(1, 101, 'GME', 172.99, 22.08),
(2, 102, 'AMC', 34.92, 26.56),
(3, 103, 'RBLX', 79.50, 53.41);

INSERT INTO Orders (order_id, portfolio_id, order_type, order_date_time, order_status)
VALUES -- (:order_id_input, :portfolio_id_input, :order_type_input, :order_date_time_input, :order_status_input)
(1, 1, 'Buy', '2021-05-05', 'Pending'),
(2, 1, 'Buy', '2021-04-10', 'Filled'),
(3, 2, 'Buy', '2021-02-01', 'Filled');

INSERT INTO Order_Details (order_id, stock_id, quantity)
VALUES -- (:order_id_input, :stock_id_input, :quantity_input)
(1, 1, 10),
(2, 2, 330),
(3, 3, 112);

-- We have not fully implemented ETFs yet as it might not be part of the final draft
-- We will need to rework our FK relationships and certain attributes to allow for NULL values
-- i.e Companies(ceo, headquarter, number_employee), Stocks(market_cap) 
-- INSERT INTO ETFs (etf_id, etf_symbol)
-- VALUES -- (:etf_id_input, :etf_symbol_input)
-- (1, 'LLX'),
-- (2, 'PXAA'),
-- (3, 'SSSX');

-- INSERT INTO ETFs_Stocks (etf_id, stock_id)
-- VALUES -- (:etf_id_input, :stock_id_input)
-- (1, 101),
-- (2, 102),
-- (3, 103);
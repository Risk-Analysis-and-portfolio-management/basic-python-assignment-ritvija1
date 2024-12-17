import yfinance as yf
import pandas as pd

def analyze_portfolio (tickers, weights, start_date, end_date, investment = 10000):

    data = yf.download(tickers, start = start_date, end = end_date)['Close']

    daily_return = data.pct_change()

    portfolio_return = daily_return.dot(weights)

    returns = (1 + portfolio_return).cumprod()

    final_value = returns.iloc[-1] * investment

    print("Initial Investment = ", investment)
    print()
    print("Final Portfolio Value = ", final_value)
    

print("*Portfolio Analysis*")

tickers = input("Enter Stocks: ").split(',')

weights = list(map(float, input("Enter respective weights: ").split(',')))

start_date = input("Enter the Start Date (YYYY-MM-DD): ")

end_date = input("Enter the End Date (YYYY-MM-DD): ")

analyze_portfolio(tickers, weights, start_date, end_date)

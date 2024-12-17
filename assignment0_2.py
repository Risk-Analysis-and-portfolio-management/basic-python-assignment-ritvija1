import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

tickers = ['AAPL', 'MSFT', 'GOOGL']

data = yf.download(tickers, period = '6mo')
print(data.head())

closePrice = data['Close']

invest = 10000
stock = len(tickers)
invest_stock = invest/stock

print()
print()
print("Price invested on each stock = $", invest_stock)
print()
print()

#using % change formula for daily returns

print("**Daily Return**")
print()
print()

daily_return = closePrice.pct_change()
print(daily_return.head())
print()
print()

weight = [1/3,1/3,1/3]

print("**Daily Return on Portfolio**")
print()
print()

portfolio_return = daily_return.dot(weight)
print(portfolio_return.head())
print()
print()

plt.plot(portfolio_return)
plt.xlabel('Date')
plt.ylabel('Daily Return on Portfolio (in USD)')
plt.grid(True)
plt.show()

returns = (1 + portfolio_return).cumprod()
portfolio_totalValue = invest * returns
print()
print()
print("**Total Value of Portfolio at the end of the 6 Month Investment Period**")
print()
print()
print(portfolio_totalValue.head())

plt.plot(portfolio_totalValue)
plt.xlabel('Date')
plt.ylabel('Total Return on Portfolio (in USD)')
plt.grid(True)
plt.show()
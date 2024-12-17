import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


ticker = "AAPL"
tick = yf.Ticker("AAPL")
currency = tick.info['currency']
print("Currency : ", currency)

data = yf.download(ticker, period = "1y")

print(data)

#data is a Pandas DataFrame
print()
print("*CLOSE COLUMN*")
print()

closePrice = data['Close']
print(closePrice)

plt.figure(figsize = (10,5))

plt.plot(closePrice)
plt.title("AAPL Closing Prices for Last Year")
plt.xlabel("Date")
plt.ylabel("Close Price (in USD)")
plt.grid(True)
plt.show()

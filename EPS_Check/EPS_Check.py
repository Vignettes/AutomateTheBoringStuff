'''
#importing stock data to automate the lookups

import pandas as pd
import yfinance as yf

user_input = input()
user_check = yf.Ticker(user_input)
print(user_check.sustainability) 

#This will not be in the present version for the sake of simplicity.

Ultimate goal should be to automatically grab the current stock price, and EPS or P/E.
Potential to allow user to enter their own P/E ratios based on investment tendencies.

I would like to build a selection upfront for valuating P/E or gathering other info.
'''
#Conservative valuation function 
def conservative():
    if stock_one_pe >= 25:
        print(f'Stock is trading at {stock_one_pe}x EPS and may be over-valued')
    elif stock_one_pe <= 24:
        print(f'Stock is trading at {stock_one_pe}x EPS and may be under-valued')

#aggressive value function
def aggressive():
    if stock_one_pe >= 40:
        print(f'Stock is trading at {stock_one_pe}x EPS and may be over-valued')
    elif stock_one_pe <= 39:
        print(f'Stock is trading at {stock_one_pe}x EPS and may be under-valued')

#Ask user to input the current stock price
stock_one = int(input("Provide the current stock price: "))

#Ask user to input the current stock EPS
stock_one_eps = float(input("Provide the current stock EPS: "))

#Provide current trading multipler against EPS for cost
stock_one_pe = stock_one / stock_one_eps


#Notify if this is a value purchase based on risk tolerance
tolerance_select = input("What is your risk tolerance? Conservative or Aggressive?\n").lower()
if tolerance_select == "conservative":
    conservative()
else:
    aggressive()
#Sepearate and provide analysis on P/E ratio

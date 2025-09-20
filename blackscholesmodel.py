#Here I am importing python's math module and only the 'norm' object from the scipy.stats as it is huge 

import math
from scipy.stats import norm

#Defining the variables in the Black-Scholes model
vol = 0.2 # Volatility: How much the price flunctuates (the annualised standard deviation for stock price returns) 
r = 0.1 # Risk-Free Rate: The rate of return you can earn with zero risk of losing money
T = 0.5 # Time to Expiration (in years)
K = 40 # Strike Price: The price at which you buy/sell the stock
S = 42 # Underlying price: The current price of the stock

d1 = (math.log(S/K) + (r + (math.pow(vol, 2)/2))*T)/(vol * math.sqrt(T))
d2 = d1 - (vol * math.sqrt(T))

#Calculating Call Option price
C = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)

#Calculating Put Option price
P = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

print("Call option price is: £", round(C, 2))
print("Put option price is: £", round(P, 2))
[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

Problem:

Draw a sample with size n = 10 from an exponential distribution with lambda = 2.  Simulate this experiment 1000 times and plot the sampling distribution of the estimate L.  Compute the standard error of the estimate and 90% confidence interval.

Repeat with a few different values of n and make a plot of standard error vs. n.


Methodology and Solution:

Created a list of 1000 randomly generated numbers from an exponential distribution with the aforementioned parameters.  Afterward, computed the standard error (0.84799) where n = 10, 100, and 1000.  To find the 90% confidence interval, I took the top and bottom 5% values where n = 10, 100, and 1000.  These values were then plotted to show the standard error linearly decreasing as n increased.


My Work:

import numpy as np

from estimation import RMSE, MeanError

import thinkstats2

import thinkplot



lam = 2

n = 10

m = 1000



estimates = []

for j in range(m):

    xs = np.random.exponential(1.0/lam, n)
    
    lamhat = 1.0 / np.mean(xs)
    
    estimates.append(lamhat)
    
stderr = RMSE(estimates, lam)

print(estimates)

print('standard error', stderr)


cdf = thinkstats2.Cdf(estimates)


ci = cdf.Percentile(5), cdf.Percentile(95)

print('confidence interval bottom 5, top 5', ci)

thinkplot.Cdf(cdf)

thinkplot.Show()




n_vals = [10, 100, 1000]

st_error = [0.8488, 0.2259, 0.06549]

thinkplot.Plot(n_vals, st_error)

thinkplot.Show()

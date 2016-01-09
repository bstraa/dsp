[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Problem:

In order to join the Blue Man Group you must be male and between 5'10'' and 6'1''.  What percentage of the US male population is within this range?

Solution and Methodology:

Used the distribution of heights with parameters mu = 178 and sigma = 7.7 to normalize this distribution.  Then, found the percentage of males within the range of 5'10'' to 6'1''.

My Work:

import thinkstats2

import thinkplot

import scipy



mu = 178

sigma = 7.7

dist = scipy.stats.norm(loc=mu, scale=sigma)

low = dist.cdf(177.8)

high = dist.cdf(185.4)

print(high - low)

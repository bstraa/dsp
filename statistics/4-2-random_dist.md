[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

Problem:

Generate 1000  numbers from random.random and plot their PMF and CDF.  Is the distribution uniform?


Methodology and Solution:

Generated 1000 numbers and plotted their PMF and CDF.  Looked at the CDF and because it is a straight line, the distribution is uniform.

Work Shown:

import thinkplot

import thinkstats2

import random


t = [random.random() for x in range(1000)]

pmf = thinkstats2.Pmf(t)

thinkplot.Pmf(pmf, linewidth=0.1)

thinkplot.Show()


cdf = thinkstats2.Cdf(t)

thinkplot.Cdf(cdf)

thinkplot.Show()

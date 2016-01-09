[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Problem:
-The class size paradox appears if you survey children and ask how many children are in their family.  Families with many children are more likely to appear in the sample and families with no children have no chance to appear in the sample.  Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.  Then, compute the biased distribution.  Plot the actual and biased distributions and their means.

Methodology and Solution:
-Plotted a PMF of the actual distribution for the number of children under 18 using thinkplot.  Then, created an algorithm to plot the biased distributions.  The actual and biased means were then computed.


Work Shown:

import random

import thinkstats2

import thinkplot

import chap01soln


resp = chap01soln.ReadFemResp()

pmf = thinkstats2.Pmf(resp.numkdhh)

thinkplot.Pmf(pmf, label='numkdhh')

thinkplot.Show()


new_pmf = pmf.Copy(label=label)

for x, p in pmf.Items():

  new_pmf.Mult(x, x)
  
new_pmf.Normalize()

biased = new_pmf


thinkplot.PrePlot(2)

thinkplot.Pmfs([pmf, biased])

thinkplot.Show()


print(pmf.Mean(), biased.Mean())

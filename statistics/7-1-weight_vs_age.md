[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Problem:

Make a scatter plot of birth weight versus mother's age.  Plot percentiles of birth weight versus mother's age.  Computer Pearson's and Spearman's correlations.  How would you characterize the relationship between these variables?


Methodology and Solution:

Created a scatter plot of mothers age and birthweight.  To further understand the relationship between variables, I created a percentiles graph.  Visually, it is obvious there is a linear relationship for ages between 18 and 37.  Furthermore, Spearman's and Pearson's correlations are 0.0946 and 0.0688, respectively.  This would be consistent with a linear relationship for most ages; but would account for outliers and a certain non-linear correlation after 37.

My Work:

import numpy as np

import first

import thinkplot

import thinkstats2


live, firsts, others = first.MakeFrames()

live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

bins = np.arange(10, 45, 5)

indices = np.digitize(live.agepreg, bins)

groups = live.groupby(indices)



ages = live.agepreg

weights = live.totalwgt_lb

alpha = 1.0


print('thinkstats2 Corr', thinkstats2.Corr(ages, weights))

print('thinkstats2 SpearmanCorr', thinkstats2.SpearmanCorr(ages, weights))



for i, group in groups:

    print(i, len(group))
    
ages = [group.agepreg.mean() for i, group in groups]

cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75, 50, 25]:

    weights = [cdf.Percentile(percent) for cdf in cdfs]
    
    label = '%dth' % percent
    
    thinkplot.Plot(ages, weights)
    
thinkplot.Show()
    


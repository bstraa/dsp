[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Problem:

Investigate whether first babies are lighter or heavier than others.  Compute Cohen's D to quantify this difference.  How does this difference compare to difference in pregnancy length?

Methodology and Solution:

-Sorted 'birthord' and 'totalwgt_lb' columns after envoking 'value_counts()' on each.  Furthermore, 'birthord' was split into 'firsts' and 'others' to distinguish between first births and non-first births.  

-Mean and variance was then calculated for both first births and non-first births.

-Pooled variance was calculated and implented into the Cohen's D formula resulting in 0.08867 standard deviations; which is nearly three times larger than that of pregnancy length.  However, it is still very small.  As the book mentions, the difference in height for males and females is 1.7 standard deviations.

Work shown below:

import nsfg

import math

df = nsfg.ReadFemPreg()

df.birthord.value_counts().sort_index()

df.totalwgt_lb.value_counts().sort_index()

df.totalwgt_lb.mean()


firsts = df[df.birthord==1]

others = df[df.birthord>1]

firsts_len = len(firsts)

others_len = len(others)


firsts_mean = firsts.totalwgt_lb.mean()

print(firsts_mean)

firsts_var = firsts.totalwgt_lb.var()

print(firsts_var)


pooled_var = (firsts_len * firsts_var + others_len * others_var) / (firsts_len + others_len)

diff = firsts_mean - others_mean

d = diff / math.sqrt(pooled_var)

print('This is Cohens D: {} \n This is nearly 3x larger than the difference of .029 in pregnancy length'.format(d))

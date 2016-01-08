[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Problem:
Investigate whether first babies are lighter or heavier than others.  Compute Cohen's D to quantify this difference.  How does this difference compare to difference in pregnancy length?

Methodology and Solution (work shown is in MyWork2.4.ipynb):
-Sorted 'birthord' and 'totalwgt_lb' columns after envoking 'value_counts()' on each.  Furthermore, 'birthord' was split into 'firsts' and 'others' to distinguish between first births and non-first births.  

-Mean and variance was then calculated for both first births and non-first births.

-Pooled variance was calculated and implented into the Cohen's D formula resulting in 0.08867 standard deviations; which is nearly three times larger than that of pregnancy length.  However, it is still very small.  As the book mentions, the difference in height for males and females is 1.7 standard deviations.

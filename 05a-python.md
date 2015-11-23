# Learn Python

Read please  Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are similar because they are both data structures and can be composed of ANY data type - strings, ints, etc.  However, they differ because tuples are immutable - they cannot be changed.  Whereas, lists are mutable - they can be changed.  Tuples will work as keys in dictionaries (lists won't work!) because by definition, the keys in the dictionary are immutable.  Mutable data types cannot be dictionary keys (they can be values, though).
---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists differ from sets in that sets contain unique data types (no duplicates), and lists can contain duplicates.  Furthermore, lists maintain order, whereas sets do not.  A good example of using sets would be checking to see if a person has visited a website or not.  Sets provide mapping and are very fast at answering yes/no questions.  A good example of using lists would be determining the number of times someone has visited a website.  Sets provide o(1) lookup where lists are o(n).  Therefore, sets are MUCH faster at answering yes/no questions; however, they are limited in their flexibility in answering questions.
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

'lambda' is a fancy word for 'function'.  When we use lambda, we can apply a function to another function.  For example:

a = ['alpha', 'beta', 'Theta']
sorted(a) returns ['Theta', 'alpha', 'beta']

sorted(a, key=lambda word: word.lower()) returns ['alpha', 'beta', 'Theta']

In the previous pseudocode, we are applying a function to our list before it is sorted so that it is sorted with disregard to uppercase.
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






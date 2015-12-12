# Install software on your computer
 

### Install [git](http://git-scm.com/).

You have it installed if you can run `git --version` at the command
line and get output like `git version 2.3.5`.


### Install [Anaconda](http://continuum.io/downloads).

There are two things you can verify to check your install.

First, from the command line, all of the following should start up
some kind of Python interpreter:

```bash
python
ipython
ipython notebook
spyder
```

Second, inside any of those Python interpreters, you should be able to
do all of these without error:

```python
import numpy
import scipy
import matplotlib
import pandas
import statsmodels
import sklearn
```

---

Did you install Python 2 or 3? Why? How can you check the version of Python installed if you happen to be on an unfamiliar computer?

I decided to install Python 2 because it provides the opportunity to learn both simultaneously.  I'll mostly be using syntax for Python 2; however, I will use the newer Python 3 syntax for things that will certainly be implemented in the future.  I think it is important to know both -as not every system will be updated to Python 3 immediately.  However, eventually it will.

You can check the version by typing 'python --version' in the terminal.

---


### Homebrew

If you use a Mac, install [Homebrew](http://brew.sh/) if you don't
have it yet. You could use Homebrew to manage your `git` and `python`
installs as well, but the methods given above are very good and more
cross-platform.

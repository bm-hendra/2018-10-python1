## Pre-readings

1. [A Quick Guide to Organizing Computational Biology Projects][1]
2. [Tidy Data][2]
3. [Best Practices for Scientific Computing][3]
4. [Good enough practices in scientific computing][4]

## Setup

### Python
<a href="https://www.anaconda.com/download/">Anaconda</a>,
an all-in-one installer, is recommended.

Regardless of how you choose to install it,
<strong>please make sure you install Python version 3.x</strong>
(e.g., 3.7 is fine).

When using the IPython notebook, a programming environment
that runs in a web browser, you will need a reasonably
up-to-date browser. The current versions of the Chrome, Safari and
Firefox browsers are all
<a href="http://ipython.org/ipython-doc/2/install/install.html#browser-compatibility">supported</a>
(some older browsers, including Internet Explorer version 9
and below, are not).

#### Windows
<a href="https://www.youtube.com/watch?v=xxQ0mzZ8UvA">Video Tutorial</a>
<ol>
<li>Open <a href="https://www.anaconda.com/download/">http://continuum.io/downloads</a> with your web browser.</li>
<li>Download the Python 3 installer for Windows.</li>
<li>Install Python 3 using all of the defaults for installation <em>except</em> make sure to check <strong>Make Anaconda the default Python</strong>.</li>
</ol>

<!--
#### Mac OS X
<a href="https://www.youtube.com/watch?v=TcSAln46u9U">Video Tutorial</a>
<ol>
<li>Open <a href="http://continuum.io/downloads">http://continuum.io/downloads</a> with your web browser.</li>
<li>Download the Python 3 installer for OS X.</li>
<li>Install Python 3 using all of the defaults for installation.</li>
</ol>

#### Linux
<ol>
<li>Open <a href="http://continuum.io/downloads">http://continuum.io/downloads</a> with your web browser.</li>
<li>Download the Python 3 installer for Linux.<br>
(Installation requires using the shell. If you aren't
comfortable doing the installation yourself
stop here and request help at the workshop.)
</li>
<li>
Open a terminal window.
</li>
<li>
Type <pre>bash Anaconda3-</pre> and then press
tab. The name of the file you just downloaded should
appear. If it does not, navigate to the folder where you
downloaded the file, for example with:
<pre>cd Downloads</pre>
Then, try again.
</li>
<li>
Press enter. You will follow the text-only prompts. To move through
the text, press the space key. Type <code>yes</code> and
press enter to approve the license. Press enter to approve the
default location for the files. Type <code>yes</code> and
press enter to prepend Anaconda to your <code>PATH</code>
(this makes the Anaconda distribution the default Python).
</li>
<li>
Close the terminal window.
</ol>
-->

### Testing If Anaconda was installed


1. Open up the Anaconda Command Prompt
2. Type "ipython" into the prompt
3. You should see Python open up with Python 3.7.x and using the Anaconda distribution
4. Type "quit()" to exit
5. Type "jupyer notebook" to launch the notebook (this may take a while if it is the first time you are launching it)
6. Note the URL (with the token), paste it into your browser
7. Close the anaconda prompt when you're done

### Installing Packages

To install the packages needed for the class you can follow the instructions below:

1. Open your Anaconda Command prompt (Windows)
2. Run the following lines of code
    - note that ctrl+v may not paste in windows,
	  you can paste by pressing shift + insert,
	  or by clicking the icon to the top left of the Anaconda Command promt then edit then paste

``` bash
conda install xlwt openpyxl feather-format seaborn statsmodels scikit-learn regex wget odo numba
pip install lifelines pandas-datareader
```

## Syllabus

- Running python
	- Anaconda, Python, IPython, and Jupyter notebooks
	- Spyder, nteract, Rodeo IDEs
- Installing packages
- Loading libraries, dot notation, and namespaces
- Pandas basics
	- Load, subset, slice, filter data
	- The Pandas Series and DataFrame object
	- Conditional and ‘fancy’ subsetting
- Manual creation of data objects
	- Series and DataFrame object methods
- Saving/loading data: csv, excel, feather, odo library
- Quick whirlwind of grouped operations and plots
- Basic plotting
	- Parts of a matplotlib figure
	- The Seaborn library
- Combining datasets
	- Contatenation
	- Joins
- Missing data
- Tidying and reshaping data
- Data types
- Functions and applying them
	- Testing functions
- Fitting models
	- scikitlearn
	- statsmodels

## Further learning (DataCamp)

- Cleaning Data in Python
	- Review from the class
- Supervised Learning with scikit-learn
	- All of it
	- Particularly, Ch4: Preprocessing and pipelines
- Unsupervised Learning in Python
	- Clustering
	- Projections
- Pandas Foundations
	- Ch3: Time series in pandas
- Manipulating Time Series Data in Python
	- All of it
- Intro to Python for Data Science
	- Ch4: NumPy
- Importing Data in Python (Part 1)
	- Importing data from other file types
	- SAS/Stata
	- HDF5
	- MATLAB
	- SQL
- Importing Data in Python (Part 2)
	- If you are working with web interfaces and APIs
- Importing & Managing Financial Data in Python
- Python Data Science Toolbox (Part 1)
	- Ch3: Lambda functions and error-handling
- Python Data Science Toolbox (Part 2)
	- More "pythonic" code
	- Ch3: Bringing it all together!
		- Iterators to load data in chunks
- Manipulating DataFrames with pandas
	- Ch2: Advanced indexing: MultiIndex
	- Ch4: Grouping data
- Intermediate Python for Data Science
	- Ch1: Matplotlib
- Introduction to Data Visualization with Python
- Interactive Data Visualization with Bokeh
- Statistical Thinking in Python (all the parts)
- Natural Language Processing Fundamentals in Python (as needed)
- Introduction to Databases in Python
	- Using SQLAlchemy in stead of raw SQL querry strings

[1]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424
[2]: http://vita.had.co.nz/papers/tidy-data.html
[3]: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
[4]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510
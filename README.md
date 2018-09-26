<h2>Setup</h2>

<h3>Python</h3>

<p>
Installing the computational, research, and/or data science packages individually in Python can be a bit difficult.
<a href="https://www.continuum.io/anaconda">Anaconda</a>,
an all-in-one installer, is recommended.
</p>

<p>
Regardless of how you choose to install it,
<strong>please make sure you install Python version 3.x</strong>
(e.g., 3.7 is fine).
</p>

<p>
When using the IPython notebook, a programming environment
that runs in a web browser, you will need a reasonably
up-to-date browser. The current versions of the Chrome, Safari and
Firefox browsers are all
<a href="http://ipython.org/ipython-doc/2/install/install.html#browser-compatibility">supported</a>
(some older browsers, including Internet Explorer version 9
and below, are not).
</p>

<h4 id="python-windows">Windows</h4>
      <a href="https://www.youtube.com/watch?v=xxQ0mzZ8UvA">Video Tutorial</a>
      <ol>
        <li>Open <a href="http://continuum.io/downloads">http://continuum.io/downloads</a> with your web browser.</li>
        <li>Download the Python 3 installer for Windows.</li>
        <li>Install Python 3 using all of the defaults for installation <em>except</em> make sure to check <strong>Make Anaconda the default Python</strong>.</li>
      </ol>

<h4 id="python-macosx">Mac OS X</h4>
      <a href="https://www.youtube.com/watch?v=TcSAln46u9U">Video Tutorial</a>
      <ol>
        <li>Open <a href="http://continuum.io/downloads">http://continuum.io/downloads</a> with your web browser.</li>
        <li>Download the Python 3 installer for OS X.</li>
        <li>Install Python 3 using all of the defaults for installation.</li>
      </ol>
<h4 id="python-linux">Linux</h4>
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

<h3>Testing If Anaconda was installed</h3>

<ol>
	<li>Open up the Anaconda Command Prompt</li>
	<li>Type "ipython" into the prompt</li>
	<li>You should see Python open up with Python 3.7.x and using the Anaconda distribution</li>
	<li>Type "quit()" to exit</li>
	<li>Type "jupyer notebook" to launch the notebook (this may take a while if it is the first time you are launching it)</li>
	<li>Close the anaconda prompt when you're done</li>
</ol>

<h3>Installing Packages</h3>

To install the packages needed for the class you can follow the instructions below:

<ol>
	<li>Open your Anaconda Command prompt (Windows)</li>
	<li>Run the following lines of code (note that ctrl+v may not paste in windows, you can paste by pressing shift + insert, or by clicking the icon to the top right of the Anaconda Command promt > edit > paste)</li>
<pre><code>conda install xlwt openpyxl feather-format seaborn statsmodels scikit-learn regex wget odo numba
pip install lifelines pandas-datareader
</code></pre>
</ol>

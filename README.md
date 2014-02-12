Infix Evaluator
===============

A program for evaluating and infix expression and printing out the tree
associated with it

Installation (Development)
--------------------------

For development, you should be using *virtualenv* AND *virtualenvwrapper*. Create a virtualenvwrapper
that uses Python 3 and add the root of the project to your PYTHONPATH using ```add2virtualenv [project_root]```.

PyQt5 is a dependency, which you can either compile in your virtual environment (it's not available from PyPI)
or install system wide (recommended). If you do install it system wide, make sure you include the 
```--system-site-packages``` flag when you create your virtualenv.

Installation (Frozen)
---------------------

If your development environment is set up, you can install [cx_freeze](http://cx-freeze.sourceforge.net "cx_freeze")
and create a frozen executable for the OS you have set up on by running ```python setup.py build```. This executable
should automatically include PyQt5 and any modules from the Python standard library, so
it will be completely self-contained.

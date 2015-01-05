Python Tips
===========

Python Virtual Environments
---------------------------

Python comes in many different flavors, versions, and installations. Most UNIX-like systems today come with Python preinstalled. This Python installation is set at a specific version and it may not provide you with the required version or packages that you require.

The best practice is to utilize a virtual environment. A virtual environment is simply a self-contained hierarchy of a Python installation. The trick to utilize it is simply changing your path to point to the new Python environment. While that does sound tricky the good news is that this is a common problem. Because of that some tools exist to assist you in creating your Python virtual environment. Almost all languages utilize this neat trick.

Setting up your Python environment
----------------------------------

There are many philosophies in how to configure your Python environment. To simplify the philosophy and cut to the chase please use pyenv. It is the most commonly used tool for this purpose. If you would like to use another environment manager please do so. For everyone else here is how to use pyenv.

[pyenv](https://github.com/yyuu/pyenv) and [virtualenv](https://github.com/yyuu/pyenv-virtualenv) were used

Python *requirements.txt* file
------------------------------

Using the PIP tool it is simple to install these packages. In the file "requirements.txt" all of these modules are listed.

Simple do the following and PIP will install the modules for you. Depending on your platform and or Python configuration these modules may need to be compiled.

```
pip install -r requirements.txt
```

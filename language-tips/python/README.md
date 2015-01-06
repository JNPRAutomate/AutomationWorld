Python Tips
===========

Python Virtual Environments
---------------------------

Python comes in many different flavors, versions, and installations. Most UNIX-like systems today come with Python pre-installed. This Python installation is set at a specific version and it may not provide you with the required version or packages that you require.

The best practice is to utilize a virtual environment. A virtual environment is simply a self-contained hierarchy of a Python installation. The trick to utilize it is simply changing your path to point to the new Python environment. While that does sound tricky the good news is that this is a common problem. Because of that some tools exist to assist you in creating your Python virtual environment. Almost all languages utilize this neat trick.

Python Virtual Environment Managers
-----------------------------------

There are many philosophies in how to configure your Python environment. Here are some of the most popular tools to manage virtual environments.

### Pyenv (Mac OS X, Linux)

Most popular on Mac and Linux

-	[pyenv](https://github.com/yyuu/pyenv)
-	[pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)

### Virtualenvwrapper

-	[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)
-	[virtualenvwrapper-win](https://pypi.python.org/pypi/virtualenvwrapper-win)

### Virtualenv

-	[virtualenv](https://virtualenv.pypa.io/en/latest/)

Using PIP to install packages
=============================

PIP is a tool that simplifies the installation of python packages or modules.

-	[PIP Documentation](https://pip.pypa.io/en/latest/reference/index.html)
-	[Using PIP to install packages](https://pip.pypa.io/en/latest/reference/pip_install.html)

Python *requirements.txt* file
------------------------------

Using the PIP tool it is simple to install defined requirements package lists. In the file "requirements.txt" all of these modules are listed. Many tools utilize the requirements.txt file to list the required modules for the tool to work.

Simple do the following and PIP will install the modules for you. Depending on your platform and or Python configuration these modules may need to be compiled.

Many tools, scripts, and modules use this

### Load a requirements file into pip

```
pip install -r requirements.txt
```

### Save a requirements file

```
pip freeze > requirements.txt
```

### What exactly is in a requirements file?

A requiremetns file is simply a key/value pairing of the installed modules

#### Example file

```
Jinja2==2.7.3
MarkupSafe==0.23
PyYAML==3.11
ecdsa==0.11
junos-eznc==1.0.2
lxml==3.4.1
ncclient==0.4.2
netaddr==0.7.12
paramiko==1.15.1
pycrypto==2.6.1
redis==2.10.3
scp==0.8.0
wsgiref==0.1.2

```

Configuration templating with Python
====================================

One of the most popular languages today is Python. It has become the gold standard for software development. Juniper has heavily embraced Python as well. In the realm of automation the majority of the coding is done in either Ruby or Python.

Goal
----

The goal of this example are two show you two similar methods to utilize configuration templating of configurations.

Template Language
-----------------

In Python the most popular templating language is called [Jinja](http://jinja.pocoo.org/). The original use case for Jinja was to provide developers a simpler method for developing web applications. Today most of the HTML pages that you see are actually created via templating. In the use case of of Junos configurations we most likely do not need all of the features of Jinja.

The complete documentation can be found here [Jinja Dev Documentation](http://jinja.pocoo.org/docs/dev/). However we will highlight the specific language use cases here.

### Utilized Jinja features

Jinja has a huge set of features that can be utilized to accomplish your goals. But the hardest part in getting started is learning where to start. For this demo we will use only a small subset of the Jinja template engine.

#### Variable Substitution

The most basic example of Jinja is variable substitution. Think of this as a simple search and replace within a text editor or using the UNIX command *sed*. Their are several benefits to utilizing a Python script to accomplish this task.

-	Repeatability
	-	The ability to repeatedly call a script with fixed input and specified output
-	Chaining
	-	The ability to chain scripts and or actions together

To create a Jinja template it is quite simple. Below is an example of a Jinja substitution variable.

##### Hello World Template

```
"Hello, {{ world }}!"
```

In our example you see "Hello, " which is just treated as plain text. When run through the Jinja engine this text will be output as is. What Jinja is interested in is the contents of the double curly braces "{{ world }}". Jinja sees this as a variable named "world". When applying a variable you are simply applying a key and value to the variable. In this case "world" is the variable. In the Python code we would simply apply world="Automation". The message outputted would be "Hello, Automation!" if you applied this simple key and value.

Here is the full example of what we just discussed.

##### Full Hello World Template

```
Template:
"Hello, {{ world }}!"

Key/Value:
world="Automation"

Final Output:
"Hello, Automation!"
```

The documentation for this can be found [here](http://jinja.pocoo.org/docs/dev/templates/#variables).

#### Using loops

The second step in substitution is utilizing loops. Loops provide true automation advantage to not require the user to repetitively type in commands. We can apply a more complex data structure in Python to a template and iterate over the items. To do this we use the age old "for loop". A for loop is used in many different languages to loop or iterate over items.

##### A Jinja for loop example:

```
{% for item in items %}
Hello, {{ item }}!
{% endfor %}

```

In this example we use an array or list called *items*. This contains a list of strings. When run Jinja will take each item out of the list *items*. A list can contain mixed types or different types of information. The same list could contain numbers/integers, strings, or even more complex items such as dictionaries. The loop takes the next item in the list, starting at item 0, and substitutes it in the loop.

##### Full for loop example

```
Template:
{% for item in items %}
Hello, {{ item }}!
{% endfor %}

Key/Value:
items = ["Automation","Shoe","Socks","Pants"]

Final Output:
Hello, Automation!
Hello, Shoe!
Hello, Socks!
Hello, Pants!
```

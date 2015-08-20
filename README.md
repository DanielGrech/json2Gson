json2Gson
=========

Python script to convert json input into a Java class for use with the GSON java library

Usage
-----

<pre>
	<code>
usage: json2Gson.py [-h] [--class_name NAME]

Convert a sample json feed into Java classes for use with Gson

optional arguments:
  -h, --help         show this help message and exit
  --class_name NAME  The name of the class for the top level Json object

	</code>
</pre>


Example:

`cat sample.json | ./json2Gson.py --class_name=Person`

json2Gson
=========

Python script to convert json input into a Java class for use with the GSON java library

Whilst the results will compile and things will look as you expect, there are things this script can't do for you (Eg using enums instead of strings ..). Be sure to look over the output :)

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


Example
--------

Given the following json:

<pre>
	<code>
{
  "id" : 123,
  "name" : "Homer Simpson",
  "current_fund" : 12.34,
  "is_parent" : true,
  "eligible_for_benefits": false,
  "address" : {
    "street" : "Evergreen Terrace",
    "number" : 742,
    "town" : "Springfield"
  },
  "children": [
    {
      "name" : "Bart Simpson"
    },

    {
      "name" : "Lisa Simpson"
    }
  ]
}
	</code>
</pre>

.. running the command:

`cat sample.json | ./json2Gson.py --class_name=Person`

.. will produce:

<pre>
	<code>
public class Child {

	@SerializedName("name")
 	String name;

	public String getName() {
		return this.name;
	}
}


public class Address {

	@SerializedName("town")
 	String town;

	@SerializedName("street")
 	String street;

	@SerializedName("number")
 	int number;

	public String getTown() {
		return this.town;
	}

	public String getStreet() {
		return this.street;
	}

	public int getNumber() {
		return this.number;
	}
}


public class Person {

	@SerializedName("eligible_for_benefits")
 	boolean eligibleForBenefits;

	@SerializedName("name")
 	String name;

	@SerializedName("is_parent")
 	boolean isParent;

	@SerializedName("children")
 	List<Child> children;

	@SerializedName("current_fund")
 	float currentFund;

	@SerializedName("address")
 	Address address;

	@SerializedName("id")
 	int id;

	public boolean isEligibleForBenefits() {
		return this.eligibleForBenefits;
	}

	public String getName() {
		return this.name;
	}

	public boolean isParent() {
		return this.isParent;
	}

	public List<Child> getChildren() {
		return this.children;
	}

	public float getCurrentFund() {
		return this.currentFund;
	}

	public Address getAddress() {
		return this.address;
	}

	public int getId() {
		return this.id;
	}
}
	
	</code>
</pre>

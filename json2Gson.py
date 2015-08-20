#!/usr/bin/python
import sys
import json

java_classes = []

class JavaClass:
  def __init__(self, name):
    self.name = name
    self.fields = []

  def __repr__(self):
    fields = '\n\n\t'.join(str(f) for f in self.fields)
    getters = '\n\n\t'.join(self._generateGetter(f) for f in self.fields)
    return "public class %s {\n\t%s\n\n\t%s\n}" % (self.name, fields, getters)

  def _generateGetter(self, field):
    retval = field.field_type
    prefix = "is" if retval == "boolean" else "get"
    prop = field.field_name.title()

    return "public %s %s%s() {\n\t\treturn this.%s;\n\t}" % (retval, prefix, prop, field.field_name)

class JavaField:
  def __init__(self, java_type, serialized_name, field_name):
    self.field_type = java_type
    self.field_name = field_name
    self.serialized_name = serialized_name

  def __repr__(self):
    return "@SerializedName(\"%s\")\n \t%s %s;" % (self.serialized_name, self.field_type, self.field_name)

def plural_to_singular(input):
  if input.endswith("ren"):
    return input[:-3]
  elif input.endswith("s"):
    return input[:-1]

def convert_type(input, generic="Object"):
  if input is str or input is unicode:
    return "String"
  elif input is int:
    return "int"
  elif input is float:
    return "float"
  elif input is list:
    return "List<%s>" % (generic)
  else:
    return "Object"

def process(java_class, json_data):
  for key in json_data.keys():
    data = json_data[key]
    t = type(data)
    if t is dict:
      new_java_class = JavaClass(key.title())
      java_class.fields.append(JavaField(new_java_class.name, key, key))
      process(new_java_class, data)
    elif t is list:
      generic_type = plural_to_singular(key.title())
      java_class.fields.append(JavaField(convert_type(t, generic_type), key, key))

      if len(data) > 0:
        new_java_class = JavaClass(generic_type)
        process(new_java_class, data[0])
    else:
      java_class.fields.append(JavaField(convert_type(t), key, key))

  java_classes.append(java_class)

    # print key, type(json_data[key]), json_data[key]

def std_in_to_json():
  json_str = ""
  for line in sys.stdin:
      json_str += line
  return json_str

json_data = json.loads(std_in_to_json())
 
top_level_class = JavaClass("MyAwesomeClass")
process(top_level_class, json_data)

for jc in java_classes:
  print str(jc) + "\n\n"
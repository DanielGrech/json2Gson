#!/usr/bin/python
import sys
import json

java_classes = []

class JavaClass:
  def __init__(self, name):
    self.name = name
    self.fields = []

  def __repr__(self):
    return "%s %s" % (self.name, self.fields)

class JavaField:
  def __init__(self, java_type, field_name):
    self.field_type = java_type
    self.field_name = field_name

  def __repr__(self):
    return "%s %s" % (self.field_type, self.field_name)

def convert_type(input):
  if input is str or input is unicode:
    return "String"
  elif input is int:
    return "int"
  elif input is float:
    return "float"
  else:
    return "Object"

def process(java_class, json_data):
  for key in json_data.keys():
    data = json_data[key]
    t = type(data)
    if t is dict:
      new_java_class = JavaClass(key.title())

      java_class.fields.append(JavaField(new_java_class.name, key))
      
      process(new_java_class, data)
    else:
      java_class.fields.append(JavaField(convert_type(t), key))

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
  print jc.name
  for f in jc.fields:
    print "\t%s" % (f)
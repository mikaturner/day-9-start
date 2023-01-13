programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#To retrieve an item from the dictionary 
#print(programming_dictionary["Bug"])

#Adding items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

#Create and empty dictionary.
empty_dictionary = {}

#You can also wipe and entire dictionary by doing exactly the same thing:

#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#print(programming_dictionary)

#Loop through a dictionary
#This code just gives you the keys in the dictionary not the key value paires
for thing in programming_dictionary:
  print(thing)

#A more accurate way of thinking about this
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
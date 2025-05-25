'''

# String Buildin Functions
message = "corona vaccine is available now"

print(message.upper())  
print(message.lower())  
print(message.title())  
print(message.capitalize())  
print(message.count("a"))  
print(message.find("a")) 
print(message.replace("a", "A")) 

# dir function
print(dir("")) 
print(dir([]))
print(dir(()))
print(dir({}))


'''

# join method
words = ("Python", "is", "awesome")
sentence = " ".join(words)
print(sentence) 

# list methods

fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
fruits.extend(["kiwi", "mango"])
fruits.insert(1, "lemon")
fruits.remove("banana")
fruits.pop(2)
fruits.clear()
print(fruits)


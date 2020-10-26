#!/usr/bin/python3

'''
In this chapter we will talk about dictionaries and sets.
dictionaries uses key value pair and you can use key to refer to the value.

'''
Students = {
            "Name" : "Ramesh" ,
            "Roll No": 21 ,
            "Class" : "X" ,
            "Age" : 16 ,
            "list" : [10,20,30,40]


}

print(Students["Name"])
print(Students["Roll No"])
print(Students["list"])
Students["Age"] = 19
print(Students["Age"])

# The dictonary is unordered list, is it mutable
# Dictonary is indexed, however cannot contain duplicate keys.

Students["Teacher"] = "Nobody"
print(Students["Teacher"])


# We will discuss the other functions of dictionaries available to us.
print(Students.items())

# The following function only return the key and not the values assocaited with the keys.
print(Students.keys())

# The following method is another method of updating
Students.update({"Message" : "Hello All"})

print(Students.items())

# The following method is use to retrive the value of a key.
print(Students.get("Message"))
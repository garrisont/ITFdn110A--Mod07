# Module 7 – Pickling & Error Handling
**Dev:** *TGarrison*  
**Date:** *2022-11-30*
## Introduction
The assignment for this week was defined as: “…create a new script that demonstrates how Pickling and Structured error handling work.”
To accomplish this task I created a few stand alone testing scripts and then combined the key concepts into a single “demonstration” script.

## Pickling
### Pickling - Load & Dump 
To begin with I experimented with pickling by writing “pickled” data to and retrieving it from a file.

Writing / pickle.dump() example:
```
# Write pickled data
objF = open("pickletest.dat", "wb") # Open for writing as binary
pickle.dump(test, objF ) # "dump" pickled data to the binary file
objF.close()
print("Pickled file created:", strFile)
```

Reading a pickled file as if it were text:
```
# Read (raw)pickled data
objF = open("pickletest.dat", "r") # Open the file as non-binary
results = objF.readline() # Read what the user would read when opening the file
objF.close()
print("Raw pickled valeus are:", str(results))
```

Reading and un-pickling with pickle.load()
```
# Read (un)pickled data
objF = open("pickletest.dat", "rb") # Open the file as binary
results = pickle.load(objF) # Load (un-pickle) the data into a variable
objF.close()
print("Unpickled values are:", results)
```

Results:


### asdfasf
asdfasdf



## Topic 1
### Subtopic
## Summary

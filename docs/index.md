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

Reading and un-pickling with pickle.load():
```
# Read (un)pickled data
objF = open("pickletest.dat", "rb") # Open the file as binary
results = pickle.load(objF) # Load (un-pickle) the data into a variable
objF.close()
print("Unpickled values are:", results)
```

Results:

![some alt text](https://github.com/garrisont/ITFdn110A--Mod07/blob/53361071cfd2b71394f2f2036c82431da9495ba3/docs/initial%20pickle%20test.png?raw=true "Some tool tip text")

### Pickling Multiple Entries 
In the process of experimenting with pickling I realized that the pickle.dump and pickle.load commands work like the .write() and .readline() methods.  That is to say that pickle.dump will add/append serialized data to a file. 

```
import pickle
test = ["test1", "test2", "test3"]
others = ["something", "something else"]
third = "solo string"

with open("pickletest.dat", "wb") as f:
    pickle.dump(test, f)
    pickle.dump(others, f)
    pickle.dump(third, f)
```

Note that although I’m using the “wb” option the with open() as f: logic is keeping the file open until the last pickle.dump() is called.
Based on the write (‘dump’) block it shouldn’t have surprised me that pickle.load() reads that same data line by line, acting as a cursor.  This does make it difficult to extract an unknown number of objects:

```
f = open(strFile, "rb")
lstMain.append( pickle.load(f) ) # This will only read the first line
f.close()
print(lstMain)
```

Reading a single object results in the following:

```
[['test1', 'test2', 'test3']]
```

I did a little searching and found a [stackoverflow](https://stackoverflow.com/questions/18675863/load-data-from-python-pickle-file-in-a-loop) discussion of looping through all the objects in a pickled file (visited on 2022-11-26):

```
def pickleLoader(pklFile):
    try:
        while True:
            yield pickle.load(pklFile)
    except EOFError:
        pass

with open(strFile, "rb") as f:
    for event in pickleLoader(f):
        print(event)
```

Conveniently this also provides an example of error handling by breaking the loop when and end of file exception (EOFError) is encountered.
I found the logic in the original example a little confusing so I changed it to something that’s more intuitive for me:
```
# Simplified to:
f = open(strFile, "rb")
while True:
    try:
        lstMain.append( pickle.load(f) ) # Read the pickled file line by line
    except EOFError:
        break # break loop at end of file
f.close()
print(lstMain)
```

Looped pickle.load() results:
```
[['test1', 'test2', 'test3'], ['something', 'something else'], 'solo string']
```


## Topic 1
### Subtopic
## Summary

# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: This script is intended to demonstrate "pickling"
#              and error handling.
# ChangeLog (Who,When,What):
# Travis Garrison, 2022-11-26, Script created
# ---------------------------------------------------------------------------- #
import pickle # The pickle module must be imported before pickling data
lstData = []
strFile = "pickled_entries.dat"

print("""
Note:   This script is intended to present the concepts of try/except/else/finally 
        AND pickle.load() / pickle.dump() with minimal extra code. As a result
        actual error handling is minimal.
        
        Try/except can be used to take action when an exception is encountered.
        Observe that if \'{}\' is deleted the \'except FileNotFoundError:\' 
        block will create the missing file.
        
        Pickling can be used to preserve the data object structure when saving
        to disk/file.  Observe that the "list of dictionaries structure is 
        preserved over the read/write/read cycle.
""".format(strFile)
      )


# >>>> Error Handling (1) - Try/Except for file opening <<<<
try: # Script will execute this block and check for exceptions
    objF = open(strFile, "rb") # Attempt to open the file

except FileNotFoundError: # Take specific action for file not found exception
    print("{} not found, new file created!".format(strFile))
    objF = open(strFile, 'wb') # Create the file
    objF.close() # Close the file

except Exception as e:  # Any other excpetion will be caught here
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')  # Print the exception name, documentation and type

else: # The else block will only be run if the try succeeded
    # >>>> Pickle Example (1) - Loading pickled data <<<<
    lstData = pickle.load(objF) # The .load() method converts pickle data to plain text
    objF.close()
    # NOTE: In this case the above lines of code could/should
    #       have been placed in the "try" block.  They were
    #       placed here to demonstrate the "else" block.

finally: # The finally block will always be run
    print("Current un-pickled values are:\n", lstData) # Finally block will be printed no matter what




# Prompt user for more data to pickle
print("-------------------------------------------------")
strName = input(">> Enter a new item NAME:")
fltCost = input(">> Enter the new item COST: $")
print("-------------------------------------------------")

# >>>> Error Handling (2) - Validate user input <<<<
if fltCost.isnumeric() != True: # Logic statements can be used for simple error handling
    input("Invalid cost entry, press any key to exit") # Inputs can be used to pass on a last user message
    raise Exception("Cost must be numeric") # Raise exception can be used to close a script


# >>>> Pickle Example (2) - Pickle data to file <<<<
lstData.append({"item": str(strName).strip(), "cost":fltCost}) # Append to list as dictionary
objF = open(strFile, "wb")
pickle.dump(lstData, objF ) # .dump() method pickles data into the specified file
objF.close()
print("Pickled file updated:", strFile)



# >>>> Pickle Example (3) - Show pickled and un-pickled list <<<<
# Read (raw)pickled data
objF = open(strFile, "r")
rawValues = objF.readline()
objF.close()
objF = open(strFile, "rb")
unPickledValues = pickle.load(objF)
objF.close()
print("-------------------------------------------------")
print("Raw pickled values are:", str(rawValues)) # Note that the pickled values have to be converted to string
print("Un-pickled values are:", unPickledValues)
print("-------------------------------------------------")
input("(Press Enter to exit)")
'''
@Author: Javeed
@Date: 2021-08-26 
@Last Modified by: Javeed
@Last Modified time: 2021-08-26 12:34:25
@Title : Python program to check whether a file exists.
'''

import os

print("Used if conditions")
if os.path.isfile('Sample.txt'):
    print("File exists")
else:
    print("File does not exist")

# used exceptions
print("\nUsed exceptions")
try:
    open("SampleFile.txt")
    print("File exists")
except:
    print("File Not Found Error")

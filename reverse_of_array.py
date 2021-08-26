'''
@Author: Javeed
@Date: 2021-08-26 
@Last Modified by: Javeed
@Last Modified time: 2021-08-26 22:56:49
@Title : Python program to reverse the order of the items in the array
'''
import array

#Reverse a list array
arr = [1,2,'a',3,'b',4,5,6,'t']
print("List Array\nArray before reversing :",arr)
arr.reverse()
print("Array after reversing :",arr)

#Array Modules
arr_mod = array.array('i',[1,2,3])
arr_mod1 = array.array('u',['a','b','c','d'])
print("Array Modules\nArray before reversing :",arr_mod)
arr_mod.reverse()
print("Array after reversing :",arr_mod)
print("Array before reversing :",arr_mod1)
arr_mod1.reverse()
print("Array after reversing :",arr_mod1)
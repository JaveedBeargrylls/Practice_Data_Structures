'''
@Author: Javeed
@Date: 2021-08-26 
@Last Modified by: Javeed
@Last Modified time: 2021-08-26 22:56:49
@Title : Practice on arrays
'''
import array

#Reverse a list array
arr = [1,2,2,'a',3,'b',4,5,6,'t']
print("List Array\nArray before reversing :",arr)
arr.reverse()
print("count of an element(2) in array :",arr.count(2))
print("Array after reversing :",arr)

#Array Modules
arr_mod = array.array('i',[1,2,3,4,3,5,6,3,4])
arr_mod1 = array.array('u',['a','b','c','d','d','d','d'])
print("\nArray Modules\nArray before reversing :",arr_mod)
arr_mod.reverse()
print("Array after reversing :",arr_mod)

#the number of occurrences of a specified element in an array.
print("Occurence of an element(3) in given array : "+str(arr_mod.count(3)))
print("\nArray before reversing :",arr_mod1)
arr_mod1.reverse()
print("Array after reversing :",arr_mod1)
print("Occurence of an element(d) in given array : "+str(arr_mod1.count('d')))

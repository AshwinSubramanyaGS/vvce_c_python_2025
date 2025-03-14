'''
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the     specified value
extend()	    Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list
'''
#Declare a list
array=[]
arr=[7,9,79,69,80]

#Input list with 5 elements
for i in range(5):
    temp=int(input("NO: "))
    array.append(temp)
array.extend(arr)
#Print list
print(array)

target=int(input("Enter the element to be counted: "))

print(f"{target} is repeated {array.count(target)} times")

print(f"target value is fist present at {array.index(target)}")

my_list = [1,3,5,7,9,2,4,6,8]
print "The third element in my_list is " + str(my_list[2])



#We use the "import" command to tell python that we want to load a new module
import numpy 

#Whenever I want to use something from the imported module, I have to write its name (numpy), then put a dot (.), then say the name of the thing in the module I want to use.

#Here I want to make a numpy-style array, so I use "numpy.array()". The parentheses mean that it's a function - It does stuff, and it may require inputs (which would go inside the parentheses). The input for numpy.array is a list of numbers that you want to turn into an array. 
my_numpy_list = numpy.array([1,3,5,7,9,2,4,6,8])
#I can pick elements from my_numpy_list just the same as from a normal list
print "The third element in my_numpy_list is ", my_numpy_list[2]

#But I can also "slice" the numpy list in different ways
print "The first 5 elements of my_numpy_list are ", my_numpy_list[:5]
print "Every other element in my_numpy_list is ", my_numpy_list[::2]

#EXERCISE: The last command returned the 1st, 3rd, 5th, etc... item from the list. Now I want the 2nd, 4th, 6th, etc. Add a print statement here to do that.

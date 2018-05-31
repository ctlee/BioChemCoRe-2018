#As a good coding practice, I do my importing at the very beginning of my program
import numpy

# Here I'm using python's built-in list to hold a 3x3 matrix of numbers
my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print "my_matrix is "
print my_matrix
print "The first row of my_matrix is ", my_matrix[0]
print "The top left item in my_matrix is ", my_matrix[0][0]
print "the first column of my_matrix is ", [my_matrix[0][0], my_matrix[1][0], my_matrix[2][0]]

#EXERCISE: Add code here to add each number in the first row of my_matrix to the numbers below it (in the second row) and print the new row for the user. That is, this should return [5, 7, 9]. This will be pretty ugly.



#I'll put a blank print statement here to separate the sections of output
print


#Now I'll do the same thing as above, but using a numpy array.
my_np_matrix = numpy.array(my_matrix)
print "my_np_matrix is"
print my_np_matrix
print "The first row of my_np_matrix is ", my_np_matrix[0,:]
print "The top left item in my_np_matrix is ", my_np_matrix[0,0]
print "the first column of my_np_matrix is ", my_np_matrix[:,0]

#EXERCISE: Same as previous, but with numpy: Add code here to add the numbers in the first row of my_np_matrix to the numbers in the second row and print them for the user. This should be a lot easier using a numpy array.



#EXERCISE: Add code to print the top left 2x2 matrix from my_np_matrix. Since the original matrix is 
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# This should print:
# [[1 2]
#  [4 5]]



#In numpy, I can also get a cool index of positions in the matrix I like, for instance like this
my_truth_matrix = my_np_matrix % 3 == 0
#(The "%" operation will return the remainder of a division. For example 5%3 will give the remainder of 5/3, or 2). The operation is called a "modulus", or "mod" for short. So now my_truth_matrix contains "True" and "False" entries corresponding to whether each element in my_np_matrix divides evenly by 3.
print 'The items in my_np_matrix that divide evenly by 3 are in these positions:'
print my_truth_matrix

#I can use this truth matrix as a different type of index for selecting parts of the original matrix
print 'Their values are', my_np_matrix[my_truth_matrix]

#EXERCISE: Add code here to do the same as above for all the items which are greater than 5



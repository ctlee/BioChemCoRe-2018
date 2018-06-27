import numpy

# Here I'm loading a file containing average attendance and ticket prices for different NBA teams (the team names aren't listed).

# Note: Don't think that you need to know absolutely all of the vague little commands in numpy in order to use it - I only know about these commands because I use them very frequently. Same with the pylab module that I use later in this example. I use both numpy and pylab extensively in my work but have probably used less than 10% of all their functions. 

# Another note: When you approach data processing tasks, you should open the file in a text editor to see what the formatting looks like. Look for patterns like columns in simple cases or certain words or phrases that appear near values of interest in more complex data extraction work.

# Here's one of my favorite commands in numpy. It loads files into numpy arrays. 
my_data = numpy.genfromtxt('NBA_attendance_price_simple.csv', delimiter = ',')



# I'll put in a nice little message for the user to understand what they're seeing
print " Average Attendance |  Ticket Price"
print my_data

# EXERCISE: Add code here to print out the average revenue for each team (the ticket price times the attendance). The first number should be 280699.58 (from 13993 * 20.06)

print my_data[:,0]*my_data[:,1]

# Now I'll import a simple plotting module called "pylab" to help me show some data
import pylab

# I want to create a scatter plot of ticket price vs. attendance. The pylab.scatter command takes two lists of numbers - The first corresponds to the x values of the points, the second corresponds to the y values. 
pylab.scatter(my_data[:,0], my_data[:,1])
# Be sure you understand what my_data[:,0] and my_data[:,1] are! If you don't, you should add code to print out their values.


#Here we modify the plot before it's shown
pylab.xlabel('Average Attendance')

# EXERCISE: Modify the above code to properly label the Y-axis
pylab.ylabel('Average ticket price')


# Once we've plotted our data and formatted it how we want, we show the plot.
pylab.show()


# EXERCISE: Add code here to make a scatter plot of the average attendance vs. the total revenue that you calculated above. Note that, when we do a pylab.show() command, pylab clears everything it's going to show so we start with a clean slate.

pylab.scatter(my_data[:,0], my_data[:,0]*my_data[:,1])
pylab.xlabel('Average Attendance')
pylab.ylabel('Total Revenue')
pylab.show()

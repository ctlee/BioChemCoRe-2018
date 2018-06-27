


import numpy
import pylab
#import scipy.interpolate
points = numpy.load('points.npy')
pylab.scatter(points[:,0], points[:,1])
#pylab.show()

my_x_values = range(-100,100)
my_y_values = numpy.interp(my_x_values, points[:,0], points[:,1])
pylab.scatter(my_x_values, my_y_values)
pylab.show()

import scipy.interpolate

f = scipy.interpolate.interp1d(points[:,0], points[:,1])
f2 = scipy.interpolate.interp1d(points[:,0], points[:,1], kind='cubic')

xnew = range(-80,70)
f_points = f(xnew)
pylab.scatter(xnew, f_points)

#pylab.show()

f2_points = f2(xnew)
pylab.scatter(xnew, f2_points)

pylab.show()


#func = scipy.interpolate.interp1d(points[:,0],points[:,1])
#interpolated_points = []
#for i in range(-80,80):
#    interpolated_points.append([i,func(i)])
#pylab.scatter(interpolated_points[:,0], interpolated_points[:,1])

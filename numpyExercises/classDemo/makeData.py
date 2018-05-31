import numpy
import pylab

points=numpy.array([[i,numpy.exp(-float((i-25)**2)/1000) -1.5*numpy.exp(-float((i+55)**2)/500)]  for i in range(-100,100,25)])

pylab.scatter(points[:,0], points[:,1])
pylab.show()

numpy.save('points.npy',points)

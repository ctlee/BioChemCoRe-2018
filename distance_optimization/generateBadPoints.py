import numpy

# This is an algorithm to determine points that are equidistant on the surface of a sphere. You'll find that it doesn't do too well. Remember that any point on the surface of a unit sphere must satisfy x^2 + y^2 + z^2 = 1. 

points = []

# The strategy used here picks x values between -.95 and .95, then computes what values Y could take, then picks y values in .95 * that range, then determines the value that z must have given the above equation. I use this scaling factor so that I'm guaranteed to have many possible y values

factor = 0.95

# I give 10 possible x and y values, which each correspond to one value of z^2. Thus this algorithm generates 200 points
minX = -factor
# Because the "numpy.arange" function doesn't include the upper limit as a possible value, I make it a tiny bit larger to ensure taht the 10th point makes it in.
maxX = factor + 0.00001
xStep = factor * 2.0 / 10
for x in numpy.arange(minX, maxX, xStep):
    minY = -factor * numpy.sqrt(1.0 - x**2)
    maxY = factor * numpy.sqrt(1.0 - x**2) + 0.00001
    yStep = factor * numpy.sqrt(1.0 - x**2) / 10
    for y in numpy.arange(minY, maxY, yStep):
        z = numpy.sqrt(1.0 - x**2 - y**2)
        points.append([x,y,z])
        points.append([x,y,-z])

points = numpy.array(points)
numpy.save('examplePoints.npy',points)

import sys
import numpy
import scipy.spatial.distance as ssd

inputFile = sys.argv[1]

data = numpy.load(inputFile)

distances = ssd.pdist(data)
print distances.shape
badPoints = 0
for point in data:
    radius = point[0]**2 + point[1]**2 + point[2]**2
    if radius > 1.0001 or radius < 0.9999:
        badPoints += 1


print 'number of points not on the surface of the sphere:', badPoints
        

print 'mean:', numpy.mean(distances)
print 'max:', numpy.max(distances)
print 'min:', numpy.min(distances)
print 'std:', numpy.std(distances)

sortedDistances = numpy.sort(distances)
print 'Mean of the closest 400 pairs', numpy.mean(sortedDistances[:400])
print 'Max of the closest 400 pairs', numpy.max(sortedDistances[:400])
print 'Min of the closest 400 pairs', numpy.min(sortedDistances[:400])
print 'St. dev of the closest 400 pairs', numpy.std(sortedDistances[:400])

    


if 'vis' in sys.argv:
    import matplotlib as mpl
    from mpl_toolkits.mplot3d import Axes3D
    import matplotlib.pyplot as plt
    fig = plt.figure(1)
    fig.clf()
    ax = Axes3D(fig)
    ax.scatter(data[:,0],data[:,1],data[:,2])
    ax.set_zlim3d([-1, 1])
    ax.set_ylim3d([-1, 1])
    ax.set_xlim3d([-1, 1])
    plt.show()

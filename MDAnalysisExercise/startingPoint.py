import MDAnalysis as MDA
import numpy
import pylab

# We load the trajectory using a topology file (in this case a pdb) and a trajectory file (the dcd)
U = MDA.Universe('exampleProtein.pdb','exampleTraj.dcd')

# And get the number of frames in our trajectory
numFrames = len(U.trajectory)


# Prepare a list to contain the atom numbers of each first shell water's oxygen in each frame
firstShells = []

for frame in U.trajectory:
    # Select all the water oxygens within 2 angstroms of the protein.
    firstShellSelection = U.selectAtoms('resname WAT and name O and around 2 protein')
    # Get a list of the "atom index" of each of the oxygens
    firstShellResIndices = firstShellSelection.indices()
    # Make a "set" based on these numbers. You'll see why sets are useful later
    firstShellResIndicesSet = set(firstShellResIndices)
    # Store the set in a list
    firstShells.append(firstShellResIndicesSet)

# Prepare a numpy array (a generally useful format for large amounts of data) to hold the frame-to-frame similarity values
firstOverlapMat = numpy.zeros((numFrames, numFrames))
nLeftList = []
nStayedList = []

# Now we go through each frame and compare it to all the others
for frameIndex in range(numFrames-1):
    # Here's one handy thing we can do with sets - subtraction find the elements of one set that aren't in another
    watersThatLeft = firstShells[frameIndex] - firstShells[frameIndex+1]
    # And the len() of a set is the number of items in it
    numWatersThatLeft = len(watersThatLeft)
    # The & operator returns items which appear in both 
    watersThatStayed = firstShells[frameIndex] & firstShells[frameIndex+1]
    numWatersThatStayed = len(watersThatStayed)
    
    print  '%i waters left the first shell this frame, and %i stayed' %(numWatersThatLeft,numWatersThatStayed)

    # Store the results in a list
    nLeftList.append(numWatersThatLeft)
    nStayedList.append(numWatersThatStayed)

# And now we can use the pylab module to plot them
pylab.plot(nLeftList,label='Number of waters that left')
pylab.plot(nStayedList,label='Number of waters that stayed')
pylab.legend()
pylab.show()

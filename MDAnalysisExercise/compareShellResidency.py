import MDAnalysis as MDA
import numpy
import pylab

#This is generated from frames 450 to 500 of the simulation in /extra/banzai2/j5wagner/PkaRuns/092713/solv_hightemp-400 (warning - It's 10000 frames and has a broken periodic box - load into VMD and align then pbc wrap after loading... You may just want to put a better simulation here)
U = MDA.Universe('exampleProtein.pdb','exampleTraj.dcd')

firstShells = []
secondShells = []
thirdShells = []
c=0
for frame in U.trajectory:
    if c%10 == 0:
        print 'Finding hydration shells for frame', c

    ## Note that a selection like 'resname WAT and name O and around 4 protein and not (around 2 protein)'
    ## will not correctly filter out the first shell for some reason. That's why I switch to set notation so soon here.
    firstShell = set(U.selectAtoms('resname WAT and name O and around 2 protein').indices())
    secondShell = set(U.selectAtoms('resname WAT and name O and around 4 protein').indices()) - firstShell
    thirdShell = set(U.selectAtoms('resname WAT and name O and around 6 protein').indices()) - firstShell - secondShell

    firstShells.append(firstShell)
    secondShells.append(secondShell)
    thirdShells.append(thirdShell)
    c += 1

# Preallocate the overlap arrays
firstOverlapMat = numpy.zeros((len(U.trajectory),len(U.trajectory)))
secondOverlapMat = numpy.zeros((len(U.trajectory),len(U.trajectory)))
thirdOverlapMat = numpy.zeros((len(U.trajectory),len(U.trajectory)))

# Calculate similarities of all frames as tanimoto score ( A intersect B / A union B )
for frame1 in range(len(U.trajectory)):
    if frame1%10 == 0:
        print 'performing overlap calc for frame', frame1

    for frame2 in range(frame1,len(U.trajectory)):
        firstOverlap = float(len(firstShells[frame1].intersection(firstShells[frame2])))/(len(firstShells[frame1].union(firstShells[frame2])))
        firstOverlapMat[frame1, frame2] = firstOverlap
        firstOverlapMat[frame2, frame1] = firstOverlap

        secondOverlap = float(len(secondShells[frame1].intersection(secondShells[frame2])))/(len(secondShells[frame1].union(secondShells[frame2])))
        secondOverlapMat[frame1, frame2] = secondOverlap
        secondOverlapMat[frame2, frame1] = secondOverlap

        thirdOverlap = float(len(thirdShells[frame1].intersection(thirdShells[frame2])))/(len(thirdShells[frame1].union(thirdShells[frame2])))
        thirdOverlapMat[frame1, frame2] = thirdOverlap
        thirdOverlapMat[frame2, frame1] = thirdOverlap

## THIS IS THE IMPORTANT PART - Here we calculate the overlap scores between successive frames        
# Calculate the average 1-off-diagional value, that being the average overlap between frames i and i+1    
avgFirstShellOverlap = numpy.mean([firstOverlapMat[i,i+1] for i in range(len(firstOverlapMat)-1)])
avgSecondShellOverlap = numpy.mean([secondOverlapMat[i,i+1] for i in range(len(secondOverlapMat)-1)])
avgThirdShellOverlap = numpy.mean([thirdOverlapMat[i,i+1] for i in range(len(thirdOverlapMat)-1)])

print 'avgFirstShellOverlap:', avgFirstShellOverlap
print 'avgSecondShellOverlap:', avgSecondShellOverlap
print 'avgThirdShellOverlap:', avgThirdShellOverlap

pylab.subplot(311)
pylab.imshow(firstOverlapMat)
pylab.colorbar()
pylab.subplot(312)
pylab.imshow(secondOverlapMat)
pylab.colorbar()
pylab.subplot(313)
pylab.imshow(thirdOverlapMat)
pylab.colorbar()
pylab.show()

for row in firstOverlapMat:
    pylab.plot(row)
pylab.show()

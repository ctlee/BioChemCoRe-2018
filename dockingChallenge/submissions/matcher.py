import glob
knowns = glob.glob('scoring/*-clean.pdb')
unknowns = glob.glob('../encodedProteins/*pdb')

firstLines = []
for known in knowns:
    firstLines.append(open(known).readline())

knowns = zip(knowns,firstLines)

firstLines = []
for unknown in unknowns:
    firstLines.append(open(unknown).readline())

unknowns = zip(unknowns,firstLines)
for known in knowns:
    for unknown in unknowns:
        if known[1]==unknown[1]:
            print '"%s":"%s",' %(unknown[0], known[0])

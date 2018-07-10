#!/usr/bin/env python

# Author: Christian Seitz and Zied Gaieb
# copyright (c): us
# Script follows here

#start up the programs we will use, after importing the full name, you can rename it whatever you want
from __future__ import print_function
import mdtraj as md
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import sys

#load the MD trajectory
traj = md.load_netcdf(filename='/scratch/bcc2018_trajectories/6WCGO/md1/6WCGO-Pro01.nc',top='/scratch/bcc2018_trajectories/6WCGO/6WCGO.prmtop')
traj

#we want to project our data into 2D, this sets up a 2D (replace n with 2)
pca1 = PCA(n_components=2)
traj.superpose(traj, 0)

#for n principal components, put the number you want here
pca_all = PCA(n_components=10)

#reshapes the data into the 2 component system created above
reduced_cartesian = pca1.fit_transform(traj.xyz.reshape(traj.n_frames, traj.n_atoms * 3))
print(reduced_cartesian.shape)

#reshapes the data for the n principal component system
non_reduced_cartesian = pca_all.fit_transform(traj.xyz.reshape(traj.n_frames, traj.n_atoms * 3))

#plot the 2 component data reshaped above into the 2D space created before
plt.figure()
plt.scatter(reduced_cartesian[:, 0], reduced_cartesian[:, 1], marker='x', c=traj.time)
plt.xlabel('PC1')
plt.ylabel('PC2')
cbar = plt.colorbar()
cbar.set_label('legend')
plt.show()

#plot the variance of the n-component system created above
plt.figure()
plt.plot(pca_all.explained_variance_ratio_)
plt.title("PCA Analysis")
plt.xlabel("PC #")
plt.ylabel("Variance")
plt.show()

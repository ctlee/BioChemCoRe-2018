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
#traj = md.load('$trajectory_name')
#nc = /net/gpfs/jam-amaro-shared/bcc2018_trajectories/0YDD5-Pro01.nc
#param = /net/gpfs/jam-amaro-shared/bcc2018_trajectories/0YDD5.prmtop
traj = md.load_netcdf(filename='/scratch/bcc2018_trajectories/6WCGO/md1/6WCGO-Pro01.nc',top='/scratch/bcc2018_trajectories/6WCGO/6WCGO.prmtop')
traj

#the trajectory must be entered on the command line after this script
#trajectory_name=$1

#we want to project our data into 2D, this sets up a 2D (replace n with 2)
pca1 = PCA(n_components=2)
traj.superpose(traj, 0)

#for more PCA
pca_all = PCA(n_components=10)

#reshapes the data into the system created above, edit this for 2 components
reduced_cartesian = pca1.fit_transform(traj.xyz.reshape(traj.n_frames, traj.n_atoms * 3))
print(reduced_cartesian.shape)

non_reduced_cartesian = pca_all.fit_transform(traj.xyz.reshape(traj.n_frames, traj.n_atoms * 3))




#plot the data reshaped above into the 2D space created before
plt.figure()
plt.scatter(reduced_cartesian[:, 0], reduced_cartesian[:, 1], marker='x', c=traj.time)
plt.xlabel('PC1')
plt.ylabel('PC2')
cbar = plt.colorbar()
cbar.set_label('legend')
plt.show()

#variance plot
plt.figure()
plt.plot(pca_all.explained_variance_ratio_)
plt.title("PCA Analysis")
plt.xlabel("PC #")
plt.ylabel("Variance")
plt.show()

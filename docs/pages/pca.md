---
title: "PCA"
permalink: /PCA/
toc: true

summary: "Summary goes here"
---

Principal Component Analysis (PCA)

Summary: This tutorial will help you see how to analyze and visualize multi-dimensional data in an easily understandable way. We will use PCA to analyze and visualize MD trajectories.
Written by Christian Seitz and Zied Gaieb
Motivation
If you have a set of 1D data (for example, the height of all your friends), how can you analyze if those heights are similar or not? There are a number of ways to do this, such as measuring the variance of the heights, the deviation, and others. However, what if you also measured the shoe size of your friends along with their height? How can you tell if the height of your friends is related to their shoe size? In other words, how can you tell if these two sets of data are correlated or not?
Principal component analysis (PCA) is a method of taking multi-dimensional data and transforming it into an easily-understandable, 2D or 3D plot. This is much easier to analyze and visualize than multi-dimensional data, which can have dozens of dimensions. You will take the six HSP90 system trajectories, and analyze XXX vs IC50 of these systems, to see if that correlates with the toxicity of the system. Overall, you will need to check out this potential correlation for each of your six systems, each of which has three trajectories, for a total of 18 PCA analyses. You could do each step for each of your 18 PCA analyses as you go about the tutorial. However, a famous professor once told me that it is a much better idea to pick system, and take it from start to finish, before starting on any others. That way, you will fix any bugs on the one system, and if you mess up a step, you will only have to redo one system, instead of 18.
Part 1 assemble data of the heights of the people in the class, look at variance, then add in the data of their shoe size, run PCA NOT ESSENTIAL should this be done in setosa or plotted the same way as the following stuff???
Part 2 take their trajectories, load MDtraj, create a code to do PCA of these, write their own comments
A.	Set up a python script to do PCA of your trajectories
commands at once. This automates your work. Considering automation makes work easier, more reproducible and easier to follow and remember, it is a good idea to automate your work whenever possible. 
We will work in python, as it is an easy language to use. First, you need to create the shell of the script, that you can later load commands into. You can use gedit, vi, vim, nano, or whatever else you are familiar with, and you can call the script whatever you want, as long as you remember what you called it. Here is how I would create the shell of my PCA script:

cseitz@chemcca3:~/scripts$ vi PCA_tutorial.py

Note: cseitz is the username, and chemcca3 is the name of the workstation. Yours will be different. The directory I made this in what my scripts directory, but you can make yours wherever you want. However, make sure that you end your script with “.py” to demarcate it as a python script.
B.	Load what you need into your script
Inside PCA_tutorial.py you will place in the commands to run PCA on your MD trajectories. First of all, you need to tell your script that it is a python script by adding

#!/usr/bin/env python

In vi, this is done by pressing “i” for insert, then typing whatever you want.
Next, you need to import the modules needed to run PCA. You can think of software modules like normal software programs on your home screen, the kind that you need to double click to open. If they are not open, you can’t use them. Similarly, if your script doesn’t load the module you need, you can’t use it.
Next, you will add a bunch of modules and commands to your script. It is good practice to document your script, which means adding in comments that tell what the modules and commands do. A well-documented script makes it much easier for other people to use your script and understand what it does, and also makes it easier for you to understand what you did, if you come back to a script a while later. For each of the commands and modules that you put into your script, please add a comment, writing in your own words what’s going on. In a python script, a “#” at the start of any line signifies a comment. What that means is that the line will be bypassed by the terminal, and you can write whatever you want without fear of it messing up your script. For example, in a simple script I wrote
NAME=”Christian Seitz”
Echo $NAME
#this prints out my name

And the comment reminds me what the two commands above it are doing. When you first start writing scripts, it is a good idea to put in copious amounts of comments. Back to loading modules. Add this to your script:
from __future__ import print_function
import mdtraj as md
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import sys

These are modules needed to run PCA in MDtraj. Again, the from __future__ import print_function just means you are selecting a single module from a larger library to import, and import mdtraj as md means you are importing mdtraj, and hereafter going to refer to it as md. If you do not want to refer to mdtraj as md, you can either leave out the as md part, or call it something other than md. The rest you understand.
C.	Set up PCA
Now that we have loaded in the modules needed for PCA, we need to tell our script what data we want to use, and how we are going to use it. The first part is to load in the MD trajectory as follows:
traj = md.load_netcdf(filename=’/net/gpfs/jam-amaro-shared/bcc_2018_trajectories/0YDD5-Pro01.nc’, top=’/net/gpfs/jam-amaro-shared/bcc2018_trajectories/0YDD5.prmtop’)
traj
This is saying that your trajectory and parameter files will be loaded into MDtraj, in its netcdf module, and will hereafter be referred to as “traj”. Again, you can refer to these as something other than “traj” if you want, just be consistent with what you choose. The trajectory files are not in your folder, so you are simply telling your script where to find them. Also, the “0YDD5-Pro01.nc” and “0YDD5.prmtop” files will be replaced with each of your own trajectories, so you will need to keep editing this part when you analyze a new trajectory (i.e. put in your own nc and prmtop files, and keep the single quotation marks around the whole thing). Don’t forget to put in a comment on what’s going on here!
Next, you will tell MDtraj to do PCA on the trajectory you just loaded above. Do it like this:
pca1 = PCA(n_components=2)
traj.superpose(traj, 0)
Remember, PCA can be projected into 2D or 3D space, so you need to tell MDtraj how many components you want to have as an output. We are doing XXXXX and IC50, so we need two components. The second command tells the output to be placed in the same place (i.e. not have multiple unitcells of output).
Now that we have loaded the data and told MDtraj we want to do PCA, we need to tell MDtraj how exactly we want it to use the data. We want to have a 2D output. PCA does a number of math manipulations of the data, so even though we started out with two dimensions, we still need to specify how many dimensions we want as an output. We want to have two dimensions, which will still require a transformation and reshaping of the data. This is done as follows:
reduced_cartesian = pca1.fit_transform(traj.xyz.reshape(traj.n_frames, traj.n_atoms * 3))
print(reduced_cartesian.shape)
D.	Plot your results
Now that you have performed PCA on your data, you need to be able to visualize what you have done. It is easy to do this in matplotlib, which you already loaded above. From here, you simply need to tell matplotlib how you want it to make a graph for you. This is what we will do:
plt.figure()
plt.scatter(reduced_cartesian[:, 0], reduced_cartesian[:, 1], marker=’x’, c=traj.time)
plt.xlabel(‘PC1’)
plt.ylabel(‘PC2’)
cbar = plt.colorbar()
cbar.set_label(‘legend’)
plt.show()

This is just one way of graphing your results, you can tinker with other ways that might look better if you want. Now that you have written your script, you need to exit the script AND save it. Remember, the way to exit and save a file in vi is to do 
:wq
Which will return you to whatever directory you were in before. Congratulations, you have written a script to do PCA! Now that you have completed the analysis for one system, you will need to do this for the remaining 17 systems. You have already written the script to do PCA analysis of an MD trajectory, so you just need to change the files that you are using for each of the 17 other systems. 

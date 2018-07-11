---
title: "RMSD-based Clustering Tutorial"
permalink: /clustering/
toc: true

summary: "In this tutorial you will learn how to cluster your trajectories "
---

## Why Cluster?

We cluster our trajectories to reduce the number of frames that we have to look at ourselves.

## Generate Gromacs-compatible trajectory

First, we prepare the trajectory file. Gromacs does not read in NETCDF (.NC) files, but can read multi-frame PDB files. Thus, we start by converting our trajectory into the appropriate PDB format.
1.	Load the parameter file (the .prmtop file) and the coordinates file (.NC file) in VMD.
2.	Align the trajectory: It is typical to align the trajectory by certain atoms and then to do the clustering by another atom set. For example, one might choose to first align the trajectory by the protein alpha carbons, and then to cluster based on the positions of the residue atoms lining the active site.
    In VMD, click on Extensions => Analysis => RMSD Trajectory Tool.
    The large text box initially contains the selection "protein." Change this to whatever atom selection you wish to use to align the  trajectory. To align by all alpha carbons, for example, replace "protein" with "name CA". Or to align by all backbone atoms, replace "protein" with "backbone".
    Now click on the "Align" button.
    Your trajectory has now been aligned.
3.	Right click on the trajectory name in the VMD main menu.
4.	Select "Save Coordinates..."
5.	In the "Selected Atoms" field, type “protein” 


{% include image.html file="/clustering/science.png" alt="" caption="Figure 1. This is a test!" width=10 %}

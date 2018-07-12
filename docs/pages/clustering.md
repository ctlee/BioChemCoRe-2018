---
title: "RMSD-based Clustering Tutorial"
permalink: /clustering/
toc: true

summary: "In this tutorial you will learn how to cluster your trajectories with RMSD-based clustering"
---

## Why Cluster?

We cluster our trajectories to reduce the large number of frames in a typical trajectory file to a representative set of distinct frames.

## Generate Gromacs-compatible trajectory

First, we prepare the trajectory file. Gromacs does not read NETCDF (.NC) files, but can read multi-frame PDB files. Thus, we start by converting our trajectory into the appropriate PDB format.
1.	Load the parameter file (the .prmtop file) and the coordinates file (.NC file) in VMD.
2.	Align the trajectory: It is typical to align the trajectory by certain atoms and then to do the clustering by another atom set. For example, one might choose to first align the trajectory by the protein alpha carbons, and then to cluster based on the positions of the residue atoms lining the active site.
    In VMD, click on Extensions => Analysis => RMSD Trajectory Tool.
    In the new window that popped up, the large text box initially contains the selection `protein`. Change this to whatever atom selection you wish to use to align the  trajectory. To align by all alpha carbons, for example, replace `protein` with `name CA`. Or to align by all backbone atoms, replace `protein` with `backbone`.
    Now click on the "Align" button.
    Your trajectory has now been aligned. You can close this window.
3.	Now right click on the trajectory name in the VMD main menu.
4.	Select "Save Coordinates..."
5.	In the "Selected Atoms" field, type `protein` or whatever selection of atoms you want to cluster.

Note: If you have too many frames, you might choose a Stride larger than the default value of 1 (which means including all frames). And if you do, make sure you take note of your Stride value.

6.  Click on the "Save..." button and save the PDB file trajectory.pdb
7.  Now we need to edit the trajectory.pdb file to be Gromacs-compatible. First, we need to delete the VMD-generated header. Second, we need to replace the `END` delimiters used by VMD to separate frames by the `ENDMDL` delimiters that Gromacs uses. These two things could be done by any text editor, but it will be faster to do with command lines like below.

To remove the VMD-generated header:

`cat trajectory.pdb | grep -v CRYST1 > temp.pdb`

`mv -f temp.pdb trajectory.pdb`

To replace `END` delimiters between frames by `ENDMDL` delimiters:

`perl -pi -e 's/END/ENDMDL/g' trajectory.pdb`

Now, your Gromacs-compatible trajectory file is ready.


You also will need to prepare a separate PDB file for the first frame of your trajectory.
1.  Open the trajectory.pdb file in VMD.
2.  Right click on the trajectory name in the VMD main menu.
3.  Select "Save Coordinates..."
4.  In the Frames section, set First and Last to 0, and Stride to 1.
5.  Click on the "Save..." button and save the PDB file first_frame.pdb
6.  Edit the PDB file in an editor like vi or gedit to remove the VMD-generated header.
Now, your first frame is also ready for our clustering exercise.


## Identify the Protein Residues that Line the Active Site

Typically when clustering protein trajectories for drug-design purposes, you want to know about the various conformations of the protein active site. Thus, we must identify the residues that line the active site.

While there are various methods to identify active-site residues, you can start with the first frame of your trajectory (first_frame.pdb) and use VMD to identify all protein residues within 10 Angstroms of the ligand.

Example of VMD Selection:
`same residue as protein within 10 of resname LIG`

To get the indices of the atoms of the active-site residues, save a PDB file containing only the relevant active-site residues.

Right click on the protein name in the VMD main menu.
Select "Save Coordinates..."
In the "Selected Atoms" field, type something like:
`same residue as protein within 10 of resname LIG`

Click on the "Save..." button to save the PDB file. Name your file active_site.pdb.
Edit the PDB file in an editor to remove all lines but the coordinate data. (Remove all HEADER lines and END line).
Unfortunately, VMD reindexes all the atoms when you save a new pdb file, so atom indices in your new file (active_site.pdb) do not match the indices in the original PDB containing the entire protein (trajectory.pdb or first_frame.pdb). Fortunately, the residue indices are not changed, so let's just save those. From the command line, extract just the residue index numbers like this:

`cat active_site.pdb | awk '{print $6}' | sort -n | uniq > resid_activesite.dat`

So now you have a file containing all the residue indices of the active-site residues. Let's pick out the lines of the original PDB file (first_frame.pdb) the have those same residue indices.

`cat resid_activesite.dat | awk '{print "cat first_frame.pdb | awk STARTif ($6==" $1  ") print $0 END" }' | sed "s/START/'{/g" | sed "s/END/}'/g"  | csh > active_site_correct_residues.pdb`

Note that you may get the following error:

`awk: {if ($6==) print $0 }`

`awk:          ^ syntax error`

This error can be corrected if a blank line is removed from the resid_activesite.dat file.

## Identify Key Atom Indices


{% include image.html file="/clustering/science.png" alt="" caption="Figure 1. This is a test!" width=10 %}

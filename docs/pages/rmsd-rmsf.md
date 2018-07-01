---
title: "RMSD/RMSF Analysis"
permalink: /rmsd-rmsf/
toc: true

summary: "In this analysis tutorial, you will learn how to use AMBER's cpptraj module to calculate the RMSD and RMSF of a system. You will learn the definitions of these terms and when and how to use them in your data analysis. Additionally, you will hone your python skills in generating files, running scripts, extracting data from files and plotting with matplotlib."
---

You may now have a trajectory from your protein simulations. In case you don't, you can use the training data sets we have provided for you. 

## What are RMSD and RMSF? 

**RMSD: root mean square deviation**

RMSD stands for root mean square deviation. RMSD is a numerical measurement representing the difference between two structures: a target structure and a reference. In molecular dynamics, we are interested in how structures and parts of structures change over time as compared to the starting point. For example, if a protein, over a course of a simulation, has a lid opening and closing motion (like pacman opening and closing his mouth), a plot of RMSD vs. time will indicate that with large RMSDs. RMSD is typically plotted vs. time. 

RMSD can be used to identify large changes in protein structure as compared to the starting point. A leveling off or flattening of the RMSD curve can also indicate that the protein has equilibrated. 

**RMSF: root mean square fluctuation**

RMSF stands for root mean square fluctuation. This is a numerical measurement similar to RMSD, but instead of indicating positional differences between entire structures over time, RMSF is a calculation of individual residue flexibility, or how much a particular residue moves (fluctuates) during a simulation. RMSF per residue is typically plotted vs. residue number, and can indicate structurally which amino acids in a protein contribute the most to a molecular motion. 

In our case of pacman, the parts of pacman's face that make up his mouth will have high RMSFs because the mouth in constant motion, but the parts making up the rest of his head would maintain consistently low RMSFs. 

## Create a Jupyter Notebook for Analysis

Let's set up a brand new jupyter notebook for your RMSD & RMSF calculations that you can use for all your analyses moving forward.

### Generate the Notebook

1. Navigate to your home directory and start up a jupyter notebook by running the following commands in your terminal: 

```bash
module load anaconda
jupyter-notebook
```

This should launch a browser opening into the Jupyter Notebook interface. The URL will look something like: localhost:8888/tree. This is the working directory. 

{:start="2"}
2. Create a new notebook by selecting "New" from the Files tab and then selectiong "Python 3" Notebook.

	`New > Python 3`

This should immediately open up a new 'Untitled' notebook in a new window or tab. Name the notebook 'RMSD_RMSF_Analaysis.'

### Import Necessary Modules

{:start="3"}
3. To do our analysis, we will need to import some useful (and, hopefully, familar!) python libraries. In the first code block, write and run:

	```import numpy as np
	import mdtraj as md
	import matplotlib.pyplot as plt
	%matplotlib inline
	```
## Load Training Data

We can't do any analysis unless we've got data to analyze! Your training set data is located in keck2's `/scratch/bcc2018_trajectories/${BCCID}`, where ${BCCID} is the name of the BCCID for your training file. 

{:start="4"}
4. Cd into your trajectory folder and take a look around. You should find a topology file `*.prmtop` and three replicate trajectory folders named `md1`, `md2`, and `md3`. Inside each of these `md` files you will find the trajectory file, `*.nc`. 

5. In your jupyter notebook, load the data you wish to inspect. It may be helpful for you to create a BCCID variable, as well as a filedir variable for easier coding. 

	```
	BCCID = #your BCCID
	filedir = '/scratch/bcc2018_trajectories/BCCID}/'
	traj1 = md.load(top=filedir+BCCID+'.prmtop', filedir+'md1/'+BCCID+'-Pro01.nc')
	traj2 = md.load(top=filedir+BCCID+'.prmtop', filedir+'md2/'+BCCID+'-Pro01.nc')
	traj3 = md.load(top=filedir+BCCID+'.prmtop', filedir+'md3/'+BCCID+'-Pro01.nc')
	```

Key in `Shift + Enter` to run this cell, load your trajectories, and define your variables!

## Calculate RMSD

### Generate RMSD Data

{:start="6"}
6. Use the built-in MDTraj (`md`) trajectory function to generate RMSD data from your trajectories. In a new code block:

	```
	rmsd1 = md.rmsd(traj1, traj1, 0)
	print(rmsd1)
	```

The [documentation](http://mdtraj.org/1.6.2/api/generated/mdtraj.rmsd.html) tells you all about what arguments this function takes, and what they each mean. 

You should also obtan the data for your replicate trajectories, traj2 & traj3. 

### Plot RMSD v Time

{:start="7"}
7. To visualize this data, use a plt scatterplot. In a new code block:
	```
	plt.scatter(np.arange(0, len(rmsd1), rmsd1, marker='.', color='m', s=3, label='Rep 1'))
	## what does np.arange do?
	plt.xlabel('Time (ns)')
	plt.ylabel('RMSD ($\AA$)')
	```

### Overlay RMSD replicate plots

{:start="8"}
8. You may want to overlay your data to compare your three replicates. To do this, you can add two more scatterplots to the above code, after the first call to plt:

	```
	plt.scatter(np.arange(0, len(rmsd2), rmsd2, marker='.', color='c', s=3, label='Rep 2'))
	plt.scatter(np.arange(0, len(rmsd3), rmsd3, marker='.', color='b', s=3, label='Rep 3'))
	```

9. Add a legend to your plot.

	```
	plt.legend(loc=4)
	```

I encourage you to play around with the matplotlib pyplot [documentation](https://matplotlib.org/api/pyplot_summary.html) to adjust your plots to your liking. You can vary the colors, legend location, marker sizes and types, etc, until your figures are as clear as possible. 


## Calculate RMSF

To calculate RMSF, we will need to invoke `cpptraj`, which is part of the AmberTools software. In addition to RMSF, `cpptraj` can also calculate RMSD and diffusion, as well as many other useful quantities. 

Cpptraj requires an executable script and an input file. I'll walk you through how to make them, and what needs to go in each.

### Preparing the Input File
### Preparing the Executable
### Running the Script
### Extracting .dat Data
### Plotting the Data




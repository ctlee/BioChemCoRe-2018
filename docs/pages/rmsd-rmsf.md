---
title: "RMSD/RMSF Analysis"
permalink: /rmsd-rmsf/
toc: true

summary: "In this analysis tutorial, you will learn how to use AMBER's cpptraj module to calculate the RMSD and RMSF of a system. You will learn the definitions of these terms and when and how to use them in your data analysis. Additionally, you will hone your python skills in generating files, running scripts, extracting data from files and plotting with matplotlib."
---

You may now have a trajectory from your simulations. In case you don't, you can use the training data sets we have provided for you. 

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

1. Navigate to your scratch directory and start up a jupyter notebook by running the following commands in your terminal: 

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


	```
	import numpy as np
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
	filedir = '/scratch/bcc2018_trajectories/'+BCCID+'/'
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

You should also obtain the data for your replicate trajectories, traj2 & traj3. 

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

Cpptraj requires an input file that looks like this:

```
trajin ${our_trajectory_file}.nc 
rmsd @C,CA,N first
atomicfluct out ${output_file_name}.dat @C,CA,N byres
```

The variable ${your_trajectory_file} needs to be replaced with the name of your trajectory file, which is probably something like: `filedir+BCCID+'.nc'`. 

The second line, 'rmsd @C,CA,N first,' is the program aligning your protein to the structure given by the first frame in the simulation. This is done to avoid the biasing of your RMSD and RMSF values by protein diffusion. 

The @C, CA, N is the 'mask,' or atom selection of your alignment and calculations. This aligns the protein backbone only. 

Your ${output_file_name} should be a name of your choice to which you'd like the program to output the data. The flag 'byres' means that the data output file will give an residue index and a corresponding RMSF value.

 {% include note.html content="In addition to RMSF, cpptraj can also calculate RMSD, and can do it for specific residues and specific atom selections, just like mdtraj. If you'd like to learn more about cpptraj's functions, you can visit the [AmberTools](ambermd.org/doc12/Amber18.pdf) manual." %}

{:start="10"}
10. In your jupyter notebook, you will use python to generate this input file. In a new code block: 

	```
	mydir = '/scratch/${username}/'
	with open(mydir+BCCID+'_rmsf.in', 'w') as file:
		file.write('trajin '+filedir+BCCID+'/md1/'+BCCID+'-Pro01.nc\n')
		file.write('rmsd @C1,CA,N first\n')
		file.write('atomicfluct out '+mydir+BCCID+'.dat @C,CA,N byres')
	```

In running this block, you create a file in your scratch directory called BCCID_rmsf.in, which is your cpptraj input file. If you look at it with your favorite text editor, you should see two lines. If you only see one line, double check your code to make sure that you have a line separator '\n' at the end of the first line.

### Preparing the Executable

The second thing you need to run cpptraj is the executable script. This is what acts as the command line to tell cpptraj to run. This script needs to have this structure:

	```
	cpptraj ${path_to_topology}.prmtop ${your_input_file_name}.in > ${your_log_file_name}.log
	```

Where ${path_to_topology} indicates the filename of your prmtop file, which should be found in `filedir+BCCID`. Your input file name is the name of the input file you created in the above code block, `mydir+BCCID+'_rmsf.in'`. The `>` is what we use to specify that we'd like the output to be stored into a log file, which you name yourself. 


{:start="11"}
11. We could run all of this in the command line, but for the purposes of this tutorial and showing you how these analyses can be automated, we are going to generate a script instead. In a new code block in Jupyter Notebook:

	```
	with open(mydir+BCCID+'_rmsf.sh', 'w') as file:
		file.write('cpptraj '+filedir+BCCID+'.prmtop '+mydir+BCCID+'_rmsf.in > '+mydir+BCCID+'_rmsf.log\n')
	```

Double check to make sure that the input file name in your *.sh matches the input file name *.in, and that all your other file names and file paths are correct. If you need to make a change, it is okay to rerun the code block in Jupyter Notebook. 

### Running the Script

Now that your cpptraj files have been generated, you can now run the program by running the executable shell script (*.sh) in your command line. 

{:start="12"}
12. Give permissions to run the file:

	```
	chmod 744 ${your_shell_script_name}.sh 
	```

13. Execute:
	
	```
	./${your_shell_script_name}.sh
	```

Once you run this in the command line, you should wait for it to complete. When $bash pops up again, you can `ls` in your scratch directory, where you will hopefully see two new files: the *.dat and *.log files which cpptraj should have created. 

If the log file has been created but not the dat file, open and look at the log file to see what errors came up. Double check all your input scripts and file paths, and if you still cannot isolate the source of error, check with a mentor. 

### Extracting .dat Data

Your *.dat file should contain two columns, headed by "#Res" and "AtomicFlx." 

{:start="14"}
14. See if you can use the python methods you've learned so far to extract each column of this data file into a numpy array in your jupyter notebook! Be sure to give your arrays reasonable names. A mentor will go over this with you if you get stuck.


{% include warning.html content="Now is a good time to check in with a mentor. Go back through and edit your scripts to include running cpptraj for your other replicates, md2 and md3, then extract the new data into new arrays in preparation for plotting. If you've made it this far easily, challenge yourself to change your entire jupyter notebook into a function that will take ANY BCCID and output RMSD and RMSF data." %}

### Plotting the Data

**RMSF vs. Residue Number**

RMSF is typically plotted vs. residue number. At this point, you should have three data sets: one for each md replicate. 

{:start="15"}
15. Create a plot of RMSF on the y-axis and residue number on the x-axis. What does this plot tell you about the dynamics of your protein? Do the replicates line up? (Should they line up? Why or why not?) 

**RMSF vs. IC50**

Now you will be challenged to use all of your python skills to generate a plot of RMSF vs. IC50. Recall that IC50 is a measurement of drug potency. High IC50 correlates to a low potency, and low IC50 correlates to a high potency. 

Sometimes, IC50 is also expressed as pIC50. Similar to the pH scale, where pH = -log[H+], pIC50 = -log(IC50). This means a high pIC50 corresponds to a **high** potency, and vice versa. 

{:start="16"}
16. In your jupyter notebook, create a function called calculateMeanRMSF. Have it take the input ${BCCID} and output list [x, y], where x = pIC50 and y = mean RMSF. 
	
	```
	def calculateMeanRMSF(id):
		#return [pIC50, mRMSF]
	```

You should be able to populate this function with everything you need to calculate the RMSF values of a given BCCID and calculate the mean RMSF value of the entire system. The pIC50 values can be found in a dictionary located in the bccHelper.py located [here](https://ctlee.github.io/BioChemCoRe-2018/pdbs/).

17. Once this function has been created, use it to calculate the mean RMSF value for all systems in the training set. 

18. Plot this new data on a scatter plot with log(IC50) on the x-axis and meanRMSF on the y-axis. You should have 6 data points. Does mean RMSF of a system correspond to drug efficacy? Is mean RMSF a good `metric` for describing drug efficacy? 

19. Think about what your data mean, and start coming up with a list of metrics you could use to correlate RMSF or RMSD to IC50 of a system. Do you want to look at one specific residue or a group of residues? Do you want to investigate the dynamics of the ligand? Talk this over with your group, and maybe play around with mdtraj and cpptraj's atom selection tools to look at different parts of the system. 



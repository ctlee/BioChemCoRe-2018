
## System Energy Tutorial

In this tutorial, you will postprocess an amber output file obtained through a production MD simulation
to obtain avaerage total energies, for each of the ligands with measured IC50s. 
Amber MD output files are contained in the corresponding 
` ../ligand_ID/md1,  ../ligand_ID/md2, etc ` folders. The code employed herein cds into each of these 
folders, calls an amber analysis script to create the energy vs time files, and calculates the average 
(predicted) energy for each of these ligands. Finally, the script will plot the measured vs. 
predicted ic50s. Detailed comments are provided in the analysis script to guide the student through the analysis.

## System energy

Recall that the output file from an Amber MD simulaiton contains a lot of information about the system, such as 
temperature, density, energy, etc.. We could write a script that uses ` awk ` or ` sed ` to extract the desired information for each timestep.
Fortunately, we do not need to do this since Amber already has a script for this purpose!

As a first pass, let's look at the energy of a single MD run. 

1. Inside the "md1" directory of your chosen system, create a new directory called "energy_analysis_test"
2. load the amber module if you have not done so already
3. move into your new directory and run the amber perl script with the command, remember to change the name of the file to match your system!
``` $AMBERHOME/bin/process_mdout.perl ../$your_production_output_file$ ```
4. After this completes, you should see many summary files for different properties in the directory.
5. Lets explore these files by opening them with your favorite text editor. **What information is inside?**
6. Lets quickly plot one of these time series with xmgrace
``` xmgrace summary.EPTOT ```
**What is this plot showing us?**


This is a really useful tool if we only want to look at these properties for a single system, but it would quickly become tedious 
if we had many different systems. This is where automation can be a huge time saver!

## Running the Automated Energy Analysis Script ##

1. In the top level directory that contains all of the systems, create a new directory called "energy_analysis" 
2. In this new directory, place the files: `run_Energy_Analysis.py` and `BCCHelper.py'
3. Take a look at this script with your favorite text editor. What does the `subprocess` command do?
4. Run the script ` python run_Energy_Analysis.py 1` **What is the number "1" doing here?**
5. At this point, take some time to discuss your results with your fellow students and the BCC mentors.

## Discussion Questions ##

1. Does there appear to be quality correlation between measured (system energy) and predicted ic50, in your produced plot?
2. How can we determine if differences between values are significant?
3. Is total energy a good metric, or might another metric be better?

## Additional Challenges ##

1. Can you modify the script to plot pIC50 vs predicted ic50? Hint: pIC50 = -log(IC50)
2. Can you quantify the **correlation** between measured and predicted ic50s, in your produced plots?
3. Plot other properties produced by the perl script. Consider using another series on the same plot.
4. Can you calculate the standard deviation of the values in addition to the average? How could you
include this in the plot?
5. What other things might it be useful to automate with the `subprocess` command
















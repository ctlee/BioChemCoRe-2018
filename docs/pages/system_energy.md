---
title: "System Energy Tutorial"
permalink: /system-energy/
toc: true

summary: "In this tutorial we will analyze the correlation of system energy with measured ic50 values. We will also lwearn more about automation through the subprocess python command"
---

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

1. Create a new directory called "energy_analysis_test" in your scratch directory.
2. Load the amber module if you have not done so already
3. Move into your new directory and run the amber perl script with the command, remember to change the path and name of the file to match your chosen system!

``` $AMBERHOME/bin/process_mdout.perl path/to/$your_production_output_file$.out ```

4. After this completes, you should see many summary files for different properties in the directory.
5. Lets explore these files by opening them with your favorite text editor. **What information is inside?**
6. Lets quickly plot one of these time series with xmgrace
``` xmgrace summary.ETOT ```
**What is this plot showing us?**


This is a really useful tool if we only want to look at these properties for a single system, but it would quickly become tediousif we had many different systems. This is where automation can be a huge time saver!

## Running the Automated Energy Analysis Script ##

1. Download the necessary scripts  <a href="{{ '/assets/pdbs/make_directories.py' | prepend: site.baseurl }}">make_directories.py</a> and <a href="{{ '/assets/pdbs/run_Energy_Analysis.py' | prepend: site.baseurl }}">run_Energy_Analysis.py</a>
1. In your personal scratch directory, we will create a new filetree for energy analysis by running `python make_directories.py`
2. In this new directory, place the files: `run_Energy_Analysis.py` and `BCCHelper.py`
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
Include the correlation and a regression line on your figure.
2. Plot the number of atoms in each system vs. the system energy. **What trends do you notice?** 
3. Plot other properties produced by the perl script (kinetic energy, potential energy, etc.). Consider using multiple series on the same plot. **Do any of these show better correlation?**
4. Can you calculate the standard deviation of the values in addition to the averages? **How could you
include this in the plot?** Use the calculated standard deviation as an error bar on the average energies.
5. Take some time to polish the figure you are creating. Try to change the colors and shapes of data points. Consider adding additional lables.
6. What other things might it be useful to automate with the `subprocess` command
















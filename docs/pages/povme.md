---
title: "POVME: The POcket Volume MEasurer"
permalink: /povme/
toc: true

summary: ""
---

Written by Jeff Wagner

Jeff’s note: I am the current lead developer of POVME. I also have two other essentially full-time projects. You can expect far less stability and user-friendliness from this software than you could from things like VMD. Please don’t hesitate to complain - The problems that give you the hardest time are the ones I’ll focus on fixing first!

gcq#395: "It was something to at least have a choice of nightmares" (Joseph Conrad)
grompp -h

## Why is POVME important?

Molecular Dynamics simulations are getting really popular in our field of science. However, what usually happens is that scientists run simulations (at great computational cost), and then see a big protein wiggling around, and have no idea what to do with it. There are a growing number of tools that try to quantitatively answer the question of "what in the world just happened in this simulation", but they often do abstract analyses with no clear actionable output. In other words, conclusions like “The RMSD went up” do not tell us why people get cancer or what to do about it.

Everyone does simulations different ways and for different specific reasons, but I’d argue that the most directly valuable question that people can try to answer is "how does this simulation help me make a drug?" The normal way for people to use a protein structure to make a drug is by using "docking" software, which tells them how likely a given small molecule is to fit into a binding site. However, even moderately effective docking is computationally expensive. Sometimes, a scientist will do a simulation and end up with hundreds of thousands of snapshots (each a single protein structure), and it is impractical to dock to all of them. POVME3 is primarily intended to solve this problem of making molecular dynamics simulations more useful to drug designers.

## How does POVME enable better drug design?

In the above situation, POVME can perform two useful tasks:

1. Pocket shape-based clustering: POVME will analyze the whole simulation from the perspective of the binding pocket, and find unique families of conformations that were visited. This way, a scientist can dock to just a few, unique snapshots of the protein binding pocket (the cluster representatives), under the assumption that the drugs revealed by docking to these few conformations are the same as the drugs that you'd discover by docking to every single frame.

2. Simulation summary: POVME can generate a 3D model overlaid on the binding pocket, showing what kinds of subpockets, motions and/or conformational changes were observed in the simulation. Actual drug designers will find this output far more useful than the clustering, since drug design is present(2016)ly more of an art than a science, and this information is more readily visualized. 


## Today’s projects

We’ll be a bit busy, so let’s get moving. Today, we’ll
- Set up POVME and its VMD plugin
- Run POVME on the binding pocket in our system the old-fashioned way
- Run an advanced POVME analysis workflow on multiple trajectories of the same protein bound to different ligands
- Do more complex post-analysis on these POVME results

**1. Set up POVME and its VMD plugin**

The POVME VMD plugin is best for processing small cases (< 1000 frames), but I still use it in larger cases to define the binding pocket region.  Installing VMD plugins is a pain in the neck, but thankfully I’ve prepared the important file for you.

In your home directory, create or open the file “.vmdrc” and enter the following:

```
set auto_path "$auto_path $::env(POVME_PATH)/POVME/vmdplugin"
menu main on
vmd_install_extension povme2 povme2_tk_cb "Analysis/POVME2"
set ::povme2::povme2_directory "$::env(POVME_PATH)/POVME/POVME3.py"
```

execute `module load povme`

Now open VMD and go to `Extensions -> Analysis -> POVME2`.

**Ensure that this opens.**

**2. Run POVME on the binding pocket the old-fashioned way**

We will first look at a single trajectory from our HSP90 simulations. Select your favorite BCCID.

Make a new directory in your /scratch for the analysis, 

cd to this directory. We want all output to be written there.

Load the trajectory into VMD by specifying the correct file paths. Be sure to open VMD in your new /scratch directory.

Align the trajectory using the `RMSD Trajectory Tool`

Open the Povme2 plugin by going to `Extensions -> Analysis -> POVME2`

Under “Select molecule”, choose the protein.

Change “selection” from “all” to “protein”. If we don’t do this, POVME will think that the space which the ligand occupies isn’t part of the pocket. 

Now, you’ll want to draw an inclusion shape that encompasses the binding pocket. Under “Inclusion Shapes”, go to “Add new shape...”. Say “yes” to switching to GLSL mode. You will play around with the different options, but you will ultimately decide to use a sphere (cylinders and cubes are broken right now). You can use the mouse to snap the shape center to an atom - One click snaps it to an atom center, another releases it. I usually snap it to an atom center near where I want it, and then use the arrows by the number box values to move it around. VMD is a bit rough around the edges when it comes to input boxes like this. If I modify a number by hand, I sometimes have to increase and decrease the value by 1 before VMD recognizes it and updates the shape on the screen. 

Here is a short digression on seed regions: Seed regions are a smaller, “core” part of the binding pocket, whereas the inclusion region is a kind of “maximum size”, or limit for how large our pocket can be defined. Why did we do this? One problem that arose often in doing POVME analysis of binding pockets was that some conformational changes would “split’ the binding pockets into two smaller pockets. If we’re focusing on putting a drug in one of the smaller pockets, then it’s a waste of time to analyze the other while the protein conformation is splitting them. But when the two pockets are joined, we are interested in their combined shape. How do we manage this?

We solve this problem using “seed” regions. These are regions that we are definitely interested in, and we are only interested in the rest of the pocket if it’s connected to a seed region. When POVME runs on a frame, it starts by defining the pocket as the seed region only, then discards any points which are overlapping with a protein atom. It then iteratively grows the seed region out in all directions, one grid point at a time, until it runs into a protein atom or the edge of the inclusion region. When the pocket stops growing, it moves onto the next frame. This way, we define only useful contiguous regions each frame, rather than adding noise from disconnected pockets and little bubbles between imperfectly-packed amino acids in the protein.

Add a “Contiguous Pocked Seed” sphere as well (in the third box) with the same center as the original, but only half the radius.

Also, for the sake of speed, go to Settings -> Output… and change the number of processors to however many you can spare (max 8).

Now hit `Run POVME`.  This should take a few minutes. 

When it finishes, it should load the volume trajectory file as well as a bunch of other files into VMD. 

For complicated reasons, loading the volume trajectory will un-center your camera. To fix that, go to the VMD Main window and double-click the “T” column next to the protein to make that the “Top” molecule, then go to the 3D window and hit “=” to re-center the visualization on the “Top” molecule. 

VMD is going to have trouble understanding what’s going on with the binding pocket, which is a bunch of dummy atoms that pop around on a grid. In the VMD Main window, go to Graphics -> Representations and change volume_trajectory’s drawing style to “VDW”. 


**Now hit play and watch the binding site change with each frame!**

Here is a short digression on the meaning of “average” in the context of a pocket: We have seen what binding pocket look like in each frame. What does it look like on average? In the volume_trajectory file, each frame shows a single snapshot of the pocket. Each point is either a 1 (part of the pocket) or a 0 (not part of the pocket - Maybe it was blocked by the protein or outside the inclusion region). Since the grid that these 0’s and 1’s are on is always in the same location in space, we can take the average value of each grid point over all of the frames, to see what fraction of the time a certain region is part of the binding pocket. So maybe a certain grid point was part of the pocket in 10 frames, and not part of the pocket in 90 frames. Then it would have an average value of 10%, or 0.1.

We can visualize this “average pocket” by looking at volumetric_density.dx. 

A Data Explorer (DX) file doesn’t contain atoms - It instead describes the density of some phenomenon in a 3D region. In this case, our phenomenon is “volumes that are part of the binding pocket”. We visualize dx files by giving VMD a cutoff (eg. “I want to see everything that’s part of the binding pocket at least 50% of the time”), and then VMD draws an “isosurface” around all of the points that satisfy our condition.

Take a look at the other files VMD has loaded. 
**What do they show?**
**Do they agree with what you have seen with other analysis techniques?**


- Once you’re comfortable with the concept of averages and isosurfaces, let’s tinker around with seed regions. We’ll do that by removing the seed region (so that the entire inclusion region becomes the seed) and re-running the analysis

- In the VMD Main window, double click the “T” column next to our original protein trajectory (not the pocket trajectory - Just the protein!) to make it “top”
 
- Delete the seed region in the POVME2 window. 

- To avoid overwriting our original files, go to Settings -> Output… and change “Output Filename Prefix” to “./noSeed_”, then hit OK

- In the POVME2 window, press `Run POVME2`
 
- When this is complete, look at noSeed_volume_trajectory.pdb and compare the two volume trajectories (maybe draw one of them in VDW with a sphere scale of 0.4 and the transparent material, and the other in VDW with a sphere scale of 0.3 and the Coloring Method ColorID with a value of “10 cyan”)

**How do these two pocket trajectories differ?**


The pocket-growing algorithm requires a certain number of “neighbors” before the pocket can grow out to a new point (default 3 neighbors). This prevents it from going way down into little crevices, and so the pocket only fills in places where a ligand atom might reasonably fit. When we don’t use a seed region, we don’t use these growing rules. 

**Take a screenshot of a place where the pockets differ and put it in your notes. Be sure to label which representation is which mode.**


Based on the user’s discretion and the nature of the pocket, we can forego using a seed region altogether. In essence, when we don’t define a seed region, the entire inclusion region becomes the seed. This means that we’ll occasionally capture little packing defects in the protein and little random crevices as part of the pocket. But in some cases, there can be proteins with segmented, tight pockets or other factors that make abandoning the seed region worthwhile.

In this case, I’d say that the pocket is open enough to justify using the seed regions.

**Exit VMD.** 

When POVME ran in VMD, it was actually spewing files all over the place. Most of them were stored in a mean little folder called “frameInfo”, which is packed to the gills with all sorts of information about each frame. The post-analysis tools will be interested in these.

Run `ls frameInfo` and appreciate how much junk is in there.


## Running POVME on the command line for multiple systems

Using the POVME VMD plugin, we were able to calculate the pocket volume for one trajectory. However, this is not practical 
if we want to calculate pocket volumes for many systems. Instead we will run POVME from the command line.
Using the skills you have learned from previous exercises, you will automate the POVME analysis for all of the HSP90 systems

Here is an outline for what you will need to do:

1. Remove all waters and align each trajectory to the reference .pdb file provided (use MDtraj)
2. Save each trajectory out in **.pdb format!** (use MDtraj)
3. Create POVME input files that contain the correct path to your new trajectories.
4. Each POVME input file needs to define the exact same inclusion and seed regions, so that we can compare between systems.
5. Run POVME for each trajectory 
```python /software/repo/moleculardynamics/povme/2018.6.21-git/POVME/POVME3.py ${myfile}.ini```

Running POVME for each system will take some time (a few hours), so make sure you are happy with the parameters you have 
chosen etc. before running.
**It is a good idea to try everything on just one trajectory first!** 

## Analyzing the POVME results
While your calculations are running, you can start to think about how you can present the results.
**Remember we are trying to correlate to IC50 values!**

Here are some ideas:
1. Average volume vs. IC50
2. Max/Min volume vs. IC50
3. Volume fluctuations vs. IC50
4. Average surface area vs. IC50

Also, create an image or two that shows an interesting observation about a system's pocket.

Other Ideas for the Future:
1. Ligand-Based Pocket Definition
2. POVME Clustering
3. Pocket Similarity









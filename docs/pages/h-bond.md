---
title: "H-Bond Tutorial"
permalink: /h-bond/
toc: true

summary: "This tutorial will walk you through the theory and process of using hydrogen bond analysis to predict the IC50 rank ordering of ligands."
---
Written by Bryn Taylor and Terra Sztain-Pedone

## Motivation

Hydrogen bond analysis identifies the number and/or duration of hydrogen bonds in a system of interest. A hydrogen bond is formed when a single hydrogen (H) is shared between the heavy atom it is covalently bonded to (the "donor") and another heavy atom (the "acceptor"). This hydgrogen bond (which is really a "weak interaction") is usually with electronegative atoms such as fluorine (F), oxygen (O), or nitrogen (N). Remember, H-bonding is FON!  

Hydrogen bonds facilitate molecular interactions and are ubiquitous in nature. The bond between a H on a water molecule and an O on another water molecule is resposible for the cohesive property of water. H-bonds are also important for the secondary structure of proteins: depending on the spacing of the amino acids, H-bonds formed between these residues create alpha helices or beta sheets. In this tutorial, we're interested in H-bonds formed between ligands and proteins. 

Make sure to do this tutorial for each HSP90 system. 

#### Q1: What role do you think H-bonds play in the interaction between a ligand and a protein? 

## Step 1: Visual inspection of H-bonds in protein-ligand system. 

First, create a new directory for this analysis.

```
> mkdir hbond_analysis
```

Next, examine the trajectory files in VMD. In the Distance Analysis tutorial (https://ctlee.github.io/BioChemCoRe-2018/distance-analysis/), you identified some important bonds or interactions between the ligand and protein in the first frame and in the last frame. Some of these may have been H-bonds. Let's do this again, but pay attention to only the H-bonds. Recall that you need to first load and align the trajectories, and create new graphical representations for the protein, ligand, and waters. 

{% include tip.html content="Create a new representation “same residue as within 3 of (resname LIG)” and as a Drawing Method use “H-bond”; change the angle cutoff from 20 to 50 and update the selection every frame; increase the thickness of the H-bonds that are drawn from 1 to 2. This will show the H-bonds in the Display window and will help you to better determine which are the possible H-bonds." %}

#### Q2.  In your notebook, list ligand-protein or ligand-water hydrogen bonds that are in the first or last frame. For example: 

{% include image.html file="/h-bond/table.png"
alt="h-bond table" caption="Table 1: Example table"
width=100 %}

Repeat this for each trajectory (md1, md2, md3) of the three replicates for each HSP90 system. You may have already done some of this work; save time by repurposing and/or adding to it! 

#### Q3. For each system and replicate, make a clear and informative figure that shows the hydrogen bonds you identified in Q2. Don't forget labels! 

#### Q4. Do the number of H-bonds differ much between md1, md2, md3 replicates? What about between HSP90 systems? 

## Step 2: Finding and plotting all protein-ligand H-bonds

Now that you're familiar with the types and number of H-bonds at the beginning and end of the simulations, we're going to take a look at the number of H-bonds over time. Counting these on a frame-by-frame basis in VMD would take forever, so we're going to write a script that will do it for us. 

### 1. Launch a jupyter notebook. 

```
> cd hbond_analysis

> jupyter notebook 
```
Create a new notebook by clicking new python 3 notebook in the upper right corner of the page. Name this notebook "hbond_analysis.ipynb". The next steps will be done in your notebook.

### 2. Load Modules 

import mdtraj as md
import pytraj as pt # we need to make sure this is installed on the Keck II computers
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline # this makes your plot print in the jupyter notebook

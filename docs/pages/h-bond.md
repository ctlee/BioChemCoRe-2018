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

#### Q1: What role do you think H-bonds play in the interaction between a ligand and a protein? 

You are expected to do this tutorial for each HSP90 system. 

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


---
title: "Preparing Your System for Molecular Dynamics (MD)"
permalink: /system-prep/
layout: page
toc: true

summary: In this tutorial you will learn how to setup your system to begin running molecular dynamics in Amber. As a part of this tutorial you will be introduced to the use of Schrödinger's Maestro software for protein preparation followed by parameterization using AmberTools Antechamber.
---

At this point, you should have been given a PDB file containing your system
of interest from the BioChemCoRe teaching team. If you did not, please let
us know now.

## Motivation

Why do we need to go through system setup for MD?

Protein structures from various structural determination methods often are not
complete. For example, structures from x-ray crystallography typically do not
have resolved protons. Take a second and research why this is. Write your
answer in your notebook.

Given the importance of hydrogen bonding, which requires proton participation,
for protein stability and receptor-ligand interactions, X-ray crystal s
tructures cannot be used used in molecular dynamics (MD) right “off the
shelf”. To help resolve this and many other issues, a variety of software
tools have been developed.

## Looking at the Crystal Structure


1. First download the Protein Data Bank (PDB) structure that corresponds with you
BioChemCoRe PDB identifier from the website.

2. Visualize this structure by loading it in PyMol; replacing "my_proein_name"
with the appropriate filename for your structure.

```
module load pymol
pymol my_protein_name.pdb
```

TODO: image of HSP90 Structure

3. Take some time to examine the structure, can you locate the inhibitor molecule?
Are there any crystallographic waters present?


TODO: Sequence Alignment


## Protein Preparation Workflow

1. One tool of extreme utility is Maestro (http://www.schrodinger.com/Maestro/). It acts as a molecular visualizer, and a workflow starting point for many of Schrodinger’s tools. Today we will be using the Protein Preparation workflow to clean up our structure. To load the Schrodinger toolkits, in Keck II issue the command:

   ```
   module load schrodinger
   maestro
   ```

2. Next, load your pdb file.

   ```File > Import Structures```

   After importing, the Workspace will show a representation of our protein. Using the left mouse button allows you to select residues or areas, middle mouse rotates the view, and the right mouse button translates.

3. HSP90 is a dimer, which means it may have multiple chains.
On the bottom center of the Maestro window, look for the info table entry for "CHAINS." If there are multiple chains, separate them by right clicking on the structure name in the left pane and selecting:

   ```Split > By Chain```

4. Once split, each chain will show up in the "Entry List" pane on the left. Select chain A by clicking the blue dot.

5. With Chain A selected, click the "Protein Preparation" button in the top bar. This will open up the Protein Preparation workflow tab.


   TODO: Image of protein prep window

   TODO: check structure for addtl ligands


6. On the first tab, we have Import and Process. We have the option of also including the diffraction data, biological unit, and alternate positions. These are often useful for validating the quality of the structure, but here we will not be using them.

   Click the boxes to select the following options:

   - Assign bond orders:							assigns whether each bond is a single or double bond
   - Add Hydrogens: 								hydrogens are not resolved, so we have to add them back
   - Remove original hydrogens: 					delete any resloved hydrogens from the X-ray structure
   - Create disulfide bonds:
   - Convert selenomethionines to methionines: 		Selenomethionine is used for phasing (not biologically relevant)
   - Fill in missing side chains using Prime:		this structure has both missing side chains and loops. Prime will fill them in.
   - Fill in missing loops using Prime:
   - Cap termini:
   - Delete waters...:								delete waters beyond 5 A, we will further filter later.


   Next, click preprocess. You should see a pop-up asking for a .fasta ..

   Prime will take a couple of minutes to run and the results will be incorporated into the Workspace automatically. After this is complete you can “View Problems”, “Protein Reports”, and the “Ramachandran Plot”, these tools give you an idea of what potential issues to lookout for when preparing your structure.

   TODO: Image of Import and process pane of prep wizard

   TODO: Image Ramachandran Plot


4. We can now move on to the next tab, Review and Modify. First click on Analyze Workspace, Maestro will take a second to load up all waters and other ligands (metals, inhibitors etc). In this pane, we can manually inspect each water or ligand to determine whether or not to modify or delete it. For this protein, we need to generate states for the inhibitor. Click the line for the inhibitor and Generate States for pH 7.0 +/- 3.0. This will take the ligand and generate a couple of possible protonation states. When the generation is complete, you can view the structures of each state in the Workspace.

{% include links.html %}
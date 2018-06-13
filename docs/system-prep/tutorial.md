---
title: "Preparing Your System for Molecular Dynamics (MD)"
permalink: /system-prep/tutorial
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

   Before proceeding, make sure only the following options are selected:

   - Assign bond orders:						assigns whether each bond is a single or double bond
   - Use CCD database:                    look up information about the bound inhibitor to make sure it gets modeled correctly
   - Add Hydrogens: 								hydrogens are not resolved, so we have to add them back
   - Remove original hydrogens: 					delete any resloved hydrogens from the X-ray structure
   - Create disulfide bonds:
   - Convert selenomethionines to methionines: 		Selenomethionine is used for phasing (not biologically relevant)
   - Fill in missing side chains using Prime:		this structure has both missing side chains and loops. Prime will fill them in.
   - Fill in missing loops using Prime:
   - Cap termini:
NO   - Generate het states using Epik:  pH 7.0 +/- 3.0   : use protonation states that might really be present at a cell-like pH


   Next, click Preprocess. You should see a pop-up asking for a .fasta ..

   Prime will take a couple of minutes to run and the results will be incorporated into the Workspace automatically. After this is complete you can “View Problems”, “Protein Reports”, and the “Ramachandran Plot”, these tools give you an idea of what potential issues to lookout for when preparing your structure.

   TODO: Image of Import and process pane of prep wizard

![Ramachandran Plot](https://github.com/ctlee/BioChemCoRe-2018/blob/master/docs/images/system-prep/ramaPlot.png "Figure 1: An example Ramachandran plot")

Figure 1: An example Ramachandran plot


7. We can now move on to the next tab, Review and Modify. First click on Analyze Workspace, Maestro will take a second to load up all waters and other ligands (metals, inhibitors etc). In this pane, we can manually inspect each water or ligand to determine whether or not to modify or delete it. 

### As we are only going to run one system per ligand, I'm not sure if we need multiple pH states for the ligand.
For this protein, we need to generate states for the inhibitor. Click the line for the inhibitor and Generate States for pH 7.0 +/- 3.0. This will take the ligand and generate a couple of possible protonation states. When the generation is complete, you can view the structures of each state in the Workspace.


8. Move onto the final tab of the Workflow, Refine. Here under H-bond assignment to Sample Water Orientations, as well as to use PROPKA to assign the protonation states of each residue. Click optimize…

![Maestro Protein Prep Refine Tab](https://github.com/ctlee/BioChemCoRe-2018/blob/master/docs/images/system-prep/proteinRefine.png "Figure 8. The Refine tab contains options for hydrogen bond assignment, pKa prediction, and minimization.")

Figure 8. The Refine tab contains options for hydrogen bond assignment, pKa prediction, and minimization.

After optimization is complete, remove all waters will fewer than 2 H-bonds to non-waters and perform a restrained minimization with the default RMSD of 0.30 A. This removes all waters which are not interacting substantially with the protein, and relaxes the structure in preparation for MD. Each step will create a new entry in the Entry List. Make sure you're using the lastest entry before you move forward through each step.

9. First, let’s try to assign parameters to the resulting pdb using the Amber forcefield 14SB. Parameterization requires a lot of technical expertise, and can be one of the most frustrating parts of setting up an MD simulation. 

First we must load amber into our work environment, in the terminal type:

```module load amber```

10. xleap and tleap are the utilities provided by Amber for system setup. Today we will be using the terminal-based version of leap (tleap). Simply type “tleap” in the terminal. A new program will pop up in the terminal. Type “help” to show lists of available commands.

Into this prompt type the following commands:
```source leaprc.ff14SB
pdb=loadpdb 1sj0_maestro.pdb 
```

At this point you will see a bunch of error messages pop up!

```Loading PDB file: ./0YDD5_maestro.pdb
Unknown residue: NMA   number: 209   type: Terminal/last
..relaxing end constraints to try for a dbase match
  -no luck
Unknown residue: 99B   number: 210   type: Terminal/beginning
..relaxing end constraints to try for a dbase match
  -no luck
Created a new atom named: H within residue: .R<ACE 16>
Created a new atom named: H1 within residue: .R<VAL 17>
Created a new atom named: HD1 within residue: .R<HIE 189>
Creating new UNIT for residue: NMA sequence: 225
One sided connection. Residue:  missing connect0 atom.
Created a new atom named: N within residue: .R<NMA 225>

...
```

These errors are popping up because the force field “ff14SB” does not contain types for several of these molecules. 

There are three classes of errors here:
1) AMBER has a built-in forcefield for proteins (and a few other molecules) called FF14SB. This expects each protein atom to have a residue and atom name which perfectly matches what it expects. However, Maestro has different names for a few of these.
2) We capped the termini of the protein so it wouldn't have charged groups hanging out at the beginning and end of the amino acid chain. While real proteins do have these charged groups hanging out at their N- and C-termini, we're missing amino acids from the beginning and end, so there shouldn't really be a charge there. We use "caps" to add a small, neutral group to the termini of the chains to prevent there from being a charge. This is important, because +1 and -1 charges make a big difference on an atomic scale.
3) We have this non-protein molecule (the ligand) in the mix. AMBER has never seen this thing before, so it has no clue how to parameterize it.

At this point, exit out of tleap to resolve these problems. We will return later to try to setup the simulation once things are resolved. Open the PDB file in a text editor. 

11. **First, the capping groups.** The caps are the first and last "residues" in the protein. They're not really amino acids, just little groups that were stuck on the ends, but PDB files require everything to have a residue number. It's a real pain in the neck to rename all the atoms in a capping group, so let's not. Tleap is clever and will reconstruct any atoms that it knows should be there, so let's just leave in one atom from each cap and let tleap do the rest. In the ACE cap, delete all the atoms except the one named "C". Then, scroll down to the end of the chain and delete all the NMA atoms except the "N". Also, FF14SB calls it NME instead of NMA, so change that too. Save the current file with a new name, replacing "_maestro" with "fixedCaps".

11. **Now let's take care of the histidines.** First let’s open up the structure in vmd. Open up the Tinker Console by going to `Extensions > Tk Console`. Execute the following command which selects the alpha carbons of all residues which have the namd HIS, it then gets the residue ID’s for our convenience.

`[atomselect top “resname HIS and alpha”] get resid`

We can then go to Graphics-Graphical Representations and go through each of the histidines to assign it’s state. Shown in Figure 10 is an example of how to view an individual histidine. The zoom in the main window can be set using the = key.

![VMD view of a histidine](https://github.com/ctlee/BioChemCoRe-2018/blob/master/docs/images/system-prep/vmdHisView.png "Figure 10. VMD view of a histidine. This instance should be named HID.")

Figure 10. VMD view of a histidine. This instance should be named HID.


![VMD view of a histidine](https://github.com/ctlee/BioChemCoRe-2018/blob/master/docs/images/system-prep/hisProtNames.png "Scheme 1. The Amber residue naming convention for the various histidine connectivities.")

Scheme 1. The Amber residue naming convention for the various histidine connectivities.

Visually inspect and compare with Scheme 1 to determine what the name of each histidine should be. Then go to the appropriate atoms in your PDB file and change the HIS label to what it should be.


NOTE: How much easier would this be if you could write a script to parse each residue automatically?!?

12. When done, save the coordinates to a new PDB file “1sj0_leap.pdb”. Open up this new file in your favorite text editor (i.e., gedit). Scroll to the last residue ALA 551, and delete the line containing HXT. Amber expects terminal alanines, resname CALA, to contain an atom OXT which maestro does not generate, we will use xleap to add it for us based upon optimal geometry. Save the file. 


{% include links.html %}

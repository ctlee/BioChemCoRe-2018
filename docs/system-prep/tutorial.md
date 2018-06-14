---
title: "Preparing Your System for Molecular Dynamics (MD)"
permalink: /system-prep/
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
for protein stability and receptor-ligand interactions, X-ray crystal
structures cannot be used used in molecular dynamics (MD) right “off the
shelf”. To help resolve this and many other issues, a variety of software
tools have been developed.

## Looking at the Crystal Structure

1. **Visualize this structure** by loading it in PyMol; replacing "my_protein_name"
with the appropriate filename for your structure.

```
module load pymol
pymol my_protein_name.pdb
```

TODO: image of HSP90 Structure


2. **Take some time to examine the structure.** Can you locate the inhibitor molecule?
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

5. **Cut your structure down to the desired length.** With chain A selected, go to `Tasks`  (in the top right) and open "Multiple Sequence Viewer" by searching. This window shows the sequence of your loaded protein highlighted in dark letters. If there's additional data in the pdb file about unresolved residues, there may be some light shaded letters as well.

In the MSA window, click on `File > Import Sequence`. Then go one directory up and load HSP90.fasta. Ensure that the loaded sequence begins with "VETFA" and ends with "TLFVE". Now, click the "Pairwise Alignment" button, which looks like two blue arrows going opposite directions. This will align the protein sequences.

Do you have any dark-shaded residues extending past the beginning or end of the reference sequence? If so, go to the sequence view at the bottom of the main Maestro window, and right-click any overhanging residues, then click "Delete"

6. With Chain A selected, click the "Protein Preparation" button in the top bar. This will open up the Protein Preparation workflow tab.

7. On the first tab, we have Import and Process. We have the option of also including the diffraction data, biological unit, and alternate positions. These are often useful for validating the quality of the structure, but here we will not be using them.

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


   Next, click Preprocess. You should see a pop-up asking for a .fasta. Click "Yes". Just like when we did the sequence alignment, go up one directory and select HSP90.fasta. This will tell Maestro how to fill in missing residues and atoms.

   Prime will take a couple of minutes to run and the results will be incorporated into the Workspace automatically. You can monitor the progress of these jobs by clicking on the "Jobs" tab on the top right of the main window. Preprocessing will notify you that the results have been incorporated when it's done.

   After this is complete you can “View Problems”, “Protein Reports”, and “Ramachandran Plot”, these tools give you an idea of what potential issues to lookout for when preparing your structure.

{% include image.html file="/system-prep/ramaPlot.png" alt="Ramachandran Plot" caption="Figure 1: An example Ramachandran plot" width-percent=30 %}

8. We can now move on to the next tab, Review and Modify. First click on Analyze Workspace, Maestro will take a second to load up all waters and other ligands (metals, inhibitors etc). In this pane, we can manually inspect each water or ligand to determine whether or not to modify or delete it. You should keep the waters and the inhibitor in the active site, but delete any other small molecules that are around.

9. Move onto the final tab of the Workflow, Refine. Here under H-bond assignment select Sample Water Orientations, as well as Use PROPKA to assign the protonation states of each residue. Click optimize.

{% include image.html file="/system-prep/proteinRefine.png" alt="Maestro Protein Prep Refine Tab" caption="Figure 8. The Refine tab contains options for hydrogen bond assignment, pKa prediction, and minimization." %}

After optimization is complete, remove all waters will fewer than 2 H-bonds to non-waters and perform a restrained minimization with the default RMSD of 0.30 A. This removes all waters which are not interacting substantially with the protein, and relaxes the structure in preparation for MD. Each step will create a new entry in the Entry List. Make sure you're using the lastest entry before you move forward through each step.

Finally, look at your protein structure in the main window. We're going to save the whole system first, then we're going to save the ligand in a separate file.

To save the whole system, right click the minimized entry in the Entry List and select `Export > Structures`, then save this as `<your protein name>_maestro.pdb`.

To save the ligand, go to the Structure Hierarchy listing below the Entry List. Expand the object corresponding to your final prepared protein, then Expand "Ligands", and right click the ligand and select "Copy to New Entry". You should learn your ligand's 3-character name. View just the ligand by itself. Make sure that Maestro is in residue selecting mode (There will be a big "R" in the top left corner of the screen). Then, click on your ligand to select it. In the bottom center of the screen, there should be a 3-character code. **That is your ligand's name - Write it down!** Now, right click on the new entry (should be called "Structure##") in the Entry List and select `Export > Structures`. Save this as `<your ligand name>_maestro.mol2`.

Before leaving Maestro,

<!-- Also, this is the time to determine the net charge on your ligand. View just the ligand by itself. Make sure that Maestro is in residue sleecting mode (There will be a bit "R" in the top left corner of the screen). Then, click on your ligand to select it. The net charge should be shown at the bottom of the screen next to the word "Charge". For most of you this should be 0, but write it down just in case. -->

10. First, let’s try to assign parameters to the resulting whole system pdb using the Amber forcefield "FF14SB". Parameterization requires a lot of technical expertise, and can be one of the most frustrating parts of setting up an MD simulation.

First we must load amber into our work environment, in the terminal type:

```module load amber```

11. tleap is a utility provided by Amber for system setup. Simply type `tleap` in the terminal. A new program will pop up in the terminal. Type “help” to show lists of available commands.

Into this prompt type the following commands (Note that my protein file is called "1sj0_maestro.pdb" in this tutorial -- Yours will have a different name):
```
source leaprc.protein.ff14SB
source leaprc.water.tip4pew
pdb=loadpdb 1sj0_maestro.pdb
```

At this point you will see a bunch of error messages pop up!

```
Loading PDB file: ./1sj0_maestro.pdb
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
3) We have this non-protein molecule (the ligand) in the mix. AMBER has never seen this thing before (it's not in FF14SB), so it has no clue how to parameterize it. We'll have to determine the charges on these atoms (because that's what will determine most of its interactions), and then we can use generic parameters for the bonds (the Generalized Amber Force Field, or GAFF).

At this point, let's exit out of tleap to resolve these problems. We will return later to try to setup the simulation once things are resolved.

In the tleap terminal, type `quit`.

12. **First, the capping groups.** Open the PDB file in a text editor. The caps are the first and last "residues" in the protein. They're not really residues/amino acids, just little groups that were stuck on the ends, but PDB files require everything to have a residue number. It's a real pain in the neck to rename all the atoms in a capping group, so let's not. Tleap is clever and will reconstruct any atoms that it knows should be there, so let's just leave in the important atoms from each cap and let tleap do the rest.
  * In the ACE ("acetyl") cap, delete all the atoms except the ones named "C", "O", and "CH3".
  * In Val17, delete H1 if it's there
  * Then, scroll down to the end of the chain to NMA ("N-methyl amide"). Change "CA" to "CH3" (delete a space afterwards to make the columns line up.
  * Then delete all the NMA atoms except "N" and "CH3".
  * Also, FF14SB calls it NME instead of NMA, so change that too. Save the current file with a new name, replacing "_maestro" with "_fixedCaps".

13. **Now let's take care of the histidines.** A histidine sidechain can have three protonation states. Maestro already did the calculation to figure out where the hydrogen on each histidine sidechain should be, but it didn't name them in the way that AMBER/FF14SB wants. We'll need to look at each one by eye. First let’s open up the structure in vmd. Open up the Tinker Console by going to `Extensions > Tk Console`. Execute the following command which selects the alpha carbons of all residues which have the namd HIS, it then gets the residue ID’s for our convenience.

`[atomselect top “resname HIS and alpha”] get resid`

We can then go to `Graphics > Graphical Representations` and go through each of the histidines to assign it’s state. Shown in Figure 10 is an example of how to view an individual histidine. The the main window can be reoriented on the visible atoms using the `=` key.

{% include image.html file="/system-prep/vmdHisView.png" alt="VMD view of a histidine" caption="Figure 10. VMD view of a histidine. This instance should be named HID." %}

{% include image.html file="/system-prep/hisProtNames.png" alt="HIS Protonation Names" caption="Scheme 1. The Amber residue naming convention for the various histidine connectivities." max-width=500 %}

Visually inspect and compare with Scheme 1 to determine what the name of each histidine should be. Then go to the appropriate atoms in your PDB file and change the HIS label to what it should be ("HID", "HIE", or "HIP").

{% include note.html content="How much easier would this be if you could write a script to do this automatically?!?" %}


When done, save the coordinates to a new PDB file with "fixedCaps" replaced by "namedHises".

14. **Singling out the ligand for special treatment** The next step is to prepare the ligand for simulation. Here we use the AMBER utility "antechamber" to run an AM1-BCC semi-empirical quantum mechanics calculation to determine partial charges. The ligand used in this example is "e4d.pdb", but yours will have a different name.

Does your ligand have a net charge? This is imporant!
# Note: Students need to know how to see if there's a net ligand charge here

With the ligand pdb, we are now ready to run the calculation
`antechamber -i e4d.pdb -fi pdb -o e4d.in -fo prepi -c bcc -nc 1`

In english, these arguments mean:

```
-i		input file
-fi 		input format
-o		output file
-fo		output format
-c 		calculation type here AM1-BCC
-nc		net charge +1 (e4d has a protonated amide)
```

Once the program completes, execute the following command to parse the prepi file to generate a frcmod.

```
parmchk -i e4d.in -o e4d.frcmod -f prepi -a Y
```

A frcmod file is an Amber forcefield supplementary file defining the various parameters. It’s just a normal text file, try to open it with your favorite text editor (`gedit e4d.frcmod`). We will need the e4d.in and e4d.frcmod files in the next step.


# Molecular Dynamics with pmemd.cuda

14. At this point, we should have resolved the previously encountered issues. Let’s try running everything through tleap again.

`tleap`

Comments are shown after the !, do not type this.
```
source leaprc.protein.ff14SB
source leaprc.gaff				! needed for ligand parms
source leaprc.water.tip4pew                     ! needed for water params
loadamberprep e4d.in				! from antechamber
loadamberparams e4d.frcmod			! also from antechamber
pdb=loadpdb 1sj0_leap.pdb
```

At this point, the pdb should load without any errors and tleap should add in any extra necessary atoms for you. **Have your mentor ensure that the above steps loaded the protein correctly.** If there are no issues, please proceed with the following.

First, we determine if the system has a net charge, and how many ions we'll need to counterbalance it.

`charge pdb`

This command will tell you the net charge of the system. To simulate being in cytoplasm, we will add some ions (cells are kinda salty). These atoms will be Na+ and Cl-. Add 50 or 51 ions to neutralize your system. For example, if your system has a net charge of -3, add 17 Na ions and 14 Cl- ions.

```
	solvateBox pdb TIP4PEWBOX 10		! solvate with 10 A buffer
	addions2 pdb Na+ ##			! How many positive charges should you add? I had to add 17 (see above)
	addions2 pdb C- ##			! How many negative charges should you add? I had to add 14 (see above)
	charge pdb
```
Check your ion math by making sure the resulting charge is 0.

```
	saveamberparm pdb system.prmtop system.inpcrd
	savepdb pdb 1sj0_forMd.pdb
	quit
```

15. We are now ready to run the simulation. The Amaro group has developed a set of default simulation parameters which we will be using. They can be downloaded from the following link.
https://dl.dropboxusercontent.com/u/2781671/defaultMD.tgz

The tarball tgz or tar.gz file can be extracted using the following command. Be sure to extract it to your personal scratch folder on your machine (/scratch/[username]).
	`tar -xvf defaultMD.tgz`

16. After extracting, we need to define a couple of files, one defining the ligand, and one for the protein. The bash script replace.sh uses these files to fill in wildcards in the amber.in files. Make  a file named USR_LIG which contains your ligand residue name (mine is “E4D”), also make a file USR_PRO which contains “16-224” (the residue numbers of the protein residues). Then execute the following bash script
	`./replace.sh`

19. Locate the files system.inpcrd and system.prmtop which were previously generated by xleap. Copy them into your /scratch/username/defaultMD directory. We are now ready to run molecular dynamics. We have included a convenience script which will execute pmemd.cuda for each of the inputs.
	`./runme.sh`

You can watch the progress of the calculations by executing this command which will write out the contents of the mdinfo file every 2 seconds.
	`watch cat mdinfo`

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

**Why do we need to go through system setup for MD?**

Protein structures from various structural determination methods often are not
complete. For example, structures from x-ray crystallography typically do not
have resolved protons. Take a second and research why x-ray 
crystallography does not provide the positions of protons. Write your
answer in your notebook.

(It's normal to use "proton" and "hydrogen" interchangeably 
in this field. If we were instead nuclear physicists, "proton" could refer to 
either hydrogen nuclei or a component of, for example, a carbon nucleus. 
But we aren't nuclear physicists, so here "proton" just means "hydrogen").

Given the importance of hydrogen bonding, which requires proton participation,
for protein stability and receptor-ligand interactions, X-ray crystal
structures cannot be used used in molecular dynamics (MD) right “off the
shelf”. To help resolve this and many other issues, a variety of software
tools have been developed.

## Getting the Files

Download the files corresponding to your assigned system from the [BioChemCoRe Protein Data Bank]({{ '/pdbs/' | prepend: site.baseurl }}) and place them in your personal `/scratch/username` directory.

The tarball tgz or tar.gz file can be extracted using the following command. Be sure to extract it to your personal scratch folder on your machine (`/scratch/[username]`).

{% include note.html content="You can extract the contents of tarballs using the following command: `tar -xvf protein_name.tgz`" %}


## Protein Preparation Workflow

1. One tool of extreme utility is [Maestro](http://www.schrodinger.com/Maestro/). It acts as a molecular visualizer, and a workflow starting point for many of Schrodinger’s tools. Today we will be using the Protein Preparation workflow to clean up our structure. To load the Schrodinger toolkits, in Keck II issue the command and run maestro:

   ```
   module load schrodinger
   maestro
   ```

2. Next, load your pdb file.

   ```File > Import Structures```

   After importing, the Workspace will show a representation of our protein. Using the left mouse button allows you to select residues or areas, middle mouse rotates the view, and the right mouse button translates.

3. **Take some time to examine the structure.** Can you locate the inhibitor molecule?
Are there any crystallographic waters present?


TODO: image of HSP90 Structure


3. HSP90 is a dimer, which means it may have multiple chains.
On the bottom center of the Maestro window, look for the info table entry for "CHAINS." If there are multiple chains, separate them by right clicking on the structure name in the left pane and selecting:

   ```Split > By Chain```

4. Once split, each chain will show up in the "Entry List" pane on the left. Select chain A by clicking the blue dot.

5. Open the sequence viewer pane `Window > Sequence Viewer`. Now you should see the one letter amino acid codes for your protein sequence at the bottom of the screen.

5. **Cut your structure down to the desired length.** With chain A selected, go to `Tasks`  (in the top right) and open "Multiple Sequence Viewer" by searching. This window shows the sequence of your loaded protein highlighted in dark letters. If there's additional data in the pdb file about unresolved residues, there may be some light shaded letters as well.

In the MSA window, click on `File > Import Sequence`. Then go one directory up and load HSP90.fasta. Ensure that the loaded sequence begins with "VETFA" and ends with "TLFVE". Now, click the "Pairwise Alignment" button, which looks like two blue arrows going opposite directions. This will align the protein sequences.

Do you have any dark-shaded residues extending past the beginning or end of the reference sequence? If so, return to the main Maestro window and open the sequence viewer (`Window > Sequence Viewer`). Then go to the sequence view at the bottom of the window, and right-click any overhanging residues you observed and click "Delete."

If you have deleted any C-terminal residues, there may be an additional nitrogen that was not deleted. Right click on this nitrogen in the structure (if it exists) and delete it.

Your structure should contain only Chain A, your ligand, and waters. If you have any extra solvents right click and delete them.

**Have a mentor check your structure!**

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

9. Move onto the final tab of the Workflow, Refine. Here under H-bond assignment select Sample Water Orientations, as well as Use PROPKA pH: 7.0 to assign the protonation states of each residue. Click optimize.

{% include image.html file="/system-prep/proteinRefine.png" alt="Maestro Protein Prep Refine Tab" caption="Figure 8. The Refine tab contains options for hydrogen bond assignment, pKa prediction, and minimization." %}

After optimization is complete, remove all waters with fewer than 2 H-bonds to non-waters and perform a restrained minimization with the default RMSD of 0.30 A. Make sure the "Hydrogens only" box is **NOT** checked. This removes all waters which are not interacting substantially with the protein and relaxes the structure in preparation for MD. Each step will create a new entry in the Entry List. Make sure you're using the lastest entry before you move forward through each step.

**Have your mentor check your structure again!**

Finally, look at your protein structure in the main window. We're going to save the whole system first, then we're going to save the ligand in a separate file.

To save the whole system, right click the minimized entry in the Entry List and select `Export > Structures`, then save this as `<your protein name>_maestro.pdb`.

To save the ligand, go to the Structure Hierarchy listing below the Entry List. Expand the object corresponding to your final prepared protein, then Expand "Ligands", and right click the ligand and select "Copy to New Entry". View just the ligand by itself (should be called "Structure##") in the Entry List.

You should learn your ligand's 3-character name.  Make sure that Maestro is in residue selecting mode (There will be a big "R" in the top left corner of the screen). Then, click on your ligand to select it. In the bottom center of the screen, there should be a 3-character residue code. **That is your ligand's name - Write it down!** Also, note the charge of the ligand which is visible in the bottom pane when the mouse is not over any atoms. **This is your ligand's charge - Also write this down!**

In the entry list, right click on the ligand entry and select `Export > Structures`. Save this as `<your ligand name>_maestro.mol2`.


<!-- Also, this is the time to determine the net charge on your ligand. View just the ligand by itself. Make sure that Maestro is in residue sleecting mode (There will be a bit "R" in the top left corner of the screen). Then, click on your ligand to select it. The net charge should be shown at the bottom of the screen next to the word "Charge". For most of you this should be 0, but write it down just in case. -->

10. First, let’s try to assign parameters to the resulting whole system pdb using the Amber forcefield "FF14SB". Parameterization requires a lot of technical expertise, and can be one of the most frustrating parts of setting up an MD simulation.

First we must load amber into our work environment, in the terminal type:

```module load amber/18```

11. tleap is a utility provided by Amber for system setup. Simply type `tleap` in the terminal. A new program will pop up in the terminal. Type “help” to show lists of available commands.

Into this prompt type the following commands (Note that my protein file is called "protein_name_maestro.pdb" in this tutorial -- Yours will have a different name):
```
source leaprc.protein.ff14SB
source leaprc.water.tip4pew
pdb=loadpdb protein_name_maestro.pdb
```

At this point you will see a bunch of error messages pop up!

```
Loading PDB file: ./protein_name_maestro.pdb
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
  * Also, FF14SB calls it NME instead of NMA, so change that too.
  * After the end of the protein, the next entry is the ligand. The residue name should correspond with the name you wrote down from Maestro. If your ligand has a "CL" atom, you will need to rename it to "Cl" (change the L to lowercase). 
  * Save the current file with a new name, replacing "_maestro" with "_fixedCaps".

13. **Now let's take care of the histidines.** A histidine sidechain can have three protonation states. Maestro already did the calculation to figure out where the hydrogen on each histidine sidechain should be, but it didn't name them in the way that AMBER/FF14SB wants. We'll need to look at each one by eye. If you closed the window already, reopen your final structure in Maestro.

{% include image.html file="/system-prep/hisProtNames.png" alt="HIS Protonation Names" caption="Scheme 1. The Amber residue naming convention for the various histidine connectivities." max-width=500 %}


Our HSP90 system has four histidines. Visually inspect each and compare with Scheme 1 to determine what the name of each histidine should be. To center the view on a specific histidine, middle click on its one letter code in the sequence viewer pane. Then go to the appropriate atoms in your PDB text file and change the "HIS" label to what it should be ("HID", "HIE", or "HIP").

{% include note.html content="How much easier would this be if you could write a script to do this automatically?!?" %}


When done, save the coordinates to a new PDB file with "fixedCaps" replaced by "fixedCapsHises".

14. **Singling out the ligand for special treatment** The next step is to prepare the ligand for simulation. Here we use the AMBER utility "antechamber" to run an AM1-BCC semi-empirical quantum mechanics calculation to determine partial charges. The ligand used in this example is "e4d.pdb", but yours will have a different name.

Does your ligand have a net charge? This is imporant! Change the "-nc" argument below to match.


With the ligand pdb, we are now ready to run the calculation
```antechamber -i ligand_name.mol2 -fi mol2 -o ligand_name.in -fo prepi -c bcc -nc ##```

In english, these arguments mean:

```
-i		input file
-fi 		input format
-o		output file
-fo		output format
-c 		calculation type here AM1-BCC
-nc		net charge (the charge you wrote down for your ligand)
```

Once the program completes, execute the following command to parse the prepi file to generate a frcmod.

```
parmchk -i ligand_name.in -o ligand_name.frcmod -f prepi -a Y
```

A frcmod file is an Amber forcefield supplementary file defining the various parameters. It’s just a normal text file, try to open it with your favorite text editor (`gedit ligand_name.frcmod`). We will need the e4d.in and e4d.frcmod files in the next step.


# Molecular Dynamics with pmemd.cuda

14. At this point, we should have resolved the previously encountered issues. Let’s try running everything through tleap again.

`tleap`

Comments are shown after the !, do not type this.
```
source leaprc.protein.ff14SB
source leaprc.gaff				! needed for ligand parms
source leaprc.water.tip4pew                     ! needed for water params
loadamberprep ligand_name.in			! from antechamber
loadamberparams ligand_name.frcmod		! also from antechamber
pdb=loadpdb protein_name_fixedCapsHises.pdb
```

At this point, the pdb should load without any errors and tleap should add in any extra necessary atoms for you. **Have your mentor ensure that the above steps loaded the protein correctly.** If there are no issues, please proceed with the following.

First, we determine if the system has a net charge, and how many ions we'll need to counterbalance it. In tleap type:

`charge pdb`

This command will tell you the net charge of the system. To simulate being in cytoplasm, we will add some ions (cells are kinda salty). These atoms will be Na+ and Cl-. Add 50 or 51 ions to neutralize your system. For example, if your system has a net charge of -3, add 27 Na ions and 24 Cl- ions.

```
	solvateBox pdb TIP4PEWBOX 10		! solvate with 10 A buffer
	addions2 pdb Na+ ##			! How many positive charges should you add? I had to add 17 (see above)
	addions2 pdb Cl- ##			! How many negative charges should you add? I had to add 14 (see above)
```
Check your ion math by making sure the resulting charge is 0. Again, type in tleap:
```
	charge pdb
```

If it's 0, then continue on.


```
	saveamberparm pdb protein_name.prmtop protein_name.inpcrd
	savepdb pdb protein_name_leap.pdb
	quit
```

15. We are now ready to run the MD simulation. The Amaro group has developed a set of default simulation parameters which we will be using. These can be found in the folder with your protein.


19. Locate the files protein_name.inpcrd and protein_name.prmtop which were previously generated by tleap and copy them into the "md" directory. **Make sure you are working in a subdirectory of /scratch/your username/.** We are now ready to run molecular dynamics. We have included a convenience script which will execute pmemd.cuda for each of the inputs.
	`./runme.sh`

{% include warning.html content='"CUDA" is the interface to running calculations on graphics cards. Since your machine only contains one high-performance graphics card, you will only be able to run one simulation at a time.' %}

You can watch the progress of the calculations by executing this command which will write out the contents of the mdinfo file every 2 seconds.
	`watch -n 2 cat mdinfo`

Use `Ctrl-C` to exit out of `watch` when you are done.

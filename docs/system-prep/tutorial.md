---
title: "Preparing Your System for Molecular Dynamics (MD)"
permalink: /system-prep/tutorial

summary: In this tutorial you will learn how to setup your system to begin running molecular dynamics in Amber. As a part of this tutorial you will be introduced to the use of Schrödinger's Maestro software for protein preparation followed by parameterization using AmberTools Antechamber.
---




At this point, you should
have been given a PDB file containing your system of interest from the
BioChemCoRe teaching team. If you did not, please let us know now.

## Motivation

Why do we need to go through system setup for MD?

Protein structures from various structural determination methods often are not
complete. For example, structures from x-ray crystallography typically do not
have resolved protons. Take a second and research why this is. Write your
answer in your notebook.

Given the importance of hydrogen bonding, which requires proton participation,
to protein stability and receptor-ligand interactions, X-ray crystal s
tructures cannot be used used in molecular dynamics (MD) right “off the
shelf”. To help resolve this and many other issues, a variety of software
tools have been developed.

{% include links.html %}
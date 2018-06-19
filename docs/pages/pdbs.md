---
layout: page
title: "BioChemCoRe HSP90s"
permalink: /pdbs/
summary: Here is a list of PDBs and FASTAs which will be used in the program.
sidebar: 'pdbs_sidebar'
---

## Files

<h3>All Systems: <a href="{{ '/assets/pdbs/all.tgz' | prepend: site.baseurl }}">all.tgz</a></h3>
This tarball contains the structures and MD setup files for all of the BioChemCoRe systems.

<h3>Reference FASTA: <a href="{{ '/assets/pdbs/HSP90.fasta' | prepend: site.baseurl }}">HSP90.fasta</a></h3>

This FASTA files contains the reference sequence for all of your systems. After system preparation your sequence should be the same as the one provided here!

<h3>bccHelper.py: <a href="{{ '/assets/pdbs/bccHelper.py' | prepend: site.baseurl }}">bccHelper.py</a></h3>

This python library contains useful list and dictionary definitions to help you automate your tasks. A version of this script is also already bundled with the 'all.tgz' and 'BCC_ID.tgz' tarballs.

<br/><br/>

<table id="pdbtable">
  <tr>
    <th>BCC ID:</th>
    <th>LIG ID:</th>
    <th>IC50 (nM):</th>
    <th>Tarfile:</th>
    <th>PDB:</th>
  </tr>
{% for pdb in site.pdbs %}
  <tr>
    <td><a href="{{ pdb.title }}">{{ pdb.title }}</a></td>
    <td>{{ pdb.ligand }}</td>
      {% if pdb.set == 'Training' %}
        <td>{{ pdb.IC50 }}</td>
      {% else %}
        <td>-</td>
      {% endif %}
    <td><a href="{{ site.baseurl }}/assets/pdbs/{{ pdb.title }}.tgz">{{ pdb.title }}.tgz</a></td>
    <td><a href="{{ site.baseurl }}/assets/pdbs/{{ pdb.title }}/{{ pdb.title }}.pdb">{{ pdb.title }}.pdb</a></td>
  </tr>
{% endfor %}
</table>
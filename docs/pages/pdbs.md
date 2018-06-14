---
layout: page
title: "BioChemCoRe HSP90s"
permalink: /pdbs/
summary: Here is a list of PDBs and FASTAs which will be used in the program.
sidebar: 'pdbs_sidebar'
---

## Files

<h3>All Systems: <a href="{{ '/assets/pdbs/all.tgz' | prepend: site.baseurl }}">all.tgz</a></h3>

<h3>Reference FASTA: <a href="{{ '/assets/pdbs/HSP90.fasta' | prepend: site.baseurl }}">HSP90.fasta</a></h3>

<br/><br/>

<table id="pdbtable">
  <tr>
    <th>BCC ID:</th>
    <th>LIG ID:</th>
    <th>Tarfile:</th>
    <th>PDB:</th>
  </tr>
{% for pdb in site.pdbs %}
  <tr>
    <td><a href="{{ pdb.title }}">{{ pdb.title }}</a></td>
    <td>{{ pdb.ligand }}</td>
    <td><a href="{{ site.baseurl }}/assets/pdbs/{{ pdb.title }}.tgz">{{ pdb.title }}.tgz</a></td>
    <td><a href="{{ site.baseurl }}/assets/pdbs/{{ pdb.title }}/{{ pdb.title }}.pdb">{{ pdb.title }}.pdb</a></td>
  </tr>
{% endfor %}
</table>
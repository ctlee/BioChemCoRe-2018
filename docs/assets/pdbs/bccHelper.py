# List of BioChemCoRe BCC IDs corresponding to structures
bccids = ['0YDD5', '6WCGO', 'A73SR', 'DJ1H3',
          'JHGSB', 'LLCXM', 'NEQSA', 'NIZGV',
          'NLSYQ', 'OVHRZ', 'TNRT6', 'VEH1I']

# Dictionary mapping BCCID to ligand residue name
bccid_to_lig = {
'TNRT6' : '05S',
'VEH1I' : '06H',
'NIZGV' : '2D9',
'DJ1H3' : '2DD',
'OVHRZ' : '99A',
'0YDD5' : '99B',
'NLSYQ' : 'B2K',
'NEQSA' : 'B2L',
'6WCGO' : 'PU1',
'A73SR' : 'PU2',
'JHGSB' : 'ZZ2',
'LLCXM' : 'ZZ3'
}

# Dictionary mapping BCCID to boolean representing if BCCID is in the
# training set or not.
# True  : in training set
# False : in test set
bccid_isTraining = {
'TNRT6' : True,
'VEH1I' : True,
'NIZGV' : False,
'DJ1H3' : False,
'OVHRZ' : True,
'0YDD5' : False,
'NLSYQ' : False,
'NEQSA' : True,
'6WCGO' : True,
'A73SR' : False,
'JHGSB' : False,
'LLCXM' : True
}

# Dictionary of BCCID to reported IC50s for training set systems
training_IC50 = {
'TNRT6' : 110,
'VEH1I' : 92,
'OVHRZ' : 81,
'NEQSA' : 6900,
'6WCGO' : 30000,
'LLCXM' : 350000
}
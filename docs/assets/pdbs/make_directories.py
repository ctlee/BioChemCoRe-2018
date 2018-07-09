import bccHelper as bcc
import os

#os.chdir('../')
os.mkdir('system_energy_analysis')
os.chdir('system_energy_analysis')
for keys, values in bcc.training_IC50.items():

    print(keys)

    md1=keys+'/md1'
    md2=keys+'/md2'
    md3=keys+'/md3'

    os.makedirs(keys)
    os.makedirs(md1)
    os.makedirs(md2)
    os.makedirs(md3)

import bccHelper as bcc
import os
import subprocess
import matplotlib.pyplot as plt
import numpy as np
import sys


path2data='/scratch/bcc2018_trajectories/'
#===========================================================
# if this flag is set to 1, energy plots will be prodcued
plt_flag = int( sys.argv[1] )

#===python dictionary to store our predicted ic50s
predicted_ic50={}

#======loop over all the ligands
for k in range(0, len(bcc.bccids) ):
    
   

    #===ensure the ligand has a measured ic50 for comparison
    if( not bcc.bccid_isTraining[ bcc.bccids[k] ] ):
        continue
    
    #====move to path of corresponding ligand MD folder
    path0= '../' + bcc.bccids[k]
    os.chdir(path0)
    

    #====variable storing the name of the AMBER production .out file
    trajectory_output= path2data + '/' + bcc.bccids[k] + '-Pro01.out'

    #====initialize energy value for avaeraging
    average_energy_triplicate= 0.0
    for a in range(1, 4):


        #===move into md1, md2, md3, etc...
        md_folder = 'md'+str(a)
        path1 = md_folder + '/'
        os.chdir(path1)

        #===make a directory to keep our data analysis files
        #===if this folder exists from a prior run. delete and make anew
        #===move into that directory
        subprocess.getoutput('rm -r DATA_ANALYSIS/')
        subprocess.getoutput('mkdir DATA_ANALYSIS')
        os.chdir('DATA_ANALYSIS/')


        #====run amaber analysis script to conver output file into time vs. energy file
        subprocess.getoutput('$AMBERHOME/bin/process_mdout.perl ../%s'%(trajectory_output) )
        
        #===load data into numpy array for averaging
        #===time is stored in first column
        #===energy is stroed in second column
        data = np.genfromtxt( 'summary.ETOT')

        #===check if energy is equilibrated
        if( plt_flag == 1):
            plt.scatter( data[:,0], data[:,1] )
            plt.xlabel('time (ps) ')
            plt.ylabel('energy (kcal/mol) ' )
            plt.show()



        #===calculate average energy and append to avaerage_energy_triplicate
        average_energy = np.mean( data[:,1] )
        average_energy_triplicate += average_energy

        #===make sure to move back up two directories!
        os.chdir('..')
        os.chdir('..')


    #====calculate the average ic50 over md1,md2,md3 folders
    average_energy_triplicate = average_energy_triplicate/3.0
    #====stored calculated energy in dictionary
    predicted_ic50[ bcc.bccids[k] ] = average_energy_triplicate





#=================================================
# want to plot measured ic50 vs predicted ic50
# look up measured ic50s from training_ic50 dictionary. store in measure_val 
# look up corresponding predicted ic50 for same ligand. stroe in predicted_val

measured_val = []
predicted_val = []
for key, value in bcc.training_IC50.items() :
    
    predicted = predicted_ic50 [ key ]

    print('we have the measured and predicted %s %s %s'%(key, value, predicted ) )
    measured_val.append( value )
    predicted_val.append( predicted ) 


#===make scatter plots!
plt.scatter( measured_val, predicted_val )
plt.xlabel('measured ic50' )
plt.ylabel('predicted ic50' )
plt.show()

    

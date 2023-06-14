#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:34:00 2020

@author: kate
"""
#Package imports
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
      
#GAMES imports
import Settings_COVID_Dx
from Solvers_COVID_Dx import calcRsq
from Run_COVID_Dx import solveAll
from Saving_COVID_Dx import createFolder
from Analysis_Plots import plotModelingObjectives123, plotModelingObjectives456, parityPlot, plot_all_states, plot_states_RHS

#Define settings
conditions_dictionary, initial_params_dictionary, data_dictionary = Settings_COVID_Dx.init()
full_path = conditions_dictionary["directory"]
model = conditions_dictionary["model"]
data = conditions_dictionary["data"]
error = data_dictionary["error"]
exp_data = data_dictionary["exp_data"]
timecourses_err = data_dictionary["timecourses_err"]
timecourses_exp = data_dictionary["timecourses"]
x = data_dictionary["x_vals"]
problem_free = conditions_dictionary["problem"]
bounds = problem_free['bounds']
df_data = pd.read_pickle('./PROCESSED DATA EXP.pkl')
df_error = pd.read_pickle('./PROCESSED DATA ERR.pkl')  
plt.style.use('/Users/kdreyer/Desktop/Github/PlantDX_GAMES/paper.mplstyle.py')
    

def testSingleSet(p):
    ''' 
    Purpose: Simulate the entire dataset for a single parameter set
        
    Inputs: 
        p: list of floats, each float corresponds to a parameter value 
            (length = # parameters in p_all). 
            Parameter labels and order defined in init() (in Settings.py)   
           
    Output: None
    
    Figures: FIT TO TRAINING DATA.svg - parity plot showing agreement between xperimental and simulated data
             Modeling objectives 123 sim.svg - histograms of summary metrics for simulations run with parameter set, p
             MODELING OBJECTIVE 4.svg - plot showing readout dynamics for the experimental and simulated data 
                 for the data set involved with modeling objective 4 (run with parameter set, p)
             MODELING OBJECTIVE 5.svg - plot showing readout dynamics for the experimental and simulated data 
                 for the data set involved with modeling objective 5 (run with parameter set, p)
             MODELING OBJECTIVE 6.svg - plot showing readout dynamics for the experimental and simulated data 
                 for the data set involved with modeling objective 6 (run with parameter set, p)
    '''
    
    os.chdir(full_path)
    sub_folder_name = './TEST'
    createFolder('./' + sub_folder_name)
    os.chdir('./' + sub_folder_name)
    
    doses, solutions, chi2, df_sim, df_all_states = solveAll(p, exp_data, 'all states')
    R_sq = calcRsq(solutions, exp_data)  
    # parityPlot(solutions, exp_data, data)
    
    #Plot modeling objectives
    # plotModelingObjectives123(solutions)
    # plotModelingObjectives456(df_sim)

    #Plot all model states ('ensemble' or 'slice')
    plot_all_states(df_all_states, 'mid', 'slice', '2 hours')
    plot_all_states(df_all_states, 'opt', 'slice', '2 hours')

    #Plot all states ODE RHS
    plot_states_RHS(df_all_states, 'mid', 'slice', p, '2 hours')
    plot_states_RHS(df_all_states, 'opt', 'slice', p, '2 hours')
    
    print('*******')
    print('R2: ' + str(np.round(R_sq, 3)))
    print('chi2: ' + str(np.round(chi2, 3)))
    print('*******')
    # print(df_all_states.at['target aCas13a-gRNA', str([5.0, 2.5, 0.005, 1, 90])])
    
#ensemble model params
# p = [0.00039, 17890.64388, 1392.99139, 0.08828, 79.9926, 2.11343, 6.74207] #use for CV       

#params from fitting to slice
p = [5.98681E-05,	721.1529526,	1360.727836,	0.385250686,	2.580973544,	58.85708085,	7.876468573]

testSingleSet(p)   


   



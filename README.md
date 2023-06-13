# PlantDX_GAMES

This repository contains supporting code for the Plant-DX modeling work. More details coming soon regarding how to conduct a test run of the code to produce results plots for the base case Plant-Dx model fit to a dataset from the COVID-Dx system. <br />

## PLANNED UPDATES <br />
this codebase is under construction to:
1. add an additional mechanism to the base case model, supported by data from the COVID-Dx system. <br />
2. refactor the model code into GAMESv2.0.0 from GAMESv1.0.1.<br />


## INITIAL SETUP ON YOUR DEVICE <br />
### macOS: <br />
1. install dependencies with your preferred package manager (I recommend conda--i.e. anaconda or miniconda-- or pip): <br />
- dependencies: <br />
python >=3.7 <br />
lmfit >=0.9.14 <br />
matplotlib >=3.1.3 <br />
numpy >=1.18.1 <br />
pandas >=1.0.5 <br />
salib >=1.3.8 <br />
scipy >=1.4 <br /> <br />
- install with conda: <br />
conda install <package_name> <br /> <br />
- install with pip: <br /> 
pip install <package_name> <br />
<br />

2. clone the repo with the http or ssh url (I usually recommend ssh, but http* is easier and does not require additional setup): <br />
- using the terminal (on macOS), cd into the directory in which you would like the repo to be cloned. To clone the repo into a directory with the *same* name as the repo, use one of the following options: <br /> <br />
- clone with http**: git clone https://github.com/leonardlab/PlantDX_GAMES.git <br /> <br />
*cloning with http requires that you login to your github account <br />
**to clone with ssh, use the ssh url instead of the http url. <br />
<br />

3. make results folder: <br />
in the directory of your local PlantDX_GAMES repo, make a new directory named "Results". Files from each run of the code will be saved there. <br />
 <br />

4. update the required paths in the code files to make them executable on your machine: <br />
The absolute file path for this folder must be updated in the file Saving.py.  <br /> Absolute paths may also need to be provided when importing REFERENCE TRAINING DATA.py and paper.mplstyle.py.
<br />

### windows: <br />
#### information based on GAMES v1.0 release: <br />
The parallelization component of this code was written using Python’s multiprocessing package, which has a different implementation on mac vs. windows OS. This code was run and tested on macOS and is *not* currently set up to support any other OS. <br />
However, GAMES v1.0.1 code was successfully run on Linux, and on Windows *without* parallelization. <br /> If you are a Windows user, we recommend setting parallelization = ‘no’ on line XXX in Run.py to use a version of the code that does not use parallelization. However, this particular model is not well suited to run without parallelization and there is a chance it is not feasible for parameter estimation (module 2) or parameter identifiability analysis (module 3).
 <br />

## TEST RUNNING THE CODE: <br />
### coming soon  <br />
___________________________________________________________________________________________________________________________________________________________________

Key information from GAMESv1.0 code release: <br />
This code is associated with the [Dray, K.E. et al. ACS Synthetic Biology manuscript] (https://pubs.acs.org/doi/10.1021/acssynbio.1c00528) "GAMES: A dynamic model development workflow for rigorous characterization of synthetic genetic systems".*
*please contact corresponding author J.N. Leonard for a copy of the manuscript if needed.

Detailed descriptions of the files and functions in this repository are included in the Supplementary Information (Supplementary Notes 2-3) of the manuscript. Simulation outputs associated with the manuscript are included as Supplementary Data 1. Test.py and Run.py are the executable files. Settings.py can be used to change the settings for different simulation runs.

After cloning the repository, the user must create a folder called "Results" - the code will automatically save all simulation outputs in this folder. The absolute file path for this folder must be updated in the file Saving.py. Absolute paths may also need to be provided when importing REFERENCE TRAINING DATA.py and paper.mplstyle.py.

WINDOWS USERS: The parallelization component of this code is written using Python’s multiprocessing package, which has a different implementation for Mac and Windows operating systems. This code was run and tested with a Mac OS and is not set up to support Windows users. If you are a Windows user, we recommend setting parallelization = ‘no’ on line 79 in Run.py to use a version of the code that does not use parallelization. This option can be used for modules 1 and 2, but not for module 3 due to computational efficiency limitations.

RELEASE NOTE v1.0.1: The previous release of this code included an incorrect standard error value to define the error distribution used to randomly add noise to data points, leading to a slightly smaller error distribution. This new release uses the appropriate value, which will slightly impact some figures relating to generation of PEM evaluation data and calculation of PPL thresholds. To reproduce the figures exactly as in the manuscript, please use the initial release of the code (v1.0.0).

PACKAGE VERSIONS: The GAMES code uses the following versions of each Python package and was not tested with other versions: python 3.7, lmfit 0.9.14, matplotlib 3.1.3, numpy1.18.1, salib 1.3.8, pandas 1.0.5, scipy 1.4

___________________________________________________________________________________________________________________________________________________________________
Outdated README info from COVID-Dx repo:

This code is associated with Chapter 3 of Kate Dray's PhD thesis (Northwestern University, Chemical Engineering) and follows the GAMES conceptual workflow (Dray et al. (2022). ACS Synthetic Biology). Since the completeion of this code, the GAMES code has been significantly refactored; the code presented here uses v1.1 of the GAMES software package (along with Python 3.7). Other package requirements can be found in the documentatation for v1.1 on the GAMES code (can be found on the Leonard Lab GitHub account).

Run_COVID_Dx.py and Test_COVID_Dx.py are the main executable files. Test_COVID_Dx.py solves the ODEs for a single parameter set, while  Run_COVID_Dx.py is used to execute one or more modules of the GAMES workflow (as defined in Settings_COVID_Dx.py).

Analysis_Cross_Validation.py and Analysis_PEM_Evaluation.py are also executable and can be used to analyze cross validation results and PEM evaluation results (requires input of results folder names to run - results folders are currently set to the final results used in the paper). 

SensitivityAnalysis.py is also executable and can be uused to run sensitivity analysis and plot results. 

The ODEs are defined in gen_mechanism.py. 

Settings, including parameter estimation method hyperparameters, definition of free parameters, and choice of model and training data, are set in Settings_COVID_Dx.py). 

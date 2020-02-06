# OSeMOSYS-CR

## Contents

- [Contents](#contents)
- [About](#about)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Usage](#usage)
- [Citing OSeMOSYS-CR](#citing-osemosys-cr)
- [License](#license)

# About 

OSeMOSYS-CR is an Energy System Optimization Model (ESOM) based on the Open Source Energy Modelling System (OSeMOSYS), this model finds the most cost-effective technological transitions towards a deep decarbonisation in the energy sector. OSeMOSYS-CR focuses in the electricity and transport sector, and the interaction among them. The repository contains three different climatic scenarios: i) Business-as-usual, and two scenarios consistent with the ii) 2°C (SR20) and iii) 1.5°C SR15) targets. 

# Quick start

The repository contains the following folders: 

* 0_Model Structure:contains two files that describes the structure of the model. 

* 1_Scenarios_Inputs: contains three folders representing each one of the climatic scenarios (i.e. BAU, SR20, and SR15). Each folder holds 30 individual comma-separated (csv) files with the parameters of the model. 

* 2_Scenarios_Outputs: ** stores the outputs generated after running the model. 

In order to run the model, the following files are needed: 

* 1_csv_to_txt.py: ** converts the csv files in 1_Scenarios_Inputs into a text (txt) file of the parameters of the model. 

* 2_run_model_mathprog.py: ** runs the model and generates two wide format file with the results of the model: i) a file containing the original names of the fuels, technologies and emissions, and ii) a file with coded names for an easier understanding. 

 Running the model, generates the following files, all of them are store in 2_Scenarios_Outputs:

* Osemosyscr_data.txt: ** is the output file of 1_csv_to_txt.py. 

* Osemosyscr_data_Output.txt:** is one of the output files of 2_run_model_mathprog.py. Contains the results of the scenario.

* Osemosys_data_Output.csv:** is one of the output files of 2_run_model_mathprog.py. Contains the results of the scenario in a wide format csv file. 

* Osemosys_data_Output_CODED:** is one of the output files of 2_run_model_mathprog.py. Contains the results of the scenario in a wide format csv file with coded names for the fuels, technologies and emissions of the model. 

# Documentation

Documentation is available on Read the Docs:

* [Read the documentation online](https://osemosyscr.readthedocs.io/en/stable/)

# Usage

In order to run the model, the [GLPK] (https://www.gnu.org/software/glpk/) solver needs to be installed. 2_Scenarios_Outputs should be empty before running the model. 1_csv_to_txt.py and 2_run_model_mathprog.py must be respectively run. In both codes the scenario of interest needs to be specified in the first lines. 2_run_model_mathprog.py should be executed in Python from an external system terminal.

# Releases
* 2019-02-XX: First released version of OSeMOSYS-CR.

## Citing OSMOSYS-CR
Guido Godínez and Luis Victor and Jam Anguloa and .. (2020) *Journal of Open Source Software*, 3(29), 825. [doi: XXXXX (https://doi.org/XXX/XXX.XXX)


# License

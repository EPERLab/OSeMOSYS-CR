---
title: 'OSeMOSYS-CR: Energy System Optimization Model for Costa Rica'
tags:
  - Energy Policy
  - Energy Modelling
  - Energy System Optimization Model
  - Deep Decarbonization
  - OSeMOSYS
authors:
  - name: Guido Godínez-Zamora
    orcid: 0000-0002-0256-1640
    affiliation: 1
  - name: Luis Victor-Gallardo
    affiliation: 1
  - name: Jam Angulo-Paniagua
    affiliation: 1
  - name: Eunice Ramos
    affiliation: 2
  - name: Mark Howells2
    affiliation: 2
  - name: Will Usher
    affiliation: 2
 - name: Felipe De León
    affiliation: 3
 - name: Jairo Quirós-Tortós
    affiliation: 1

affiliations:
 - name: School of Electrical Engineering, University of Costa Rica, San José, Costa Rica
   index: 1
 - name: Division of Energy Systems Analysis, KTH Royal Institute of Technology, Stockholm, Sweden.
   index: 2
- name: Climate Change Directorate, Ministry of Environment and Energy, San José, Costa Rica.
   index: 3
date: 30 January 2020
bibliography: paper.bib
---

# Summary

Costa Rica has excelled for nature protection and leadership to fight climate change. With an almost 100% renewable electricity matrix and a forest coverage of approximately 60%, the country is moving towards the transformation of the transport sector as its third major step towards decarbonisation. In 2015, this sector represented 44% of the total Greenhouses Gases (GHG) emission of the country [@MinisteriodeAmbienteyEnergia2019]. 
In this context, the University of Costa Rica, The Royal Institute of Technology, and the Climate Change Directorate worked together using data available in the country to develop the ``OSeMOSYS-CR`` which currently supports national energy-related climate change policy. This work emerged as part of the Deep Decarbonisation Pathways Project in Latin America and the Caribbean (DDPP-LAC), which is coordinated by the Institute for Sustainable Development and International Relations (IDDRI) and the Inter-American Development Bank (IADB) [@IDB2019]. 
As a result, the model helped to formulate and analyse the National Decarbonisation Plan of Costa Rica (NDP) [@MINAE2019], 
which is the long-term low-level GHG strategy of the country, representing an advance in terms of transparency and the decision-making process.


``OSeMOSYS-CR`` is an Energy System Optimization Model (ESOM) based on Open Source Energy Modelling System (OSeMOSYS) [@HOWELLS20115850;@GARDUMI2018209] that follows a bottom-up approach to establishing the most cost-effective technological transitions towards a deep decarbonisation in the energy sector of Costa Rica. The model focuses on the transport sector (passenger and freight) 
and its relationship with the electricity system and alternatives energy carriers. OSeMOSYS-CR was built on a countrywide scale using the best available data and considering the effect of rainy and dry months and including the entire process from energy sources supply to demands

The model combines more than one hundred commodities and two hundred technologies. A simple representation of the model, including primary energy supply (i.e., renewable, fossil fuel imports, biomass, and electricity imports), groups of technologies (i.e., power plants, vehicles, and distribution systems), energy demands by sector (i.e., industrial, residential, commercial and agricultural) and transport requirements (i.e., passenger and cargo) is shown in Figure 1. The model includes a module for co-benefits related to the activity of fossil fuels which was @used to calculate the effects on health, congestion, and the number of accidents in a cost-benefit assessment of the NDP [@Quiros-Tortos2020]. The parametrization of technologies includes costs, emissions, 
activity level, and capacities, according to their characteristics. Documentation of these parameters is available in the repository.  

The release of OSeMOSYS-CR pursues to support the transparency of the model and the collaboration through knowledge transfer with other teams. Additionally, the model can serve as a framework for future developers, interested in the implementation of ESOMs. To enhance this process, we offer three different pre-build scenarios included in the repository. A business-as-usual (BAU) scenario representing the evolution of the energy sector based on historical trends which serves as benchmark of mitigation strategies. Two decarbonisation scenarios, one consistent with the 2°C (SR20) and another with the 1.5°C SR15) targets, are provided with some mitigation strategies already being discussed in the country. Adaptations can be made to properly capture additional measures. The modelling framework runs using a Python tool. The process begins with comma-separated values (CSV) files containing the parameters of the model (editable if needed). A first module translates the CSV file to a text file (txt) suitable to GNU MathProg versions, which should then be executed with the OSeMOSYS code. A second module executes the linear optimization process using the GLPK package and generates a CSV output file that allows visualization of results.


![Simple reference energy system for OSeMOSYS-CR model.](SimpleModel.png)

The following images presents a graphic representation of the scenarios. Figure 2 shows the emission trajectories and the corresponding 2050 carbon intensity for the three scenarios [[Godinez-ZamoraGuido2020]]. The 2°C and 1.5°C scenarios lead to the corresponding target emissions by 2050. Figure 3 highlights that both decarbonisation scenarios lead to a cleaner system by 2050 with an increased efficiency.


![Emission trajectories for the BAU, SR20 and SR15 scenarios.](CO2_emissions.png)

![Emission trajectories for the BAU, SR20 and SR15 scenarios.](energy.png)

Ongoing projects in storage modelling, the deployment of robust decision making methodologies, and the modelling of complementary sectors such as land and water, to analyse the linkages between them and the energy sector will help improving the model in future iterations which will then be submitted to share with experts.


# Acknowledgements

This work was funded by the Interamerican Development Bank and the University of Costa Rica. The authors want to recognize the contribution from many stakeholders in Costa Rica in providing valuable data and discussing different aspects of the model that led to a robust model currently available in the country.

# References

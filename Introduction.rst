The OSeMOSYS – CR model Documentation
=======================================

This documentation has been structured to provide basic ideas about OSeMOSYS, establish an overview of the energy sector in Costa Rica, present the model structure, give synthesis regarding assumptions, and support the numerical inputs for the sets, parameters, and scenario building.   

=================================
General overview
=================================

**OSeMOSYS-CR** was developed by University Costa Rica (UCR), the KTH Royal Institute of Technology and the Climate Change Directorate (DDC) as part of the Deep Decarbonization Pathways Project in Latin America (DDPP-LAC). 
In order to contribute to the understanding of the model and guide new modelers, the team presents this comprehensive documentation which contains the general vision of design, sets, parameters, sources of information, key assumptions and explanation of data processing.

Introduction to OSeMOSYS
+++++++++

Costa Rica is promoting a transcendental digital transformation to improve processes and decision making. Based on the principles of transparency, consistency, comparability, and precision the Open Source energy MOdel SYStem (OSeMOSYS) was adopted to study the energy system. The model minimizes the total cost of the system for a certain period of time, defining the configuration of the supply system, considering some restrictions on activity, capacity, and emissions of technologies. The objective function of OSeMOSYS is presented in (1). 

**EQUATION (1)**

Where: 
*	Discounted Operational Cost: It corresponds to the cost related to maintenance (fixed, usually associate to capacity) and operation of technologies (variable, linked to fuel uses and level of activity).  
*	Discounted Capital Investment: It represents the cost of investment of all technologies selected to supply energy on the whole period. 
*	Discounted Technology Emission Penalty: This is associated to the use of pollutants. The calculation is based on the emission factor and the activity of technologies and the specific cost by pollutant.    
*	Discounted Salvage Value: As the capital cost of the technologies is discounted during an operational life up to zero, if in the last year the technologies have life, the corresponding value is counted.


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

Energy balance of Costa Rica
+++++++++

The energy balance is the most important source of data for the model. It is prepared for the Secretariat of Planning of the Energy Subsector (SEPSE). The analysis concentrates and processes data from institutions such as The Costa Rica Institute of Electricity (ICE), the Costa Rican Petroleum Refinery (RECOPE) and the National Center for Energy Control (CENCE). The information is usually presented annually with excel books and a SANKEY diagram. Figure 1 shows the diagram for 2011.  In Costa Rica, the fossil fuels are completely imported, and the electricity is generated almost completely with renewable sources. Figure 2 shows the historical trending and the general distribution for 2016. 

General model structure 
+++++++++

The entire Costa Rican energy sector is modeled in OSeMOSYS. However, only the transport and electricity sectors are subject to linear optimization, while other energy sources and demands are only represented with trends to account for their possible greenhouse gases (GHG) contributions. The overall structure of the model can be represented by the reference energy system shown in Figure 3. The primary energy supply consists of four main sources: renewable, imports of fossil fuels, biomass and electricity imports. These sources are transformed to different demands including industrial, residential and commercial requirements, and the transport of passengers and cargo. 

In OSeMOSYS-CR, the connection between the electricity and transport sectors is crucial for understanding the technological transition of fossil-powered vehicles to other lower or zero carbon emissions. In the model, all fuels and technologies are incorporated to OSeMOSYS taking into account other sets, such as temporary divisions and emission factors, as well as the parameters. The latter are classified, among others, into costs, activity levels and infrastructure capabilities. The establishment of these parameters was done after a data processing and a review of the available national energy information. Table X shows the main data sources.  

Data and key assumptions 
+++++++++

	
+------------+------------+--------------------------+-----------------------------------------------------------------------------+
| Category   | Source     | Data                     | Descriptions and assumption made                                            |
+============+============+==========================+=============================================================================+
| Energy     | SEPSE      | Energy balance           | It is used to build the structure of the energy system, time-series         |
| System     |            |                          | from 1989 to 2017 and forecasted with ARIMA models.                         |
+------------+------------+--------------------------+-----------------------------------------------------------------------------+
| Demand     | SEPSE      | Final energy             | Built based on final end-use by sectors: industry, transport, households,   |
|            |            |                          | services and agriculture.                                                   |
+            +------------+--------------------------+-----------------------------------------------------------------------------+
|            | ICE        | Electricity load shapes  | Assumed constant for industry, curve for commerce (peak mid-day) and        |
|            |            |                          | classical two valleys, two peaks and night for residential.                 |
+------------+------------+--------------------------+-----------------------------------------------------------------------------+




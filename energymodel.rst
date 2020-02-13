The OSeMOSYS – CR Energy model Documentation
=======================================

This documentation has been structured to provide  an overview of the energy sector in Costa Rica, present the model structure, give synthesis regarding assumptions, and support the numerical inputs for the sets, parameters, and scenario building.   

Energy balance of Costa Rica
+++++++++

The energy balance is the most important source of data for the model. It is prepared for the Secretariat of Planning of the Energy Subsector (SEPSE). The analysis concentrates and processes data from institutions such as The Costa Rica Institute of Electricity (ICE), the Costa Rican Petroleum Refinery (RECOPE) and the National Center for Energy Control (CENCE). The information is usually presented annually with excel books and a SANKEY diagram. Figure 1 shows the diagram for 2011.  As can be noted, in Costa Rica the fossil fuels are completely imported, and the electricity is generated almost completely with renewable sources. Figure 2 shows the historical trending and the general distribution for 2016. 

General model structure 
+++++++++

The entire Costa Rican energy sector is modeled in OSeMOSYS. However, only the transport and electricity sectors are subject to linear optimization, while other energy sources and demands are only represented with trends to account for their possible greenhouse gases (GHG) contributions. The overall structure of the model can be represented by the reference energy system shown in Figure 3. The primary energy supply consists of four main sources: renewable, imports of fossil fuels, biomass and electricity imports. These sources are transformed to different demands including industrial, residential and commercial requirements, and the transport of passengers and cargo. 

In OSeMOSYS-CR, the connection between the electricity and transport sectors is crucial for understanding the technological transition of fossil-powered vehicles to other lower or zero carbon emissions. In the model, all fuels and technologies are incorporated to OSeMOSYS taking into account other sets, such as temporary divisions and emission factors, as well as the parameters. The latter are classified, among others, into costs, activity levels and infrastructure capabilities. The establishment of these parameters was done after a data processing and a review of the available national energy information. The following table summarizes the main souces of data for OSeMOSYS-CR: 

.. table:: Table 1. Main data sources used in OSeMOSYS-CR. 

+-------------+------------+--------------------------+------------------------------------------------------------------------------+
| Category    | Source     | Data                     | Descriptions and assumption made                                             |
+=============+============+==========================+==============================================================================+
| Energy      | SEPSE      | Energy balance           | It is used to build the structure of the energy system, time-series          |
| System      |            |                          | from 1989 to 2017 and forecasted with ARIMA models.                          |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
| Demand      | SEPSE      | Final energy             | Built based on final end-use by sectors: industry, transport, households,    |
|             |            |                          | services and agriculture.                                                    |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | ICE        | Electricity load shapes  | Assumed constant for industry, curve for commerce (peak mid-day) and         |
|             |            |                          | classical two valleys, two peaks and night for residential.                  |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | SEPSE      | Transport                | It includes load factors, vehicle fleet, and energy consumption, efficiencies|
|             | RITEVE     | (passengers and cargo)   | and annual kilometers. We combine international standard data of technologies|
|             | MOPT       |                          | with national records. Technological groups are defined to study modal change|
|             | ETSAP      |                          | and fuel use. Non-motorized mobility is considered zero in the base case.    |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
|Electricity  | ICE        | Capital and fixed costs  | Based on national data. The costs were assumed constant in the whole period, |
|technologies | Bloomberg  |                          | except for solar and wind systems, which decrease according to international |
|             | IEA        |                          | trends. Residual capacity is constant.                                       |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | ICE        | Capacities and activity  | Based on the operational performance registered by the National Energy       |
|             |            |                          | Control Centre. Lifespan is according to national plans.                     |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
|Transport    | Hacienda   | Capital and fixed costs  | Based on the Ministry of Finance (Hacienda) database. We assumed that cost of|
|technologies | Bloomberg  |                          | electric vehicles' decreases (Bloomberg). For cargo transport, we review cost|
|             | Companies  |                          | of companies like Nicola and Tesla.                                          |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | SEPSE      | Capacities and activity  | Based on the performance register by national surveys, concession for public |
|             | RITEVE     |                          | transport and the annual Vehicle technical review (RITEVE). Lifespan is      |
|             | MOPT       |                          | according to manufacturers and the residual capacity decreases linearly and  | 
|             |            |                          | proportionally with this value.                                              |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
|Fuel prices  | RECOPE     | Fossil Fuels and Biofuels| Based on current tariffs and projection uses in national plans. It considers |
|             | IEA        |                          | international prices and the tariff given by the regulator in Costa Rica     |
|             | ARESEP     |                          | (ARESEP) and trend provide by international Energy Agency (IEA).             |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | ICE        | Electricity              | Base of the average of national tariffs and projections.                     |
|             | ARESEP     |                          |                                                                              |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | SEPSE      | Biomass                  |  Not included. It is produced and consumed locally.                          |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | ETSAP      | Hydrogen                 | Based on data publish by Energy Technology Systems Analysis Programme (ETSAP)|
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
|Infraestruc -| ICE        | Plants and power grid    | Based on Transmission and generation national plans. It assumes losses of 6% |
| ture        |            |                          | from the bulk transmission system and 6% for distribution. Charging          |
|             |            |                          | infrastructure is not included.                                              |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | RECOPE     | Pipeline and road        | Based on national reports, we do not consider the current does no growth (for|
|             |            | distribution             | gasoline and Diesel). It includes new infrastructure for LPG. The model      |
|             |            |                          | includes natural gas but is not used.                                        |
+             +------------+--------------------------+------------------------------------------------------------------------------+
|             | ETSAP      | Hydrogen                 | Consider local production, road transport and supply stations.               |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
| Sustainable | MINAE      | Urban plans and mobility | Regarding the Integrated Public Transport System, the cost consideration come|
| mobility    | MOPT       |                          | from  Costa Rican Railways Institute (INCOFER) and MOTP studies.             |
|             | INCOFER    |                          |                                                                              |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
| Cargo       | MINAE      | Electric cargo train and | Cost was taken from national reports and demand based on expert criteria     |
| transport   | MOPT       | Logistic                 | given in the participatory process.                                          |
|             | INCOFER    |                          |                                                                              |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
| Emissions   | IPCC       |  Factors                 |  Based on the IPCC and the national GHG inventory.                           |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+
| Co-benefits | PEN        | Coefficients             | It considers coefficients for health congestion and accidents by State of the|
|             | IMF        |                          | Nation Project (PEN) and International Monetary Fund (IMF)                   |
+-------------+------------+--------------------------+------------------------------------------------------------------------------+

Sets 
+++++++++

The sets are responsible for defining the structure of the model (i.e. temporal space, geographic space, elements of the system, etc.), the group of sets include: years, fuels, technologies, emissions and modes of operation. Each parameter, as it going to be further explained, is dependent of one or more sets. This sections presents the sets composing the current version of OSeMOSYS-CR.  

Year
---------

This corresponds to the period of analysis. For OSeMOSYS-CR it is from 2018 to 2055. Five additional years are added in order to extend the optimization process.  Therefore, decisions right before 2050 (i.e. national decarbonisation target) will not be affected by the model considering it is the last year. 

Fuels
---------

Figure 6 shows the different levels and transformations fuels go through, and their relations with some technologies. Groups E0, E1, E3, E4, E5, and E6 are crucial elements of the current supply chain, while E8 and E9 are modeled for control purposes.  Groups E9, E10  and E11 complement the model to enable the inclusion of hydrogen and infrastructure.  

The following table presents a synthesis of the included groups of commodities, including a brief description and examples.  See Annex 2 for the whole list of fuels.

+-------+------------------------------------------+-------------------------------------------------------------------------------+
| Group | Descriptions                             | Examples                                                                      |
+=======+==========================================+===============================================================================+
| E0    | Pre-sources: Imports and fuel production | Import and production (fossil fuels and Biofuels), and their distribution.    |
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E1    | Primary sources (energy balance)         | Water, Wind, diesel, gasoline, biomass, and firewood.                         |
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E2-E3 | Electricity                              | Electricity from power plants to its distribution.                            |
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E4    | Electricity demand by sector             | Diesel for agriculture, firewood for residential, petroleum coke for industry.|
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E6    | Transport demand                         | Private and public passenger transport, and light and heavy cargo transport.  |
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E7    | Distribution                             | Diesel for industry, LPG* for heavy cargo transport, electricity for vehicles.|
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E8    | Transport managers                       | Fossil fuels for public transport, low carbon fuels for light freight.        |
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E10   | Infraestrucuture                         | Roads, rails, and bikeways.                                                   |
+-------+------------------------------------------+-------------------------------------------------------------------------------+
| E11   | Specific category for Hydrogen           | Produced hydrogen and ready to use.                                           |
+-------+------------------------------------------+-------------------------------------------------------------------------------+

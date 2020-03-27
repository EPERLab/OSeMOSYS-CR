4. Energy model: Scenario building
=====================

OSeMOSYS-CR started by estimating a base case, and subsequently, including the effect of a set of policies defined by stakeholders in two levels of decarbonization. This exercise allowed the creation of three different scenarios: 

(i) A Business-as-usual (BAU) scenario, that represents the behavior of the emissions without considering public policy interventions (i.e. following the historic trends). 
(ii) A 2°C scenario, compatible with the 2015 NDC's goals of Costa Rica. 
(iii) A 1.5°C that is compatible with a goal of net zero emissions by 2050.

The BAU scenario considers that the energy consumption, economic activity and population grow according to the historical trends. This scenario incorporates the electricity generation expansion plan from the Costa Rican Electricity Institute to represent the development of the electricity sector. It also includes a moderate penetration of solar and wind generation, distributed generation for self-consumption, prived electric vehicles and electric public transport (buses). In terms of emissions, this scenario does not have a significant change in relation to the trend trajectory. 

The 2°C and 1.5°C scenarios consider that the social and economic situation described in the BAU scenario remains the same. However, they incorporate the political objectives generated in the stakeholder engagement and the participatory process. The main strategies in the 2° and 1.5° scenarios are focused in *i)* urban planning and mobility, *ii)* switching fossil fuel technologies, and *iii)* switching energy carriers. Figure 2.1 sumarizes the main aspects of each scenario. 

.. figure:: img/Scenarios.PNG
   :align:   center
   :width:   700 px

   *Figure 2.1: Scenarios in OSeMOSYS-CR*

*Table 4.1: Summary of parameters and actions in the OSeMOSYS-CR model to represent strategies.*

.. table:: 
   :align:   center

+-----------+--------------------------+------------------------------------------------------------------------------------------+
|Subsector  | Action                   | Description on modelling process                                                         |
+===========+==========================+==========================================================================================+
| Passenger | Mode shift: Demand in    | Mobility demand is an entry for the model. We use an S-curve to model a smooth           |
| Transport | public and private sector| transition from private to public transport with a target by 2050. Load factors,         |
|           |                          | distances, and efficiencies are similar to BAU. To estimate the costs of this process,   |
|           |                          | we use coefficients linked to the level of activity and based on the urban planning      |
|           |                          | studies developed in Costa Rica.                                                         |
|           +--------------------------+------------------------------------------------------------------------------------------+
|           | Non-motorized mobility   | The transition is carried out by lineal reduction of the demand in private and public    |
|           | and digitalization       | transport from 2022 to 2050. The cost of the infrastructure was embedded with the mode   |
|           |                          | shift. In terms of the digitalization, we do not consider cost due to the existing and   |
|           |                          | growth communication infrastructure of the country.                                      |
|           +--------------------------+------------------------------------------------------------------------------------------+
|           | Electrification private  | Similar to the mode shift, we use an S-curve to model the adoption rate of technologies. |
|           | and public sectors       | We parametrized the curve considering targets by 2030, 2035, and 2050. The procedure     |
|           |                          | consists in introducing a level of activities for low-carbon technologies while the      |
|           |                          | proportions of groups of technologies as keeping proportional to the base year.          |
+-----------+--------------------------+------------------------------------------------------------------------------------------+
| Cargo     | Demand absorbed by       | The TELCA began to absorb demand for heavy freight linearly from 2022 to 2024, in which  |
| Transport | TELCA and Logistic       | the electric train reaches a maximum value of 10% through 2050. The logistic actions     |
|           |                          | reduce the light freight demand, and we use the same procedure as TELCA, but with 2022   |
|           |                          | and 2030 as transition years. In both cases, the capital cost is introduced linearly in  |
|           |                          | the transition years. Fixed costs also increase in the transition period to the maximum  |
|           |                          | rate, which remains until 2050                                                           |
|           +--------------------------+------------------------------------------------------------------------------------------+
|           | Use of LPG               | Considering the uncertainty in cargo transport related to low-carbon technologies, the   |
|           |                          | stakeholders consider this as an alternative. It is modelled as a maximum value of       |
|           |                          | activity from 0% to 20% between 2022 and 2050                                            |
|           +--------------------------+------------------------------------------------------------------------------------------+
|           | Low carbon               | Similar to the above related to uncertainty, there are no absolute values for the        |
|           | technologies             | transition. In this context, we use the reference value of emission (in cargo) of 2018   |
|           |                          | and define a linear constraint of emissions from 2022 to 2050, limiting the emission     |
|           |                          | from 0% to -20% and -70%, according to the scenario. The model optimizes under this      |
|           |                          | constraint.                                                                              |
+-----------+--------------------------+------------------------------------------------------------------------------------------+
| Fuels and | Blend with biofuels      | A specific process in the model makes the volumetric mixture of biofuels and fossil      |
| general   |                          | fuels, defining percentages of activities. For these cases, it establishes a linear      |
|           |                          | level of activity from 0 to 8% for ethanol and 0 to 10% for biodiesel, between 2022 and  |
|           |                          | 2050. This consideration responds to the uncertainty linked to biofuel imports and       |
|           |                          | productions. At this time, we consider only importations and comparable prices with      |
|           |                          | fossil fuels.                                                                            |
|           +--------------------------+------------------------------------------------------------------------------------------+
|           | Renewable electricity    | The assumption limits the operation of thermal power plants from 2.5% to 0% between 2022 |
|           |                          | and 2050.                                                                                |
|           +--------------------------+------------------------------------------------------------------------------------------+
|           | Efficiency               | It is assumed a linear reduction of demands from 0% to 10% between 2022 and 2050 as a    |
|           |                          | response to the increased efficiency in the energy sector.                               |
+-----------+--------------------------+------------------------------------------------------------------------------------------+
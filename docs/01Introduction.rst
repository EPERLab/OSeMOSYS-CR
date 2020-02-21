.. Title:

1. Introduction 
=====================================

1.1 Project overview
+++++++++

This work is part of the “Deep Decarbonization Pathways Project in Latin America and the Caribbean (DDPP-LAC)” which is coordinated by the Institute for Sustainable Development and International Relations (IDDRI) and the Inter-American Development Bank (IADB).

The project involves six different teams, and each team is formed by experts from a Latin American (LA) country (Argentina, Colombia, Costa Rica, Ecuador, Mexico, and Peru) and experts from other countries (France, USA, Sweden and Brazil). The main purpose of these alliances is to transfer capacities from one country to another, while engaging with policy makers to address a modeling aspect of local importance. The Costa Rican team is composed by researchers from the University of Costa Rica (UCR) and the Royal Institute of Technology (KTH) in Stockholm. While each team has its own goals, the common objectives of this project are:

* Provide support and training to teams of researchers in Latin America and the Caribbean (LAC) in the use of new models, relying on best practices drawn by more advanced teams of researchers.
* Demonstrate these models to local policymakers with an emphasis on a specific policy question of local importance.
* Develop long-term decarbonization pathways that can inform a transparent public debate on Nationally Determined Contributions (NDC) planning.
* Develop a collaborative community of climate policy modelers in LAC capable of continually developing their expertise. 

The Costa Rican team focuses on the development of an Energy System Optimization Model (ESOM) for its energy system, paying particular attention to the electricity and the transport sectors, to establish the most cost-effective technological transition towards a deep decarbonization, while assessing the corresponding impacts over the economy and society. The project also aims at promoting a dialogue on the national policy related to the future concerning the decarbonization of the economy.

1.2 Motivation and problem statement
+++++++++

Costa Rica is a Latin American country worldwide known for its environmental protection, political, social and economic stability, and renewable electricity generation. Despite these achievements, there are many challenges to tackle in the energy sector, especially when it concerns transportation. According to the 2016’s National Energy Balance [1], in the country’s energy mix, fossil fuels are
the main energy source with an overwhelming 62.6%. From that share the transport sector accounts for 82.8% and at the same time correspondS to approximately 44 % of national Green House Gases (GHG) emissions [2].

The previously mentioned challenges are exacerbated by the international and national commitments that Costa Rica has acquired, such as its ambitious NDCs [3]. Therefore, it is crucial for the country to further transform the energy sector by reducing oil consumption through alternative sources, and create a more sustainable energy mix. In this context, the main purpose of the project is to develop an ESOM to characterize the transport and electricity sectors. The objective is to analyze the energy system in order to identify decarbonization pathways scenarios focusing on the transport sector through the examination of transport scenarios with different vectors of final energy demand. 

The produced ESOM will support policymakers in Costa Rica understanding the most suitable strategies to achieve a deep decarbonization. It could also be used to decide what type of technologies (in the electricity and transport sector) should be incentivized for the different scenarios. In addition, the project aims to produce a scalable ESOM that will remain in the government for different energy related decisions. The project tries to understand the percentage of existing fossil-based taxis, buses, and light-duty vehicles that should be changed to other more efficient technologies (electric, biogas, etc.). While the previous example applies for the transport sector, similar conclusions are expected in terms of the electricity sector. The modeling tool chosen was the Open Source energy Modelling System (OSeMOSYS) [4].

1.3 The Open Source energy Modelling System (OSeMOSYS)
+++++++++

OSeMOSYS is an optimization software for long-term energy planning. It is an open source model structured in blocks of functionality that allows easy modifications to the code, providing a great flexibility for the creative process of the solution. the models that are built in OSeMOSYS minimize the total cost of the system for a certain period of time, defining the configuration of the supply system, considering some restrictions on activity, capacity, and emissions of technologies. As shown in the following equation: 

.. math::

   Minimize \sum_{y,t,r}Total Discounted Cost_{y,t,r},
   
where: *y* corresponds to the year, *t* to the technology and *r* to the region. 

The discounted cost can be express as follows: 

.. math::

 ∀_{y,t,r} Total Discounted Cost_{y,t,r} =  Discounted Operational Cost_{y,t,r} +
 Discounted Capital Investment_{y,t,r} + Discounted Technology Emmisions Penalty_{y,t,r} -
 Discounted Salvage value_{y,t,r},

where: 

*	*Discounted Operational Cost:* Corresponds the cost related to maintenance (fixed, usually associate to capacity) and operation of technologies (variable, linked to fuel uses and level of activity).  
*	*Discounted Capital Investment:* It is the cost of investment of all technologies selected to supply energy on the whole period. 
*	*Discounted Technology Emission Penalty:* It is associated to the use of pollutants. The calculation is based on the emission factor and the activity of technologies and the specific cost by pollutant.    
*	*Discounted Salvage Value:* As the capital cost of the technologies is discounted during an operational life up to zero, if in the last year the technologies have life, the corresponding value is counted.

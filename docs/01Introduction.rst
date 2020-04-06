.. Title:

1. Introduction 
=====================================

1.1 Projects overview
+++++++++

The creation of OSeMOSYS-CR started as part of the “Deep Decarbonization Pathways Project in Latin America and the Caribbean (DDPP-LAC)” which is coordinated by the Institute for Sustainable Development and International Relations (IDDRI) and the Inter-American Development Bank (IADB) :cite:`IDBandDDPLAC2019` :cite:`Godinez-Zamora2020`.

The project involves six different teams, and each team is formed by experts from a Latin American (LA) country (Argentina, Colombia, Costa Rica, Ecuador, Mexico, and Peru) and experts from other countries (France, USA, Sweden and Brazil). The main purpose of these alliances is to transfer capacities from one country to another, while engaging with policy makers to address a modeling aspect of local importance.  

The Costa Rican team is composed by researchers from the University of Costa Rica (UCR) and the Royal Institute of Technology (KTH) in Stockholm, and focuses on the development of an Energy System Optimization Model (ESOM) for its energy system, paying particular attention to the electricity and the transport sectors, to establish the most cost-effective technological transition towards a deep decarbonization, while assessing the corresponding impacts over the economy and society. The project also aims at promoting a dialogue on the national policy related to the future concerning the decarbonization of the economy. 

The development of OSeMOSYS-CR has been also supported by the project "Assessing Options to Decarbonize the Transport Sector under Technological Uncertainty: The Case of Costa Rica". This work was contracted by the Interamerican Development Bank (IADB) for the Directorate of Climate Change (DCC) of the Ministry of Environment and Energy in Costa Rica. The project aimed at developing a framework to evaluate mitigation actions in the Costa Rican transport sector that contribute to achieve the deep decarbonization, considering its uncertainty and socioeconomic impact, and implementing it in OSeMOSYS-CR to evaluate multiple climate actions towards a clean transport sector :cite:`Quiros-Tortos2020`. 

The project "Development And Assesment of Decarbonization Pathways to Inform Dialogue with Costa Rica Regarding The Updating Process of Nationally Determined Contribution (NDC)" also contributed to upgrading OSeMOSYS-CR. It involved the development of  complementary land and water models, and the integration of them with the energy model. This project was funded by the World Bank for the Directorate of Climate Change (DCC) of the Ministry of Environment and Energy in Costa Rica. 

This is the first released version of OSeMOSYS-CR, however the model is expected to grow and new versions will be shared.

1.2 Motivation and problem statement
+++++++++

Costa Rica is a Latin American country worldwide known for its environmental protection, political, social and economic stability, and renewable electricity generation. Despite these achievements, there are many challenges to tackle in the energy sector, especially when it concerns transportation. According to the 2016’s National Energy Balance :cite:`SEPSE2016`, in the country’s energy mix, fossil fuels arethe main energy source with an overwhelming 62.6%. The transport sector accounts for 82.8% of the total fossiel fuel consumption and at the same time corresponds to approximately 44 % of national Green House Gases (GHG) emissions :cite:`InstitutoMeteorologicoNacional2012`.

The previously mentioned challenges are exacerbated by the international and national commitments that Costa Rica has acquired, such as its ambitious NDCs :cite:`MinisteriodeAmbienteyEnergiaMINAE2015`. Therefore, it is crucial for the country to further transform the energy sector by reducing oil consumption through alternative sources, and create a more sustainable energy mix. In this context, the main purpose of the project is to develop an ESOM to characterize the transport and electricity sectors. The objective is to analyze the energy system in order to identify decarbonization pathways scenarios focusing on the transport sector through the examination of transport scenarios with different vectors of final energy demand. 

The produced ESOM will support policymakers in Costa Rica understanding the most suitable strategies to achieve a deep decarbonization. It could also be used to decide what type of technologies (in the electricity and transport sector) should be incentivized for the different scenarios. In addition, the project aims to produce a scalable ESOM that will remain in the government for different energy related decisions. The project tries to understand the percentage of existing fossil-based taxis, buses, and light-duty vehicles that should be changed to other more efficient technologies (electric, biogas, etc.). While the previous example applies for the transport sector, similar conclusions are expected in terms of the electricity sector. The modeling tool chosen was the Open Source energy Modelling System (OSeMOSYS) :cite:`HOWELLS20115850`.

1.3 The Open Source energy Modelling System (OSeMOSYS)
+++++++++

OSeMOSYS is an optimization software for long-term energy planning. It is an open source model structured in blocks of functionality that allows easy modifications to the code, providing a great flexibility for the creative process of the solution. The models that are built in OSeMOSYS minimize the total cost of the system for a certain period of time, defining the configuration of the supply system, considering some restrictions on activity, capacity, and emissions of technologies :cite:`HOWELLS20115850`. This is shown in the following equation: 

.. math::

   Minimize \sum_{y,t,r}Total\ discounted\ cost_{y,t,r},
   
where: *y* corresponds to the year, *t* to the technology and *r* to the region. 

The discounted cost can be expressed as follows: 

.. math::

   \forall _{y,t,r}\  Total\ discounted\ cost_{y,t,r}\  =   DOC_{y,t,r} + DCI_{y,t,r}  + DTEP_{y,t,r} - DSV_{y,t,r},
 
where: 

*	*DOC (Discounted Operational Cost):* Corresponds to the cost related to maintenance (fixed, usually associate to capacity) and operation of technologies (variable, linked to fuel uses and level of activity).  
*	*DCI (Discounted Capital Investment):* It is the cost of investment of all technologies selected to supply energy on the whole period. 
*	*DTEP (Discounted Technology Emission Penalty):* It is associated to the use of pollutants. The calculation is based on the emission factor and the activity of technologies and the specific cost by pollutant.    
*	*DSV (Discounted Salvage Value):* As the capital cost is discounted in the first year a technology is acquired, if in the last year of study the technologies have remaining years of operational life, the corresponding value is counted.

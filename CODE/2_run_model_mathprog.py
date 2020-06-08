import os, os.path
import time
import re
import csv
import xlrd
import linecache
import pandas as pd
from copy import deepcopy
import gc

#Select the scenario you want to run
sce = 'BAU'
#sce ='SR20'
#sce = 'SR15'

#%%
def set_txt_list( model_to_run ):
    txt_list_raw = os.listdir( './2_Scenarios_Outputs/' )
    global txt_list, structural_list
    txt_list = [e for e in txt_list_raw if ( '.txt' in e ) ]
    structural_list = []
    structural_list.append( 'STRUCTURE_OSEMOSYS_CR.xlsx' )
#%%
def data_processor( case ):
    # First, we call the structure of the model:
    table1 = xlrd.open_workbook( "0_Model Structure/" + str( structural_list[ case ] ) ) # works for all scenarios
    print("$$$$$$")
    print( str( structural_list[ case ] ) )
    print("$$$$$$")
    sheet_sets_structure = table1.sheet_by_index(0) 
    sheet_params_structure = table1.sheet_by_index(1) 
    sheet_vars_structure = table1.sheet_by_index(2) 
    #
    S_DICT_sets_structure = {'set':[],'initial':[],'number_of_elements':[],'elements_list':[]}
    for col in range(1,11+1):
        S_DICT_sets_structure['set'].append( sheet_sets_structure.cell_value(rowx=0, colx=col) )
        S_DICT_sets_structure['initial'].append( sheet_sets_structure.cell_value(rowx=1, colx=col) )
        S_DICT_sets_structure['number_of_elements'].append( int( sheet_sets_structure.cell_value(rowx=2, colx=col) ) )
        #
        element_number = int( sheet_sets_structure.cell_value(rowx=2, colx=col) )
        this_elements_list = []
        if element_number > 0:
            for n in range( 1, element_number+1 ):
                this_elements_list.append( sheet_sets_structure.cell_value(rowx=2+n, colx=col) )
        S_DICT_sets_structure['elements_list'].append( this_elements_list )
    #
    S_DICT_params_structure = {'category':[],'parameter':[],'number_of_elements':[],'index_list':[]}
    param_category_list = []
    for col in range(1,30+1):
        if str( sheet_params_structure.cell_value(rowx=0, colx=col) ) != '':
            param_category_list.append( sheet_params_structure.cell_value(rowx=0, colx=col) )
        S_DICT_params_structure['category'].append( param_category_list[-1] )
        S_DICT_params_structure['parameter'].append( sheet_params_structure.cell_value(rowx=1, colx=col) )
        S_DICT_params_structure['number_of_elements'].append( int( sheet_params_structure.cell_value(rowx=2, colx=col) ) )
        #
        index_number = int( sheet_params_structure.cell_value(rowx=2, colx=col) )
        this_index_list = []
        for n in range(1, index_number+1):
            this_index_list.append( sheet_params_structure.cell_value(rowx=2+n, colx=col) )
        S_DICT_params_structure['index_list'].append( this_index_list )
    #
    S_DICT_vars_structure = {'category':[],'variable':[],'number_of_elements':[],'index_list':[]}
    var_category_list = []
    for col in range(1,43+1):
        if str( sheet_vars_structure.cell_value(rowx=0, colx=col) ) != '':
            var_category_list.append( sheet_vars_structure.cell_value(rowx=0, colx=col) )
        S_DICT_vars_structure['category'].append( var_category_list[-1] )
        S_DICT_vars_structure['variable'].append( sheet_vars_structure.cell_value(rowx=1, colx=col) )
        S_DICT_vars_structure['number_of_elements'].append( int( sheet_vars_structure.cell_value(rowx=2, colx=col) ) )
        #
        index_number = int( sheet_vars_structure.cell_value(rowx=2, colx=col) )
        this_index_list = []
        for n in range(1, index_number+1):
            this_index_list.append( sheet_vars_structure.cell_value(rowx=2+n, colx=col) )
        S_DICT_vars_structure['index_list'].append( this_index_list )
    #-------------------------------------------#
    #
    all_vars = S_DICT_vars_structure['variable']
    #
    all_vars_output_dict = [ {} for e in range( len( txt_list ) ) ]
    #
    output_header = ['Run.ID','Fuel','Fuel.DESCRIPTION','Technology','Technology.DESCRIPTION','Emission','Emission.DESCRIPTION','Year']
    #-------------------------------------------------------#
    for v in range( len( all_vars ) ):
        output_header.append( all_vars[v] )
    #-------------------------------------------------------#
    vars_as_appear = []
    case_name = txt_list[case].replace('.txt','')
    #
    data_name = './2_Scenarios_Outputs/' + str( case_name ) + '_output.txt'
    print( data_name )
    #
    ini_line = 5741012+2
    end_line = 11438802
    #
    for n in range(ini_line, end_line, 2 ):
        structure_line_raw = linecache.getline(data_name, n)
        structure_list_raw = structure_line_raw.split(' ')
        # print( structure_line_raw, data_name, n, ini_line, end_line )
        # time.sleep(20)
        structure_list_raw_2 = [ s_line for s_line in structure_list_raw if s_line != '' ]
        structure_line = structure_list_raw_2[1]
        structure_list = structure_line.split('[')
        the_variable = structure_list[0]
        #
        if the_variable in all_vars:
            set_list = structure_list[1].replace(']','').replace('\n','').split(',')
            #--%
            index = S_DICT_vars_structure['variable'].index( the_variable )
            this_variable_indices = S_DICT_vars_structure['index_list'][ index ]
            #
            if 'y' in this_variable_indices:
                data_line = linecache.getline(data_name, n+1)
                data_line_list_raw = data_line.split(' ')
                data_line_list = [ data_cell for data_cell in data_line_list_raw if data_cell != '' ]
                useful_data_cell = data_line_list[1]
                #--%
                if useful_data_cell != '0':
                    #
                    if the_variable not in vars_as_appear:
                        vars_as_appear.append( the_variable )
                        all_vars_output_dict[case].update({ the_variable:{} })
                        all_vars_output_dict[case][the_variable].update({ the_variable:[] })
                        #
                        for n in range( len( this_variable_indices ) ):
                            all_vars_output_dict[case][the_variable].update( { this_variable_indices[n]:[] } )
                    #--%
                    this_variable = vars_as_appear[-1]
                    all_vars_output_dict[case][this_variable][this_variable].append( useful_data_cell )
                    for n in range( len( this_variable_indices ) ):
                        all_vars_output_dict[case][the_variable][ this_variable_indices[n] ].append( set_list[n] )
                #
            #
            elif 'y' not in this_variable_indices:
                data_line = linecache.getline(data_name, n+1)
                data_line_list_raw = data_line.split(' ')
                data_line_list = [ data_cell for data_cell in data_line_list_raw if data_cell != '' ]
                useful_data_cell = data_line_list[1]
                #--%
                if useful_data_cell != '0':
                    #
                    if the_variable not in vars_as_appear:
                        vars_as_appear.append( the_variable )
                        all_vars_output_dict[case].update({ the_variable:{} })
                        all_vars_output_dict[case][the_variable].update({ the_variable:[] })
                        #
                        for n in range( len( this_variable_indices ) ):
                            all_vars_output_dict[case][the_variable].update( { this_variable_indices[n]:[] } )
                    #--%
                    this_variable = vars_as_appear[-1]
                    all_vars_output_dict[case][this_variable][this_variable].append( useful_data_cell )
                    for n in range( len( this_variable_indices ) ):
                        all_vars_output_dict[case][the_variable][ this_variable_indices[n] ].append( set_list[n] )
        #--%
        else:
            pass
    #
    linecache.clearcache()  
    #%%
    output_adress = './2_Scenarios_Outputs'
    combination_list = [] # [fuel, technology, emission, year]
    data_row_list = []
    for var in range( len( vars_as_appear ) ):
        this_variable = vars_as_appear[var]
        this_var_dict = all_vars_output_dict[case][this_variable]
        #--%
        index = S_DICT_vars_structure['variable'].index( this_variable )
        this_variable_indices = S_DICT_vars_structure['index_list'][ index ]
        #--------------------------------------#
        for k in range( len( this_var_dict[this_variable] ) ):
            this_combination = []
            #
            if 'f' in this_variable_indices:
                this_combination.append( this_var_dict['f'][k] )
            else:
                this_combination.append( '' )
            #
            if 't' in this_variable_indices:
                this_combination.append( this_var_dict['t'][k] )
            else:
                this_combination.append( '' )
            #
            if 'e' in this_variable_indices:
                this_combination.append( this_var_dict['e'][k] )
            else:
                this_combination.append( '' )
            #
            if 'l' in this_variable_indices:
                this_combination.append( '' )
            else:
                this_combination.append( '' )
            #
            if 'y' in this_variable_indices:
                this_combination.append( this_var_dict['y'][k] )
            else:
                this_combination.append( '' )
            #
            if this_combination not in combination_list:
                combination_list.append( this_combination )
                data_row = ['' for n in range( len( output_header ) ) ]
                # print('check', len(data_row), len(run_id) )
                data_row[0] = 0
                data_row[1] = this_combination[0]
                data_row[3] = this_combination[1]
                data_row[5] = this_combination[2]
                # data_row[7] = this_combination[3]
                data_row[7] = this_combination[4]
                #
                var_position_index = output_header.index( this_variable )
                data_row[ var_position_index ] = this_var_dict[ this_variable ][ k ]
                data_row_list.append( data_row )
            else:
                ref_index = combination_list.index( this_combination )
                this_data_row = deepcopy( data_row_list[ ref_index ] )
                #
                var_position_index = output_header.index( this_variable )
                #
                if 'l' in this_variable_indices: 
                    #
                    if str(this_data_row[ var_position_index ]) != '' and str(this_var_dict[ this_variable ][ k ]) != '' and ( 'Rate' not in this_variable ):
                        this_data_row[ var_position_index ] = str(  float( this_data_row[ var_position_index ] ) + float( this_var_dict[ this_variable ][ k ] ) )
                    elif str(this_data_row[ var_position_index ]) == '' and str(this_var_dict[ this_variable ][ k ]) != '':
                        this_data_row[ var_position_index ] = str( float( this_var_dict[ this_variable ][ k ] ) )
                    elif str(this_data_row[ var_position_index ]) != '' and str(this_var_dict[ this_variable ][ k ]) == '':
                        pass
                else:
                    this_data_row[ var_position_index ] = this_var_dict[ this_variable ][ k ]
                #
                data_row_list[ ref_index ]  = deepcopy( this_data_row )
    #
    non_year_combination_list = []
    non_year_combination_list_years = []
    for n in range( len( combination_list ) ):
        this_combination = combination_list[ n ]
        this_non_year_combination = [ this_combination[0], this_combination[1], this_combination[2] ]
        if this_combination[4] != '' and this_non_year_combination not in non_year_combination_list:
            non_year_combination_list.append( this_non_year_combination )
            non_year_combination_list_years.append( [ this_combination[4] ] )
        elif this_combination[4] != '' and this_non_year_combination in non_year_combination_list:
            non_year_combination_list_years[ non_year_combination_list.index( this_non_year_combination ) ].append( this_combination[4] )
    #
    # complete_years = [ '2015', '2019', '2025', '2030', '2035', '2040', '2045', '2050' ]
    complete_years = [ str(a_year) for a_year in range(2015,2050+1,1) ]
    #
    for n in range( len( non_year_combination_list ) ):
        if len( non_year_combination_list_years[n] ) != len(complete_years):
            #
            this_existing_combination = non_year_combination_list[n]
            # print('flag 1', this_existing_combination )
            this_existing_combination.append( '' )
            # print('flag 2', this_existing_combination )
            this_existing_combination.append( non_year_combination_list_years[n][0] )
            # print('flag 3', this_existing_combination )
            ref_index = combination_list.index( this_existing_combination )
            this_existing_data_row = deepcopy( data_row_list[ ref_index ] )
            #
            for n2 in range( len(complete_years) ):
                #
                if complete_years[n2] not in non_year_combination_list_years[n]:
                    #
                    data_row = ['' for n in range( len( output_header ) ) ]
                    data_row[0] = 0
                    data_row[1] = non_year_combination_list[n][0]
                    data_row[3] = non_year_combination_list[n][1]
                    data_row[5] = non_year_combination_list[n][2]
                    data_row[7] = complete_years[n2]
                    #
                    for n3 in range( len( vars_as_appear ) ):
                        this_variable = vars_as_appear[n3]
                        this_var_dict = all_vars_output_dict[case][this_variable]
                        index = S_DICT_vars_structure['variable'].index( this_variable )
                        this_variable_indices = S_DICT_vars_structure['index_list'][ index ]
                        #
                        var_position_index = output_header.index( this_variable )
                        #
                        print_true = False
                        #
                        if ( 'f' in this_variable_indices and str(non_year_combination_list[n][0]) != '' ): # or ( 'f' not in this_variable_indices and str(non_year_combination_list[n][0]) == '' ):
                            print_true = True
                        else:
                            pass
                        #
                        if ( 't' in this_variable_indices and str(non_year_combination_list[n][1]) != '' ): # or ( 't' not in this_variable_indices and str(non_year_combination_list[n][1]) == '' ):
                            print_true = True
                        else:
                            pass
                        #
                        if ( 'e' in this_variable_indices and str(non_year_combination_list[n][2]) != '' ): # or ( 'e' not in this_variable_indices and str(non_year_combination_list[n][2]) == '' ):
                            print_true = True
                        else:
                            pass
                        #
                        if 'y' in this_variable_indices and ( str( this_existing_data_row[ var_position_index ] ) != '' ) and print_true == True:
                            data_row[ var_position_index ] = '0'
                            #
                        else:
                            pass
                    #
                    data_row_list.append( data_row )
   
    with open( output_adress + '/' + case_name + '_Output' + '.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow( output_header )
        for n in range( len( data_row_list ) ):
            csvwriter.writerow( data_row_list[n] )
   
    gc.collect(generation=2)
    time.sleep(0.05)
#%%    
def main_executer( n1 ):
    #
    set_txt_list( model_to_run )
    #
    file_aboslute_address = os.path.abspath("2_run_model_mathprog.py")
    file_adress = re.escape( file_aboslute_address.replace( '2_run_model_mathprog.py', '' ) ).replace( '\:', ':' )
    #
    print('$$')
    print( txt_list )
    print('$$')
    data_file = file_adress + r'2_Scenarios_Outputs\\' + str( txt_list[n1] )
    #
    str1 = "start /B start cmd.exe @cmd /k cd " + file_adress
    #
    output_file = data_file.replace('.txt','') + '_output' + '.txt'
    #
    str2 = "glpsol -m Long_Model.txt -d " + str( data_file )  +  " -o " + str(output_file)
    os.system( str1 and str2 )
    time.sleep(1)
    #
    print('I finished this run, now I will process')
    data_processor( n1 )
#%%    

global model_to_run
model_to_run = 'osemosyscr'
set_txt_list( model_to_run )


for n1 in range( len(txt_list) ):
    main_executer(n1)
    
#%% Here, we change the names of the fuels, technologies and emissions:

filename_orig = './2_Scenarios_Outputs/osemosyscr_data_'+sce+'_Output.csv'

df = pd.read_csv(filename_orig)
dfa = deepcopy( df )

#Technologies
dfa['Technology'] = dfa['Technology'].replace({'BACKSTOP_PS':'E_Backup Power Systems',
'BACKSTOP_TS':'Backup Transport Sector',
'BLENDDSL':'Blend Diesel',
'BLENDGAS':'Blend Gasoline',
'DBIO_El':'Biomass for electricity',
'DBIO_In':'Biomass for industry',
'DCOK_In':'Coke for industry',
'DDSL_Ag':'Diesel for agriculture',
'DDSL_El':'Diesel for electricity',
'DDSL_Eq':'Diesel for equipment',
'DDSL_HF':'Diesel for heavy freight transport',
'DDSL_In':'Diesel for industry',
'DDSL_LF':'Diesel for light freigth transport',
'DDSL_Pr':'Diesel for private transport',
'DDSL_Pu':'Diesel for public transport',
'DELAg':'Electricity for agriculture',
'DELCo':'Electricity for commerce',
'DELHF':'Electricity for heavy freight transport',
'DELIn':'Electricity for industry',
'DELLF':'Electricity for light freigth transport',
'DELPb':'Electricity for public service',
'DELPr':'Electricity for Private Transport',
'DELPu':'Electricity for Public Transport',
'DELRe':'Electricity for residencial',
'DFOI_El':'Fuel Oil for Electricity',
'DFOI_in':'Fuel Oil for Industry',
'DFWO_Co':'Wood for commerce',
'DFWO_In':'Wood for industry',
'DFWO_Re':'Wood for residential',
'DGSL_LF':'Gasoline for light freigth transport',
'DGSL_Pr':'Gasoline for private transport',
'DGSL_Pu':'Gasoline for public transport',
'DHYD_HF':'Hydrogen for heavy freight transport',
'DHYD_Pu':'Hydrogen for heavy public transport',
'DIST_FOI':'Distribution of Fuel Oil',
'DIST_FWO':'Distribution of Firewood',
'DIST_JFUEL':'Distribution of Jet Fuel',
'DIST_PCO':'Distribution of Petroleum Coke',
'DIST_DSL':'Distribution Diesel',
'DIST_GSL':'Distribution Gasoline',
'DIST_HYD':'Distribution Hydrogen',
'DIST_LPG':'Distribution LPG',
'DIST_NG':'Distribution Natural Gas',
'DJEFU_Ai':'Jet fuel air craft',
'DLPG_Co':'LPG for commerce',
'DLPG_HF':'LPG for heavy freight transport',
'DLPG_In':'LPG for industry',
'DLPG_LF':'LPG for light freight transport',
'DLPG_Pr':'LPG for private transport',
'DLPG_Pu':'LPG for public transport',
'DLPG_Re':'LPG for residential',
'DTRFF_hf':'Transport distribution demand fossil fuel heavy cargo',
'DTRFF_lf':'Transport distribution demand fossil fuel light cargo',
'DTRFF_pr':'Transport distribution demand fossil fuel private',
'DTRFF_pu':'Transport distribution demand fossil fuel public',
'DTRFF_rs':'Transport distribution demand fossil fuel ride sharing',
'DTRLC_hf':'Transport distribution demand Low carbon heavy cargo',
'DTRLC_lf':'Transport distribution demand Low carbon light cargo',
'DTRLC_pr':'Transport distribution demand Low carbon private',
'DTRLC_pu':'Transport distribution demand Low carbon public',
'DTRLC_rs':'Transport distribution demand Low carbon  ride sharing',
'DTRNM_Bk':'Transport distribution demand Bikes',
'DTRNM_Wk':'Transport distribution demand Walks',
'EDDISTAGR':'Electric Power Distribution for Agriculture',
'EDDISTCOM':'Electric Power Distribution for Commercial',
'EDDISTIND':'Electric Power Distribution for Industry',
'EDDISTPUB':'Electric Power Distribution for Public',
'EDDISTRES':'Electric Power Distribution for Residential',
'EDEBIOIND':'Biomass Distribution  Industry',
'EDEDSLAGR':'Diesel Distribution  Agriculture',
'EDEDSLIND':'Diesel Distribution  Industry',
'EDEFOIND':'Fuel Oil Distribution  Industry',
'EDEFWCOM':'Firewood Distribution  Commercial',
'EDEFWIND':'Firewood Distribution  Industry',
'EDEFWRES':'Firewood Distribution  Residential',
'EDEJFUAIR':'Jet fuel oil Distribution air',
'EDELGPCOM':'LGP Distribution  Commercial',
'EDELPGIND':'LPG Distribution  Industry',
'EDELPGRES':'LPG Distribution  Residential',
'EDEPCIND':'Petroleum Coke Distribution  Industry',
'ESIMPBIODSL':'Importing biodiesel',
'ESIMPDSL':'Importing Diesel',
'ESIMPETHAN':'Importing ethanol',
'ESIMPGAS':'Importing Gasoline',
'ESIMPJEFU':'Importing Jet Fuel',
'ESIMPLPG':'Importing LPG',
'ESIMPNG':'Importing Natural Gas',
'ESIMPOIFU':'Importing Oil Fuel',
'ESIMPPCO':'Importing Petroleum Coke',
'ESPROBIODSL':'Production biodiesel',
'ESPROBIOGAS':'Production biogas',
'ESPROETHAN':'Production ethanol',
'ESRNBIO':'Biomass Resources',
'ESRNFW':'Fire wood Resources',
'ESRNGEO':'Renewable Resource Geothermal',
'ESRNSUN':'Renewable Resource Solar',
'ESRNWAT':'Renewable Resource Water',
'ESRNWND':'Renewable Resource Wind',
'ESROMBIO':'Organic Material Resources',
'PPBIO001':'Biomass Power Plant (existing)',
'PPBIO002':'Biomass Power Plant (new)',
'PPDSL001':'Diesel Power Plant (existing)',
'PPDSL002':'Diesel Power Plant (new)',
'PPFOB001':'Oil Power Plant (existing)',
'PPFOB002':'Oil Power Plant (new)',
'PPGEO001':'Geothermal Power Plant (existing)',
'PPGEO002':'Geothermal Power Plant (new)',
'PPHDAM001':'Hydro Dam Power Plant (existing)',
'PPHDAM002':'Hydro Dam Power Plant (new)',
'PPHROR001':'Hydro Run of River Power Plant (existing)',
'PPHROR002':'Hydro Run of River Power Plant (new)',
'PPPVD001':'Photovoltaic Power Plant Distribution (existing)',
'PPPVD002':'Photovoltaic Power Plant Distribution (new)',
'PPPVT001':'Photovoltaic Power Plant Transmission (existing)',
'PPPVT002':'Photovoltaic Power Plant Transmission (new)',
'PPWND001':'Wind Power Plant Distribution (existing)',
'PPWND002':'Wind Power Plant Distribution (new)',
'PPWNT001':'Wind Power Plant Transmission  (existing)',
'PPWNT002':'Wind Power Plant Transmission (new)',
'PROD_HYD_CH4':'Production hydrogen CH4',
'PROD_HYD_H20':'Production hydrogen H2O',
'TDDIST01':'Electricity Distribution (existing)',
'TDDIST02':'Electricity Distribution (new)',
'TDMEREL01':'Imports of electricity',
'TDMEREL02':'Exports of electricity',
'TDTRANS01':'Electricity Transmission (existing)',
'TDTRANS02':'Electricity Transmission (new)',
'TI_BW_01':'Bikeway (existing)',
'TI_BW_02':'Bikeway (new)',
'TI_RaRo_01':'Railroad (existing)',
'TI_RaRo_02':'Railroad (new)',
'TI_RoNet_01':'Road network (existing)',
'TI_RoNet_02':'Road network (new)',
'TI_SW_01':'Sidewalk (existing)',
'TI_SW_02':'Sidewalk (new)',
'TRANOMOTBike':'No motorized transport bikes',
'TRANOMOTWalk':'No motorized transport Walk',
'TRBUSDSL01':'Bus Diesel (existing)',
'TRBUSDSL02':'Bus Diesel (new)',
'TRBUSELC02':'Bus Electric (new)',
'TRBUSHYBD02':'Bus Hybrid Electric-Diesel (new)',
'TRBUSHYD02':'Bus Hydrogen (new)',
'TRBUSLPG02':'Bus LPG (new)',
'TRFWDDSL01':'Four-Wheel-Drive (existing)',
'TRFWDDSL02':'Four-Wheel-Drive Diesel (new)',
'TRFWDELE02':'Four-Wheel-Drive Electric (new)',
'TRFWDGAS01':'Four-Wheel-Drive Gasoline (existing)',
'TRFWDGAS02':'Four-Wheel-Drive Gasoline (new)',
'TRFWDHYBD02':'Four-Wheel-Drive Hybrid Electric-Diesel (new)',
'TRFWDLPG01':'Four-Wheel-Drive LPG (existing)',
'TRFWDLPG02':'Four-Wheel-Drive LPG (new)',
'TRFWDPHYBD02':'Four-Wheel-Drive Plug-in Hybrid Electric-Diesel(new)',
'TRLDDSL01':'Light Duty Diesel (existing)',
'TRLDDSL02':'Light Duty Diesel (new)',
'TRLDELE02':'Light Duty Electric (new)',
'TRLDGAS01':'Light Duty Gasoline (existing)',
'TRLDGAS02':'Light Duty Gasoline (new)',
'TRLDHYBG02':'Light Hybrid Electric-Gasoline (new)',
'TRLDPHYBG02':'Light Plug-in Hybrid Electric-Gasoline  (new)',
'TRMBUSDSL01':'Microbus Diesel (existing)',
'TRMBUSDSL02':'Microbus Diesel (new)',
'TRMBUSELE02':'Microbus Electric (new)',
'TRMBUSHYBD02':'Microbus Hybrid Electric-Diesel (new)',
'TRMBUSHYD02':'Microbus Hydrogen (new)',
'TRMBUSLPG02':'Microbus LPG (new)',
'TRMIVDSL01':'Minivan Diesel (existing)',
'TRMIVDSL02':'Minivan Diesel (new)',
'TRMIVELE02':'Minivan Electric (new)',
'TRMIVGAS01':'Minivan Gasoline (existing)',
'TRMIVGAS02':'Minivan Gasoline (new)',
'TRMIVHYBD02':'Minivan Hybrid Electric-Diesel (new)',
'TRMIVHYBG02':'Minivan Hybrid Electric-Gasoline (new)',
'TRMIVLPG01':'Minivan LPG (existing)',
'TRMIVLPG02':'Minivan LPG (new)',
'TRMOTELC02':'Motorcycle electric (new)',
'TRMOTGAS01':'Motorcycle Gasoline (existing)',
'TRMOTGAS02':'Motorcycle Gasoline (new)',
'TRTAXDSL01':'Taxi Diesel (existing)',
'TRTAXDSL02':'Taxi Diesel (new)',
'TRTAXELC02':'Taxi Electric (new)',
'TRTAXGAS01':'Taxi Gasoline (existing)',
'TRTAXGAS02':'Taxi Gasoline (new)',
'TRTAXHYBD02':'Taxi Hybrid Electric-Diesel (new)',
'TRTAXHYBG02':'Taxi Hybrid Electric-Gasoline (new)',
'TRTAXLPG01':'Taxi LPG (existing)',
'TRTAXLPG02':'Taxi LPG (new)',
'TRXTRAIELEFRE02':'Train Electric for Freight (new)',
'TRXTRAINDSL01':'Train Diesel (existing)',
'TRXTRAINDSL02':'Train Diesel (new)',
'TRXTRAINELC02':'Train Electric (new)',
'TRYLFDSL01':'Mini Trucks (existing)',
'TRYLFDSL02':'Mini Trucks Diesel (new)',
'TRYLFELE02':'Mini Trucks Electric (new)',
'TRYLFGAS01':'Mini Trucks Gasoline (existing)',
'TRYLFGAS02':'Mini Trucks Gasoline (new)',
'TRYLFHYBD02':'Mini Trucks Hybrid Electric-Diesel (new)',
'TRYLFHYBG02':'Mini Trucks Electric-Gasoline (new)',
'TRYLFLPG01':'Mini Trucks LPG (existing)',
'TRYLFLPG02':'Mini Trucks LPG (new)',
'TRYTKDSL01':'Trucks Diesel (existing)',
'TRYTKDSL02':'Trucks Diesel (new)',
'TRYTKELC02':'Trucks Electric (new)',
'TRYTKHYBD02':'Trucks Hybrid Electric-Diesel (new)',
'TRYTKHYD02':'Trucks Hydrogen (new)',
'TRYTKLPG02':'Trucks LPG (new)',
'TRZAIR001':'Air (existing)',
'TRZSEQ001':'Special Equipment & Sea (existing)',
'Techs_4WD':'Four Wheel Drive',
'Techs_Buses':'Bus',
'Techs_LD':'Light Duty',
'Techs_Microbuses':'Minbus',
'Techs_Minivan':'Minivan',
'Techs_Motos':'Motorcycles',
'Techs_Taxis':'Taxis',
'Techs_Trains':'Rail'})

#Fuels
dfa['Fuel'] = dfa['Fuel'].replace({'E0BIODSL':'Biodisel imported or produced',
'E0DSL':'Diesel imported',
'E0DSLBLEND':'Diesel and biodiseal blend',
'E0ETHAN':'Ethanol  imported or produced',
'E0GSL':'Gasoline imported',
'E0GSLBLEND':'Gasoline and ethanol blend',
'E0LPG':'LPG imported',
'E0NATGAS':'Natural Gas imported',
'E1BIO':'Biomass energy',
'E1DSL':'Diesel',
'E1FOI':'Fuel Oil',
'E1FWO':'Firewood',
'E1GAS':'Gasoline',
'E1GEO':'Geothermal energy',
'E1GSL':'Gasoline',
'E1JEFU':'Jet Fuel',
'E1LPG':'Liquid Petroleum Gas',
'E1METH':'Methene',
'E1PCO':'Petroleum coke',
'E1SOL':'Solar energy',
'E1WAT':'Hydraulic energy',
'E1WIN':'Eolic Energy',
'E2ELC01':'Electricity Supply by Plants',
'E2HYD':'Hydrogen produced',
'E3ELC02':'Electricity for Transmission',
'E3ELC03':'Electricity for Distribution',
'E3ELC04':'Electricity Exports',
'E4ELC03AGR':'Agriculture  Electricity Demand',
'E4ELC03COM':'Commercial Electricity Demand',
'E4ELC03IND':'Industrial  Electricity Demand',
'E4ELC03PUB':'Public  Electricity Demand',
'E4ELC03RES':'Residential  Electricity Demand',
'E5BIOIND':'Biomass  for Industry',
'E5DSLAGR':'Diesel End Use Agriculture',
'E5DSLIND':'Diesel End Use Industry',
'E5FWCOM':'Firewood End Use Commercial',
'E5FWIND':'Firewood End Use Industry',
'E5FWRES':'Firewood End Use Residential',
'E5LGPCOM':'LGP End Use Commercial',
'E5LPGIND':'LPG End Use Industry',
'E5LPGRES':'LPG End Use Residential',
'E5OFIND':'Fuel Oil End Use Industry',
'E5PCIND':'Petroleum Coke End Use Industry',
'E6TDAIR':'Transport Demand Air',
'E6TDFREHEA':'Transport Demand Freigth Heavy',
'E6TDFRELIG':'Transport Demand Freigth Light',
'E6TDPASPRIV':'Transport Demand Passenger Private',
'E6TDPASSPUB':'Transport Demand Passenger Public',
'E6TDSPE':'Transport Demand Special Equipment & Sea',
'E6TRNOMOT':'Transport Demand Passenger No Motorize',
'E6TRRIDSHA':'Transport Demand Passenger Ride Sharing',
'E7BAG_In':'Baggase for Industry',
'E7BIKEWAYS':'Bikeways infrastructure',
'E7BIO_El':'Biomass for electricity',
'E7BIO_In':'Biomass  for Industry',
'E7COK_In':'Coke for Industry',
'E7DSL_Ag':'Diesel for agriculture',
'E7DSL_El':'Diesel for electricity',
'E7DSL_Eq':'Diesel for special equipment',
'E7DSL_HF':'Diesel for light heavy transport',
'E7DSL_In':'Diesel for industry',
'E7DSL_LF':'Diesel for light freight transport',
'E7DSL_Pr':'Diesel for private transport',
'E7DSL_Pu':'Diesel for public transport',
'E7ELAg':'Electricity for Agriculture',
'E7ELCo':'Electricity for Commerce',
'E7ELHF':'Electricity for heavy freight transport',
'E7ELInd':'Electricity for Industry',
'E7ELLF':'Electricity for light freight transport',
'E7ELPb':'Electricity for public service',
'E7ELPr':'Electricity for private transport',
'E7ELPu':'Electricity for public transport',
'E7ELRe':'Electricity for Commerce',
'E7FOI_El':'Fuel oil for electricity',
'E7FOI_In':'Fuel Oil for Industry',
'E7FWO_Co':'Wood for commerce',
'E7FWO_In':'Wood for industry',
'E7FWO_Re':'Wood for residential',
'E7GSL_LF':'Gasoline  for light freight transport',
'E7GSL_Pr':'Gasoline for private transport',
'E7GSL_Pu':'Gasoline for public transport',
'E7HYD_HF':'Hydrogen for heavy freight transport',
'E7HYD_Pu':'Hydrogen for public transport',
'E7JFU_Ai':'Jet fuel for aircraft',
'E7LPG_Co':'LPG for commerce',
'E7LPG_HF':'LPG for heavy freight transport',
'E7LPG_In':'LPG for industry',
'E7LPG_LF':'LPG for light freight transport',
'E7LPG_Pr':'LPG for private transport',
'E7LPG_Pu':'LPG for public transport',
'E7LPG_Re':'LPG for residential',
'E8Fossil_HF':'Demand Fossil Fuel Heavy Freight',
'E8Fossil_LF':'Demand Fossil Fuel Light Freight',
'E8Fossil_pri':'Demand Fossil Fuel Private',
'E8Fossil_pu':'Demand Fossil Fuel Public',
'E8Fossil_RS':'Demand Fossil Fuel RideSharing',
'E8LowCO2_HF':'Demand Low Carbon  Heavy Freight',
'E8LowCO2_LF':'Demand Low Carbon  Light Freight',
'E8LowCO2_pr':'Demand Low Carbon  Private',
'E8LowCO2_pu':'Demand Low Carbon  Public',
'E8LowCO2_RS':'Demand Low Carbon  RideSharing',
'E8NoMotor_B':'Demand No motorize Bikes',
'E8NoMotor_W':'Demand No motorize walk',
'E9ELESTOR_HF':'Electricity storage for heavy freight',
'E9ELESTOR_LF':'Electricity storage for light freight',
'E9ELESTOR_Pr':'Electricity storage for private vehicles',
'E9ELESTOR_Pu':'Electricity storage for public transport',
'E9ELESTORAGE':'Electricity storage',
'ETFREIGHT':'Cargo demand',
'ETPASSENGER':'Passanger demand',
'HYDROGEN':'Hydrogen',
'TIBIKEWAYS':'Bikeways infrastructure',
'TIRAILS':'Rails infrastructerestrucre',
'TIROADS':'Roads infrastructure',
'TISIDEWALKS':'Sidewalks infrastructure',
'FPr_4WD':'Private Transport in Four Wheel Drive',
'FPr_LightDuty':'Private Transport in Light Duty',
'FPr_Minivan':'Private Transport in Minivan',
'FPr_Moto':'Private Transport in Motorcycle',
'FPu_Buses':'Public Transport in Buses',
'FPu_Micros':'Public Transport in Minibus',
'FPu_Taxis':'Public Transport in Taxi',
'FPu_Train':'Transport in Rail',
'FHF_Trucks':'Fuels_Grouping_Heavy_Freight',
'FLF_PickUpTrucks':'Fuels_Grouping_Light_Freight'})

#Emissions
dfa['Emission'] = dfa['Emission'].replace({'C02_Freight':'Carbon Dioxide Freight',
'CO2_HeavyCargo':'Carbon Dioxide Heavy Cargo',
'CO2_LightCargo':'Carbon Dioxide Light Cargo',
'CO2_sources':'Carbon Dioxide Sources',
'CO2_Transport':'Carbon Dioxide Transport'})

dfa.to_csv ( './2_Scenarios_Outputs/osemosyscr_data_'+sce+'_Output_CODED.csv', index = None, header=True) #Coded file can be found here

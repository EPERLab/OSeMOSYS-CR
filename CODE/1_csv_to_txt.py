import xlrd
from copy import deepcopy
import pandas as pd

#Select the scenario you want to run
sce = 'BAU'
#sce ='SR20'
#sce = 'SR15'

file_table1 = './0_Model Structure/STRUCTURE_OSEMOSYS_CR.xlsx'
file_txt = './0_Model Structure/osemosyscr.txt'
if sce == 'BAU':
    pre_file_name = './1_Scenarios_Inputs/0_BAU/'
if sce == 'SR20':
    pre_file_name = './1_Scenarios_Inputs/1_SR20/'
if sce == 'SR15':
    pre_file_name = './1_Scenarios_Inputs/2_SR15/'

def listing_momani_input( data_lines, S_DICT_params_structure, S_DICT_sets_structure ):
    #
    list_set = []
    list_set_elements = []
    #
    list_param = []
    list_param_default_value = []
    list_param_elements = []
    #
    for n in range( len( data_lines ) ):
        #
        if 'set ' in data_lines[n]:
            this_line = data_lines[n].replace('\n','').split(':=')
            #
            this_set = this_line[0].replace('set','').replace(' ','')
            list_set.append( this_set )
            #
            these_elements = this_line[1].split(' ')
            these_elements.remove(';')
            these_elements.remove('')
            list_set_elements.append( these_elements )
        #
        if 'param' in data_lines[n]:
            this_line = data_lines[n].replace('\n','').split('default')
            #
            this_param = this_line[0].replace('param','').replace(' ','')
            #
            if this_param in S_DICT_params_structure['parameter']:
                list_param.append( this_param )
                #
                this_default_value = this_line[1].replace(':=','').replace(' ','')
                list_param_default_value.append( this_default_value )
                #
                # To extract the parameter input data:
                all_params_list_index = S_DICT_params_structure['parameter'].index(this_param)
                this_number_of_elements = S_DICT_params_structure['number_of_elements'][all_params_list_index]
                this_index_list = S_DICT_params_structure['index_list'][all_params_list_index]
                #
                list_param_elements.append({})
                for k in range(this_number_of_elements):
                    list_param_elements[-1].update({this_index_list[k]:[]})
                list_param_elements[-1].update({'value':[]})
                #
                inner_counter = 0
                reached_semicolon = False
                while reached_semicolon == False:
                    inner_counter+=1
                    this_line_inner = data_lines[n+inner_counter].replace('\n','')
                    #
                    if str(this_line_inner) == ';':
                        reached_semicolon = True
                    #
                    if '[' in this_line_inner:
                        this_listable_inner_line = this_line_inner.replace('[','').replace(']','').replace(':','').split(',')
                        usable_listable_inner_line = [r for r in this_listable_inner_line if str(this_listable_inner_line) != '*']
                        inferior_listable_inner_lines = []
                        #
                        reached_next_square_bracket = False
                        while reached_next_square_bracket == False:
                            inner_counter+=1
                            this_inferior_inner_line = data_lines[n+inner_counter].replace('\n','').replace(':=','')
                            #
                            if '[' in str(this_inferior_inner_line) or ';' in str(this_inferior_inner_line):
                                reached_next_square_bracket = True
                                inner_counter-=1
                            else:
                                inferior_listable_inner_lines.append( this_inferior_inner_line.split(' ') )
                        #
                        last_index_list = inferior_listable_inner_lines[0]
                        last_minus_one_index_lists = inferior_listable_inner_lines[1:]
                        #
                        for p in range( len(last_minus_one_index_lists) ): # p is for "penultima posición"
                            for v in range( len( last_index_list ) ): # v is for "values"
                                for k in range( len(this_index_list)-2 ):
                                    list_param_elements[-1][ this_index_list[k] ].append( usable_listable_inner_line[k] )
                                list_param_elements[-1][ this_index_list[k+1] ].append( last_minus_one_index_lists[p][0] )
                                list_param_elements[-1][ this_index_list[k+2] ].append( last_index_list[v] )
                                list_param_elements[-1][ 'value' ].append( last_minus_one_index_lists[p][v+1] )
                    #
                    else:
                        is_this_a_listable_inner_line = this_line_inner.split(' ')
                        if len( is_this_a_listable_inner_line ) > 1:
                            #
                            inner_counter -= 1
                            inferior_listable_inner_lines = []
                            #
                            reached_next_semicolon = False
                            #
                            while reached_next_semicolon == False:
                                inner_counter+=1
                                this_inferior_inner_line = data_lines[n+inner_counter].replace('\n','').replace(':=','')
                                #
                                if this_inferior_inner_line == ';':
                                    reached_next_semicolon = True
                                    inner_counter-=1
                                else:
                                    inferior_listable_inner_lines.append( this_inferior_inner_line.split(' ') )
                            #
                            last_index_list = inferior_listable_inner_lines[0]
                            last_minus_one_index_lists = inferior_listable_inner_lines[1:]
                            #
                            for p in range( len(last_minus_one_index_lists) ): # p is for "penultima posición"
                                for v in range( len( last_index_list ) ): # v is for "values"
                                    list_param_elements[-1][ this_index_list[0] ].append( last_minus_one_index_lists[p][0] )
                                    list_param_elements[-1][ this_index_list[1] ].append( last_index_list[v] )
                                    list_param_elements[-1][ 'value' ].append( last_minus_one_index_lists[p][v+1] )
                            #
    ###
    return list_set, list_set_elements, list_param, list_param_default_value, list_param_elements

def initial_code():
    #
    #-------------------------------------------#
    # 1 - Firstly, read the data structure to-be-used:
    #-------------------------------------------#
    table1 = xlrd.open_workbook(file_table1)
    sheet_sets_structure = table1.sheet_by_index(0) # 11 columns
    sheet_params_structure = table1.sheet_by_index(1) # 30 columns
    sheet_vars_structure = table1.sheet_by_index(2) # 43 columns
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
    # 1 - Firstly, extract data from the scenarios:
    with open(file_txt) as data_BAU_txt:
        data_BAU_lines = data_BAU_txt.readlines()
    # list_set_BAU, list_set_elements_BAU, list_param_BAU, list_param_default_value_BAU, list_param_elements_BAU = SPD_support.listing_momani_input( data_BAU_lines, S_DICT_params_structure, S_DICT_sets_structure )
    list_set_BAU, list_set_elements_BAU, list_param_BAU, list_param_default_value_BAU, list_param_elements_BAU = listing_momani_input( data_BAU_lines, S_DICT_params_structure, S_DICT_sets_structure )
    #
    #-------------------------------------------#
    # 3 - Thirdly, create inherited scenarios by manipulating an input around the value of a stable scenario:
    #futures_table = "Table2/Attribute_futures.csv"
    #equivalence_X_to_params = "Table2/Equivalence_X_to_Param.csv"
    #equivalence_natural_constraints_for_transport_demand = "Table2/Equivalence_NaturalConstraints.csv"
    #
    #changeable_scenario_list = ['BAU']
    #dict_futures, X_to_Param, future_ID_keys = function_B_lite( futures_table , equivalence_X_to_params , S_DICT_sets_structure, S_DICT_params_structure )
    ###
    return S_DICT_sets_structure, S_DICT_params_structure, list_param_BAU, list_param_default_value_BAU#, future_ID_keys

header_indices = ['Scenario','Parameter','r','t','f','e','m','l','y','ls','ld','lh','s','value']
S_DICT_sets_structure, S_DICT_params_structure, list_param_BAU, list_param_default_value_BAU = initial_code()
base_year = 2015

g= open( './2_Scenarios_Outputs/osemosyscr_data_'+sce+'.txt',"w+")
g.write( '###############\n#    Sets     #\n###############\n#\n' )
g.write( 'set DAILYTIMEBRACKET :=  ;\n' )
g.write( 'set DAYTYPE :=  ;\n' )
g.write( 'set SEASON :=  ;\n' )
g.write( 'set STORAGE :=  ;\n' )

for n1 in range( len( S_DICT_sets_structure['set'] ) ):
    if S_DICT_sets_structure['number_of_elements'][n1] != 0:
         g.write( 'set ' + S_DICT_sets_structure['set'][n1] + ' := ' )
         for n2 in range( S_DICT_sets_structure['number_of_elements'][n1] ):
             if S_DICT_sets_structure['set'][n1] == 'YEAR' or S_DICT_sets_structure['set'][n1] == 'MODE_OF_OPERATION':
                 g.write( str( int( S_DICT_sets_structure['elements_list'][n1][n2] ) ) + ' ' )
             else:
                 g.write( str( S_DICT_sets_structure['elements_list'][n1][n2] ) + ' ' )
         g.write( ';\n' )
        #
g.write( '\n' )
g.write( '#####################\n#    Parameters     #\n#####################\n#\n' )


#file_list = os.listdir( './2_Parameters/1_Integration' )

for p in range( len(list_param_BAU) ):
    this_param = list( list_param_BAU )[p]
    default_value_list_params_index = list_param_BAU.index( this_param )
    default_value = float( list_param_default_value_BAU[ default_value_list_params_index ].replace( ':','' ) )
    if default_value >= 0:
        default_value = int( default_value )
    else:
        pass

    this_param_index = S_DICT_params_structure['parameter'].index( this_param )
    this_param_keys = S_DICT_params_structure['index_list'][this_param_index]
    file_name = pre_file_name + str(this_param) + '.csv'
    df_param = pd.read_csv(file_name, index_col=None, header=0)

    if len( df_param ) != 0:
        if len(this_param_keys) != 2:
            g.write( 'param ' + this_param + ' default ' + str( default_value ) + ' :=\n' )
        else:
            g.write( 'param ' + this_param + ' default ' + str( default_value ) + ' :\n' )
            
#%%%
        if len(this_param_keys) == 2: #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            # get the last and second last parameters of the list:
            key_index_final = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-1])]
            last_set_element = df_param[ key_index_final ] # header_indices.index( this_param_keys[-1] ) ]
            last_set_element_unique = [] # list( set( last_set_element ) )
            for u in range( len( last_set_element ) ):
                if last_set_element[u] not in last_set_element_unique:
                    last_set_element_unique.append( last_set_element[u] )
                    #
            for y in range( len( last_set_element_unique ) ):
                g.write( str( last_set_element_unique[y] ) + ' ')
            g.write(':=\n')
                    #
            key_index_secondtolast = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-2])]
            second_last_set_element = df_param[ key_index_secondtolast ] # header_indices.index( this_param_keys[-2] ) ]
            second_last_set_element_unique = [] # list( set( second_last_set_element ) )
            for u in range( len( second_last_set_element ) ):
                if second_last_set_element[u] not in second_last_set_element_unique:
                    second_last_set_element_unique.append( second_last_set_element[u] )
                    #
            for s in range( len( second_last_set_element_unique ) ):
                g.write( second_last_set_element_unique[s] + ' ' )
                key_index_secondtolast = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-2])]
                value_indices = [ i for i, x in enumerate( df_param[ key_index_secondtolast ] ) if x == str( second_last_set_element_unique[s] ) ]
                these_values = []
                for val in range( len( value_indices ) ):
                    these_values.append( df_param['Value'][ value_indices[val] ] )
                for val in range( len( these_values ) ):
                    g.write( str( these_values[val] ) + ' ' )
                g.write('\n') #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#%%%
        if len(this_param_keys) == 3:
            this_set_element_unique_all = []
            for pkey in range( len(this_param_keys)-2 ):
                for i in range( 2, len(header_indices)-1 ):
                    if header_indices[i] == this_param_keys[pkey]:
                        header_name = S_DICT_sets_structure['initial'].index(header_indices[i])
                        header_index =S_DICT_sets_structure['set'][header_name]
                        this_set_element = df_param[header_index]
                this_set_element_unique_all.append( list( set( this_set_element ) ) )
            #
            this_set_element_unique_1 = deepcopy( this_set_element_unique_all[0] )
            #
            for n1 in range( len( this_set_element_unique_1 ) ): #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                g.write( '[' + str( this_set_element_unique_1[n1] ) + ',*,*]:\n' )
                # get the last and second last parameters of the list:
                key_index_last = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-1])]
                last_set_element = df_param[ key_index_last ] # header_indices.index( this_param_keys[-1] ) ]
                last_set_element_unique = [] # list( set( last_set_element ) )
                for u in range( len( last_set_element ) ):
                    if last_set_element[u] not in last_set_element_unique:
                        last_set_element_unique.append( last_set_element[u] )
                #
                for y in range( len( last_set_element_unique ) ):
                    g.write( str( last_set_element_unique[y] ) + ' ')
                g.write(':=\n')
                #
                key_index_secondtolast = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-2])]
                second_last_set_element = df_param[ key_index_secondtolast ]
                second_last_set_element_unique = [] # list( set( second_last_set_element ) )
               
                for u in range( len( second_last_set_element ) ):
                    if second_last_set_element[u] not in second_last_set_element_unique:
                        second_last_set_element_unique.append( second_last_set_element[u] )
                #
                for s in range( len( second_last_set_element_unique ) ):
                    g.write( second_last_set_element_unique[s] + ' ' )
                    #key_index_secondtolast = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-2])]
                    key_index_first = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[0])]
                    # print(this_param, this_param_keys[0], this_set_element_unique_1[n1], this_scenario_data[ this_param ][ this_param_keys[-2] ] )
                    # print(this_param, this_param_keys[-2], second_last_set_element_unique[s], this_scenario_data[ this_param ][ this_param_keys[0] ] )
                    value_indices_s = [ i for i, x in enumerate( df_param[ key_index_secondtolast  ] ) if x == str( second_last_set_element_unique[s] ) ]
                    value_indices_n1 = [ i for i, x in enumerate( df_param[ key_index_first  ] ) if x == str( this_set_element_unique_1[n1] ) ]
                    # print( len(value_indices_s) , value_indices_s )
                    # print( len(value_indices_n1) , value_indices_n1 )
                    r_index = set(value_indices_s) & set(value_indices_n1)
                    # print( r_index )
                    value_indices = list( r_index )
                    value_indices.sort()
                    # print( value_indices )
                    #
                    # these_values = this_scenario_data[ this_param ]['value'][ value_indices[0]:value_indices[-1]+1 ]
                    these_values = []
                    for val in range( len( value_indices ) ):
                        these_values.append( df_param['Value'][ value_indices[val] ] )
                    for val in range( len( these_values ) ):
                        g.write( str( these_values[val] ) + ' ' )
                    g.write('\n') #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        
#%%% 

        if len(this_param_keys) == 4:
            this_set_element_unique_all = []
            for pkey in range( len(this_param_keys)-2 ):
                for i in range( 2, len(header_indices)-1 ):
                    if header_indices[i] == this_param_keys[pkey]:
                        header_name = S_DICT_sets_structure['initial'].index(header_indices[i])
                        header_index =S_DICT_sets_structure['set'][header_name]
                        this_set_element = df_param[header_index]
                        this_set_element_unique_all.append( list( set( this_set_element ) ) )
            #
            this_set_element_unique_1 = deepcopy( this_set_element_unique_all[0] )
            this_set_element_unique_2 = deepcopy( this_set_element_unique_all[1] )
            #
            for n1 in range( len( this_set_element_unique_1 ) ):
                for n2 in range( len( this_set_element_unique_2 ) ): #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    g.write( '[' + str( this_set_element_unique_1[n1] ) + ',' + str( this_set_element_unique_2[n2] ) + ',*,*]:\n' )
                    # get the last and second last parameters of the list:
                    key_index_last = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-1])]
                    last_set_element = df_param[ key_index_last ] # header_indices.index( this_param_keys[-1] ) ]
                    last_set_element_unique = [] # list( set( last_set_element ) )
                    for u in range( len( last_set_element ) ):
                        if last_set_element[u] not in last_set_element_unique:
                            last_set_element_unique.append( last_set_element[u] )
                    #
                    for y in range( len( last_set_element_unique ) ):
                        g.write( str( last_set_element_unique[y] ) + ' ')
                    g.write(':=\n')
                    #
                    key_index_secondtolast = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[-2])]
                    second_last_set_element = df_param[ key_index_secondtolast ]
                    second_last_set_element_unique = [] # list( set( second_last_set_element ) )
                    for u in range( len( second_last_set_element ) ):
                        if second_last_set_element[u] not in second_last_set_element_unique:
                            second_last_set_element_unique.append( second_last_set_element[u] )
                    #
                    for s in range( len( second_last_set_element_unique ) ):
                        g.write( str(second_last_set_element_unique[s]) + ' ' )
                        #
                        key_index_first = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[0])]
                        key_index_second = S_DICT_sets_structure['set'][S_DICT_sets_structure['initial'].index(this_param_keys[1])]
                        value_indices_s = [ i for i, x in enumerate( df_param[ key_index_secondtolast ] ) if x == str( second_last_set_element_unique[s] ) ]
                        value_indices_n1 = [ i for i, x in enumerate( df_param[key_index_first] ) if x == str( this_set_element_unique_1[n1] ) ]
                        value_indices_n2 = [ i for i, x in enumerate( df_param[key_index_second] ) if x == str( this_set_element_unique_2[n2] ) ]
                        if this_param == 'VariableCost':
                            r_index = set(value_indices_n1) & set(value_indices_n2)
                        else:
                            r_index = set(value_indices_s) & set(value_indices_n1) & set(value_indices_n2)
                        value_indices = list( r_index )
                        value_indices.sort()
                        #
                        # these_values = this_scenario_data[ this_param ]['value'][ value_indices[0]:value_indices[-1]+1 ]
                        these_values = []
                        for val in range( len( value_indices ) ):
                            these_values.append(  df_param['Value'][ value_indices[val] ] )
                        for val in range( len( these_values ) ):
                            g.write( str( these_values[val] ) + ' ' )
                        g.write('\n') #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#%%%   
        if len(this_param_keys) == 5:
            this_param_test = this_param
            techs = df_param['TECHNOLOGY']
            if this_param == 'EmissionActivityRatio':
                f_e = df_param['EMISSION']
            else:
                f_e = df_param['FUEL']  
            value = df_param['Value']
            for k in range(int(len(techs)/36)):
                index = int(36*k)
                g.write( '['+S_DICT_sets_structure['elements_list'][6][0]+',' + str( techs[index] ) + ',' + str( f_e[index] ) + ',*,*]:\n' )
                for p in range(S_DICT_sets_structure['number_of_elements'][0]):
                    g.write( str(base_year + p))
                    if p != (S_DICT_sets_structure['number_of_elements'][0] -1):
                        g.write(' ')
                g.write(':=\n')
                g.write('1 ')
                for p in range(S_DICT_sets_structure['number_of_elements'][0]):
                    index_value = 36*k + p
                    g.write(str(value[index_value]) + ' ')
                g.write(' \n')            
                                
        g.write( ';\n\n' )                             
#%%%
g.write('param AccumulatedAnnualDemand default 0 :=\n;\n')
g.write('param AnnualEmissionLimit default 99999 :=\n;\n')
g.write('param AnnualExogenousEmission default 0 :=\n;\n')
g.write('param CapacityOfOneTechnologyUnit default 0 :=\n;\n')
g.write('param CapitalCostStorage default 0 :=\n;\n')
g.write('param Conversionld default 0 :=\n;\n')
g.write('param Conversionlh default 0 :=\n;\n')
g.write('param Conversionls default 0 :=\n;\n')
g.write('param DaySplit default 0.00137 :=\n;\n')
g.write('param DaysInDayType default 7 :=\n;\n')
g.write('param DepreciationMethod default 1 :=\n;\n')
g.write('param DiscountRate default 0.05 :=\n;\n')
g.write('param MinStorageCharge default 0 :=\n;\n')
g.write('param ModelPeriodEmissionLimit default 99999 :=\n;\n')
g.write('param ModelPeriodExogenousEmission default 0 :=\n;\n')
g.write('param OperationalLifeStorage default 1 :=\n;\n')
g.write('param REMinProductionTarget default 0 :=\n;\n')
g.write('param RETagFuel default 0 :=\n;\n')
g.write('param RETagTechnology default 0 :=\n;\n')
g.write('param ReserveMargin default 0 :=\n;\n')
g.write('param ReserveMarginTagFuel default 0 :=\n;\n')
g.write('param ReserveMarginTagTechnology default 0 :=\n;\n')
g.write('param ResidualStorageCapacity default 0 :=\n;\n')
g.write('param StorageLevelStart default 0 :=\n;\n')
g.write('param StorageMaxChargeRate default 0 :=\n;\n')
g.write('param StorageMaxDischargeRate default 0 :=\n;\n')
g.write('param TechnologyFromStorage default 0 :=\n;\n')
g.write('param TechnologyToStorage default 0 :=\n;\n')
g.write('param TotalAnnualMaxCapacityInvestment default 99999 :=\n;\n')
g.write('param TotalAnnualMinCapacity default 0 :=\n;\n')
g.write('param TotalTechnologyAnnualActivityUpperLimit default 99999 :=\n;\n')
g.write('param TotalTechnologyModelPeriodActivityLowerLimit default 0 :=\n;\n')
g.write('param TradeRoute default 0 :=\n;\n')
        #

g.write('#\n' + 'end;\n')
        #

g.close()

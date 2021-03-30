from arcgis.gis import *
from IPython.display import display
from arcgis.features import *
import time


'''
Script to move data between two identical arcGIS features for the purpose of updating the TARGET features
Deletes features based on the index column id_col_target on the TARGET layer
Some columns can throw HTML errors on the append --- include those columns in the col list
'''

#################### BEGIN PARAMS ####################

## AGOL DETAILS
target_url = 'https://www.arcgis.com'
# target_username = 'AGOLUSER'
target_password = 'AGOLPASSWORD'

## PORTAL DETAILS
source_url = 'YOURArcGISPortal.org/portal'
# source_username = 'PORTAL USER'
source_password = 'PORTALPASSWORD'

#the unique col that can be used to track the data
id_col_target = 'OBJECTID'

#columns that throw the html error 400 in arcGIS api --
col = ['TASK_DESCRIPTION', 'PRIMARY_EMAIL']

def mod_call(f, col = col):
    # modifies the columns from col and removes '<' and '>' characters
    # returns (f) the list iterator
    for x in col:
        try:
            f.attributes[x] = f.attributes[x].replace('<', '')
            f.attributes[x] = f.attributes[x].replace('>', '')
        except:
            continue
    return(f)

def divide(list, n):

    for i in range(0, len(list), n):
        yield list[i:i+n]

def run_etl(source_id, target_id ,n=1000):

    '''
    executes the data overwrite of the target feature using the source feature

    input: ESRI layer ID source, target, n(default=1000) is the split size for the data transfer

    return: # of items on the target and source layers after the write, and time per pair of ID's
                failure outpus .log file into root directory
    '''

    start_time = time.time()
    source_gis = GIS(source_url, username=source_username,
              password=source_password,
             verify_cert = False)

    source = Item(source_gis,itemid=source_id)


    target_gis = GIS(target_url, username=target_username,
              password=target_password,
             verify_cert = False)

    target = Item(target_gis,itemid=target_id)



    try:
        source_layers = source.layers
        source_flayer = source_layers[0]

    except:
        source_layers = source.tables
        source_flayer = source_layers[0]

    try:
        target_layers = target.layers
        target_flayer = target_layers[0]
    except:
        target_layers = target.tables
        target_flayer = target_layers[0]




    for x in range(len(source_layers)):

       source_flayer = source_layers[x]
       target_flayer = target_layers[x]

       print("Portal Name: " + source_flayer.properties.name)
       print("AGOL Name: " + target_flayer.properties.name)

       source_fset = source_flayer.query()
       source_features = source_fset.features

       target_fset = target_flayer.query()
       target_features = target_fset.features

       if len(target_fset)> 0:
           try:
               target_flayer.manager.truncate()
           except Exception as e:
               print(e)

       feature_layer = [mod_call(f) for f in source_features]
       div_feature_layer = list(divide(feature_layer, n))
       try:
           for v in range(len(div_feature_layer)):
               target_flayer.edit_features(adds=div_feature_layer[v])
       except Exception as e:
           print(e)
           continue


    end_time = time.time()

    return(print('\nSource Count: {}\nWrote {} records on the target table in {} seconds'.format(len(source_flayer.query()),len(target_flayer.query()) , round(end_time - start_time))))

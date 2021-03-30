# ESRI_Portal_AGOL_ETL
A script for simple Data ETL between [ESRI Portal](https://enterprise.arcgis.com/en/portal/) &amp; [ArcGIS Online](https://www.arcgis.com/index.html).
This script came out of the 
need to publish data from ESRI Portal 
to ArcGIS online a specified interval. 

------
## Usage

### Setup Parameters
In the `portal_agol.py` edit the `target` and `source` credentials represneting the ESRI Portal and ArcGIS online accounts respectively as needed.

### Python Usage
``` python
import ESRI_Portal_AGOL_ETL as agol

id_list  = [['a5d80126330c411234fb5a346311c69c1','bcaabedb9f97421346cc85d4fa77feb']] 

for x in id_list:
  agol.run_etl(source_id=x[0], target_id=x[1])
```

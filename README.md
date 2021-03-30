# ESRI_Portal_AGOL_ETL
A script for simple Data ETL between [ESRI Portal](https://enterprise.arcgis.com/en/portal/) &amp; [ArcGIS Online](https://www.arcgis.com/index.html)

## Usage
``` python
import ESRI_Portal_AGOL_ETL as agol

id_list  = [['a5d80126330c411234fb5a346311c69c1','bcaabedb9f97421346cc85d4fa77feb']] 

for x in id_list:
  agol.run_etl(source_id=x[0], target_id=x[1])
```

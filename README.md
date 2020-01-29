# Open Hazards PH QGIS Browser
**Open Hazards PH QGIS Browser** is a Python script that you can run in QGIS that lets you add geospatial hazard data created by various agencies in the Philippines as connections in the QGIS Browser. It currently adds WMTS from [https://github.com/maning/open-hazards-ph](https://github.com/maning/open-hazards-ph).

It is inspired by Klas Karlsson's ([@klakar](https://github.com/klakar)) [qgis_basemaps.py](https://github.com/klakar/QGIS_resources/blob/master/collections/Geosupportsystem/python/qgis_basemaps.py) script.

## HOW-TO
### Open the QGIS Python Console (CTRL + ALT + P)
### Click Show Editor (the icon that looks like a notepad with a pen)
### Copy the code below (or the content of open_hazards_ph_qgis_browser.py) in the editor
```python
"""
This script should be run from the Python Console inside QGIS (CTRL + ALT + P).

It adds online sources to the QGIS Browser.
Each source should contain a list with the following items (string type):
[sourcetype, title, authconfig, password, referer, url, username]

You can add or remove sources from the sources section of the code.

Script by Ben Hur Pintor

License: GPLv3

Regarding the terms of use for these background maps YOU will need to verify that you
follow the individual EULA that comes with the different services,
Most likely they will restrict how you can use the data.

"""

# Add sources
sources = []

sources.append(["connections-wms","NOAH Storm Surge SSA1", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqn7kn24phua2rpb4bronsjf/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","NOAH Storm Surge SSA2", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqn7ea9yphon2rpb8fbgkakw/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","NOAH Storm Surge SSA3", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqn7blqv00rl2rru9wm6fpbm/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","NOAH Storm Surge SSA4", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqn2fijg158t2smhiqyoq5e1/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","LiPAD 5-year Flood Hazard", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqrqpuiq3dl12rscralpdxyo/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","LiPAD 25-year Flood Hazard", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqrvwop80jpm2sqy4zu9v3c6/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","LiPAD 100-year Flood Hazard", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqrynb300m522sper0emmgs6/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])
sources.append(["connections-wms","LiPAD Landslide Hazard", "", "", "", "https://api.mapbox.com/styles/v1/osmph/cjqthna5u1mxq2rpcmg7ihe8h/wmts?access_token=sk.eyJ1Ijoib3NtcGgiLCJhIjoiY2pxbjF6czN2MGllbTQ4bXVuOW44ZDlpbSJ9.pUqHal3xOR1yZUaM6LbLkg", ""])

# Add sources to QGIS Browser
for source in sources:
	connectionType = source[0]
	connectionName = source[1]
	QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
	QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
	QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
	QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
	QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])

# Update GUI
iface.reloadConnections()
```

----
### If you want to load the data from open-hazards-ph, check put Open Hazards PH QGIS Plugin
* [Open Hazards PH QGIS Plugin](https://github.com/benhur07b/open-hazards-ph-qgis)

### Open Hazards PH QGIS Browser is maintained by:
* Ben Hur Pintor [[@benhur07b](https://github.com/benhur07b)]

### TO-DO/WISH LIST
* Add more data sources

### Pull Requests and Patches are most welcome!
Open Hazards PH QGIS Browser is on [Github](https://github.com/benhur07b/open-hazards-ph-qgis-browser).

----
## From open-hazards-ph
### What is the license of the data?
We respect the license of the original source, each data source and data files have a corresponding license file. License varies from different agencies, in most cases government data are public domain.

### Most data archived here are available in other government websites, why do this?
Philippine government data policy changes from the tenure of an administration to another, we want to ensure that what was public will remain public even if projects ran out of funds or there is a change in access policy.

### I found some cool hazards data, will you host it?
Yes! Please open a ticket on the [open-hazards-ph repo](https://github.com/maning/open-hazards-ph) and let's discuss.

### The open-hazards-ph repo is maintained by:
* Maning Sambale [[@maning](https://github.com/maning)]
* RK Aranas [[@rukku](https://github.com/rukku)]

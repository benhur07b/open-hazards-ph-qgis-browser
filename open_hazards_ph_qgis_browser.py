"""
This script should be run from the Python Console inside QGIS (CTRL + ALT + P).

It adds online sources to the QGIS Browser.
Each source should contain a list with the following items (string type):
[sourcetype, title, authconfig, password, referer, url, username]

You can add or remove sources from the sources section of the code.

Script by Ben Hur Pintor
License: GPLv3
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

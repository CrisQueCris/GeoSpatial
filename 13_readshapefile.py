# -*- coding: utf-8 -*-
"""
Created on Tue May 31 15:38:16 2022

@author: Lenovo
"""

'''
 1.3: Read shapefile data of farmers fields obtained from 
 [Agrarantrag Brandenburg](https://www.agrarantrag-bb.de/webClient_BB_P/).

1.3.1 read shapefiles using geopandas


'''

import geopandas as gpd
import matplotlib.pyplot as plt

fields = gpd.read_file('Data/AgrarantragBB/daten/129730080162_teilflaechen.shp')
fields.plot(cmap = 'jet', column = 'CODE') #plotting fields colored by the code of field use

fields.plot(cmap = 'jet', column = 'FLAECHE')

fields.crs #show coordinate system

#variable for global coordinate system:
epsg = '25833'

fields = fields.to_crs(epsg=epsg)


#fields without fill, only edgecolor

fields.plot(edgecolor = 'k', facecolor = 'none')

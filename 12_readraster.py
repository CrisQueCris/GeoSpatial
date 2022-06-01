# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:36:56 2022

@author: Lenovo
"""

import matplotlib.colors as colors
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#from termcolor import colored
from zipfile import ZipFile
from os.path import join
from glob import iglob
import pandas as pd
import numpy as np
import subprocess
import snappy
#import jpy



def output_view(product, band, min_value_VV, min_value_VH, max_value_VH):
    ''' Creates visualization
    product: snappy GPF product (input Sentinel-1 product)
    band: list (band of product to be visualized)
    min_value_VV: int (min value for color strech in VV band)
    max_value_VV: int (max value for color strech in VV band)
    min_value_VH: int (min value for color strech in VH band)
    max_value_VV: in (max value for color strech in VH band)
    '''
    band_data_list = []
    
    for i in band:
        band = product.getBand(i)
        w = band.getRasterWidth()
        h = band.getRasterHeight()
        band_data = np.zeros(w*h, np.float32)
        band_data.shape = h,w
        band_data_list.append(band_data)

    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(16,16))
    ax1.imshow(badn_data_list[0], cmap='gray', vmin=min_value_VV, vmax=max_valueVV)
    ax1.set_title(output_band[0])
    ax2.imshow(band_data_list[1], cmap='gray', vmin=min_value_VH, vmax=max_value_VH)
    ax2.set_title(output_bands[1])

    for ax in fig.get_axes():
        ax.label_outer()
    return
            
print(subprocess.Popen(['gpt', '-h'], stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]) #get decription of operators



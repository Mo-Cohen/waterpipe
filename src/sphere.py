#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:51:33 2021

@author: s1144983
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as mpl_cm
import iris, cartopy
import cartopy.crs as ccrs
import gif

savepath = '/exports/csce/datastore/geos/users/s1144983/um_data/ch1_control/gifs'
tall = iris.load('/exports/csce/datastore/geos/groups/aerosol/maureen/um_data/control_85km.nc')
hot = mpl_cm.get_cmap('hot')
blues = mpl_cm.get_cmap('Blues_r')

image = plt.imread('/home/s1144983/other_research/anistropic_diff/Images/Synthetic_data/stars1.jpg')

@gif.frame
def temp_sphere(cubes,i):
                                 
    for cube in cubes:
        if cube.standard_name == 'surface_temperature' and len(cube.cell_methods) == 0:
            surface_temp = cube.copy()
    
    lon = np.linspace(-180,180,144)
    lat = np.linspace(-90,90,90)
    
    ortho = ccrs.Orthographic(central_longitude=i,central_latitude=0)
    
    fig = plt.figure()
    # fig, ax0 = plt.subplots(figsize=(5,5))
    # ax0.imshow(image)
    fig.patch.set_facecolor('black')
    ax1 = plt.axes(projection=ortho)
    ax1.set_global()
    
    # ax.gridlines()
    ax1.contourf(lon, lat, np.roll(surface_temp[-1,:,:].data, 72, axis=1), transform=ccrs.PlateCarree(), cmap=hot)


temp_frames = []
for i in range(0,360,30):
    temp_frame = temp_sphere(tall,i)
    temp_frames.append(temp_frame)    

gif.save(temp_frames, str(savepath) + '/temp_sphere_fast_nolines.gif', duration = 12, unit = 's', between='startend')

   


@gif.frame
def cloud_sphere(cubes,i, t):
    
    for cube in cubes:
        if cube.long_name == 'cloud_area_fraction_assuming_maximum_random_overlap':
            cloud_cover = cube.copy()
            
    lon = np.linspace(-180,180,144)
    lat = np.linspace(-90,90,90)
    
    ortho = ccrs.Orthographic(central_longitude=i,central_latitude=0)
    
    fig = plt.figure()
    # fig, ax0 = plt.subplots()
    # ax0.imshow(image)
    # ax0.set_axis_off()
    fig.patch.set_facecolor('black')
    ax = plt.axes(projection=ortho)
    ax.set_global()
    
    ax.contourf(lon, lat, np.roll(cloud_cover[t,:,:].data, 72, axis=1), transform=ccrs.PlateCarree(), cmap=blues)
    plt.show()

    
cloud_frames = []
for i in range(0,360,30):
    cloud_frame = cloud_sphere(tall,i,int(i/30))
    cloud_frames.append(cloud_frame)
    
gif.save(cloud_frames, str(savepath) + '/clouds_sphere.gif', duration = 12, unit = 's', between='startend')
        
            
        
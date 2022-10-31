#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# INTERACTIVE JOINT PLOTS
# This routine shows how to plot joint spatial variables and 
# by launching two funtctions which listen the mouse click, 
# oen cal click on the left-side plot to plot the same point 
# on the right-side map. 

Created on Mon Oct 31 14:29:53 2022

@author: orianif
"""
import numpy as np
import matplotlib.pyplot as plt
font = {'family' : 'DejaVu Sans',
        'size'   : 14}

# CREATE A FAKE DATASET
n=100 # number of samples
x=np.random.rand(n) #coords
y=np.random.rand(n)
var1=np.random.rand(n) # variables
var2=np.random.rand(n)+np.sqrt(var1**2)
grid_var=np.random.rand(10,10) # grid variable
grid_extent=[np.min(x)-0.05,np.max(x)+0.05,np.max(y)+0.05,np.min(y)-0.05]

# EXPLORATORY PLOTS
fig=plt.figure()
# left-side plot
h=plt.subplot(1,2,1)
plt.scatter(var1,var2)
plt.xlabel('var1')
plt.ylabel('var2')
plt.title('var2 vs var1')

# right-side plot
h2=plt.subplot(1,2,2)
plt.imshow(grid_var,extent=grid_extent)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('map view')
ni=0

# DEFINE CALLBACK FUNCTIONS
def onclick(event): # on mouse click do...
    # get click coordinates
    global ix, iy, ni 
    ix, iy = event.xdata, event.ydata
    dx=(ix-var1)/np.std(var1) 
    dy=(iy-var2)/np.std(var2)
    D=np.sqrt(dx**2+dy**2)
    ind=np.argmin(D)
    print((var1[ind],var2[ind]))
    
    # detect the point in the plot and map
    h.scatter(var1[ind],var2[ind],marker='+',c='r') 
    h.text(var1[ind],var2[ind],str(ni))
    plt.draw()
    h2.scatter(x[ind],y[ind],marker='+',c='r')
    h2.text(x[ind],y[ind],str(ni))
    plt.draw()
    ni=ni+1

def onclose(event): # on figure close do..
    # disconnect listening functions
    fig.canvas.mpl_disconnect(cid)
    fig.canvas.mpl_disconnect(cid2)
    print('figure closed')

# connect listening functions
cid = fig.canvas.mpl_connect('button_press_event', onclick)
cid2 = fig.canvas.mpl_connect('close_event', onclose)
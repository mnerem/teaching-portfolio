#!/usr/bin/env python
# coding: utf-8

# (2018-Spring-PHYS112-Grade-Analysis)=
# # Grade Analysis
# 
# ````{panels}
# CRN: 20136 (TR Lectures)
# ^^^
# <style type="text/css">
# .tg  {border-collapse:collapse;border-spacing:0;}
# .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   overflow:hidden;padding:5px 5px;word-break:normal;}
# .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
# </style>
# <table class="tg">
# <thead>
#   <tr>
#     <th class="tg-zv4m"><span style="font-weight:bold">Semester</span>:</th>
#     <th class="tg-zv4m">Spring 2018</th>
#   </tr>
# </thead>
# <tbody>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Meet Time</span>:</td>
#     <td class="tg-zv4m">TR 11:00am - 12:15pm</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Credit Hours</span>:</td>
#     <td class="tg-zv4m">4</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Class Size</span>:</td>
#     <td class="tg-zv4m">100</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">DFWI</span>:</td>
#     <td class="tg-zv4m">9</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Effective Score</span>:</td>
#     <td class="tg-zv4m">3.88</td>
#   </tr>
# </tbody>
# </table>
# 
# ---
# CRN: 22895 (MWF Lectures)
# ^^^
# <style type="text/css">
# .tg  {border-collapse:collapse;border-spacing:0;}
# .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   overflow:hidden;padding:5px 5px;word-break:normal;}
# .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
#   font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
# .tg .tg-zv4m{border-color:#ffffff;text-align:left;vertical-align:top}
# </style>
# <table class="tg">
# <thead>
#   <tr>
#     <th class="tg-zv4m"><span style="font-weight:bold">Semester</span>:</th>
#     <th class="tg-zv4m">Spring 2018</th>
#   </tr>
# </thead>
# <tbody>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Meet Time</span>:</td>
#     <td class="tg-zv4m">MWF 11:00am - 11:50am</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Credit Hours</span>:</td>
#     <td class="tg-zv4m">4</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Class Size</span>:</td>
#     <td class="tg-zv4m">42</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">DFWI</span>:</td>
#     <td class="tg-zv4m">6</td>
#   </tr>
#   <tr>
#     <td class="tg-zv4m"><span style="font-weight:bold">Effective Score</span>:</td>
#     <td class="tg-zv4m">4.71</td>
#   </tr>
# </tbody>
# </table>
# 
# 
# ````

# Homework was manage through
# Mastering Physics and Turning Point Technologies
# for classroom participation. There was one incident
# a student caught cheating on an exam. A voluntary
# resolution was agreed on by the instructor and stu-
# dent and the incident was not upgraded any further.
# The mean class grade was an 82% with a standard
# deviation of 17.74%. There is a concerning spike of A
# grades in the course. The A spike was created by two
# compounding factors. The first is that the cut off for
# an A in the course was a 93% or higher. The second
# factor formed from an attempt to assist students at
# the lower end of the curve. The instructor created
# copious amounts of extra credit points on each exam
# and homework. The end result was that the excellent 
# and above average students were able to use the
# extra credit points to inflate their grades towards a
# 100%. While the below average students were not
# taking advantage of the extra credit opportunities.
# The next time this course is taught, the instructor
# will cut down the amount of extra credit opportunities 
# and seek other methods to assist the students
# that are struggling the most with the material.

# In[1]:


# import modules
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rc
# set font to tex interpreter
rc('text',usetex=True)
rc('font',family='serif')
import numpy as np
plt.ion()

gb=[None]*2
gb[0]=pd.read_excel('gc_PHYS112.xlsx',sheet_name='20136')
gb[1]=pd.read_excel('gc_PHYS112.xlsx',sheet_name='22895')

def MakeHistogram(x,*args):
    plt.subplots(figsize=(13,7))
    FACECOLOR=np.array([80,146,220])/255

    if np.max(x)>100:
        bins2plot=np.arange(0,np.max(x)+5,5)
    else:
        bins2plot=np.arange(0,105,5)
    n, bins, patches = plt.hist(x,bins=bins2plot,
                                edgecolor=None,
                                linewidth=.1,
                                facecolor=FACECOLOR,
                                )

    # Gaussian model of data
    MEAN = np.mean(x)
    STD = np.std(x)
    VAR = np.var(x)
    HEIGHT=max(n)
    def ygauss(X):
        return np.exp(-(X-MEAN)**2/(2*STD**2))

    # define range of x values to plot the fits to histogram
    
    xfitmax = np.max(x)
    if np.max(x) > 100:
        xfitmax = np.max(x)
    if xfitmax < 100:
        xfitmax = 100

    '''
    if STD*2+MEAN > np.max(x):
        xfitmax = STD*2+MEAN 
        
    # plot vertical bars representing the mean and standard deviations on histogram
    xstd = np.array([-2*STD, -1*STD, 1*STD, 2*STD]+MEAN)
    ystd = HEIGHT*ygauss(xstd)
    plt.plot([MEAN, MEAN], [0, HEIGHT*ygauss(MEAN)],
             color='red',
             linestyle='--',
             linewidth=1,
            )
    for ii in np.arange(0, xstd.shape[0]):
        plt.plot([xstd[ii],xstd[ii]],[0,ystd[ii]] ,
                 color='black',
                 linewidth=1,
                 linestyle='--'
                )

    # plot curve of gaussian fit to the histogram
    xfit = np.linspace(0,xfitmax,100)
    yfit = HEIGHT*ygauss(xfit)
    plt.plot(xfit,yfit,linewidth=1)
    '''

    # add title and axis labels
    plt.text(200,375,
             'mean $=$ %.2f \n median $=$ %.2f \n std $=$ %.2f' %(MEAN,np.median(x), STD),
             va='center',
             ha='right',
             backgroundcolor='white',
             fontsize=16,
             bbox=dict(boxstyle='round', facecolor='wheat'),
             transform=None
            )
    plt.xlabel('Percent Grade',fontsize=18)
    plt.ylabel('Count',fontsize=18)
    if len(args)!=0:
        plt.title(args[0],fontsize=20)
    plt.xticks(np.arange(0,xfitmax+5,5),fontsize=16)
    plt.yticks(fontsize=16)
    plt.grid(True)
    


# ## Final Course Grade distributions

# In[2]:


MakeHistogram(gb[0]['Course Grade'],'PHYS112 20136 Course Grades')
MakeHistogram(gb[1]['Course Grade'],'PHYS112 22895 Course Grades')


# ## Lab Grades

# In[3]:


MakeHistogram(gb[0]['Lab'],'PHYS112 20136 Lab Grades')
MakeHistogram(gb[1]['Lab'],'PHYS112 22895 Lab Grades')


# ## HW Grades

# In[4]:


MakeHistogram(gb[0]['HW'],'PHYS112 20136 HW Grades')
MakeHistogram(gb[1]['HW'],'PHYS112 22895 HW Grades')


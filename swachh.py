import numpy as np					#import NumPy library
import matplotlib.mlab as mlab   
import matplotlib.pyplot as plt 			#import matplot Library for plotting histogram
import seaborn as sns					#import seaborn library to aid matplot since it looks way cooler
import pandas as pd
data = pd.read_excel("swachhbharat.xlsx", skiprows=5616, header=None, skipfooter=435, usecols = [4,5])
#Extract data from xlsx file into Pandas dataframe using integers from columns 5 & 6 and Uttar Pradesh rows
datanum = data.to_records(index=False)			#Converting Dataframe into NumPy array

i = 0							#Making array of fraction of ODF villages for each district
fraction = np.zeros(len(datanum))
for districts in datanum:
	fraction[i] = (datanum[i][1])/(datanum[i][0])
	i = i+1

i = 0							#Defining Mean of the fractions							
sum = 0
for districts in fraction:
	sum = sum + fraction[i]
	i = i+1
mean = sum /len(fraction)

i = 0							#Defining Variance and Standard Deviation of the fractions
sum = 0
for districts in fraction:
	sum = sum + ((fraction[i]-mean)**2)
	i = i+1
var = sum/(len(fraction)-1)
stddev = var**(1/2)

print(mean)
print(var)
print(stddev)

sns.set()					
plt.hist(fraction)					#Plotting histogram of number of districts with certain fraction of ODF villages
plt.hlines(0.2730187077415753, 0, 1, linestyles='solid', linewidth=2, colors='k') 	
plt.vlines(0.4688791185878232, 0, 150, linestyles='solid', linewidth=2, colors='k')
plt.ylabel('Number of districts')
plt.xlabel('Fraction of ODF villages')
plt.title(r'Histogram of number of districts with a certain fraction of ODF villages')
plt.show()







''' The algorithm in this chapter for generating pink noise is conceptually simple but computationally expensive.
There are more efficient alternatives, like the Voss-McCartney algorithm.
Research this method, implement it, compute the spectrum of the result, and confirm that it has the desired relationship between power and frequency.'''

'''This script contains step by step analysis of the solution by Allen Downey with suitable screenshots/test file of the suitabl and important output'''

'''The fundamental idea of this algorithm is to ADD up SEVERAL SEQUENCES OF RANDOM NUMBERS that get updates at different sampling rates.
The FIRST SOURCE should get updated at EVERY TIME STEP; the SECOND SOURCE every OTHER TIME STEP, the THIRD SOURCE ever FOURTH TIME STEP, and so on.'''

'''Start --> With an array --> One row per timestep & one column for each white noise sources. Initially, 1st row and 1st column ae random and
rest of the array is Nan'''

import thinkdsp
import thinkplot
import thinkstats2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

nrows = 100
ncols = 5

array = np.empty((nrows, ncols))            #Return a new array of given shape and type, without initializing entries. Entries are empty they have garbage value.
np.savetxt('01_empty.txt', array)           #Save the 2D array in text file.
array.fill(np.nan)                          #np.nan --> means not a number.
np.savetxt('02_empty_nan.txt', array)
array[0,:] = np.random.random(ncols)        #zeroth row all the column #Return random floats in the half-open interval [0.0, 1.0).
np.savetxt('03_empty_column.txt', array)
array[:,0] =np.random.random(nrows)
np.savetxt('04_empty_rows.txt', array)      #zeroth column all rows.
np.savetxt('05_empty_6x6.txt',array[0:6])

'''The next step is to choose the locations where the random sources change.
If the number of rows is n, the number of changes in the first column is n, the number in the second column is n/2 on average, the number in the third column is n/4 on average, etc.
So the total number of changes in the matrix is 2n on average; since n of those are in the first column, the other n are in the rest of the matrix.
To place the remaining n changes, we generate random columns from a geometric distribution with p=0.5.
If we generate a value out of bounds, we set it to 0 (so the first column gets the extras).'''

p = 0.5                                     #probability of success.
n = nrows                                   #number of samples to be drawn.
cols = np.random.geometric(p, n)            #Draw samples from the geometric distribution. Draw 100 samples
cols[cols >= ncols] = 0
np.savetxt('06_geometric_distribtion.txt',cols)

'''Within each column, we choose a random row from a uniform distribution.
Ideally we would choose without replacement, but it is faster and easier to choose with replacement, and I doubt it matters.'''

rows = np.random.randint(nrows,size = n)    #Return random integers from low (inclusive) to high (exclusive).
                                            #Return random integers from the “discrete uniform” distribution of the specified dtype in the “half-open” interval [low, high).
                                            #If high is None (the default), then results are from [0, low).
np.savetxt('07_randint_random.txt',rows)

'''Placing random values at each position '''
array[rows, cols]=np.random.random(n)
np.savetxt('08_arrays_complete.txt',array)

'''Next we want to do a zero-order hold to fill in the NaNs. NumPy doesn't do that, but Pandas does.'''
df = pd.DataFrame(array)
np.savetxt('09_dataframe.txt',df.head(n))

filled = df.fillna(method='ffill', axis=0)
np.savetxt('10_dataframe_nan_replaced.txt',filled.head(n))

total = filled.sum(axis=1)
np.savetxt('11_total.txt',total.values)

''' Building a wave '''
wave = thinkdsp.Wave(total.values)
wave.plot()
plt.xlabel('Time (sec)')
plt.ylabel('Amplitude')
plt.savefig("01_wave.png")
plt.show()

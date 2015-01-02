# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 11:48:54 2014

@author: roonsy
"""

from pandas import DataFrame, Series
# (rahaugh) I added numpy
import numpy

def create_dataframe():
    '''
    Create a pandas dataframe called 'olympic_medal_counts_df' containing
    the data from the  table of 2014 Sochi winter olympics medal counts.  

    The columns for this dataframe should be called 
    'country_name', 'gold', 'silver', and 'bronze'.  

    There is no need to  specify row indexes for this dataframe 
    (in this case, the rows will  automatically be assigned numbered indexes).
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    # your code here
    d = {'country_name': Series(countries),
         'gold': Series(gold),
         'silver': Series(silver),
         'bronze': Series(bronze)}
    
    olympic_medal_counts_df = DataFrame(d)
    
    return olympic_medal_counts_df
    
omc = create_dataframe()

print omc

'''
###############################################################################
(rahaugh) start off piste
'''

'''
access and print a column
'''
print omc['country_name']
print omc['gold']
print omc['silver']
print omc['bronze']
# print omc['index'] - wondered if I could get hold of the indices in some way?

'''
can also project multiple columns
'''
print omc[['country_name', 'gold']]

'''
and do some searching
'''

# by index first, to get all columns
print omc.loc[0]
# and for a multiple indices
print omc.loc[[0,1]]
# no match some criteria (gold > 2)
print omc[omc['gold'] > 2]
# now do the same but also project a single column
print omc['country_name'][omc['gold'] > 2]

'''
vectorised functions
'''
print omc['bronze'].apply(numpy.mean)
b = omc['bronze']
av = b.apply(numpy.mean)
print av



'''
d = {'one': Series([1,2,3], index=['a','b','c']), 
     'two': Series([1,2,3,4], index=['a','b','c','d'])}
     
df = DataFrame(d)

print df.apply(numpy.mean)
'''

e = {'one': Series([1,2,3], index=['a','b','c'])}     
ef = DataFrame(e)

print ef.apply(numpy.mean)
print ef['one'].apply(numpy.mean)




'''
###############################################################################
(rahaugh) end off piste
'''
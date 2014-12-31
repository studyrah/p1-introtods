# -*- coding: utf-8 -*-

from pandas import *
from ggplot import *

"""
print diamonds

print diamonds.dtypes

p = ggplot(aes(x='factor(cut)', y='depth'), data=diamonds)

p = p + geom_point()

print p


print mtcars.head

p = ggplot(aes(x='factor(cyl)',weight='mpg'), data=mtcars) + \
     geom_bar()
     
print p
"""

f = [("Apple","worm"),("Apple","spider"),("Orange","worm"),("Orange","worm")]

df = DataFrame(f,columns=["Fruit","Insect"])

print df


plot = ggplot(df, aes(x="Fruit",y="Insect")) + geom_bar(aes(position = "dodge")) + facet_grid("Insect")


print plot
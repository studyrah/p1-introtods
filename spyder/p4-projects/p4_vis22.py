from pandas import *
from ggplot import *

"""
shows ridership by day of week  but also highlights (via colour gradient)
the distribution by mean temperature
"""
def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    pandas.options.mode.chained_assignment = None
    turnstile_weather['DAYOFWEEKn'] = [datetime.strptime(d,'%Y-%m-%d').weekday() for d in turnstile_weather['DATEn']]    
    
    #
    # wanted to use geom_jitter to spread the densely packed points BUT
    # the level of spread was proporionate to the x value (therefore day 6
    # was markedly more spread than day 2 for example)
    #
    # the r version of ggplot2 has api to control the spread, python does not
    # currently implement this
    #
    # to achieve the same end, I created my own jitter using a technique
    # derived from - http://nbviewer.ipython.org/gist/fonnesbeck/5850463
    # (search for jitter)
    #
    turnstile_weather['DAYOFWEEKn'] = \
            [np.random.normal(d, 0.1) for d in turnstile_weather['DAYOFWEEKn']] 

    plot = ggplot(turnstile_weather, \
                aes(x='DAYOFWEEKn',y='ENTRIESn_hourly',color='meantempi')) +\
            geom_jitter(alpha=0.5) +\
            scale_color_gradient2(low='blue', high='red') +\
            ggtitle("Entries Per Hour By Day and Mean Temperature") +\
            ylab("Hourly Entries") +\
            xlab("Day of Week")

    # at a glance it actually looks like the busiest data points occurr at
    # colder times (BUT) switch the colours around and it tells a different
    # story

    return plot


print plot_weather_data(pandas.read_csv("./turnstile_data_master_with_weather.csv"))


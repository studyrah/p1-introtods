from pandas import *
from ggplot import *
#import ggplot as gg
import pandasql



def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''
    #print list(turnstile_weather.columns.values)
    
    # o.k. this is a dodgy place to do this logic but hey
    #
    # pandasql doesn't like the first unnamed column
    # I don't need it so bin it
    turnstile_weather = turnstile_weather.drop([turnstile_weather.columns[0]], axis=1)
    
    
    #
    # I want to separately plot weekday and weekend, so categorise the two
    #
    pandas.options.mode.chained_assignment = None
    turnstile_weather['Weekday'] = [1 if datetime.strptime(d,'%Y-%m-%d').weekday() < 5 else 0 for d in turnstile_weather['DATEn']]    
    
    q = """
        SELECT Hour, Weekday, AVG(ENTRIESn_hourly) AS avg_entries
        FROM turnstile_weather 
        GROUP BY Hour, Weekday
        """

    # Execute your SQL command against the pandas frame
    hourly_avg = pandasql.sqldf(q, locals())
    
    plot = ggplot(hourly_avg,aes('Hour','avg_entries',color='Weekday')) + \
            ggtitle("Average NYC Subway Turnstile Entries by Hour of the Day") +\
            ylab("Average Entries") +\
            xlab("Hour of Day") +\
            geom_point() +\
            geom_line() +\
            stat_smooth(colour='blue') +\
            theme(legend_title = element_text(colour="chocolate", size=16, face="bold")) + \
            xlim(0,23) + \
            ylim(0)
            
            

            
                
    return plot


print plot_weather_data(pandas.read_csv("./turnstile_data_master_with_weather.csv"))

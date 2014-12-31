import sys
import logging

#from util import reducer_logfile
#logging.basicConfig(filename=reducer_logfile, format='%(message)s',
#                    level=logging.INFO, filemode='w')
                    
logging.basicConfig(filename="./p1.log", format='%(message)s',
                    level=logging.INFO, filemode='w')
                    

def reducer():
    '''
    Given the output of the mapper for this exercise, the reducer should PRINT 
    (not return) one line per UNIT along with the total number of ENTRIESn_hourly 
    over the course of May (which is the duration of our data), separated by a tab.
    An example output row from the reducer might look like this: 'R001\t500625.0'

    You can assume that the input to the reducer is sorted such that all rows
    corresponding to a particular UNIT are grouped together.

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    '''

    iunit = 0
    ientries = 1

    total_entries = 0
    old_key = None

    for line in sys.stdin:

        # your code here
        line = line.strip()
        
        splits = line.split("\t")
        
        if splits[iunit] == old_key:
            total_entries += float(splits[ientries])
        else:
            if old_key != None:
                print old_key + "\t" + str(total_entries)
            
            old_key = splits[iunit]
            total_entries = 0
        
    if old_key != None:
        print old_key + "\t" + str(total_entries)
        
reducer()

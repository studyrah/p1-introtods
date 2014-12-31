import sys
import string
import logging


# (rahaugh) go to the command line and run:
#cat aadhaar_data.csv | python l2_mapper.py | python l2_reducer.py


#from util import reducer_logfile
#logging.basicConfig(filename=reducer_logfile, format='%(message)s',
#                    level=logging.INFO, filemode='w')

logging.basicConfig(filename="./l2_log.log", format='%(message)s',
                    level=logging.INFO, filemode='w')
                    
def mapper():

    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")

    headerline = sys.stdin.readline().strip()
    headers = headerline.split(",")
    
    idist = headers.index("District")
    iaadhaar = headers.index("Aadhaar generated")
    
    for line in sys.stdin:
        #your code here
        line = line.strip()
        splits = line.split(",")
        print splits[idist] + "\t" + splits[iaadhaar]

mapper()

# -*- coding: utf-8 -*-
import csv

def create_master_turnstile_file(filenames, output_file):
    '''
    Write a function that takes the files in the list filenames, which all have the 
    columns 'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn', and consolidates
    them into one file located at output_file.  There should be ONE row with the column
    headers, located at the top of the file.
    
    For example, if file_1 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    
    and another file, file_2 has:
    'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 3 ...
    line 4 ...
    line 5 ...
    
    We need to combine file_1 and file_2 into a master_file like below:
     'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn'
    line 1 ...
    line 2 ...
    line 3 ...
    line 4 ...
    line 5 ...
    '''
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
                
        for filename in filenames:
            
            with open(filename, 'rb') as orig:      

                filereader = csv.reader(orig, delimiter=',', quotechar='"')
               
                for row in filereader:                               
               
                   master_file.write(",".join(row) + "\n")



# note: too lazy to actually find or construct an appropriate input file(s),
# here I use the output from p5, which is in the right format but doesn't
# contain the header. Luckily the csv module kind of hides this problem
filenames = ["./updated_turnstile_110528.txt"]
create_master_turnstile_file(filenames, "./combine_turnstile_110528.txt")               


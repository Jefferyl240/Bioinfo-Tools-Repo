#!/usr/bin/env python3
#New York State Statewide COVID-19 Testing
#This program will parsing recrods of New York State Statewide COVID-19 Testing based on specific county of input.
#input csvfile from health.data.ny.gov/Health/New-York-State-Statewide-COVID-19-Testing/xdss-u53e
#Usage: $0 <datafile in csv>
#Author: Jie Lin
#Date: 4/26/2022

###############################################################################
import os #os lib for accessing the operating system.
import sys #sys package to access line arguments.

#Error checking:number of arguments
if len(sys.argv) != 2:
    print('Usage: %s <csv_datafile>' % (sys.argv[0]))
    print('Incorrect number of arguments. Please input correct number of arguments.')
    exit()
pathname = sys.argv[1] 
#Error checking:file read checks
existence = os.path.exists(pathname)
if not(existence):#checking if the file exist.
    print('the datafile is not exist.')
    exit()
readable_check = os.access(pathname, os.R_OK)
if not(readable_check):#checking if the file has read permission.
    print('the datafile has no read permission.')
    exit()
#program starts parsing the data file until all error checking have passed.
county = ''
df = []
#storing the csv data into nested list like [[, , , ,], [, , , , ,]]
#storing the cvs file into variable 'dataframe' in the format of list within a list.
with open(pathname) as in_file: #with open statement, no need to close file.
    for line in in_file.readlines():
        df.append(line.rstrip("\n").split(",")) #the input file is a comma separated file so that the split based on ',' and the '\n' character has no need in the list.
df.sort(key=lambda x: x[0]) #sorting by increasing date and date is the [0] for each sublists.
#function for finding the first positive case of a specific county.
def first_positive(county):
    for list1 in df:
        for item in list1:
            #if the positive number become non-zero, the loop would break and return the first positive date.
            if item == county:
                if int(list1[2]) == 0:
                    pass
                else:
                    return list1[0]
                    break     
county_data = []
#main function
#if the user passes an invalid entry at the prompt, the program should report that the name is not one of the county names and should report an alphabetical list of all possible county names to the user. 
while True: #The loop will keep going until a 'quit' message is inputed.
    county = input('Enter the name of a county, or enter "quit" to quit: ')
    if county == 'quit':
        exit()
    if county not in map(lambda x:x[1],df[:-1]):
        print('invalid county name, please choose from following county names:')
        #Using map() to get all county name from the list and use set() to get distinct county values, then convert to list for print and sorted() to obtain alphabetical order.
        print(sorted(list(set(map(lambda x:x[1],df[:-1]))))) 
    else:
        #if the county name is within the list, the parsing begin.
        print('\n%s County:' % (county))
        print('Test Date\tPositive\tTest Performed\tFrequency(Cumulative freq.)')
        #dispatching the nested list with double for-loops.
        for list1 in df:
            for item in list1:
                if item == county: #getting the data for the specific county.
                    #try function to eliminate divide by zero. 
                    try:
                        frequency = float(list1[2])/float(list1[4]) * 100
                    except ZeroDivisionError:
                        frequency = 0
                    try:
                        frequency_cumulative = float(list1[3])/float(list1[5]) *100
                    except ZeroDivisionError:
                        frequency_cumulative = 0
                    #gathering data about this chosen county for further parsing.
                    county_data.append([list1[0],int(list1[2]),int(list1[4]),frequency,frequency_cumulative,list1[3],list1[5]])
                    #dispatching information form nested list dataframe and output to user.
                    print('%s\t%s\t\t%s\t\t%.2f%%(%.2f%%)' % (list1[0],list1[2],list1[4],frequency,frequency_cumulative))
        #further parsing statstically.
        print('\nStatistics for %s County' % (county))
        print('First Positive discovered:', first_positive(county))
        #use map() to obtain data from the data of chosen county, then do corresponding calcualtion.
        print('Highest number of tests performed: ', max(county_data, key=lambda x:x[2])[2], 'on',max(county_data, key=lambda x:x[2])[0])
        print('Highest number of positives discoverd: ', max(county_data, key=lambda x:x[1])[1], 'on',max(county_data, key=lambda x:x[1])[0])
        #averaging all single day positive frequency for the specific county.
        print('Average positivity frequency: %.2f%%' % (sum(map(lambda x:x[3],county_data))/len(county_data)))
        #averaging cumulative positivity frequency.
        print('Average cumulative positivity frequency: %.2f%%' % (sum(map(lambda x:x[4],county_data))/len(county_data)))
        print('\n')

# This code file is used to test control codes in the laboratories

import datetime
import os
#Write the time at which it started and the intervals of the readings

#Create a class to write in the csv file all the data
#The columns will give the intensity and the error
def createCsvFileData(data):


    docName = 'power_readings_' #beginning name document
    date_time = datetime.datetime.now().strftime("%Y-%b-%d_%H-%M-%S")   #adds the time to the title to make it unique
    file_extension =  '.csv'    #needs the file extension in the name
    alreadyExists_str = 'second_'
    fileName = docName+date_time+file_extension
    columns = ['timestamp','power','error'] #determines the 3 columns of the file
    separator = ',' #separator between the 3 columns in a row
    format_columns = ['%s','%.6f','%.6f']   #the datatype of the columns

    #makes sure that the headings and the columns are of the same dimensions
    if len(data[0]) != len(columns):
        print ("The dimensions of the columns and headings are not equal")
        return

    #check if the file exists if needed in order not to overwrite
    if(os.path.exists(fileName)):
        print("The file already exists")
        fileName=docName+alreadyExists_str+date_time+file_extension

    #Specifies the path mode as writing 'w'
    file = open(fileName, 'w')

    #Writes an header/description of the document: time the measures started
    line = 'Intensity recordings for experiment starting at '+ str(data[0][0]) +'. readings every '+ str(data[1][0]-data[0][0]) + ' seconds\n'
    file.write(line)

    #each case of columns is separates on a line by a comma (separator),
    #concatenated and added to the file
    #line is a template for the format
    line = separator.join(columns)
    file.write('%s\n' % line)

    #for each new row in the data, give the correct type format
    format = separator.join(format_columns)
    for row in data:
        line= format % tuple(row)
        file.write('%s\n' % line)

    #close the file
    file.close()

def formatDateTime(date_time):
    date_time = date_time.strftime("%Y-%b-%d %H:%M:%S") #gives the correct format to the time

#Tests the functions written above
#data = [[datetime.datetime.now(),0.012345,0.000001],[datetime.datetime(2021,1,19),0.234567,0.000222]]
#screateCsvFileData(data)

#!/usr/bin/python

#FolderBoulder is a tool designed to enumerate folders and files
#on web servers.


import sys
import requests

# List of valid URLs found to exist
uncoveredURLs = []

# List for number of tried URLs
requestCounter = []

def displayHelp():
    print 'Usage: folderboulder.py <http://hostname> <foldernames> <filenames>'
    print ''
    print 'Example folderboulder.py foldernames.txt filenames.txt'

    
def openFolderFiles(foldernames,filenames,hostname):
    #Read filenames into list
    listOfFiles = []
    with open(filenames) as fn:
        for filenames in fn:
            listOfFiles.append(filenames.rstrip())

    
    #Open file of folder names
    with open(foldernames) as f:
        for foldername in f:
            foldername = foldername.rstrip()
            
            #Loop thru the listOfFiles list and append it to the URL
            for currentFileName in listOfFiles:
                currentFileName = currentFileName.rstrip()
                createHTTPrequest(hostname,foldername,currentFileName)
        

# Create the HTTP request and print the result    
def createHTTPrequest(hostname,foldername,currentFileName):
    r = requests.get(hostname+'/'+foldername+'/'+currentFileName)
    print('Trying: '+r.url+' HTTP Response:'+str(r.status_code))
    requestCounter.append('x')

    
    if str(r.status_code) == '200':
        uncoveredURL(r.url)
        

# Add any URL that gets a 200 response to the uncoveredURLs list     
def uncoveredURL(uncoveredURL):
    uncoveredURLs.append(uncoveredURL)

# Print the final result
def printResults():
    if len(uncoveredURLs) > 0:
    
        print ''
        print 'RESULT'
        print 'Number of requests made: '+str(len(requestCounter))
        print 'Number of Valid URLs found: '+str(len(uncoveredURLs))
        print 'The following URLs returned status code 200 and should be valid'
        for l in uncoveredURLs:
            print l.rstrip()
            
    else:
        print ''
        print 'RESULT'
        print 'Number of requests made: '+str(len(requestCounter))
        print 'Number of Valid URLs found: '+str(len(uncoveredURLs))
        print 'The server returned no 200 responses. Try another folder and file name list'


# A very quick and dirty way of "handling" missing command line arguments
if(len(sys.argv) < 3):
    displayHelp()
try:
    hostname = str(sys.argv[1])
    foldernames = str(sys.argv[2])
    filenames = str(sys.argv[3])
    openFolderFiles(foldernames,filenames,hostname)
    printResults()
except:
        print ''








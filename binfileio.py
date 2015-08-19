# This module provides binary file read and write methods

__author__ = "wyominggeezer"
__date__ = "$Aug 19, 2015 10:02:14 AM$"
                
from chunker import *

if __name__ == "__main__":


    import sys


    for i in xrange(1,len(sys.argv), 2 ):
        token = sys.argv[i]
        if token == "-c" : 
            sCommand = sys.argv[i+1]
        if token == "-d" :
            sPath = sys.argv[i+1]
        if token == "-s" :
            sFilename = sys.argv[i+1]
        if token == "-n" :
            nChunkSize = int(sys.argv[i+1])
        if token == "-p" :
            sChunkPrefix = sys.argv[i+1]
        if token == "-h" :
            sCommand = "HELP"
            
            
    if sCommand == "CHUNK" :
        WriteChunkFiles(sPath, sFilename, sPath, sChunkPrefix, nChunkSize)
    
    if sCommand == "REBUILD" :
        RebuildChunkedFile(sPath,sFilename,sPath, sChunkPrefix)
    
    if sCommand == "HELP" :
        
        print "help is on the way"

# Sample command lines
# -c REBUILD -d "/home/wyominggeezer/Downloads/" -s "mysql-connector-java-5.0.8.tar.gz" -n 2000000 -p CHUNK
# -h

    
    

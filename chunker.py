# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.




def WriteChunk(fInput, fOutput, nMaxBytes):
    """
    Writes bytes to fOutput read from fInput.
    Writing continues until nMaxBytes bytes have been
    written or the EOF of fInput has been reached.
    INPUTS:
    fInput - file handle for the input file, opened in "rb" mode
    fOutput - file handled for the output file, opened in "wb" mode
    nMaxBytes - Maximum bytes to be held in fOutput file
    
    ON RETURN:
    The file fInput will still be open if more bytes are remaining
    
    """

    for i in xrange(nMaxBytes - 1): # loop until nMaxBytes or out of data

        byte = fInput.read(1) # read a byte
        
        if byte: # if we got one, write it, otherwise, close fInput and leave
            fOutput.write(byte)
        else:
            fInput.close()
            
            break

    # always close the fOutput file
    fOutput.close()

            
def WriteChunkFiles(sInputFilepath, sInputFilename, sOutputFilepath, sPrefix, nChunkSize):
    """
    WriteChunkFiles copies an input file into multiple smaller output files each having
    a prefix.
    INPUTS:
    sInputFilepath - folder containing sInputFilename
    sInputFilename - name of file to be chunked
    sOutputFilepath - folder to place the chunked files
    sPrefix - prefix to be added to the chunked file. For example, with a
        prefix of CHUNK, the 45th chunked file would have a prefix of
        CHUNK45_
    nChunkSize - the size of each chunked file. The last chunked file will,
        usually, be less that the nChunkSize for obvious reasons.
    
    OUTPUTS: No outputs are returned. Any errors must be handled outside of the routine.
    """
    # Setup the input filespec and initialize nChunkNumber
    sInputFilespec = sInputFilepath + sInputFilename
    nChunkNumber = 1
    
    # Open the input file and call WriteChunk until we are out of data
    with open(sInputFilespec, "rb") as f:
        while True:
            # build the output filespec and open the file for binary write
            sOutputFilespec = sOutputFilepath + sPrefix + str(nChunkNumber) + "_" + sInputFilename
            out = open(sOutputFilespec, "wb")

            # write the chunked file
            WriteChunk(f, out, nChunkSize)
            
            # if the inputfile is closed upon return, it means we are out of data and finished
            if f.closed:
                break
                
            # if here, we still have data to write. Bump the chunk number and loop back
            nChunkNumber = nChunkNumber + 1
            
                
def AppendChunk(sSourceFilespec, fDestinationFileHandle):
    """
    AppendChunk appends a file to the end of another file.
    sSourceFilespec - name of the source file
    fDestinationFileHandle - file handle of an open destiation file
    """
    
    fInput = open(sSourceFilespec, "rb") # open the source file for read binary
    
    while True:
        byte = fInput.read(1) # read a byte

        if byte: # if we got one, write it, otherwise, close fInput and leave
            fDestinationFileHandle.write(byte)
        else:
            fInput.close()
            break


    
def RebuildChunkedFile(sSourcePath, sFilename, sDestinationPath, sChunkPrefix):
    """
    RebuildChunkedFile concatenates chunked files into one large file. It
    reverses the process of the WriteChunkFiles method.
    INPUTS:
    sSourcePath - location of chunked files
    sFlename - name of the output file
    sDestinationPath - location to store the restored file
    sChunkPrefix - prefix added to the chunked files.
    """
    import os.path    
    sDestinationFilespec = sDestinationPath +  sFilename
    
    if os.path.isfile(sDestinationFilespec) :
        # refuse to overwrite existing destination
        print "Destination already exists: " + sDestinationFilespec
        return None
    
    fDestinationFile = open(sDestinationFilespec, "wb")
    
    nChunkNumber = 1
    while True:
        # build the input filename and see if it exists
        sSourceFilespec = sSourcePath + sChunkPrefix + str(nChunkNumber) + "_" + sFilename

        if os.path.isfile(sSourceFilespec):
            AppendChunk(sSourceFilespec, fDestinationFile)
            print "reading " + sSourceFilespec
            nChunkNumber = nChunkNumber + 1
        else:
            break
            
            
    fDestinationFile.close()
    
    

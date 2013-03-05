###############################################################################
# Tool for converting a single string or a file to SHA-256 base64 hash value  #
############################################################################### 



import hmac
import hashlib
import base64

class FileHandler:
    
    _filename = 0
    _myFile = 0
    _linesToHash = []
    _hashValues = []
    
    
    # Read lines we want to hash and save to message Array
    def openFile(self, pFilename):
        
        FileHandler._filename = pFilename
        FileHandler.myFile = open(FileHandler._filename, "r")
        
        for file in FileHandler.myFile:
            FileHandler._linesToHash.append(file)
            
        FileHandler.myFile.close()
    
    # decode a given string    
    def decodeSingleString(self, pString):
        
        FileHandler._linesToHash.append(pString)
    
    # Calculate hashes and push back in hashValue array    
    def calculateHashes(self):
            
        for line in FileHandler._linesToHash:
            # build crypto string
            tempHash = hmac.new(b'1234567890', msg=line, digestmod=hashlib.sha256).digest()
            # decode crypto string & save back to array
            FileHandler._hashValues.append(base64.b64encode(tempHash).decode())
    
    # print crypto strings
    def printHashes(self):
        
        for hash in FileHandler._hashValues:
            print "value:   " '%s' % hash


# Run..
myCrypto = FileHandler()
#myCrypto.decodeSingleString("asdffjk;sdf")
myCrypto.openFile("Words.txt")
myCrypto.calculateHashes()
myCrypto.printHashes()

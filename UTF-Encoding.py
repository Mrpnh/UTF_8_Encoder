# This is a class for UTF-8 Encoding and Decoding
class UTF:

    # It encodes each string given to it.
    def encodeString(self,encodingString):
        # encoded string is stored here
        encoded=""
        
        # Iterates through the string and converts each char to hex value
        for eachChar in encodingString:

            # First the character is converted to ASCII value and then that ASCII value to hex value
            tempHex=str(hex(ord(eachChar)))
            
            # Then it replaces 0xHH to \xHH as per utf-8 encoding algorithm 
            tempHex="\\"+tempHex[1:]

            # Adds it to encoded string
            encoded+=tempHex 
        return encoded


    # It decodes each string given to it
    def decodeString(self,decodingString):
        decoded=""

        # Iterates through the encoded string and splits it when a patters 0x comes
        # This will give us hex value of each character
        for eachChar in decodingString.split('\\x')[1:]:
            
            # Now it converts each character to its hexa format 0xNN
            eachChar='0x'+eachChar

            # Now this string is converted to interger equivalent
            # And int(character,16) denotes we are passing a hex value in the format of string
            decoded+=chr(int(eachChar,16))
        return decoded

    def fileEncode(self,fileName):

        # Adds the extension
        fileName=fileName+'.txt'
        
        # try opening the file in read mode and encode it and store it in encoded.txt file
        try:
            with open(fileName,'r') as f:
                encodedString=self.encodeString(f.read())
            with open('encoded.txt','w') as f:
                f.write(encodedString)
        except:
            print("Something went wrong while encoding!!")
    
    def fileDecode(self,fileName):

        # Adds the extension
        fileName=fileName+'.txt'

        # try opening the encoded file and decode it and store it in decoded.txt
        try:
            with open(fileName,'r') as f:
                encodedString=f.read()
            with open('decoded.txt','w') as f:
                f.write(self.decodeString(encodedString))
        except:
            print("Something went wrong while decoding!!")


if __name__=='__main__':
    
    # Creates an instance of UTF class
    utfEncoding=UTF()

    # Calls the Encoding function
    utfEncoding.fileEncode('readme')

    # Calls the Decoding function
    utfEncoding.fileDecode('encoded')
    
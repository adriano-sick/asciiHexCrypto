#Adriano Siqueira - 9-22-21 - Hexadecimal Encoding and Decoding

def main():
    print("Hi this is The Awesome Hexadecimal to ASCII encoding/decoding");
    print("Tell me, do u want to decode os encode an ASCII text???");
    menuOption = input("(Type '1' to encode and '2' to decoding) ");
    

    if (menuOption == "1"):
        text = input("Type your text to be encode: ");
        encript(text);        
        
    elif (menuOption == "2"):
        hex = input("Type your hexadecimal code to be decode: ");
        decode(hex);
        
    else:
        print("Choose an valid Option.");
        main();
        
def encript(text):

    byteText = text.encode( 'utf-8' );  #transform string to byte code 
    print(byteText.hex());              #transform byte code to hex  


def decode(hex):

    byteHex = bytearray.fromhex(hex);  #transform hexadecimal to byte code
    print(byteHex.decode());           #transform byte code to string


main();


#TestInfo:
#https://github.com/adriano-sick/
#



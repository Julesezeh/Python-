#The Caesar cipher is an algorithm that encrpyts and decrypts texts by addition and subtraction used by Julius caesar 
print("Ceasar cipher by Jules Okoye-ezeh.\n")
print("The caesar cipher encrypts letters by shifting them over by a key number.\n")
print("for example, with a key number of 3, A becomes D and E becomes H. ")
print()
proceed = True
try:
    import pyperclip #copies text to clipboard.
except ImportError:
    pass #If it's not imported, do nothing.

 # To know if the mode is set to encrypt or decrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 # To hold the key the user decides to use
TRANS = '' # To hold the encrypted or decrypted text
#Ask if the user wants to encrypt or decrypt
while proceed == True: 
    print("Do you want to (e)ncrpyt or (d)ecrypt? ")
    reply = input("> ").upper()
    if reply[0] == 'E':
        STATUS = 'encrypt'
        break
    elif reply[0] == 'D':
        STATUS = 'decrypt'
        break

    print("\nPlease enter 'e' or 'd'. ")

#Gets the user to select the key for encrpytion/decrpyption (within the range of symbols)
while True:
    print(f"Please enter the key (0 - {len(SYMBOLS)-1}) to use.")
    response = input("> ")
    if response.isdigit():
        response = int(response)
        if 0 <= response < len(SYMBOLS):
            KEY = response
            break
        else:
            print("Please your key should be in the range of 0-25.")
    print("\n")
# Get the text you want to encrypt/decrypt
print("Enter the message you wish to enrypt/decrtpt.")
message = input("> ").upper()
#perform the 'STATUS' operation
for item in message:
    if item in SYMBOLS:
        position = SYMBOLS.find(item)

        if STATUS == 'encrypt':
            position = position + KEY
        elif STATUS == 'decrypt':
            position = position - KEY
        #Handle the wrap around if the 'position' value is greater than or equal to the length of the 'SYMBOLS'
        if position >= len(SYMBOLS):
            position -= len(SYMBOLS)
            TRANS = TRANS + SYMBOLS[position]
            
        elif position < 0:
            position = position + len(SYMBOLS)
            TRANS = TRANS +  SYMBOLS[position]
        else:
            TRANS = TRANS + SYMBOLS[position]
            
         
    else:
        TRANS = TRANS + item   

print("\n")
print(TRANS)

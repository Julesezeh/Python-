print("Ceasar Cipher by Jules Okoye-ezeh")
print("\nThis encrypts and decrypts using addition and subtraction ")
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new = ''
while True: #Know if the user wishes to encrypt or decrypt
    print("\nDo you want to encrypt(e) or decrypt(d")
    reply = input("> ").upper()
    if reply[0] == 'E':
        statusquo = 'ENCRYPT'
        break
    elif reply[0] == 'D':
        statusquo = 'DECRYPT'
        break
    print("\nPlease reply with 'E' or 'D' ")

while True:
    print(f"\nWhat key from 0-{len(symbols)-1} do you want to use ")
    reply = input("> ")
    if reply.isdigit():
        reply = int(reply)
        if 0 <= reply < len(symbols):
            key = reply
            break
        else:
            print("\nIt has to be in the specified range")
    else:
        print("Please it can only be a number")

print(f"\nPlease enter the messsage you wish to {statusquo.lower()}")
message = input("> ").upper()
for item in message:
    if item in symbols:
        position = symbols.find(item)
        if statusquo == 'ENCRYPT':
            position = position + key
        elif statusquo == 'DECRYPT':
            position = position-key
            

        if position >= len(symbols):
            position = position - len(symbols)
            new += symbols[position]
        elif position < 0:
            position = position + len(symbols)
            new += symbols[position]
        else:
            new += symbols[position]

    else:
        new += item

print(new)
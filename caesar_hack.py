print("Caesar hack by Jules Okoye-ezeh")
print("\nThis program is designed to decrypt the caesar cipher")

symbols="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("\nEnter the encrypted message you wish to decrypt ")
message = input("> ").upper()

for key in range(len(symbols)):
    new = ''
    for letter in message:
        if letter in symbols:
            position = symbols.find(letter)
            newposition = position-key
            if newposition < 0:
                newposition = newposition + len(symbols)
            new = new + symbols[newposition]
        else:
            new += letter

    print(f"for the key {key}: {new}")
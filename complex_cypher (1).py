def get_inputlist(special_characters):
    option = input("Would you like to encrypt (e) or decrypt (d)? \n")
    if option.lower() == "e":
        inputfile = input("Please enter the name of the file you would like to encrypt: \n")
    elif option.lower() == "d":
        inputfile = input("Please enter the name of the file you would like to decrypt: \n")

    file = get_file(inputfile)
    file = list(file)
    inputlist = []
    for i in file:
        if i in special_characters:
            inputlist.append(ord(i))
        else:
            inputlist.append(ord(i) - 96)

    return option, inputlist, inputfile

def get_phraselist():
    shift_phrase = (str(input("Please enter the encryption/decryption key you would like to use: \n"))).lower()
    #Hii my name is Lukas and i think computer sciensce is an interesting but difficult subject
    shift_phrase = shift_phrase.replace(" ", "")
    shift_phrase = list(shift_phrase)
    phraselist = []

    for i in shift_phrase:
        phraselist.append(ord(i) - 96)

    return phraselist

def get_file(inputfile):
    with open(inputfile, "r", encoding="utf-8") as f:
        text = f.read()
    return text.lower()

def encrypt_decrypt(inputlist, phraselist, special_characters, option):
    count = 0
    uncyphered = []
    for i in inputlist:
        if chr(i) in special_characters:
            uncyphered.append(i)
        else:
            if count >= len(phraselist):
                count = 0
            if option.lower() == "e":
                i = i + phraselist[count]
                if int(i + 96) > 122:
                    i = i - 26
            else:
                i = i - phraselist[count]
                if int(i + 96) < 97:
                    i = i + 26
            count += 1
            uncyphered.append(i)


    output = ""
    for i in uncyphered:
        if chr(i) in special_characters:
            output = output + chr(i)
        else:
            i = i + 96
            output = output + chr(i)

    if option.lower() == "e":
        print ("Your outputted text had been output to output.txt as: \n", output)
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print ("Your input text file decyphers to: \n", output)


special_characters = " !@#$%^&*()-+?_=,<>/.!$%&'()*+,-./:;<=>?@[\]^_{|}123456789"""
phraselist = get_phraselist()
option, inputlist, inputfile = get_inputlist(special_characters)
if option.lower() == "e":
    encrypt_decrypt(inputlist, phraselist, special_characters, option)
elif option.lower() == "d":
    encrypt_decrypt(inputlist, phraselist, special_characters, option)
else:
    print("Incorrect option selected, please try again")

import random
import string

'''
Takes in a string and encrypts it
input: string of input from the user 
return: the input string encrypted
'''
def encryptString(input):
    result = ""
    allDigits = string.digits
    allChars = "abcdefghijklmnopqrstuvwxyzABEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(input)):
        if (input[i].isdigit()):
            # Mark as digit, Add 9s complement, Add random digits
            currDigit = int(input[i])
            result += "D"
            result += str(9 - currDigit)
            result += (''.join(random.choice(allDigits) for i in range(3)))

        elif (input[i] == "C"): # Have to check because will cause error in decryption, but stil want C to be valid input
            result += "["

        elif (input[i] == "D"): # Have to check because will cause error in decryption, but stil want D to be valid input
            result += "]"

        else:
            # Mark as char, Add 2 random digits, Add digit, Add 2 more random digits
            result += "C"
            result += (''.join(random.choice(allChars) for i in range(2)))
            result += input[i]
            result += (''.join(random.choice(allChars) for i in range(2)))
    return result



'''
Takes in an encrypted string and decrypts it
input: the input string encrypted
return: string of input from the user 
'''
def decryptString(input):
    i = 0 # Set to 7 to get rid of the salt
    result = ""
    while (i < len(input)):
        if (input[i] == "["):
            result += "C"

        elif (input[i] == "]"):
            result += "D"

        elif (input[i] == "D"):
            result += str(9 - int(input[i+1]))

        elif (input[i] == "C"):
            result += input[i+3]

        i += 1
    
    # Return only from 7 onwards to get rid of the salt
    return (result[7:]) 



# Main Testing Code

possiblePasswordInput = "0123456789abcdefghijklmnopqrstuvwxyzABEFGHIJKLMNOPQRSTUVWXYZ,./<?!@#$%^&*()" # All values that can be used
countCorrect = 0
countIncorrect = 0
countTotal = 100
saltString = "HOWDY00"

for i in range(countTotal):
    password = (''.join(random.choice(possiblePasswordInput) for i in range(10)))
    encrypted = encryptString(saltString) + encryptString(password)
    decrypted = decryptString(encrypted)

    try:
        assert password == decrypted
        print("PASS: " + decrypted + " was correctly deciphered from " + password, " and the encrypted string is ", encrypted)
        countCorrect += 1
    except:
        print("Error: " + decrypted + " should have been " + password, " and the encrypted string is ", encrypted)
        countIncorrect += 1

print("----")
print("FINAL RESULTS")
print("Total test: ", countTotal)
print("Correct count: ", countCorrect)
print("Incorrect count: ", countIncorrect)


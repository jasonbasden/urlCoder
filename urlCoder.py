#urlCoder
#**Version 1.0.1**
#Copyright (c) 2020 Jason Basden
#Licensed under the MIT License


import urllib.parse

userAnswer = "yes"
useranswer = "yes"

while userAnswer == "yes":
    userInput = input("Do you want to URL Encode or URL Decode?: ").lower().strip()

    if(userInput == "url encode" or userInput == "encode" or userInput == "urlencode"):

        while True:
            userEncoding = input("\nHow would you like to encode spaces? Enter %20 or + : ").lower()
            if(userEncoding == "%20"):
                userString = input("\nEnter your string: ")
                print(urllib.parse.quote(userString))

                break
            elif(userEncoding == "+"):
                userString = input("\nEnter your string: ")
                print(urllib.parse.quote_plus(userString))
                break
            elif(userEncoding == ""):
                print("Error! Enter '%20', '+' or 'quit'.")
            elif(userEncoding == "quit"):
                break
            else:
                print("Error!")
                useranswer = input("Would you like to try Encoding again?: ")
                if(useranswer == "yes"):
                    useranswer = "yes"
                else:
                    False
                    break
    elif(userInput == "url decode" or userInput == "decode" or userInput == "urldecode"):
        userString = input("\nEnter your string: ")
        while("%" in userString or "+" in userString):
            decodedString = urllib.parse.unquote_plus(userString)
            print(decodedString)
            userString = decodedString
    elif(len(userInput) < 1):
        print("Error! Enter 'Encode' or 'Decode'.")

    else:
        print("Error!")

    userAnswer = input("\nDo you want to Encode/Decode again?: ").lower()
    print("")

print("\nThanks for using URL Coder!")

from sys import *
import os

options= {
    "Desktop" : 'C:/Users/username/Desktop/', # Change username to your local user!
    "Documents" : 'C:/Users/username/Documents/',
    "Custom Path" : ""
}

def getFilePath():
    print("Welcome to the txt file generator!")
    print("Enter the location you would like to save the file to: ")
    for i in range(0,3):
        print(options.keys()[i] +  " : " + str(i))

    fileLocation = input()

    options[2] = raw_input("""Enter file path. (e.x. ~\Users\user\workspace) make sure to use FORWARD SLASH ( / )!""" + "\n") if fileLocation == 1 else ""

    try:
        return(options.get(options.keys()[fileLocation]))
    except:
        print("Your entry is invalid. Please try again.")
        exit()

def generateTxt(filePath, fileName):
    path = os.path.normpath(filePath + fileName + ".txt").format(filePath, fileName)
    try:
        doc = open(path, "w")

        name = raw_input("Enter your name!")
        doc.write(name)
        doc.close()
        print("Success!")

    except OSError as error:
        print(error)
        exit()


filePath = getFilePath()
fileName= raw_input("Enter name for file: \n")
generateTxt(filePath, fileName)

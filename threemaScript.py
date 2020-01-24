# coding=UTF-8

import sys
import re

def helloWorld(text):
    return text

def getFileName(): # extract the second argument
    return str(sys.argv[1])

def readFileContent(file):
    f=open(file, "r")
    contents = f.read()
    return contents

def extractSachverhalt(contents):
    try:
        found = re.search('Sachverhalt: (.+?)\n', contents).group(1)
        found = found.strip()
    except AttributeError:
        found = ''
    return found

def extractOrt(contents):
    try:
        contents = contents.replace(" :",":")
        strasse = re.search('Straße: (.+?)Haus-Nr.(.+?)\n', contents).group(1)
        strasse = strasse.strip()
        nr = re.search('Haus-Nr.(.+?)\n', contents).group(1)
        nr = nr.replace(":", "")
        nr = nr.strip()
        if nr != "":
            nr = nr + ' '
        ort = re.search('Ort: (.+?)\n', contents).group(1)
        ort = ort.strip()
        found = strasse + ' ' + nr + ort
    except AttributeError as err:
        found = ''
    return found

def createThreemaMessage(sachverhalt, ort):
    message = sachverhalt + "\n" + ort
    return message

def sendThreemaMessage(message):
    print("sending Threema message: " + message)


if __name__ == '__main__':
    fileContent = readFileContent(getFileName())
    sachverhalt = extractSachverhalt(fileContent)
    ort = extractOrt(fileContent)
    message = createThreemaMessage(sachverhalt, ort)
    sendThreemaMessage(message)

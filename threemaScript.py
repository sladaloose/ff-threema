# coding=UTF-8

import sys
import re
import os

from threema.gateway import (
    Connection,
    GatewayError,
    util,
)
from threema.gateway.simple import TextMessage

from dotenv import load_dotenv
load_dotenv()

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

def sendThreemaMessage(connection, message):
    threemaMessage = TextMessage(
        connection=connection,
        to_id='4JTDMYFC',
        text=message
    )
    return threemaMessage.send()

def loadUsers(filePath):
    users = list()
    with open(filePath) as f:
        for line in f:
            users.append(line[0:8])
    return users


if __name__ == '__main__':
    fileContent = readFileContent(getFileName())
    sachverhalt = extractSachverhalt(fileContent)
    ort = extractOrt(fileContent)
    users = loadUsers(os.getenv("FILE_TO_LIST_OF_USERS"))
    message = createThreemaMessage(sachverhalt, ort)
    connection = Connection(
        identity=os.getenv("THREEMA_GATEWAY_ID"),
        secret=os.getenv("THREEMA_GATEWAY_ID_SECRET"),
        verify_fingerprint=True,
        blocking=True,
    )
    try:
        with connection:
            for user in users:
                sendThreemaMessage(connection, user, message)
    except GatewayError as exc:
        print('Error:', exc)

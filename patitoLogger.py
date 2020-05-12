logs = []

def saveLogsToFile():
    with open('Patito_Logs.txt', mode='w') as myFile:
        for log in logs:
            myFile.write(log)

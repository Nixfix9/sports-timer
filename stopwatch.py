import time

stopWatchStart = True
timeSec = 0timeMin = 0
checkTime = time.time()

print ('0' + str(timeMin), ':', '0' + str(timeSec))

while stopWatchStart:
    aktTime = time.time()
        if (aktTime - checkTime) >= 1:
            stopAnweisung +=1
            timeSec += 1
            checkTime = time.time()
            if timeSec >= 60:
                timeSec = 0
                timeMin += 1
            if timeSec <= 9:
                if timeMin <= 9:
                    print('0' + str(timeMin), ':', '0' + str(timeSec))
                else:
                    print(str(timeMin), ':', '0' + str(timeSec))
            else:
                if timeMin <= 9:
                    print('0' + str(timeMin), ':', str(timeSec))
                else:
                    print(str(timeMin), ':', str(timeSec))
        if timeMin >= 59:
            stopWatchStart = False   

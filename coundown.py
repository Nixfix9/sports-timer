import time

countDownStart = True

inputMin = int(input("Minuten Eingeben"))
inputSec = int(input("Sekunden Eingeben"))

totalCount = (inputMin*60)+inputSec

checkTime = time.time()

while countDownStart:
    aktTime = time.time()
    if aktTime - checkTime >= 1:
        inputSec -= 1
        checkTime = time.time()
        
        if inputSec <=0 and totalCount >= 0:
            inputMin -= 1
            inputSec = 60
        
        if inputSec <= 9:
            if inputMin <= 9:
                print('0' + str(inputMin), ':', '0' + str(inputSec))
            else:
                print(str(inputMin), ':', '0' + str(inputSec))
        else:
            if inputMin <= 9:
                print('0' + str(inputMin), ':', str(inputSec))
            else:
                print(str(inputMin), ':', str(inputSec))
        totalCount -= 1
        if totalCount <= 0:
            countDownStart = False

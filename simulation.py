from random import randint

def generateRandomHex():
    randomInteger=randint(16,255)
    randomHex=hex(randomInteger)
    #print randomInteger
    return format(randomInteger,'02x')

def generateRandomMAC():
    macAddr=str(generateRandomHex())+":"
    for i in range(1,6):
        if(i!=5):
            macAddr=macAddr+str(generateRandomHex())+":"
        else:
            macAddr=macAddr+str(generateRandomHex())
    return macAddr

def generateDatabase():
    print " Enter number of devices "
    global n
    n=input()
    global deviceList
    deviceList=[None]*(n+1)    
    for i in range(1,n+1):
        device={'id':i,'eth0':str(generateRandomMAC()),'wlan0':str(generateRandomMAC())}
        deviceList[i]=device

def dumpWholeDatabase():
    for i in range(1,n+1):
        print deviceList[i]

while(1):
    print " --------------- "
    print " 1. Generate New Database \n 2. Check device info by ID \n 3. Display Everything \n 4. Exit "
    choice=input()
    if (choice==4):
        print " Goodbye "
        break
    elif (choice==1):
        print " > Generating New Database "
        generateDatabase()
        print " > Generated "+str(n)+" devices"
    elif(choice==2):
        print " > Enter Device ID "
        temp=input()
        print " --------------- "
        print " DEVICE ID : "+str(temp)
        print deviceList[temp]
    elif(choice==3):
        print " > Display everything "
        dumpWholeDatabase()
    else:   
        print " > Invalid Choice "

    

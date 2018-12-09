import sys
import binascii
import random

#d.ruggiero 
#first written 2013
#last updated 2018


funFile = open(sys.argv[1], "rb")

mutationRate = 0.00005
#this value multiplied by 100 is the mutation rate as a percentage.

quantity = 1

if (len(sys.argv) >= 3):
        mutationRate = (float(sys.argv[2]))/100 #input mutation rate is as percentage

if (len(sys.argv) == 4):
        quantity = int(sys.argv[3])
        
hexList = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

byte = funFile.read()

hexy = list(binascii.hexlify(byte).decode().upper())
mexy = list(binascii.hexlify(byte).decode().upper())

funFile.close()


div = 20
count = len(hexy)//div
bount = count

print("Number of nibbles in input file: " + str(len(hexy)) + "\n")


for n in range(quantity):
        hitCount = 0
        count = len(hexy)//div
        mexy = list(binascii.hexlify(byte).decode().upper())
        for i in hexy[bount:len(hexy)-1]: 
                milk = random.random() #this function returns float value between 0 and 1.
                if milk < float(mutationRate):
                        storeOld = mexy[count]
                        mexy[count] = random.choice(hexList)
                        if(mexy[count] != storeOld):
                                #only count as mutation if the nibble hex digit did NOT get changed into itself
                                hitCount = hitCount + 1
                count = count + 1

        print("Number of mutated nibbles: " + str(hitCount))

        tmexy = ''.join(mexy)
        unhexy = binascii.unhexlify(tmexy)

        if(quantity != 1):
                fileString = "glitched_" + str(n) + "_" + sys.argv[1]
        else:
                fileString = "glitched_" + sys.argv[1]
                
        print("Outputting " + fileString + "\n")
        
        writeFile = open(fileString, "wb")
        writeFile.write(unhexy)

        writeFile.close()




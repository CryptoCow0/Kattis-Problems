password, encripted = input().split()

passwordArray = []
encriptedArray = []
for x in password:
     passwordArray.append(x)
for x in encripted:
     encriptedArray.append(x)

#iterate through the set of the password



y = 0




while(len(passwordArray) > 0):
        #print(password)

        if y >= len(encriptedArray):
             print("Fail")
             break
        elif encriptedArray[y] in passwordArray and encriptedArray[y] == passwordArray[0]:
            #print(y)
            passwordArray.pop(0)
            #print(password)
            
        
        elif encriptedArray[y] in passwordArray and encriptedArray[y] != passwordArray[0]:
            #print(encriptedArray[y])
            print("FAIL")
            break
            # print(encripted[x][y])
            # print("YESSS")
        

        y+=1


if (len(passwordArray) == 0 ):
    print("PASS")
#print(password)
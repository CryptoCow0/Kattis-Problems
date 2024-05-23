PreFixes = ['T', 'Th', 'Tho', 'Thor', 'Thore', 'ThoreH', 'ThoreHu', 'ThoreHus', 'ThoreHusf', 'ThoreHusfe', 'ThoreHusfel', 'ThoreHusfeld']


Names = int(input())

NamesArray = []

for x in range(Names):
    CurrentName = input()
    NamesArray.append(CurrentName)

finalAnswer = ""
PotentialAnswers = []
for x in range(len(NamesArray)):
    if (NamesArray[0] == "ThoreHusfeldt"):
        finalAnswer = "Thore is awesome"
        break
    elif (NamesArray[x] == "ThoreHusfeldt"):
        ThoresLocation = x

if (finalAnswer != "Thore is awesome"):
    for i in range(ThoresLocation):
        for y in range(0, len(PreFixes)):

            
            if (NamesArray[i].startswith(PreFixes[-1])== True):
                print("Thore Sucks")
                exit()

            if (NamesArray[i].startswith(PreFixes[y]) != True):
                PotentialAnswers.append(PreFixes[y])            
                break

    if len(PotentialAnswers) > 0:
        Answer = PotentialAnswers[0]
        for x in PotentialAnswers:
            if (len(x) >= len(Answer)):
                Answer = x
        print(Answer)
    

else:
    print(finalAnswer)

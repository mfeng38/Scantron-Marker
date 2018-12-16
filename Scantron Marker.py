import turtle as t

### GLOBAL: DIRECTORY OF THE SCANTRONFILES ###
pathKey = "IN_key+pts.txt"
pathRes = "IN_data_studs.txt"

### ANSWER KEY ###
def answerKeyRead(pathKey):
    fileRef = open(pathKey,"r")
    localList = []
    for line in fileRef:
        string = line[0:len(line)-1]
        localList.append(string)
    fileRef.close()
    return localList

### STUDENT SCANTRON FILES ###
def studentFileRead(pathRes):
    fileRef = open(pathRes,"r")
    localList = []
    for line in fileRef:
        string = line[0:len(line)-1]
        localList.append(string)
    fileRef.close()
    return localList

### CREATE AND WRITE TO EXCEL SHEET
def write_result_to_file(lres,the_file):
    fileRef = open(the_file,"w") # opening file to be written
    for line in lres:
        fileRef.write(line)
    fileRef.close()
    return

### CONVERTS STRING OF POINTS TO A LIST OF POINTS ###
def pointsToList(p_pointskey):
    q = 0
    pointlist = []
    for i in range(len(p_pointskey)):
        if p_pointskey[i] == " ":
            pointlist.append(float(p_pointskey[q:i]))
            q += ((i + 1)-q)
    pointlist.append(float(p_pointskey[q:]))
##    print(pointlist)
    return pointlist

### TOTAL POINTS THE TEST IS OUT OF ###
def maxPoints(p_pointslist):
    mxpt = 0.0
    for i in range(len(p_pointslist)):
        mxpt += float(p_pointslist[i])
    return mxpt

### CONVERTS THE ANSWER KEY STRING TO LETTERS ###
def convertNumToAlpha(p_answerkey):
    newkey = p_answerkey
    newkey = newkey.replace("1","A")
    newkey = newkey.replace("2","B")
    newkey = newkey.replace("3","C")
    newkey = newkey.replace("4","D")
    newkey = newkey.replace("5","E")
    newStr = ""
    for i in range(len(newkey)):
        newStr = newStr + " " + newkey[i]
    return newStr[1:]

### CHECKS THE STUDENT ANSWERS WITH THE ANSWER KEY AND GIVES POINTS ACCORDINGLY ###
def checkAnswers(p_pointslist,p_rawscantron,p_answerkey):
    scores = []
    for i in range(len(p_rawscantron)):
        point = 0
        rawanswer = p_rawscantron[i].split()[1]
##      print(rawanswer)
        for k in range(len(rawanswer)):
            if rawanswer[k] == p_answerkey[k]:
                point += p_pointslist[k]
        scores.append(point)
    return scores
##print("scores is",checkAnswers("score"))

### CREATES A LIST OF STUDENT NAMES ###
def students(p_rawscantron):
    studentNames = []
    for i in range(len(p_rawscantron)):
        spacepos = p_rawscantron[i].find(" ")
        studentNames.append(rawscantron[i][0:spacepos])
    return studentNames
##print(students())

### CALCULATES THE AVERAGE OF EACH STUDENT ###
def studentAverages(p_studentscores,p_studentlist,p_maxpoints):
    studentAverages = []
    for i in range(len(p_studentscores)):
        avrg = (p_studentscores[i]/p_maxpoints)*100
        studentAverages.append(avrg)
    return studentAverages
##print(averages())

### CALCULATES THE AVERAGE OF THE WHOLE CLASS ###
def classaverage(p_studentscores):
    classPointTotal = 0.0
    for i in range(len(p_studentscores)):
        classPointTotal += p_studentscores[i]
    classPointTotal = classPointTotal/len(p_studentscores)
    return classPointTotal

### CREATES A LIST OF STUDENT NAMES WITH THEIR MARKS AND PERCENTAGE ###
def studentResults(p_studentlist,p_studentscores,p_stud_avrg):
    studentScoreList = []
    for i in range(len(p_studentlist)):
        studentScoreList.append(p_studentlist[i] + "," + str(p_studentscores[i]) + "," + str(p_stud_avrg[i]) + "\n")
    return studentScoreList

### KEEPS TRACK OF HOW MANY TIMES EACH QUESTION WAS ANSWERED CORRECTLY ###
def correctCount(p_rawscantron,p_answerkey):
    correctlist = []
    for i in range(len(p_answerkey)):
        correctlist.append(0)
    for i in range(len(p_rawscantron)):
        counter = 0
        rawanswer = p_rawscantron[i].split()[1]
        for k in range(len(rawanswer)):
            if rawanswer[k] == p_answerkey[k]:
                correctlist[k] += 1
    return correctlist

### KEEPS TRACK OF THE MOST DIFFICULT QUESTION(S) ###
def difficultQ(p_num_correct):
    mincorrect = min(p_num_correct)
    mincorrectlist = []
    for i in range(len(p_num_correct)):
        if p_num_correct[i] == mincorrect:
            mincorrectlist.append(i+1)
    return mincorrectlist

### CACULATES HOW MANY STUDENTS GOT WHAT PERCENT (IN 10% INTERVALS) ###
def distributionPoints(p_stud_avrg,p_graderanges):
    distptlist = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(p_stud_avrg)):
        j = 0
        while p_stud_avrg[i] > graderanges[j]:
            j += 1
        distptlist[j] += 1
    return distptlist

### TURTLE THAT DRAWS A GRAPH OF THE DISTRIBUTION (IN 10% INTERVALS)
def distributionGraph(p_distpts):
    t.speed(10)
    t.fillcolor("blue")
    t.pu()
    t.setpos(-200,0)
    t.pd()
    for i in range(len(p_distpts)):
        if p_distpts[i] != 0:
            t.begin_fill()
            t.lt(90)
            t.fd(p_distpts[i]*15)
            t.rt(90)
            t.fd(20)
            t.rt(90)
            t.fd(p_distpts[i]*15)
            t.rt(90)
            t.fd(20)
            t.rt(180)
            t.end_fill()
        t.fd(40)

### CALCULATES THE DISTANCE BETWEEN TWO QUESTIONS ###
def distance(q1,q2,p_rawscantron,p_answerkey):
    q1 = int(q1)
    q2 = int(q2)
    distancelist = []
    for i in range(len(p_rawscantron)):
        point = 0
        rawanswer = p_rawscantron[i].split()[1]
        if ((rawanswer[q1-1] != p_answerkey[q1-1]) and (rawanswer[q2-1] == p_answerkey[q2-1])) or ((rawanswer[q1-1] == p_answerkey[q1-1]) and (rawanswer[q2-1] != p_answerkey[q2-1])):
            distancelist.append(1)
        else:
            distancelist.append(0)
        print("TRACE dist of stud " + rawscantron[i][:rawscantron[i].find(" ")] + " is " + str(distancelist[i]))
    totdistance = 0
    for i in range(len(distancelist)):
        totdistance += int(distancelist[i])
    return totdistance

### PROGRAM OPENING MESSAGE ###
def openingMessage():
    print("\nWelcome to the CMPT 120 Scantron Processing system!\n"
          "=================================================== \n"
          "This system will process scantron files in the default folder\n"
          "Make sure that the data files do not have extra spaces!\n"
          "\nThe data file in this folder has " + str(len(rawscantron)) + " students\n"
          "There are " + str(len(answerkey)) + " questions\n"
          "The answer key is:\n" + alphakey +
          "\n\nThe points are:\n" + pointskey +
          "\nThe maximum points possible is: " + str(maxpoints) +
          "\n\nYou have to choose one of two options:\n"
          "Type ALL (not case sensitive) to process the whole class\n"
          "Type SEL (not case sensitive)  to process selected students (up to half of the whole class)")

### STATISTICS ###
def statsMessage():
    print("\nHERE ARE THE STATS!\n"
          "===================\n\n"
          "Maximum points:" + str(max(studentscores)) + "\n\n"
          "Average points: " + str(class_avrg) + "\n\n"
          "Number students processed: " + str(len(studentlist)) + "\n\n"
          "Number of times each question was answered correctly:\n",num_correct,"\n\n"
          "Most difficult questions:",most_diff,"\n\n"
          "Distribution points:",distpts,"\n"
          "Considering ranges:",graderanges)

print ("\nJUST TO TRACE, the local list of strings is:\n")
for element in answerKeyRead(pathKey):
    print (element)

print ("\nJUST TO TRACE, the local list of strings is:\n")
for element in studentFileRead(pathRes):
    print (element)

### TOP LEVEL ###
answerkey = answerKeyRead(pathKey)[0]
pointskey = answerKeyRead(pathKey)[1]
rawscantron = studentFileRead(pathRes)
pointslist = pointsToList(pointskey)
maxpoints = maxPoints(pointslist)
alphakey = convertNumToAlpha(answerkey)
studentlist = students(rawscantron)
studentscores = checkAnswers(pointslist,rawscantron,answerkey)
stud_avrg = studentAverages(studentscores,studentlist,maxpoints)
class_avrg = classaverage(studentscores)
finalresult = studentResults(studentlist,studentscores,stud_avrg)
num_correct = correctCount(rawscantron,answerkey)
most_diff = difficultQ(num_correct)

graderanges = [10,20,30,40,50,60,70,80,90,100]
distpts = distributionPoints(stud_avrg,graderanges)

selcounter = 0
selindexlist = []
selfinalresult = []
temprawscantron = []

openingMessage()

prompt = input("\nType ALL or SEL: ")
while prompt.upper() != "ALL" and prompt.upper() != "SEL":
    print("\n! INVALID INPUT, PLEASE TYPE ALL OR SEL")
    prompt = input("Type ALL or SEL: ")
if prompt.upper() == "ALL":
    print("\nAll students have been processed!\n\n"
          "\nHere is the output that will be saved in the folder!\n")
    for i in range(len(finalresult)):
        print(finalresult[i])
else:
    print("\nYou chose to process selected students\n"
          "You will be asked to provide the name of the student\n")
    selprompt = input("Type a name or END to finish: ")
    while selprompt.lower() != "end" and selcounter < len(studentlist)//2:
        while selprompt.upper() not in studentlist and selprompt.lower() != "end":
            print("This name is not in the data, type again")
            selprompt = input("Type a name or END to finish: ")
        if selprompt.lower() != "end":
            print("\nStudent",studentlist[studentlist.index(selprompt.upper())],"got",studentscores[studentlist.index(selprompt.upper())],"points\n")
            selindexlist.append(studentlist.index(selprompt.upper()))
            selcounter += 1
            if selcounter < len(studentlist)//2:
                selprompt = input("Type a name or END to finish: ")
    print("\nAll students have been processed!"
          "\nHere is the output that will be saved in the folder!\n")
    for i in range(len(selindexlist)):
        selfinalresult.append(finalresult[selindexlist[i]])
        temprawscantron.append(rawscantron[selindexlist[i]])
    rawscantron = temprawscantron
    finalresult = selfinalresult
    for i in range(len(selfinalresult)):
        print(selfinalresult[i])

    studentlist = students(rawscantron)
    studentscores = checkAnswers(pointslist,rawscantron,answerkey)
    stud_avrg = studentAverages(studentscores,studentlist,maxpoints)
    class_avrg = classaverage(studentscores)
    finalresult = studentResults(studentlist,studentscores,stud_avrg)
    num_correct = correctCount(rawscantron,answerkey)
    most_diff = difficultQ(num_correct)
    distpts = distributionPoints(stud_avrg,graderanges)

statsMessage()

graphprompt = input("Would you like to graph the distribution? (Y/N): ")
while graphprompt.lower() != "y" and graphprompt.lower() != "n":
    graphprompt = input("Would you like to graph the distribution? (Y/N): ")
if graphprompt.lower() == "y":
    distributionGraph(distpts)

rawscantron = studentFileRead(pathRes)

distanceprompt = input("Would you like to calculate the 'distance' between questions? (Y/N): ")
while distanceprompt.lower() != "y" and distanceprompt.lower() != "n":
    distanceprompt = input("Would you like to calculate the 'distance' between questions? (Y/N): ")
if distanceprompt.lower() == "y":
    print("\nSpecial analysis 2 questions\nThis will provide a 'distance' between two questions\nby accumulating the distance within each student, for all students.\nYou can check several pairs of questions. 0 - end")

    q1prompt = input("Provide q1, starting from 1, or 0 to end: ")
    while q1prompt != "0":
        while (not q1prompt.isdigit() and int(q1prompt) > len(answerkey)) and q1prompt != "0":
            q1prompt = input("Provide q1, starting from 1, or 0 to end: ")

        q2prompt = input("Provide q2, starting from 1: ")
        while not q2prompt.isdigit() and q2prompt == "" and int(q2prompt) > len(answerkey):
            q2prompt = input("Provide q1, starting from 1, or 0 to end: ")
        print("\nThe distance between questions",q1prompt,"and",q2prompt,"is",distance(q1prompt,q2prompt,rawscantron,answerkey), "\n")
        q1prompt = input("Another q1? starting from 1, or 0 to end: ")

print("\nThats all the stats! Bye!")

write_result_to_file(finalresult,"test.csv")

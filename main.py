#jaccard function to compare similarity
def jaccard(set1,set2):
    if len(set1.union(set2))==0:
        return 0
    return len(set1.intersection(set2))/len(set1.union(set2))
def printchoice(option,similarity):
    descindex=similarity[option-1][1]
    line=doctext[descindex]
    listline=line.split("|")
    name=listline[0]
    desc=listline[2]
    syntax=listline[3]
    objtext=listline[4]
    args=listline[5]
    objreturn=listline[6]
    print("\n\nName: "+name+"\n")
    print("\nDescription: "+desc)
    print("\nSyntax: "+syntax)
    print("\nObject type function is applied to: "+objtext)
    print("\nArguements: "+args)
    print("\nReturn type: "+objreturn)
def objtype(linelist,userin):
    objlist=linelist[4].split(",")
    stripper(objlist)
    for obj in objlist:
        if obj in userin:
            return True
    return False
def stripper(lis):
    for i in range(len(lis)): 
        ent = lis[i] 
        lis[i] = ent.strip()
#variable type declaration and opening function text file
userin=str()
docfile=open("CS1docu3.txt","r")
doctext=docfile.read().split("\n")
docfile.close()
simlist=list()
desclist=list()
namelist=list()
keywords=list()
choicemade=False
#while loop takes in user input and finds its similarity
while userin!="exit":
    userin=input("\n\n\n\n\nSearch(\'exit\' to end): ").strip().lower()
    if userin=="exit":
        break
    #runs through entire function text file and makes a list of the similarities and the index of the function
    #descwords is key words
    for i in range(len(doctext)):
        if "|" not in doctext[i]:
            continue
        linelist=doctext[i].split("|")
        descwords=linelist[1].split(",")
        stripper(descwords)
        descset=set(descwords)
        userinwords=userin.split(" ")
        stripper(userinwords)
        userinset=set(userinwords)
        jsim=jaccard(descset,userinset)
        simlist.append((jsim,i))
        keywords.append(linelist[1])
        namelist.append(linelist[0])
        desclist.append(linelist[2])
    simlist.sort(reverse=True)
    startindex=0
    endindex=int()
    choicemade=False
    while choicemade==False:
        print("\n\n\n")
        if startindex+5>=len(simlist):
            for i in range(len(simlist)-startindex):
                index=simlist[startindex+i][1]
                print(str(startindex+i+1)+". "+namelist[index]+"   Description: "+desclist[index])
                endindex=len(simlist)
        else:
            for i in range(startindex,startindex+5):
                index=simlist[i][1]
                print(str(i+1)+". "+namelist[index]+"   Description: "+desclist[index])
                endindex=startindex+5
        print(str(endindex+1)+". Show more results")
        choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+1)+"): ").strip()
        choice=int(choice)
        if choice==endindex+1:
            startindex+=5
            continue
        else:
            printchoice(choice, simlist)
            rightfunc=input("\nIs this the function you are looking for?(Y/N): ").strip().lower()
            if rightfunc=="y":
                choicemade=True
            else:
                continue


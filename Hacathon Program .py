'''Program Statement:  '''

'''PROGRAM ASSUMPTIONS: 

1.

'''
''' FUNCTIONS '''

#jaccard function to compare similarity
def jaccard(set1,set2):
    if len(set1.union(set2))==0:
        return 0
    return len(set1.intersection(set2))/len(set1.union(set2))

''' Takes the choice index in simularity list and '''
def printchoice(option,similarity):
    descindex=similarity[option-1][1]
    #index is same thanks to while loop 
    line=doctext[descindex]
    listline=line.split("|")
    stripper(listline) 
    #extracts data from text and outputs in correct format 
    name=listline[0]
    desc=listline[2]
    syntax=listline[3]
    objtext=listline[4]
    
    #format arg defs correctly 
    argdefs=listline[5]
    list_argdefs = argdefs.split(',') 
    stripper(list_argdefs)
    
    
    objreturn=listline[6]
    
    
    print("\n\nName: "+name+"\n")
    print("\nDescription: "+desc)
    print("\nSyntax: "+syntax)

    #prints out in correct format 
    for defs in list_argdefs:    
        #so that doesn't print empty '-' along with object defintions twice for ones not edited yet 
        if  defs != '': 
            print('- ' + defs) 
    print("\nObject Type(s) Function Applied to: "+objtext)
    
    print("\nWhat it Returns: "+objreturn)
    
'''Never used  '''
def objtype(linelist,userin):
    objlist=linelist[4].split(",")
    stripper(objlist)
    for obj in objlist:
        if obj in userin:
            return True
    return False

'''Strips all elements of a list, returns nothing and uses aliasing  '''
def stripper(lis):
    for i in range(len(lis)): 
        ent = lis[i] 
        lis[i] = ent.strip()
        
''' MAIN BODY '''   

''' VARIABLES AND INPUT '''
#variable type declaration and opening function text file
userin=str()
docfile=open("CS1docu.txt","r")
doctext=docfile.read().split("\n")
docfile.close()
simlist=list()
desclist=list()
namelist=list()
keywords=list()
choicemade=False


''' COMMANDS '''
''' Entire simulation loop for prompts '''
while userin!="exit":
    

    userin=input("\n\n\n\n\nSearch(\'exit\' to end): ").strip().lower()
    if userin=="exit":
        break
    
    '''Finding JS for each function based on user input'''
    #runs through entire function text file and makes a list of the similarities and the index of the function
    #descwords is key words
    for i in range(len(doctext)):
        if "|" not in doctext[i]:
            continue
        linelist=doctext[i].split("|")
        descwords=linelist[1].split(",")
        
        #works cause alias 
        stripper(descwords)
        
        #gets jsim between respective user input and current line (function) 
        descset=set(descwords)
        userinwords=userin.split(" ")
        stripper(userinwords)
        userinset=set(userinwords)
        jsim=jaccard(descset,userinset)
        
        
        simlist.append((jsim,i))
        
        #stores info from specific line 
        #index for each correlates with sim list 
        keywords.append(linelist[1])
        namelist.append(linelist[0])
        desclist.append(linelist[2])
        

    #so can get highest jsim in list 
    simlist.sort(reverse=True)
    
    startindex=0
    endindex=int()
    choicemade=False
    
    ''''presents user with 'best options based on simularity and allows them to pick which 
    they want info on'''
    
    while choicemade==False:
        choice=str()
        print("\n\n\n")
        if startindex+5>=len(simlist):
            for i in range(len(simlist)-startindex):
                index=simlist[startindex+i][1]
                print(str(startindex+i+1)+". "+namelist[index]+"   Description: "+desclist[index])
                endindex=len(simlist)
            print(str(endindex+1)+". Previous")
            choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+1)+"): ").strip()
            choice=int(choice)
            if choice==endindex+1:
                startindex-=5
                continue
            else:
                printchoice(choice, simlist)
                rightfunc=input("\nIs this the function you are looking for?(Y/N): ").strip().lower()
                if rightfunc=="y":
                    choicemade=True
                else:
                    continue
        else:
            for i in range(startindex,startindex+5):
                index=simlist[i][1]
                print(str(i+1)+". "+namelist[index]+"   Description: "+desclist[index])
                endindex=startindex+5
            print(str(endindex+1)+". Show more results")
            if startindex!=0:
                print(str(endindex+2)+". Previous")
                choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+2)+"): ").strip()
            else:
                choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+1)+"): ").strip()
            choice=int(choice)
            if choice==endindex+2 and startindex!=0:
                startindex-=5
                continue
            elif choice==endindex+1:
                startindex+=5
                continue
            else:
                printchoice(choice, simlist)
                rightfunc=input("\nIs this the function you are looking for?(Y/N): ").strip().lower()
                if rightfunc=="y":
                    choicemade=True
                else:
                    continue

    # while choicemade==False:
    #     print("\n\n\n")
        
    #     #if functions in document less than 5
    #     if startindex+5>=len(simlist):
    #         for i in range(len(simlist)-startindex):
    #             #index stored in tup 
    #             index=simlist[startindex+i][1]
                
    #             #+1 so doesn't start at 0 
    #             print(str(startindex+i+1)+". "+namelist[index]+"   Description: "+desclist[index])
    #             endindex=len(simlist)
    #     else:
            
    #         #if functions in document > 5 
    #         for i in range(startindex,startindex+5):
    #             #gets index stored in tup 
    #             index=simlist[i][1]
    #             #+1 so doesn't start at 0 
    #             print(str(i+1)+". "+namelist[index]+"   Description: "+desclist[index])
    #             #defines end index as last function presented 
    #             endindex=startindex+5
            
            
    #     print(str(endindex+1)+". Show more results")
        
        
    #     ''' Dealing with option user selected '''
    #     choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+1)+"): ").strip()
    #     choice=int(choice)
    #     #if they ask for more, increment start index, and run through loop again, showing new functions 
    #     if choice==endindex+1:
    #         startindex+=5
    #         continue
    #     else:
            
    #         printchoice(choice, simlist)
    #         rightfunc=input("\nIs this the function you are looking for?(Y/N): ").strip().lower()
    #         if rightfunc=="y":
    #             choicemade=True
    #         else:
    #             continue
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
'''This function takes the inputted string, adds an arrow to it and presents it to the user
 as a prompt, it then strips and prints 
their response before returning it to where the function was called'''
def ask_print(word):
    prompt = word +' ==> '
    ans = input(prompt).strip()
    print(ans)
    return ans

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
inp_file = ask_print('Which file would you like to read from: ')
docfile=open(inp_file,"r")
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
    

    userin=input("\nSearch(\'exit\' to end search and add new functions if youd like): ").strip().lower()
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
        #if functions in document less than 5
        if startindex+5>=len(simlist):
            for i in range(len(simlist)-startindex):
                #index stored in tup
                index=simlist[startindex+i][1]
                #+1 so doesn't start at 0
                print(str(startindex+i+1)+". "+namelist[index]+"   Description: "+desclist[index])
                endindex=len(simlist)
            print(str(endindex+1)+". Previous")
            #+1 so doesn't start at 0
            #Dealing with option user selected
            choiceapp=False
            while choiceapp==False:
                choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+1)+"): ").strip()
                if choice.isnumeric()==False:
                    continue
                choice=int(choice)
                if startindex+1<=choice<=endindex+1:
                    choiceapp=True
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
            #if functions in document > 5
            for i in range(startindex,startindex+5):
                #index stored in tup
                index=simlist[i][1]
                #+1 so doesn't start at 0
                print(str(i+1)+". "+namelist[index]+"   Description: "+desclist[index])
                endindex=startindex+5
            print(str(endindex+1)+". Show more results")
            if startindex!=0:
                print(str(endindex+2)+". Previous")
                #Dealing with option user selected
                choiceapp=False
                while choiceapp==False:
                    choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+2)+"): ").strip()
                    if choice.isnumeric()==False:
                        continue
                    choice=int(choice)
                    if startindex+1<=choice<=endindex+2:
                        choiceapp=True
            else:
                choiceapp=False
                while choiceapp==False:
                    choice=input("\nSelect an option ("+str(startindex+1)+"-"+str(endindex+1)+"): ").strip()
                    if choice.isnumeric()==False:
                        continue
                    choice=int(choice)
                    if startindex+1<=choice<=endindex+1:
                        choiceapp=True
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

''' EASY FILE EDITOR; ADDING MORE FUNCTIONS '''

'''Dictonary follows same format as listed on 'Project Brainstomign document'
Requires function document

Meant to make editing our text file much easier, each call writes into new file specified '''



'''Strips all elements of a list, returns nothing and uses aliasing  '''
def stripper(lis):
    for i in range(len(lis)): 
        ent = lis[i] 
        lis[i] = ent.strip()



add_funs = ask_print('do you want to add functions? ("Y", "N")').casefold()

f = open(inp_file) 

doctext= f.read().strip()
functs = doctext.split('\n') 
seg_fun_lis = []
for fun in functs: 
    seg_lis = fun.split('|') 
    stripper(seg_lis) 
    seg_fun_lis.append(seg_lis) 

forgotten_returns = []
func_dict = dict()
for funs in seg_fun_lis: 
    func_dict[funs[0]] = dict()
    func_dict[funs[0]]['Name'] = funs[0] 
    #works cause aliasing 
    kw_lis = funs[1].split(',')
    stripper(kw_lis)
    func_dict[funs[0]]['key words'] = kw_lis
    func_dict[funs[0]]['Description'] = funs[2]
    func_dict[funs[0]]['Syntax'] = funs[3]
    '''MAKE THIS A LIST '''
    func_dict[funs[0]]['Object Type(s) Function Applied To'] = funs[4]
    #works cause aliasing
    arg_defs_lis = funs[5].split(',')
    stripper(arg_defs_lis)
    func_dict[funs[0]]['Argument Definitions'] = arg_defs_lis
    func_dict[funs[0]]['What It Returns'] = funs[6]
 
f.close()

'''make any changes to dict you like 
Ex: func_dict['max()']['key words'].append('large') 

'''

#if adding entire new function
if add_funs == 'y': 
    flag = True 
    while flag:  
        print('*adding to dict*' ) 
        name = ask_print('\nEnter Name: ') 
        kw_lis = []
        flag2 = True 
        while flag2: 
            keyword = ask_print('\nEnter a key word, will be automatically entered to list (type "0" if done adding): ')
            if keyword == '0' :
                flag2 = False 
            else: 
                kw_lis.append(keyword) 
        descr = ask_print('\nEnter Description: ')
        syn = ask_print('\nEnter Syntax: ') 
        
        '''MAKE THIS A LIST '''
        otfat = ask_print('\nEnter Object Type(s) Function Applied To (in comma, space format; will not be in list): ')
        arg_defs = [] 
        flag3 = True 
        while flag3: 
            print('\nEnter an argument and corresponding definition, Example -> "element: An element of any type (string or number or object or etc.)"')
            argdef = ask_print('will be automatically entered to list (type "0" if done adding or not applicable): ')
            if argdef == '0' :
                flag3 = False 
            else: 
                arg_defs.append(argdef.replace(',',' '))
        returns = ask_print('\nEnter what it returns: ')
        
        
        func_dict[name] = dict() 
        func_dict[name]['Name'] = name
        func_dict[name]['key words'] = kw_lis
        func_dict[name]['Description'] = descr
        func_dict[name]['Syntax'] = syn
        func_dict[name]['Object Type(s) Function Applied To'] = otfat
        func_dict[name]['Argument Definitions'] = arg_defs
        func_dict[name]['What It Returns'] = returns
        
        res = ask_print('\nDo you want to enter another function?("Y", "N")').casefold()
        if res == 'n':
            flag = False 
        
#writes edited dictionary into new file 

fout = open(inp_file, 'w') 

for names in func_dict: 
    # going through 2nd dict
    line = '' 
    for sections in func_dict[names]:
        info = func_dict[names][sections]

        if type(info) == str: 
            #so that last value outputted does not have '|' after
            if sections != 'What It Returns': 
                line += info + '|'
            else: 
                line += info 
        else: 
            '''SHOULD NOT NEED TO CHANGE THIS WHEN OTFAT BECOMES LIST  '''
            #if a list; kw_lis or arg_defs
            for i in range(len(info)): 
                vals = info[i] 
                #so that last value in list does not have ',' after it 
                if i != len(info) - 1:               
                    line+= vals +','
                else: 
                    line += vals
            line +='|'
    
    fout.write(line + '\n') 
print('Dictionary copied to {} in format such that it is parsable by this program.'.format(inp_file))
print('Run again if you want to make any edits to your personal documentation list')
fout.close()



'removes object: in argdefs list.'      
# if sections == 'Argument Definitions':
#     count = 0 
#     for j in range(len(info)): 
#         val = info[j-count] 
#         if val.casefold().count('object:') != 0: 
#             info.pop(j) 
#             count += 1 


#add words 
        
        
            
        




'''Dictonary follows same format as listed on 'Project Brainstomign document'
Requires function document

Meant to make editing our text file much easier, each call writes into new file specified '''


'''This function takes the inputted string, adds an arrow to it and presents it to the user
 as a prompt, it then strips and prints 
their response before returning it to where the function was called'''
def ask_print(word):
    prompt = word +' ==> '
    ans = input(prompt).strip()
    print(ans)
    return ans

'''Strips all elements of a list, returns nothing and uses aliasing  '''
def stripper(lis):
    for i in range(len(lis)): 
        ent = lis[i] 
        lis[i] = ent.strip()


inp_file = ask_print('Enter documentation file to update:') 
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
        name = ask_print('Enter Name: ') 
        kw_lis = []
        flag2 = True 
        while flag2: 
            keyword = ask_print('Enter a key word, will be automatically entered to list (type "0" if done adding): ')
            if keyword == '0' :
                flag2 = False 
            else: 
                kw_lis.append(keyword) 
        descr = ask_print('Enter Description: ')
        syn = ask_print('Enter Syntax: ') 
        
        '''MAKE THIS A LIST '''
        otfat = ask_print('Enter Object Type(s) Function Applied To (in comma, space format; will not be in list): ')
        arg_defs = [] 
        flag3 = True 
        while flag3: 
            print('Enter an argument and corresponding definition, Example -> "element: An element of any type (string or number or object or etc.)"')
            argdef = ask_print('will be automatically entered to list (type "0" if done adding or not applicable): ')
            if argdef == '0' :
                flag3 = False 
            else: 
                arg_defs.append(argdef.replace(',',' '))
        returns = ask_print('Enter what it returns: ')
        
        
        func_dict[name] = dict() 
        func_dict[name]['Name'] = name
        func_dict[name]['key words'] = kw_lis
        func_dict[name]['Description'] = descr
        func_dict[name]['Syntax'] = syn
        func_dict[name]['Object Type(s) Function Applied To'] = otfat
        func_dict[name]['Argument Definitions'] = arg_defs
        func_dict[name]['What It Returns'] = returns
        
        res = ask_print('Do you want to enter another function?("Y", "N")').casefold()
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
        
        
            
        




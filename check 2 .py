imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

#make dict with key being movie and value being name of unique actors 
act_per_mov = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if not movie in act_per_mov:
        act_per_mov[movie] = set()

    act_per_mov[movie].add(name) 

count1 = 0 
maxim_key = ''
maxim_val =  0         
for keys in act_per_mov: 
    if len(act_per_mov[keys]) == 1:
        count1 += 1
    if len(act_per_mov[keys]) > maxim_val: 
        maxim_key = keys 
        maxim_val = len(act_per_mov[keys]) 
        
print(maxim_val) 
print(maxim_key) 
print(count1) 
   
#print("A\nB\nC")

with open("file_read_test", "r") as f:
    # read whole file at one time, not line by line
    # print(f.read())
    
    # read file line by line, line is a string
    for line in f:
        print(line.rstrip("\n"))
     
#use relative path, if in linux or mas os, don't need to add \, but in windows because it use\, escape character,we have to add \ to print \in string
with open("C:\\Users\\julie\\Desktop\\vscodewebdevelopment\\pythonpractice\\file_test") as g:
    for line in g:
        print(line.rstrip("\n"))
    
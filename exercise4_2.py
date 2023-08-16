#4.2
#read a list from file
city_list = []
with open("cityfile", "r") as c:
    for line in c:
        city_list.append(line.rstrip("\n"))
    
#sort with built in method alphabetically
sorted_city_list = sorted(city_list)
#read them to another file
with open("written_city_file", "w")as g:
    for city in sorted_city_list:
        g.write(city + "\n")
        
print("done")
from computation import find_max

#read from a file
num_list = []
with open("file_read_test", "r") as file:
    for line in file:
        num_list.append(int(line.rstrip("\n")))
print(num_list)
#find max in the read file
print("max is: " + str(find_max(num_list)))

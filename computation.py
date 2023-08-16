

def average(num_list):
    return sum(num_list)/len(num_list)

def find_max(num_list):
    a = num_list[0]
    for num in num_list:
        if(num > a):
            a = num
    return a
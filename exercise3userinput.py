'''
#3.1

def find_max(num_list):
    a = num_list[0]
    for num in num_list:
        if(num > a):
            a = num
    return a

num_list = [3, 65,4353,-2, 1, 0]
print("the max number is " + str(find_max(num_list)))



num_list = []
for i in range(5):
    a = int(input("enter a number"))
    num_list.append(a)
print(average(num_list))


#3.2
def average(num_list):
    return sum(num_list)/len(num_list)
'''
#3.3
number_list = []
ask_user_for_numbers = True
while(ask_user_for_numbers):
    user_input = float(input("choose a number: "))
    if user_input == 0.0:
        ask_user_for_numbers = False
    else:
        number_list.append(user_input)

print(average(number_list))
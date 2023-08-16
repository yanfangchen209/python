from computation import average

num_list = []
ask_user_input = True
while ask_user_input:
    user_input = float(input("Enter a number:"))
    if user_input == 0:
        ask_user_input = False
    else:
        num_list.append(user_input)
    
    
print(average(num_list))
    

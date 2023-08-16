tropical = ['banana', 'apple', 'berry', 'pipeapple', 'pear']


#method 1
for x in tropical:
    print(x)

#method 2
for i in range(len(tropical)):
    print(tropical[i])

#method 3
'''
i = 0
while(i < len(tropical)):
    print(tropical[i])
    i += 1
'''

#method 4 List Comprehension
[print(x)  for x in tropical]
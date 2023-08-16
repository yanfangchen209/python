
#2.1 

def hello(name, age):
    return "hello " + name + " you are " + age


#2.2

def add(first, second):
    return first + second

print(add(1, 2))

#2.3

def getSum(num_list):
    return sum(num_list)/len(num_list)
print(getSum(num_list))



#2.4

def celsiusToFahrenheit(celsius):
    fahrenheit = 1.8 * celsius + 32
    return fahrenheit

print(celsiusToFahrenheit(32))

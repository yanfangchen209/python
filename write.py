
#w: write, if new_file exists, overwrite its content and write to it
with open("new_file", "w") as file:
    file.write("test 123\n")
    
#a: append new content, don't overwrite 
with open("new_file", "a") as file:
    file.write("test 123\n")
    
#w+: write and read the same file
with open("new_file", "w+") as file:
    file.write("test 123\n")
    # Move the cursor back to the beginning of the file
    file.seek(0)
    # Read and print the content of the file
    content = file.read()
    print(content)

#a+: append and read the same file
with open("new_file", "a+") as file:
    file.write("test 123\n")
# practice write/read file

with open("test.txt","w") as f: # create a new txt file (overwrite if exists)
    f.write("First line test\n")
    f.write("Second line test\n")

with open("test.txt","a") as f: # append a new line to the file
    f.write("Add third line\n")

with open("test.txt","r") as f: # read a whole file as one string
    content = f.read()

print(content)

with open("test.txt","r") as f: # read line by line
    for line in f:
        print(line.strip()) # .strip() removes \n

with open("test.txt","r") as f: # read all lines into a list
    lines = f.readlines()

print(lines)
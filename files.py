# First program
out_file = open("name.txt","w")
name = input("What is your name?")
print(name,file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

# Second program
in_file = open("numbers.txt","r")
num1 = int(in_file.readline())
num2 = int(in_file.readline())
print(num1+num2)
in_file.close()

# Third program
in_file = open("numbers.txt","r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
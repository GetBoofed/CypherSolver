code1 : str = ""
num1 : str = ""
code2 : str = ""
num2 : str = ""
cypher : str = ""
done = False

while done == False:
    if len(code1) != 3:
        code1 : str = input("Input first 3 letters:")
    elif len(num1) != 3:
        num1 : str = input("Input first 3 numbers:")
    elif len(code2) != 3:
        code2 : str = input("Input second 3 letters:")
    elif len(num2) != 3:
        num2 : str = input("Input second 3 numbers:")
    else: 
        done = True

cypher : str = input("Input the main cypher:")

code1 = list(code1)
num1 = list(num1)
code2 = list(code2)
num2 = list(num2)
cypher = list(cypher)

code1dict : dict = {code1[0]:num1[0],code1[1]:num1[1],code1[2]:num1[2]}
code2dict : dict = {code2[0]:num2[0],code2[1]:num2[1],code2[2]:num2[2]}

code : str = ""

for x in cypher:
    if x in code1dict:
        code = code + code1dict[x]
    elif x in code2dict:
        code = code + code2dict[x]

if len(code) != 3:
    print("You fucked up.")
else:
    print("Your code is " + code)

print("Type exit to kill this program.")
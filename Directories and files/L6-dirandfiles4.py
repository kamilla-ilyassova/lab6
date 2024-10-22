import os
with open('c:/Users/hp/Desktop/Камилла/c++/.vscode/lab6/Directories and files/examplefile.txt', 'r') as file:
    x = sum(1 for line in file)
print(x)

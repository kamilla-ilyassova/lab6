import os
list = list(input().split())
with open('c:/Users/hp/Desktop/Камилла/c++/.vscode/lab6/Directories and files/examplefile.txt', 'w') as file:
    for i in list:
        file.write(str(i) + ' ')

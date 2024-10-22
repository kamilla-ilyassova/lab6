import os
with open('c:/Users/hp/Desktop/Камилла/c++/.vscode/lab6/Directories and files/examplefile.txt', 'r') as r:
    with open('c:/Users/hp/Desktop/Камилла/c++/.vscode/lab6/Directories and files/examplefile_copy.txt', 'w') as w:
        for line in r:
            w.write(line)

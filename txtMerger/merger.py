import glob2
from datetime import datetime

def merger():
    now = datetime.now()
    filenames = glob2.glob("*.txt")
    with open(now.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt","w") as myfile:
        for filename in filenames:
            with open(filename,"r") as f:
                myfile.write(f.read() + '\n')

merger()

'''
s = {}
with open("file1.txt", "r") as string1:
    s[1] = string1.read()
with open("file2.txt", "r") as string2:
    s[2] = string2.read()
with open("file3.txt", "r") as string3:
    s[3] = string3.read()

    with open("merger.txt","a") as merger:
        for value in s.values():
            merger.write(value + "\n")
'''

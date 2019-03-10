import os

txt ='This is the sample text to be written to  a file'

with open("sample.txt","w")as outfile:
    outfile.write(txt)
    outfile.close()


with open("sample.txt", "r") as infile:
    while infile.read():
        print(infile)

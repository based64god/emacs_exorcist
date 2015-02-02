#because no one likes her coding style
import os

input_file=raw_input("Please enter the directory of the file you wish to exorcise (or file name if this script is in the same folder). I.E. ~/Desktop/somefolder/somefile.txt:  ")
print(input_file)
file_working=open(os.path.expanduser(input_file))
for line in file_working.readline()
	line.replace("  ","    ")
	line.replace("{\n","\n{\n    ")

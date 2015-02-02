#because no one likes her coding style
import os

input_file=raw_input("Please enter the directory of the file you wish to exorcise (or file name if this script is in the same folder). I.E. ~/Desktop/somefolder/somefile.txt:  ")
print(input_file)
file_working=open(os.path.expanduser(input_file))
output_file=os.path.expanduser(input_file)+"_EXORCISED"
for line in file_working.read()
	line.replace("  ","\t")
	line.replace("{\n","\n{\n\t")
	output_file.write(line)


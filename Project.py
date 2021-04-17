
import re
import subprocess 
import fnmatch
import os


#path1 = input("Enter the directory for Shell Folder=  " )
#path2 = input("Enter the directory for Version.txt file=  " )



file_content = []
file_new = []
file_scriptname = []


for file2 in os.listdir('Version'):
        if file2.endswith(".txt"):
                x= os.path.join('Version',file2)
                file_content.append(x) #Open the version file

for item in file_content:
	newfile = open(item,'r')
	content = newfile.read()
	content = content.strip()
	final = re.findall('\d+',content)
	Value = ' '.join(final)
	Versionvalue = int(Value) #Integer value of Version
	

for file1 in os.listdir('ShellFolder' ):
	if file1.endswith(".sh"):
		list = (os.path.join(file1))
		file_scriptname.append(list)
		list = re.findall('(\d+)',list)
		Val = ' '.join(list)
		Shellvalue = int(Val)
		file_new.append(Shellvalue) 


file_new.sort()

maxvalue = max(file_new)
if Versionvalue == maxvalue :
        print("Already exists")

j= 0
filelen= len(file_new)
for i in range(filelen):
	if (j >= filelen):
		break
	if (file_new[i] > Versionvalue) :
		executevalue = file_new[i]
		string1 = str(executevalue)
		Versionvalue = executevalue
		print("Version number= ", Versionvalue)
		j= j+1
	
 
	for scriptname in file_scriptname:
		if string1 in scriptname:
			out = subprocess.Popen(['ShellFolder/'+ scriptname], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			stdout,stderr = out.communicate()
			print(stdout)
	
		


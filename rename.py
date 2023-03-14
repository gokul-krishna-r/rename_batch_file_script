import os
import csv


arr=[]
with open('test.csv') as csv_file:  #csv file name
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		arr.append(row[0])
		print(arr);
		line_count += 1

os.chdir("") #file location: eg C:\\Users\\name\Documents\test
print(os.getcwd())

for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = "certificate_" + arr[count+1] #new name to be replaced with
	oldname=f"Untitled-{count+1}.pdf";  #current file name
 
	new_name = f'{f_name}{f_ext}'
	os.rename(oldname, new_name)

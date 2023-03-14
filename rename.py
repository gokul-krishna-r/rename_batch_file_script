import os
import csv


arr=[]
with open('spacesummit_1.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		arr.append(row[0])
		print(arr);
		line_count += 1

os.chdir("C:\\Users\\rahul\Documents\cognifox_works\Affinity\space_up\spaceup_certificates\prevent_1")
print(os.getcwd())

for count, f in enumerate(os.listdir()):
	f_name, f_ext = os.path.splitext(f)
	f_name = "certificate_" + arr[count+1]
	oldname=f"Untitled-{count+1}.pdf";
 
	new_name = f'{f_name}{f_ext}'
	os.rename(oldname, new_name)
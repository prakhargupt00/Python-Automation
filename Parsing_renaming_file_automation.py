#============================================================================================
# The Problem 
# Many times we face issue such that file name is like "automate-#1.mkv" ,"automate-#2.mkv"
# and this often  makes them unordered and auto playlist gets messed up unable to recognise the order
# solution so we are writing a script  to solve this issue and make something like "1 automate.mkv"
#===================================================================================================
import os 

os.chdir('/desktop/programme_codes/python/videos') 

for file in os.lisdir():
	file_name, file_ext = os.path.splitext(f) #spitting file name from extension
	
	file_title,file_num = file_name.split('-') #splitting with delimeter '-'
	
	file_title = file_title.strip() #strip any space 
	file_num = file_num.strip()[1:].zfill(2)   #removing space .strip () and 
	# removing the #sign infront of num like #1 [1:] and zfill fills 1 with 01 2 means total length 02 is 2 

	new_name = '{}-{}{}'.format(f_num, file_title, f_ext)

	os.rename(file,new_name)
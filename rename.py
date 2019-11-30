import os

blacklist = ["VirtualBox VMs", "listSyntaxReminder"]

walk_option = input("Rename only this Directory or walk down all recursive directories? (cwd) (all): ")



if walk_option == "cwd":
	path = os.getcwd()
	filenames = os.listdir(path)

	#Looping through every item in the dir
	for filename in filenames:
	
		#Check for potential blacklisted items
		if filename in blacklist:
			print(str(filename) + ": Blacklisted item, not renaming")
	
		#If the item is a file, remove spaces and make all characters lower
		elif os.path.isfile(filename):
			os.rename(filename, filename.replace(" ", "_").lower())
		
		#If the item is a dir, remove spaces and Capitalize the first character
		elif os.path.isdir(filename):
			os.rename(filename, filename.replace(" ", "_").capitalize())
				
		#Catch all for something that isn't a file or dir and informs the user
		else:
			print(str(filename) + ": Possibly a symlink, won't risk breaking path dependencies")

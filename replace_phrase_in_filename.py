import sys, shutil, os, re

print("This program replaces the first instance of a phrase in a filename if it exists.")
old_phrase = input("Which phrase would you like to replace? : ")
new_phrase = input("What would you like to replace it with? : ")

prompt = input("Are you sure? y/n? ('n' will exit the program): ")

if(prompt == 'n'):
	exit()

for oldfile in os.listdir('.'):

	if(oldfile == "replace_phrase_in_filename.py"):
		continue

	m = re.search(old_phrase, oldfile)
	if m:
		newfile = oldfile[:m.start()] + new_phrase + oldfile[m.end():]

		absWorkingDir = os.path.abspath('.')
		oldfile = os.path.join(absWorkingDir, oldfile)
		newfile = os.path.join(absWorkingDir, newfile)

		print('Renaming %s to %s' % (oldfile, newfile))
		shutil.move(oldfile, newfile)
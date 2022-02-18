import sys, shutil, os

append_phrase = input("Phrase to add to beginning of files: ")

prompt = input("Are you sure? y/n? ('n' will exit the program): ")

if(prompt == 'n'):
	exit()

for oldfile in os.listdir('.'):

	if(oldfile == "append_phrase_to_beginning_of_files.py"):
		continue

	newfile = append_phrase + oldfile

	absWorkingDir = os.path.abspath('.')
	oldfile = os.path.join(absWorkingDir, oldfile)
	newfile = os.path.join(absWorkingDir, newfile)

	print('Renaming %s to %s' % (oldfile, newfile))
	shutil.move(oldfile, newfile)
import shutil, os, re

filePattern = re.compile(r'(PICT)(00)(\d\d)(\.JPG)', re.VERBOSE)

for slidefile in os.listdir('.'):
	mo = filePattern.search(slidefile)

	if mo == None:
		continue

	filenumber = mo.group(3)
	filenumber = int(filenumber)
	testnum = filenumber = filenumber - 12
	filenumber = str(filenumber)

	if(testnum < 10):
		newslidefile = 'PICT000' + filenumber + '.JPG'
	else:
		newslidefile = 'PICT00' + filenumber + '.JPG'

	absWorkingDir = os.path.abspath('.')
	slidefile = os.path.join(absWorkingDir, slidefile)
	newslidefile = os.path.join(absWorkingDir, newslidefile)

	print('Renaming %s to %s' % (slidefile, newslidefile))
	shutil.move(slidefile, newslidefile)
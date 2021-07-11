# shiftfilenames

ShiftFiles.py is supposed to take a group of files with PICT0013.JPG with filenames of 13 to 99
and subtract 12 from the number to obtain a filename like PICT0001.JPG or for PICT0022.JPG for example PICT0010.JPG

Make directory with ShiftFilenames.py and makepictfiles.sh
Run ./makepictfiles.sh to create files PICT0013.JPG to PICT0025.JPG
Run python3 ShiftFilenames.py

Bugs: The output is missing one file. i.e. You get PICT0001.JPG to PICT0012.JPG instead of PICT0001 to PICT0013.JPG. Why?

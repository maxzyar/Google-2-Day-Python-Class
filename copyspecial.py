#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def extraxt_especial_files(direc):
	pathslist = []
	if os.path.exists(direc):
		filenames = os.listdir(direc)
		for filename in filenames:
			match = re.search(r'__(\w+)__', filename)
			if match:
				filepath = os.path.join(direc, filename)
				pathslist.append(filepath)
	else:
		sys.stderr.write('No such directory!!!')
	pathslist = sorted(pathslist)
	for item in pathslist:
		print '\n', item
	return pathslist
	
def copy_to(pathslist, dest):
	if not os.path.exists(dest):
		os.mkdir(dest)
	for path in pathslist:
		shutil.copy(path, dest)
		
def zip_to(paths, zipto):
	sys.stderr.write(output)
	sys.exit(1)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for arg in args:
	paths = extraxt_especial_files(arg)
	
  if todir:
    copy_to(paths, todir)
  elif tozip:
    zip_to(paths, tozip)
  else:
    print '\n'.join(paths)
	
if __name__ == "__main__":
  main()

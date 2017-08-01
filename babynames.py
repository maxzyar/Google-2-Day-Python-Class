#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  names = []
  f = open(filename, 'rU')
  text = f.read()
  year = re.search('Popularity\sin\s(\d\d\d\d)', text)
  if not year:
	print 'ERROR: No Year Detected!'
	sys.exit(1)
  year=year.group(1)
  names.append(year)
  
  tuples = re.findall(r'<td>(\d*)</td><td>(\w+)</td><td>(\w+)</td>', text)
  tuples = sorted(tuples, key = lambda tup:tup[0])
  
  names2rank = {}
  for tuple in tuples:
	if tuple[1] not in names2rank:
		names2rank[tuple[1]] = tuple[0]
	else:
		names2rank[tuple[1]] = names2rank[tuple[1]] + ', '+tuple[0]
	if tuple[2] not in names2rank:
		names2rank[tuple[2]] = tuple[0]
	else:
		names2rank[tuple[2]] = names2rank[tuple[2]] + ', '+tuple[0]
  
  for key in sorted(names2rank.iterkeys()):
    names.append("%s: %s" % (key, names2rank[key]))

  return names


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
	names = extract_names(filename)
	outputtext = '\n'.join(names)
	if summary:
		outputfile = open(filename + '.summary' , 'w')
		outputfile.write(outputtext)
		outputfile.close()
	else:
		print outputtext
  
  
if __name__ == '__main__':
  main()

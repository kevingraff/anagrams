# solution.py
# Main module for the solution to the anagrams problem

# Assumptions:
# 	Spaces are ignored
#	Apostrophes are ignored
#	All letters are treated as lowercase

import sys, re
from collections import defaultdict

# if no arg provided display help and exit

# read dict line by line
	# >3 letters tolower then sort the letters
	# add word to dictionary key = sorted letters

# read dictionary keys
	# if number of values >= keylength
	# print the values
	
def cleanWord(word):
	w = re.sub('\W', '', word.lower(), count=0) # Remove all non-alphanumeric characters from word and make it lower case
	w = ''.join(sorted(w))
	return w
	
dictionary = open(sys.argv[1]).read().splitlines()

keyedList = defaultdict(list) # Initialize the sorted-letter key:value list

for word in dictionary:
	keyWord = cleanWord(word.strip())
	
	if len(keyWord) >= 4:
		keyedList[keyWord].append(word)

for key, val in keyedList.items():
	if len(val) >= len(key):
		print(', '.join(val))		

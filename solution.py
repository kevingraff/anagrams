# solution.py
# Main module for the solution to the anagrams problem

# Assumptions:
# 	Spaces are ignored
#	Apostrophes are ignored
#	All letters are treated as lowercase
#	Dictionary is in the format of one word per line

import sys, re
from collections import defaultdict
	
def make_key(word):
	'''Remove all non-alphanumeric characters from word and make it
	lower case then sort the letters.
	
	Keyword arguments:
	word -- string to operate on
	
	Returns: cleaned string with letters sorted
	'''
	w = re.sub('[\W\n]', '', word.lower(), count=0)
	w = ''.join(sorted(w))
	return w

# Quit if no dictionary is given
if len(sys.argv) <= 1:
	print("\tsolution.py: Please provide a dictionary as an argument")
	sys.exit()

# Initialize the sorted-letter key:value list
keyed_list = defaultdict(list)

try:
	with open(sys.argv[1]) as dictionary:
		# Iterate through the dictionary file
		for word in dictionary:
			# Remove newlines and turn word into a hash key
			key_word = make_key(word.rstrip())
			# Ignore words less than 4 characters after removing apostrophes
			if len(key_word) >= 4:
				# Append word to the hash
				keyed_list[key_word].append(word.rstrip())
except IOError:
	print("\tsolution.py: Error, invalid file")

# Iterate through the hash pulling each key and value
for key, val in keyed_list.items():
	# For key length n, ignore any entries with fewer than n anagrams
	if len(val) >= len(key):
		# Format the output
		print(", ".join(val))

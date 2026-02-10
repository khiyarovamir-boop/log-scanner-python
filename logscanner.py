#!/usr/bin/env python3
"""
log scanner CLI tool
text and regex based searching
memory safe line by line processing
"""

import sys
import re

def check_args():
	if len(sys.argv) == 3:
		return 1
	elif len(sys.argv) == 4:
		return 2
	else:
		return False

def check_flags(flag):
	if flag == "--regex":
		return "re"

def scan_filereg(pattern, filename):
	number = 0
	matchnumber = 0
	try:
		reg = re.compile(pattern, re.IGNORECASE)
	except re.error:
		print("REGEX_ERROR")
		sys.exit(1)
	try:
		with open (filename, encoding='utf-8', newline='') as f:
			for line in f:
				number += 1
				if re.search(pattern, line, re.IGNORECASE):
					matchnumber += 1 
					print(str(number) + ":", line, end="")
		print ("Total matches:", matchnumber)
	except:
		print("FILE_ERROR")
		sys.exit(1)

def scan_filenorm(pattern, filename):
	number = 0
	matchnumber = 0
	try:
		with open (filename, encoding='utf-8', newline='') as f:
			for line in f:
				number += 1
				if pattern.lower() in line.lower():
					matchnumber += 1 
					print(str(number) + ":", line, end="")
		print ("Total matches:", matchnumber)
	except:
		print("FILE_ERROR")
		sys.exit(1)

def main():
	x = check_args()
	if x == 1:
		scan_filenorm(sys.argv[1], sys.argv[2])

	elif x == 2:
		y = check_flags(sys.argv[1])
		if y == "re":
			scan_filereg(sys.argv[2], sys.argv[3])

	else:
		print("ARGUMENT_ERROR")
		sys.exit(1)

if __name__ == "__main__":
	main()

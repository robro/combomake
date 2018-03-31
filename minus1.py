#!/usr/bin/env python
import os
import re
import sys

def minusOne(matchobj):
  num = int(matchobj.group(0))

  return str(num) if num == 1 else str(num - 1)

def plusOne(matchobj):
  num = int(matchobj.group(0))

  return str(num + 1)

def main():
  with open('timing.py', 'r') as timing_file:
    timing_str = timing_file.read()

  # numbers = re.findall(r'(?<=\s)\d+', timing_str)

  # new_timing_str = re.sub(r'(?<=\s)\d+', minusOne, timing_str)

  new_timing_str = re.sub(r'\s+1,', '', timing_str)
  new_timing_str = re.sub(r',\s1(?=])', '', new_timing_str)
  new_timing_str = re.sub(r'(?<=\s)\d+', plusOne, new_timing_str)

  print new_timing_str

  return 0

if __name__ == "__main__":
    main()
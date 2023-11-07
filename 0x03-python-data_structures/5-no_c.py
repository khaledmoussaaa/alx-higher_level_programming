#!/usr/bin/python3
def no_c(my_string):
  word = ""
  if not my_string:
      return None
  for i in my_string:
    if i != 'c' and i != 'C':
      word = word + i
  return word 

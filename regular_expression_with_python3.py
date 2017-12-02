# ==============================================================
# built in module for python:

import re
dir(re)


pattern = r'testpattern'
string = r'teststring'
repl = r'testrepl'
# ==============================================================
# common re function
re.search(pattern, string)
re.match(pattern, string)
re.findall(pattern, string)
re.finditer(pattern, string)
re.sub(pattern, repl, string)
# pattern is a string that we define

# The function re.finditer does the same thing as re.findall,
# except it returns an iterator, rather than a list


# ==============================================================
# METACHARACTERS for pattern

# . matches any character, other than a new line
pattern = r"gr.y"
'''
will match grey, grEy, gr*y
'''

# ^ and $ match the start and end of a string
pattern = r"^gr.y$"
'''
 matches string started with gr, then follow with any character,
 except a newline, and end with y
'''

# * means "zero or more repetitions of the previous thing"
pattern = r"egg(spam)*"
'''
matches strings that start with "egg" and follow with zero or more "spam"s
'''

# + is very similar to *, except it means "one or more repetitions",
# as opposed to "zero or more repetitions"

pattern = r"g+"
'''
matches one or more g in string
'''

# ? means "zero or one repetitions"
pattern = r"ice(-)?cream"
'''
matches any string start with ice then followed by zero or one '-'
'''

# Curly Braces {x,y} represent the number of repetitions between two numbers x,y
pattern = r"a{1,3}$"
'''
matches string that have 1 to 3 'a' character
'''

# | means "or", so red|blue matches either "red" or "blue"
pattern = r"gr(a|e)y"
'''
matches gray or grey, otherwise not match
'''


# ==============================================================
# CHARACTER CLASSES

# square brackets [] match only one of a specific set of characters in []
pattern = r"[aeiou]"
'''
matches any string with 'a' or 'e' or 'i' or 'o' or 'u'
'''

# [a-z] matches any lowercase alphabetic character
# [G-P] matches any uppercase character from G to P
# [0-9] matches any digit
pattern = r"[A-Z][A-Z][0-9]"
'''
matches strings that contain two alphabetic uppercase letters
followed by a digit
'''

# ^ at the start of a character class to invert it
# Note: Other metacharacters such as $ and .,
# have no meaning within character classes
pattern = r"[^A-Z]"
'''
matches any string with character a to z
'''

# another example
pattern = r'([^aeiou][aeiou][^aeiou])+'
'''
matches One or more repetitions of a non-vowel, a vowel and a non-vowel
'''


# ==============================================================
# GROUP
# A group can be created by surrounding part of a regular expression with
# parentheses ()
pattern = r"egg(spam)*"
'''
matches strings starts with "egg" and follow with zero or more group "spam"s
'''

# nested group
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
'''
abcdefghi
abcdefghi
bc
de
('bc', 'de', 'fgh', 'g')
'''

# ==============================================================
# SPECIAL SEQUENCES
# a backslash and a number between 1 and 99, e.g., \1 or \17
# This matches the expression of the group of that number
pattern = r"(.+) \1"
'''
matches "word word", "?! ?!"
'''

# \d matches digits, \D matches non-digits
# \s matches whitespace, \S matches non-whitespce
# \w matches word characters, \W matches non-word characters
pattern = r"(\D+\d)"
'''
matches one or more non-digits followed by a digit
'''

# \A and \Z match the beginning and end of a string
# \b matches the empty string between \w and \W characters, or \w characters
# and the beginning or end of the string
# \B matches the empty string anywhere else
pattern = r"\b(cat)\b"
'''
matches the word "cat" surrounded by word boundaries
'''

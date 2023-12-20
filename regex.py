"""Write a regular expression to match a valid phone number in the format XXX-XXX-XXXX.import re"""


"""pattern =r'\d{3}-\d{3}-\d{4}'
text="contact me at 123-456-7890 or 9090909090"
matches=re.findall(pattern,text)
print(matches)"""

"""Exercise 2:
Write a regular expression to match a valid date in the format MM/DD/YYYY.
"""
"""import re
pattern =r'\d{2}/\d{2}/\d{4}'
text="My date of birth is 14/08/1995 and current date is 10/10/2023"
matches=re.findall(pattern,text)
print(matches)"""

"""The given text for the question number 3 to 9 is:
text = '''The quick brown fox jumps over the lazy dog.
The quick brown fox jumps over the lazy dog again.
The quick brown cat jumps over the lazy dog.'''


Exercise 3:
Write a regular expression to find all occurrences of the word "fox" in the given text
"""

"""import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern="fox"
match = re.findall(pattern,text)
print(match)"""

"""Exercise 4:
Write a regular expression to find all occurrences of the word "quick" in the given text"""


"""import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern="quick"
match = re.findall(pattern,text)
print(match)"""

"""Exercise 5:
Write a regular expression to find all occurrences of words that start with the letter "c" in the given text."""

"""import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern= r'\b[c]\w+'
match = re.findall(pattern,text)
print(match)"""

"""Exercise 6:
Write a regular expression to find all occurrences of the word "lazy" followed by any one character in the given text.
"""


"""import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern= r'lazy'
match = re.findall(pattern,text)
print(match)"""

"""Exercise 7:
Use match() to find if the text starts with "The" """

"""import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern= r'the'
match = re.match(pattern,text,re.IGNORECASE)
if match:
    print("text starts with 'The'")
else:
    print("text doen't start with 'The")
"""
"""Exercise 8:
Use search() to find the first occurrence of the word 'fox' """
"""import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern= r'fox'
match = re.search(pattern,text,re.IGNORECASE)

if match:
    print(f"The first occurrence of 'fox' is at {match.start()} ")
else:
    print("there is no occurence of 'fox' ")"""

"""Exercise 9:
Use search() to find the first occurrence of words that start with the letter "c" """

import re
text= ("The quick brown fox jumps over the lazy dog. "
       "The quick brown fox jumps over the lazy dog again."
       "The quick brown cat jumps over the lazy dog.")
pattern= r'\b[c]\w+'
match = re.search(pattern,text,re.IGNORECASE)

if match:
    print(f"The first occurrence of word start with 'c' is at {match.start()} ")
    print(f"And the word is {match.group()}")
else:
    print("there is no occurrence of words that starts with 'c' ")










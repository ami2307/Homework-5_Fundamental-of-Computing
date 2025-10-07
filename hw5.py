# pequod():  the hunt for the white whale
import re

def pequod(f):
    text = open(f).read()
    pattern = re.compile(
        r'w\s*h\s*i\s*t\s*e\s*\s*w\s*h\s*a\s*l\s*e(\'s)?(?!s)\b',
        re.IGNORECASE
    )
    matches = pattern.findall(text)
    return len(matches)

    

# find_dotcoms():  extracting information
import re

def find_dotcoms(s):
  
    pattern = re.compile(r'\b([a-zA-Z0-9-]+)\.com\b')
    return pattern.findall(s)
    

# palindrome_re:  identifying palindromes the hard way
def palindrome_re(n):
    half = n // 2
    front = ''.join(f'(?P<a{i}>.)' for i in range(half))
    mid = '.' if n % 2 else ''
    back = ''.join(f'(?P=a{i})' for i in reversed(range(half)))
    return f'{front}{mid}{back}'


# palindrome_direct:  identifying palindromes the easy way
def palindrome_direct(s):
    return s == s[::-1]



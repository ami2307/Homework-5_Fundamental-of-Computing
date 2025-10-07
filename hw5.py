# pequod():  the hunt for the white whale
import re

def pequod(f):
    text = open(f, 'r', encoding='utf-8').read()
    pattern = re.compile(
        r"\b"                     
        r"w\s*h\s*i\s*t\s*e"       
        r"\s+"                     
        r"w\s*h\s*a\s*l\s*e"       
        r"(?:'s)?\b",              
        re.IGNORECASE
    )

    matches = list(pattern.finditer(text))
    return len(matches)


# find_dotcoms():  extracting information
import re

def find_dotcoms(s):
    pattern = re.compile(r'([A-Za-z0-9-]+)\.com(?!\.)')
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



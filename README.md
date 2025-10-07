# Homework-5_Fundamental-of-Computing

Ami Raj araj2@stevens.edu

1. Are there any known bugs or issues with your program?  
No.

2. Describe an issue that you encountered and resolved when writing and testing your code.

While implementing the `pequod()` function to count occurrences of the phrase "white whale," I initially wrote a regular expression that only matched the exact phrase with a single space. This caused the function to miss occurrences where extra spaces or no spaces appeared between "white" and "whale," or when capitalization varied.

I resolved this by crafting a flexible regex pattern using `\s*` between every letter of "white" and "whale," and adding the `re.IGNORECASE` flag. 


import re

# Define the regular expression pattern
pattern = r'a(b*)s'

# Test strings
test_strings = ['abs', 'abbs', 'abbbbbbbbs', 'as', 'abbas']

# Loop through the test strings and find matches
for string in test_strings:
    match = re.search(pattern, string)
    if match:
        print(f"{string} ")
    else:
        print(f"{string}")
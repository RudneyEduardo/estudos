import re
n = input()
if re.search("\\<br>\\b", n, re.IGNORECASE):
    print("tem br")
